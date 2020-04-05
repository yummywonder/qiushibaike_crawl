from bs4 import BeautifulSoup
import requests
import time
import random

class Qiushibaike():
    def __init__(self):
        self.url = "https://www.qiushibaike.com/text/"
        #self.headers = {'User-Agent': 'Mozilla/5.0'}
        #self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"}
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}


    # 获取响应
    def get_response(self):
        res = requests.get(url = self.url,headers = self.headers)
        res.encoding = "utf-8"
        html = res.text
        # print(res.status_code)
        # print(html)
        self.parse_page(html)



    # 解析网址
    def parse_page(self,html):
        soup = BeautifulSoup(html,"html.parser")
        r_list = soup.find_all('div',class_= 'article')
        qiushibaike = []
        for item in r_list:
            content = item.find('div', class_='content').find('span').get_text()
            qiushibaike.append(content)
        self.save_text('qiushibaike.txt',qiushibaike)


    # 保存数据
    def save_text(self,filename,list):
        for item in list:
            with open(filename,'a',encoding='utf-8') as fd:
                fd.write(item)
                fd.write("______________________-")

    def main(self):
        self.get_response()





spider = Qiushibaike()
spider.main()

 # x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")

# res = requests.get(url = "https://www.qiushibaike.com/text/", headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0"})
# res.encoding = "utf-8"
# html = res.text
# print(res.status_code)
# print(html)