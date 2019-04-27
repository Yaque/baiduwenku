# encoding:utf8
from PyQt5.QtCore import QThread
from PyQt5 import QtCore
from selenium import webdriver
import time
from WenKu import BaikuSpider


class MyWorkThread(QThread):
    trigger = QtCore.pyqtSignal(str)

    def __int__(self):
        super(MyWorkThread, self).__init__()
        self.search_key = None
        self.save_path = None

    def set_paramter(self, search_key, save_path, number):
        self.search_key =search_key
        self.save_path = save_path
        self.number = number

    def run(self):
        print(self.search_key)
        all_down_file = []
        browser = webdriver.Chrome()

        # 打开百度文库的首界面
        browser.get("https://wenku.baidu.com/")
        # 通过ID找网页的标签，找到搜索框的标签
        seek_input = browser.find_element_by_id("kw")
        # 设置搜索的内容
        contents = self.search_key
        seek_input.send_keys(contents)
        # 找到搜索文档按钮
        seek_but = browser.find_element_by_id("sb")
        # 并点击搜索文档按钮
        seek_but.click()
        # 设置是否为第一次打开点击搜索按钮
        isfirst = True
        down_c = 0
        get_out = False
        print(self.number)
        while True:
            # 是，需要去掉我知道了按钮
            if isfirst:
                btn_know = browser.find_element_by_class_name("btn-know")
                btn_know.click()
                isfirst = False
                # 去掉之后睡眠2s
                time.sleep(2)

            # 获取所有的文档a标签，这里的elements指的是有多个元素,*表示的是任意的（在xpath中可以用）
            # div[5]指第5个div
            all_a = browser.find_elements_by_xpath("//*[@id=\"bd\"]/div/div/div[5]/div/dl[*]/dt/p[1]/a")
            # 用于存储下当前页面的所有文档链接
            list_one_page_file = []

            for a in all_a:
                a_href = a.get_attribute("href")
                a_title = a.get_attribute("title")
                a_href = a_href.split("?")[0]
                if a_title != "" and a_href !="":
                    list_one_page_file.append([a_href, a_title])
                    baiku = BaikuSpider(self.save_path)
                    baiku.run(a_href)
                    # 循环完毕后发出信号
                    self.trigger.emit(a_href + "+:+" + a_title + "+:+" + str(down_c))
                    # print(down_c)
                    if down_c == self.number:
                        get_out = True
                        break
                    down_c += 1
                    # print(a_href)
                    # print(a_title)
            all_down_file.append(list_one_page_file)
            if get_out:
                break

            # 获取body标签，的html
            body = browser.find_element_by_tag_name("body")
            body_html = body.get_attribute("innerHTML")

            # 判断下一页按钮是否存在
            flag = str(body_html).find("class=\"next\"")
            if flag != -1:
                # 获取下一页按钮的标签，这里用的是class标签，因为它只有一个
                next_page = browser.find_element_by_class_name("next")
                # 点击下一页
                next_page.click()
                # 点击之后，睡眠5s，防止页面没有加载完全，报no such element的错误
                time.sleep(5)
            else:
                break

        # 保存本次下载的所有文件的连接和文件名
        with open(self.save_path + "/" + self.save_path + ".txt", "w+") as download_f:
            # print(len(all_down_file[0]))
            for one in all_down_file:
                for data in one:
                    download_f.writelines(data[0] + "====" + data[1] + "\n")

        self.trigger.emit("plsay" + "+:+I like you, my wife." + "+:+I promise.")
