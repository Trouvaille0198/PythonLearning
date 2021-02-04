import requests
from requests.exceptions import RequestException
from lxml import etree
import pandas as pd
import numpy as np
from xpinyin import Pinyin
import time
import os
# 拼音对象初始化
p = Pinyin()


class LianjiaCrawler():
    def __init__(self, city, location, page, path='.'):
        self.city = city
        self.location = location
        self.page = page
        self.column = [
            '标题', '介绍', '小区', '价格（万元）', '平米单价（元）', '建筑面积（平米）', '套内面积（平米）',
            '大区域', '小区域', '户型', '朝向', '所在楼层', '装修情况', '户型结构', '建筑类型', '建筑结构',
            '建造时间', '房屋用途', '挂牌时间', '上次交易时间', '房屋年限', '产权所属', '配备电梯', '梯户比例'
        ]
        if path != '':
            self.path = path
        else:
            self.path = os.getcwd()

    # 辅助函数
    def organize_url(self, i):
        '''
        组合url
        '''
        pinyin_city = p.get_initials(self.city, '').lower()  # 将城市名由中文改为首字母小写
        pinyin_location = p.get_pinyin(self.location, '')  # 将区域由中文改为拼音
        url = 'https://{}.lianjia.com/ershoufang/{}/pg{}sf1sf2sf3/'.format(
            pinyin_city, pinyin_location, str(i))
        return url

    def get_one_page_text(self, url):
        '''
        获取单个页面的html文本
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

    def switch_to_xpath(self, url_text):
        '''
        将html文本转换为xpath解析对象
        '''
        html = etree.HTML(url_text)
        return html

    def get_house_list(self, html):
        '''
        获取单个页面的房源url列表
        '''
        one_page_url = html.xpath('//div[@class="title"]/a/@href')
        return one_page_url

    def is_null(self, feature):
        '''
        判断空特征
        '''
        if not feature:
            return ['暂无数据']
        else:
            return feature

    # 可调用函数
    def get_whole_house_url(self):
        '''
        获取所有房源url列表
        '''
        url_list = []
        for i in range(1, int(self.page) + 1):
            # print('正在获取第{}页房源url'.format(str(i)))
            url = self.organize_url(i)
            text = self.get_one_page_text(url)
            if text:
                html = self.switch_to_xpath(text)
                url_list.extend(self.get_house_list(html))
                time.sleep(0.5)
        return url_list

    def parse_house_info(self, url):
        '''
        分析并获取单条房源信息
        '''
        text = self.get_one_page_text(url)
        if not text:
            return []
        html = self.switch_to_xpath(text)
        one_piece = []
        # 块区域
        around_info = html.xpath('//div[@class="aroundInfo"]')[0]
        intro_content = html.xpath('//div[@class="introContent"]')[0]

        # 特征
        title = html.xpath(
            '//div[@class="title-wrapper"]//h1[@class="main"]/@title')
        # 标题

        sub = html.xpath(
            '//div[@class="title-wrapper"]//div[@class="sub"]/@title')  # 介绍

        community = around_info.xpath(
            '//div[@class="communityName"]//a[@class="info "]/text()')  # 小区

        total_price = html.xpath(
            '//div[@class="price "]//span[@class="total"]/text()')  # 价格（万元）

        average_price = html.xpath(
            '//div[@class="price "]//span[@class="unitPriceValue"]/text()'
        )  # 平米单价（元）

        total_area = intro_content.xpath(
            '//div[@class="base"]//ul/li/span[contains(text(),"建筑面积")]/../text()'
        )  # 建筑面积（平米）

        inner_area = intro_content.xpath(
            '//div[@class="base"]//ul/li/span[contains(text(),"套内面积")]/../text()'
        )  # 套内面积（平米）

        main_region = around_info.xpath(
            '//div[@class="areaName"]//a[1]/text()')  # 大区域

        sub_region = around_info.xpath(
            '//div[@class="areaName"]//a[2]/text()')  # 小区域

        layout = intro_content.xpath(
            '//div[@class="base"]//ul/li/span[contains(text(),"房屋户型")]/../text()'
        )  # 户型

        direction = intro_content.xpath(
            '//div[@class="base"]//ul/li/span[contains(text(),"房屋朝向")]/../text()'
        )  # 朝向

        floor = intro_content.xpath(
            '//div[@class="base"]//ul/li/span[contains(text(),"所在楼层")]/../text()'
        )  # 所在楼层

        decoration = intro_content.xpath(
            '//div[@class="base"]//ul/li/span[contains(text(),"装修情况")]/../text()'
        )  # 装修情况

        layout_structure = intro_content.xpath(
            '//div[@class="base"]//ul/li/span[contains(text(),"户型结构")]/../text()'
        )  # 户型结构

        building_type = intro_content.xpath(
            '//div[@class="base"]//ul/li/span[contains(text(),"建筑类型")]/../text()'
        )  # 建筑类型

        building_structure = intro_content.xpath(
            '//div[@class="base"]//ul/li/span[contains(text(),"建筑结构")]/../text()'
        )  # 建筑结构

        build_time = html.xpath(
            '//div[@class="houseInfo"]//div[@class="area"]/div[@class="subInfo noHidden"]/text()'
        )  # 建造时间

        usage = intro_content.xpath(
            '//div[@class="transaction"]//ul/li/span[contains(text(),"房屋用途")]/../span[last()]/text()'
        )  # 房屋用途

        list_time = intro_content.xpath(
            '//div[@class="transaction"]//ul/li/span[contains(text(),"挂牌时间")]/../span[last()]/text()'
        )  # 挂牌时间

        last_trade_time = intro_content.xpath(
            '//div[@class="transaction"]//ul/li/span[contains(text(),"上次交易")]/../span[last()]/text()'
        )  # 上次交易时间

        time_limit = intro_content.xpath(
            '//div[@class="transaction"]//ul/li/span[contains(text(),"房屋年限")]/../span[last()]/text()'
        )  # 房屋年限

        ownership = intro_content.xpath(
            '//div[@class="transaction"]//ul/li/span[contains(text(),"产权所属")]/../span[last()]/text()'
        )  # 产权所属

        elevator = intro_content.xpath(
            '//div[@class="base"]//ul/li/span[contains(text(),"配备电梯")]/../text()'
        )  # 配备电梯

        elevator_scale = intro_content.xpath(
            '//div[@class="base"]//ul/li/span[contains(text(),"梯户比例")]/../text()'
        )  # 梯户比例

        # 数据整理
        title = self.is_null(title)[0]

        sub = self.is_null(sub)[0]
        if sub == '链家网真房源，更多房源信息请联系经纪人':
            sub = '暂无数据'

        community = self.is_null(community)[0]

        total_price = self.is_null(total_price)[0]
        if total_price.isdigit():
            total_price = int(total_price)
        else:
            total_price = np.nan

        average_price = self.is_null(average_price)[0]
        if average_price.isdigit():
            average_price = int(average_price)
        else:
            average_price = np.nan

        total_area = self.is_null(total_area)[0][:-1]
        if total_area.replace('.', '', 1).isdigit():
            total_area = float(total_area)
        else:
            total_area = np.nan

        inner_area = self.is_null(inner_area)[0][:-1]
        if inner_area.replace('.', '', 1).isdigit():
            inner_area = float(inner_area)
        else:
            inner_area = np.nan

        main_region = self.is_null(main_region)[0]
        sub_region = self.is_null(sub_region)[0]
        layout = self.is_null(layout)[0]
        direction = self.is_null(direction)[0]
        floor = self.is_null(floor)[0]
        decoration = self.is_null(decoration)[0]
        layout_structure = self.is_null(layout_structure)[0]
        building_type = self.is_null(building_type)[0]
        building_structure = self.is_null(building_structure)[0]

        build_time = self.is_null(build_time)[0][:4]
        if build_time.isdigit():
            build_time = int(build_time)
        else:
            build_time = np.nan

        usage = self.is_null(usage)[0]
        list_time = self.is_null(list_time)[0]
        last_trade_time = self.is_null(last_trade_time)[0]
        time_limit = self.is_null(time_limit)[0]
        ownership = self.is_null(ownership)[0]
        elevator = self.is_null(elevator)[0]
        elevator_scale = self.is_null(elevator_scale)[0]

        one_piece.append(title)
        one_piece.append(sub)
        one_piece.append(community)
        one_piece.append(total_price)
        one_piece.append(average_price)
        one_piece.append(total_area)
        one_piece.append(inner_area)
        one_piece.append(main_region)
        one_piece.append(sub_region)
        one_piece.append(layout)
        one_piece.append(direction)
        one_piece.append(floor)
        one_piece.append(decoration)
        one_piece.append(layout_structure)
        one_piece.append(building_type)
        one_piece.append(building_structure)
        one_piece.append(build_time)
        one_piece.append(usage)
        one_piece.append(list_time)
        one_piece.append(last_trade_time)
        one_piece.append(time_limit)
        one_piece.append(ownership)
        one_piece.append(elevator)
        one_piece.append(elevator_scale)

        return one_piece

    def get_whole_house_info(self, url_list):
        '''
        将所有房源信息整合成复合列表
        '''
        house_list = []
        for url in url_list:
            print('正在获取第{}条房源信息'.format(url_list.index(url) + 1))
            one_piece = self.parse_house_info(url)
            if not one_piece:
                house_list.append(one_piece)
            # time.sleep(0.5)
        print('完成所有爬取~')
        return house_list

    def switch_to_pandas(self, house_list):
        '''
        将房源复合列表转换为 DataFrame 格式
        '''
        df = pd.DataFrame(house_list, columns=self.column)
        return df

    def save_to_path(self, df):
        '''
        保存 DataFrame
        '''
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        df.to_csv(self.path + '/{}房源.csv'.format(self.location),
                  index=False,
                  encoding="utf-8-sig")
