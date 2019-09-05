# 线程池
from concurrent import futures
from concurrent.futures import ThreadPoolExecutor, as_completed



# 线程池 为什么要线程池
# 主线程中可以获取某一个线程的状态或者某一个任务的状态，以及返回值

import time
from threading import Thread


def get_html(times):
    time.sleep(times)
    print('get page {} success'.format(times))
    return times

executor = ThreadPoolExecutor(max_workers=2)
task1 = executor.submit(get_html, (3))
task2 = executor.submit(get_html, (2  ))

# 用于判定某个人物是否完成
print(task1.done())

# print(task1.result())

import this
