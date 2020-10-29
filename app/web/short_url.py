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

code_map = (
    'a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' ,
    'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' ,
    'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' ,
    'y' , 'z' , '0' , '1' , '2' , '3' , '4' , '5' ,
    '6' , '7' , '8' , '9' , 'A' , 'B' , 'C' , 'D' ,
    'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' ,
    'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' ,
    'U' , 'V' , 'W' , 'X' , 'Y' , 'Z'
)


def get_hash_key(long_url):
    res = []
    hex = get_md5(long_url)
    for i in range(0, 4):
        s = ""
        n = int(hex[i*8:(i+1)*8], 16)
        for j in range(0, 6):
            x = 0x0000003D & n
            s += code_map[x]
            n = n >> 5
        res.append(s)
    return res

a = get_hash_key("https://www.cnblogs.com/rickiyang/p/12178644.html")
print(a)