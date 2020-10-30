# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 11:42
# @Author  : xhb
# @FileName: base.py
# @Software: PyCharm


# 利用yield 控制内存大小
def get_lines():
    l = []
    for i in range(1, 100000):
        if i % 10 != 0:
            l.append(i)
        else:
            l.append(i)
            yield l
            l = []

