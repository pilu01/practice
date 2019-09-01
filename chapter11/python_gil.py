# GIL 全局解释器锁
# python 中一个线程对应与c语言中的一个线程，
# gil 一次只有一个线程运行在一个cpu上执行 字节码, 无法将多个线程映射到多个cpu上
# gil 在遇到io操作的时候主动释放

# import dis
#
# def add(a):
#     a += 1
#     return a
#
# print(dis.dis(add))


total = 0


def add():
    global total
    for i in range(10000000):
        total += 1


def desc():
    global total
    for i in range(10000000):
        total -= 1

import threading

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=desc)
thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)
