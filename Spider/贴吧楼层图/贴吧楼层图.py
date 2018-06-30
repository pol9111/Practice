from multiprocessing.pool import ThreadPool

import os
import requests
from datetime import datetime
from lxml import etree
from urllib import parse
import threading
from multiprocessing import Pool, cpu_count




def loadPage(url):
    """
        作用：根据url发送请求，获取服务器响应文件
        url: 需要爬取的url地址
    """
    print url
    headers = {
    # "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    # 'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
    # 'Accept - Language': 'zh - CN, zh;q = 0.9, en - US;q = 0.8, en;q = 0.7, zh - TW;q = 0.6',
    # }

    request = requests.get(url)
    # 解析HTML文档为HTML DOM模型
    content = etree.HTML(request.content)
    #print content
    # 返回所有匹配成功的列表集合
    link_list = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
    #link_list = content.xpath('//a[@class="j_th_tit"]/@href')
    print(link_list)
    for link in link_list:
        fulllink = "http://tieba.baidu.com" + link
        # 组合为每个帖子的链接
        #print link
        loadImage(fulllink)


# 取出每个帖子里的每个图片连接
def loadImage(link):
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    #     'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
    # }
    request = requests.get(link)
    # 解析
    content = etree.HTML(request.content)
    # 取出帖子里每层层主发送的图片连接集合
    #link_list = content.xpath('//img[@class="BDE_Image"]/@src')
    # link_list = content.xpath('//div[@class="post_bubble_middle"]')
    link_list = content.xpath('//img[@class="BDE_Image"]/@src')
    # 取出每个图片的连接
    for link in link_list:
        print (link)
        writeImage(link)


def writeImage(link):
    """
        作用：将html内容写入到本地
        link：图片连接
    """
    print ("正在保存 " + filename)
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    #     'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
    # }
    # 文件写入
    request = requests.get(link)
    # 图片原始数据
    image = request.content
    # 取出连接后10位做为文件名
    filename = link[-10:]
    # 写入到本地磁盘文件内
    with open(filename, "ab") as f:
        f.write(image)
    print ("已经成功下载 "+ filename)

def tiebaSpider(url, beginPage, endPage):
    """
        作用：贴吧爬虫调度器，负责组合处理每个页面的url
        url : 贴吧url的前部分
        beginPage : 起始页
        endPage : 结束页
    """
    start_time = datetime.now()
    urls = []
    pool = Pool(processes=cpu_count())
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        #filename = "第" + str(page) + "页.html"
        fullurl = url + "&pn=" + str(pn)
        urls.append(fullurl)

    pool.map(loadPage, urls)
    #     loadPage(fullurl)
    end_time = datetime.now()
    total_time = end_time - start_time
    print ("谢谢使用, 总时间:", total_time)

if __name__ == "__main__":
    path = 'F:\py_first\\new'
    if not os.path.exists(path):
        os.mkdir(path)
        os.chdir(path)
    kw = input("请输入需要爬取的贴吧名:")
    beginPage = int(input("请输入起始页："))
    endPage = int(input("请输入结束页："))
    url = "http://tieba.baidu.com/f?"
    key = parse.urlencode({"kw": kw})
    fullurl = url + key
    tiebaSpider(fullurl, beginPage, endPage)

















