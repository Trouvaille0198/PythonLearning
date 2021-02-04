import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import time
import re
import os


def get_one_page(url):  # 获取html页面
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if(response.status_code == 200):
            return response.text
        return None
    except RequestException:
        return None


def get_download_url(html):  # 获取图片下载地址（列表形式）
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find_all('div', class_='cover')
    download_list = [div[i].a.img['src'] for i in range(len(div))]
    return download_list


def change_m_into_l(url):  # 将缩略图格式的下载地址替换成原图格式下载地址
    content = re.sub('/m/', '/l/', url)  # 豆瓣真的蠢
    return content


def download_photo(url, index, foldername):  # 下载图片
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
    }
    r = requests.get(url, headers=headers, stream=True)  # 发送请求
    folderpath = "D:/Pictures/" + foldername
    if not os.path.exists(folderpath):
        os.mkdir(folderpath)
    filename = folderpath + "/img{}.png".format(str(index))
    with open(filename, 'wb') as file_object:  # 写入图片
        file_object.write(r.content)


def main(number, start, foldername):

    url = 'https://movie.douban.com/subject/{}/photos?type=S&start={}&sortby=like&size=a&subtype=a'.format(
        number, str(start))
    html = get_one_page(url)
    download_url = get_download_url(html)
    for i in range(len(download_url)):
        download_photo(change_m_into_l(download_url[i]), start + i, foldername)


if __name__ == '__main__':
    number = input("请输入电影编号：")
    page = input("请输入爬取页数：")
    foldername = input("请输入文件夹名：")
    for start in range(0, int(page) * 30, 30):
        main(number, start, foldername)
        time.sleep(1)
    print("下载完成~")
