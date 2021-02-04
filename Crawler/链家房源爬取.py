import requests
from requests.exceptions import RequestException
from pyquery import PyQuery as pq
import pandas as pd
import numpy as np
import os
from xpinyin import Pinyin
p = Pinyin()


def get_one_page(url):
    '''
    获取单个页面的html
    :param url: string类型，网址
    :return: string类型，单页html文本
    '''
    try:
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if (response.status_code == 200):
            return response.text
        return None
    except RequestException:
        return None


def get_info_block(pq_doc):
    '''
    获取一个房源的未处理数据块
    :param pq_doc: pyquery对象，单页html内容
    :return: pyquery对象列表，（30个）数据块列表
    '''
    infos = pq_doc('.info.clear').items()  # 得到数据块生成器
    info_block_list = []
    for info in infos:
        info_block_list.append(info)
    return info_block_list


def anal_house_info(info_block_list):
    '''
    将数据块列表处理成特征集
    :param info_block_list: pyquery对象，数据块列表
    :return: 房源特征集列表
    '''
    final_info_list = []
    for info in info_block_list:
        one_piece = []
        title = info('.title a').text()  # 标题
        community = info(
            '.flood .positionInfo [data-el="region"]').text()  # 小区
        price = float(info('.priceInfo .totalPrice').text()[:-1])  # 房价
        average_price = float(
            info('.priceInfo .unitPrice span').text()[2:-4])  # 每平米均价
        ori_info = info('.address .houseInfo').text()
        more_info = ori_info.split(' | ')

        one_piece.append(title)
        one_piece.append(community)
        one_piece.append(price)
        one_piece.append(average_price)
        one_piece.append(more_info[0])  # 房型
        one_piece.append(float(more_info[1][:-2]))  # 面积
        one_piece.append(more_info[2])  # 朝向
        one_piece.append(more_info[3])  # 装修
        one_piece.append(more_info[4])  # 楼层
        one_piece.append(more_info[-1])  # 建筑类型
        # 建造时间特征可能会缺失，需要做个判断
        if len(more_info) == 6:
            # 若缺失
            one_piece.append(np.nan)
        elif not more_info[-2][0:4].isdigit():
            one_piece.append(np.nan)
        else:
            one_piece.append(int(more_info[-2][0:4]))  # 建楼时间

        final_info_list.append(one_piece)
    return final_info_list


def main(city, location, page):
    '''
    :param city: string类型，城市名
    :param location: string类型，区域名
    :param page: string类型，爬取页数
    '''
    final = []
    print('开始爬取！')
    pinyin_city = p.get_initials(city, '').lower()  # 将城市名由中文改为首字母小写
    pinyin_location = p.get_pinyin(location, '')  # 将区域由中文改为拼音
    for i in range(1, int(page) + 1):
        url = 'https://{}.lianjia.com/ershoufang/{}/pg{}/'.format(
            pinyin_city, pinyin_location, str(i))
        pq_doc = pq(get_one_page(url))
        info_block_list = get_info_block(pq_doc)
        info_list = anal_house_info(info_block_list)
        final.extend(info_list)  # 数据集列表合并
        print('已爬取第{}页'.format(i))
    print('爬取完成！')
    return final


if __name__ == '__main__':

    city = input('请输入城市：')
    location = input('请输入区域：')
    page = input('请输入页数：')

    info_list = main(city, location, page)

    column = [
        '标题', '小区', '价格（万元）', '平米单价（元）', '户型', '面积（平米）', '朝向', '装修', '楼层',
        '建筑类型', '建成时间（年）'
    ]
    df = pd.DataFrame(info_list, columns=column)
    if not os.path.exists('Data'):
        os.mkdir('Data')
    df.to_csv('Data/{}房源.csv'.format(location),
              index=False,
              encoding="utf-8-sig")
