import time, threading


detail_url_list = []

def get_detail_html(url):
    # 爬取文章详情页
    global detail_url_list
    url = detail_url_list.pop()
    # for url in detail_url_list:
    print('get detail html start')
    time.sleep(2)
    print('get detail html end')


def get_detail_url(url):
    # 爬取文章列表页
    global detail_url_list
    print('get detail url start')
    time.sleep(4)
    for i in range(20):
        detail_url_list.append("http://projectsedu.com/{}".format(i))
    print('get detail url end')



"""
1, 通过共享变量通信
"""

thread_detail_url = threading.Thread(target=get_detail_url)
for i in range(10):
    html_thread = threading.Thread(target=get_detail_html)
    html_thread.start()