class Aninmal():
    @classmethod
    def say(cls):
        print('i am a {}'.format(cls.__name__))


class Cat(Aninmal):
    pass


class Dog(Aninmal):
    pass


class Duck(Aninmal):
    pass


# Cat().say()
# Dog().say()
# Duck().say()


# 抽象基类（abc模块 ）
# 我们需要强制某个子类必须实现某些方法
# 实现了一个web框架，集成cache(redis, cache, memorychache)
# 需要设计一个抽象基类，指定子类必须实现某些方法


import abc


# 强制子类实现get、set 方法，否则报错
class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass



