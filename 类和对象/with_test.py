# try except finally


import contextlib


# 将一个普通函数生成一个上下文管理器
@contextlib.contextmanager
def file_open(filename):
    print('file open')
    yield "dsadasd"
    print('file exit')



with file_open('body.txt') as f:
    print('file processing')