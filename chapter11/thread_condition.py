from threading import Condition
import threading
# 条件变量，用于复杂的线程间同步
# wait 方法只有通过notif 才能唤醒

class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name='小爱')
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print('{} : 在'.format(self.name))
            self.cond.notify()

            self.cond.wait()
            print('{} : 好啊'.format(self.name))
            self.cond.notify()

            self.cond.wait()
            print('{} : 君住长江尾'.format(self.name))
            self.cond.notify()


class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name='天猫')
        self.cond = cond

    def run(self):
        with self.cond:
            print('{} : 小爱同学'.format(self.name))
            self.cond.notify()
            self.cond.wait()

            print('{}: 我们来对古诗'.format(self.name))
            self.cond.notify()
            self.cond.wait()

            print('{}: 我住长江头'.format(self.name))
            self.cond.notify()
            self.cond.wait()


if __name__ == '__main__':
    lock = threading.Condition()
    xiaoai = XiaoAi(lock)
    tianmao = TianMao(lock)


    xiaoai.start()
    tianmao.start()