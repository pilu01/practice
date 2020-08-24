import re
import requests
import time
import os
from multiprocessing.dummy import Pool


start_url = 'http://www.kanunu8.com/book3/6879/'


def get_source(url):
    """
    获取网页源代码。
    :param url: 网址
    :return: 网页源代码
    """
    html = requests.get(url)
    return html.content.decode('gbk') #这个网页需要使用gbk方式解码才能让中文正常显示


def get_toc(html):
    toc_url_list = []
    toc_block = re.findall('<tr bgcolor="#ffffff">(.*?)</tr>', html, re.S)
    for chapter in toc_block:
        title = re.findall('.html">(.*?)</a>', chapter, re.S)
        url = re.findall('<a href="(.*?)"', chapter, re.S)
        toc_url_list.extend(list(zip(title, url)))

    return toc_url_list


def save(chapter, article):
    os.makedirs('动物农场', exist_ok=True)
    with open(os.path.join('动物农场', chapter + '.txt'), 'w', encoding='utf-8') as f:
        f.write(article)


def query_article(items):
    """
    根据正文网址获取正文源代码，并调用get_article函数获得正文内容最后保存到本地。
    :param url: 正文网址
    :return: None
    """
    title, url = items
    u = start_url + url
    text = get_source(u)
    text_block = re.search('<p>(.*?)</p>', text, re.S).group(1)
    text_block = text_block.replace('<br />', '')
    save(title, text_block)


if __name__ == '__main__':
    html = get_source(start_url)
    datas = get_toc(html)
    # 多线程
    p = Pool(5)
    p.map(query_article, datas)
