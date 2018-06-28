import json
import requests
from lxml import etree

url = 'https://www.qiushibaike.com/8hr/page/1/'

HEADERS = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

html = requests.get(url, headers=HEADERS, timeout=10).text

# 响应返回的是字符串，解析为HTML DOM模式 text = etree.HTML(html)
text = etree.HTML(html)

# 返回所有段子的结点位置，contains()模糊查询方法，第一个参数是要匹配的标签，第二个参数是标签名部分内容
node_list = text.xpath('//div[contains(@id, "qiushi_tag")]')

items = {}

for item in node_list:
    # xpath返回的列表，这个列表就这一个参数，用索引方式取出来，用户名
    username = item.xpath('.//a/h2')[0].text
    print(username)
    # 图片连接
    image = item.xpath('.//div[@class="thumb"]/a/img/@src')
    print(image)
    # 取出标签下的内容,段子内容
    content = item.xpath('.//div[@class="content"]/span[@class]/text()')
    print(content)
    # 取出标签里包含的内容，点赞
    up = item.xpath('.//span/i')[0].text
    print(up)
    # 评论
    comments = item.xpath('.//i')[1].text
    print(comments)

    items = {
        "username" : username,
        "image" : image,
        "content" : content,
        "up" : up,
        "comments" : comments
    }

    with open('qiushi.json', 'a') as f:
        f.write(json.dumps(items, ensure_ascii=False) + '\n')
