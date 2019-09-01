# 什么是迭代协议
# 迭代器是什么？ 迭代器是访问集合内元素的一种方式，一般用来遍历数据
# 迭代器和以下标的访问方式不一样，迭代器是不能返回的，迭代器提供一种惰性访问数据的方式
#  [] list  __getitem__

# python 中的协议
from collections.abc import Iterable, Iterator


# 斐波那契数列
# 1 1 2 3 5 8

def fib(index):
    n, a, b = 0,0,1
    while n < index:
        yield b
        a, b = b, a+b
        n += 1


# 读取大文件，500g, 一行
def myreadlines(f, newline):
    # f 是文件， newline是分隔符
    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline)]
        chunk = f.read(4096*10)
        if not chunk:
            yield buf
            break
        buf += chunk




