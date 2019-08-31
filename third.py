"""
代码的完整性
"""

# 求一个数的整数次方
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        n = 1
        while exponent > 0:
            n *= base
            exponent -= 1
        return n
    else:
        return 1/(power(base, -exponent))


# 打印出从1到最大n位数
def print_max_n(n):
    for i in range(10 ** n):
        print(i)


import logging

def use_logging(func):
    def wrapper():
        logging.warn("{} is running".format(func.__name__))
        return func()
    return wrapper
