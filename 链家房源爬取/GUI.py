import tkinter as tk
from tkinter import filedialog
from lianjia_crawler import LianjiaCrawler
import threading
import os


def thread_it(func, *args):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()


class Gui():
    def __init__(self, master):
        self.root = master
        self.root.title('链家房源爬取')
        self.root.geometry('600x600')
        MainPage(self.root)


class MainPage():
    def __init__(self, master):
        self.master = master
        self.main_page = tk.Frame(self.master)
        self.main_page.grid()
        self.crawl_button = tk.Button(self.main_page,
                                      text='爬虫',
                                      command=self.go_crawl).grid(row=0,
                                                                  column=0)
        self.ml_button = tk.Button(self.main_page,
                                   text='房价预测',
                                   state='disabled').grid(row=1, column=0)

    def go_crawl(self):
        self.main_page.destroy()
        CrawlPage(self.master)


class CrawlPage():
    def __init__(self, master):
        self.master = master
        self.crawl_page = tk.Frame(self.master)
        self.crawl_page.grid()
        self.back_Button = tk.Button(self.crawl_page,
                                     text='返回',
                                     command=self.go_main).grid(row=0,
                                                                column=0)

        self.city_label = tk.Label(self.crawl_page,
                                   text='请输入城市：').grid(row=1, column=0)
        self.city_text = tk.Entry(self.crawl_page)
        self.city_text.grid(row=1, column=1)

        self.location_label = tk.Label(self.crawl_page,
                                       text='请输入地区：').grid(row=2, column=0)
        self.location_text = tk.Entry(self.crawl_page)
        self.location_text.grid(row=2, column=1)

        self.page_label = tk.Label(self.crawl_page,
                                   text='请输入爬取页数：').grid(row=3, column=0)
        self.page_text = tk.Entry(self.crawl_page)
        self.page_text.grid(row=3, column=1)

        self.path_button = tk.Button(self.crawl_page,
                                     text="选择保存路径",
                                     command=self.get_path)
        self.path_button.grid(row=4, column=0)

        self.comfirm_button = tk.Button(
            self.crawl_page,
            text='确定',
            command=lambda: thread_it(self.begin_crawl)).grid(row=5, column=0)

    def go_main(self):
        self.crawl_page.destroy()
        MainPage(self.master)

    def get_path(self):
        path = filedialog.askdirectory(initialdir=os.getcwd())
        self.path = path

    def begin_crawl(self):
        city = self.city_text.get()
        location = self.location_text.get()
        page = self.page_text.get()

        crawler = LianjiaCrawler(city, location, page, self.path)

        self.message_text = tk.Text(self.crawl_page)
        self.message_text.grid(row=6, column=0)

        self.message_text.insert('insert', '开始爬取，正在解析页面...\n')
        url_list = crawler.get_whole_house_url()
        house_list = []
        for url in url_list:
            tip = '正在获取第{}条房源信息\n'.format(url_list.index(url) + 1)
            self.message_text.insert('insert', tip)
            one_piece = crawler.parse_house_info(url)
            house_list.append(one_piece)
            # time.sleep(0.5)
        self.message_text.insert('insert', '完成所有爬取~\n')
        df = crawler.switch_to_pandas(house_list)
        crawler.save_to_path(df)
