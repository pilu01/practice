import aiomysql


class Field():
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default


class StringField(Field):
    def __init__(self, name=None, column_type='varchar(100)', primary_key=False, default=None):
        super().__init__(name, column_type, primary_key, default)


class BooleanField(Field):

    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)


# 整数类型
class IntegerField(Field):

    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)


# 浮点类型
class FloatField(Field):
    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)


# 长文本类型
class TextField(Field):
    def __int__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)


def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ', '.join(L)


class ModeelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        pass




