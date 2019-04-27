# coding:utf-8

import io
import re
import sys
import requests
from lxml import etree

DOWNLOAD_PATH = "0"
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding="utf8")


class BaikuSpider(object):
    """docstring for BaikuSpider"""
    def __init__(self, d_p):
        self.url = "https://wenku.baidu.com/view/6b2016c49ec3d5bbfd0a742d.html"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                        "Origin": "https://wenku.baidu.com",
                        "Referer": "https://wenku.baidu.com/view/c20e5ad684254b35eefd3402.html"
                        }
        self.downloadUrl = ""
        self.data = {}
        self.name = ""
        self.download_path = d_p
    
    def parse_url(self,url):
        response = requests.get(url,headers=self.headers)
        return response.content.decode("gb2312","ignore")

    def init_post(self,str_content):
        html = etree.HTML(str_content)
        doc_id = re.search(r'view/(\S*)\.html$',self.url).group(1)
        downloadToken = html.xpath("//form/input[@name='downloadToken']/@value")
        sz = html.xpath("//form/input[@name='sz']/@value")
        storage = html.xpath("//form/input[@name='storage']/@value")
        retType = html.xpath("//form/input[@name='retType']/@value")
        ct = html.xpath("//form/input[@name='ct']/@value")
        useTicket = html.xpath("//form/input[@name='useTicket']/@value")
        target_uticket_num = html.xpath("//form/input[@name='target_uticket_num']/@value")
        v_code = html.xpath("//form/input[@name='v_code']/@value")
        v_input = html.xpath("//form/input[@name='v_input']/@value")
        req_vip_free_doc = html.xpath("//form/input[@name='req_vip_free_doc']/@value")
        self.name = html.xpath("//div[@id='doc-header-test']/h1/span/text()")[0].strip();
        self.data = {
            "ct": ct,
            "doc_id": doc_id,
            "retType": retType,
            "storage": storage,
            "useTicket": useTicket,
            "target_uticket_num": target_uticket_num,
            "downloadToken": downloadToken,
            "sz": sz,
            "v_code": v_code,
            "v_input": v_input,
            "req_vip_free_doc": req_vip_free_doc
        }
        file = requests.post("https://wenku.baidu.com/orgvip/submit/download",headers=self.headers,data=self.data)
        if file.content is not None:
            with open(self.download_path + "/" + self.name+".doc","wb") as f:
                f.write(file.content)
            print("下载成功")
            print("="*40)
            print("\n"*3)

    def run(self, url):
        # self.url = input("请输入您要下载的百度文库地址：")
        self.url = url
        #1.发送请求，获取响应内容
        try:
            str_content = self.parse_url(self.url)
        except:
            print("请输入正确的百度文库文档地址（不含get参数）")
            print("="*40)
            print("\n"*3)
        else:
            try:
                 #2.解析内容，构造新请求及表单数据
                self.init_post(str_content)
            except:
                print("下载失败，请使用校内网下载！！！")
                print("="*40)
                print("\n"*3)


if __name__ == '__main__':
    baiku = BaikuSpider()
    baiku.run("https://wenku.baidu.com/view/5ba7b14d854769eae009581b6bd97f192279bfe7.html")
