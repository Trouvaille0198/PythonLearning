from bs4 import BeautifulSoup
import pandas as pd
import requests
复制代码
lst = []
url = 'https://tophub.today/n/mproPpoq6O'


def get(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
        url = requests.get(url, timeout=30, headers=headers)
        url.raise_for_status()
        url.encoding = 'utf-8'
        return url.text
    except:
        return "产生异常"


def create(lst, html, num):
        soup = BeautifulSoup(html, 'html.parser'
                             b=soup.find_all('span', class_='e')
                             print('{:^10}\t{:^30}\t{:^10}'.format(
                                 '排名', '标题', '热度'))
                             for i in range(num):
                             print('{:^10}\t{:^30}\t{:^10}'.format(i+1, a[i+50].string, b[i+50].string)
                                   lst.append([i+1, a[i+50].string, b[i+50].string]
                                              html=get(url)
                                              create(lst, html, 10)
                                              df=pd.DataFrame(
                                                  lst, columns=['排名', '标题', '热度'])
                                              ZHHot='D:\Python\知乎热搜'
                                              df.to_excel(ZHHot)
