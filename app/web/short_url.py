# -*- coding: utf-8 -*-
# @Time    : 2020/10/28 9:11
# @Author  : xhb
# @FileName: short_url.py
# @Software: PyCharm

from app.web import *
import hashlib


def get_md5(s):
    s = s.encode('utf8')
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()


def get_hash_key(long_url):
    res = []
    hex = get_md5(long_url)
    for i in range(0, 4):
        s = ""
        n = int(hex[i*8:(i+1)*8], 16)
        for j in range(0, 6):
            x = 0x0000003D & n
            s += current_app.config['code_map'][x]
            n = n >> 5
        res.append(s)
    return res[0]


@web.route('/shorturl', methods=['POST', 'GET'])
def short_url():
    if request.method == 'POST':
        pass
    return render_template('short_url/index.html')



