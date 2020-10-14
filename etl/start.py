# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 9:18
# @Author  : xhb
# @FileName: start.py
# @Software: PyCharm

from functools import reduce


class Field():
    def __init__(self, column_type, max_length, **kwargs):
        self.column_type = column_type
        self.max_length = max_length
        self.default = None
        if kwargs:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)


class StringField(Field):
    def __init__(self, max_length, **kwargs):
        super().__init__(column_type='VARCHAR({})'.format(max_length), max_length=max_length, **kwargs)


class IntegerField(Field):
    def __init__(self, **kwargs):
        super().__init__(column_type='bigint', max_length=8)


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] = attrs.get('__table__', None) or name
        print(mappings)
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        for k, v in self.__mappings__.items():
            fields.append(k)
            params.append(getattr(self, k, v.default))
        sql = "insert into {} ({}) values ({})".format(self.__table__, self.join(fields), self.join(params))
        print('SQL: %s' % sql)

    def join(self, attrs, pattern=','):
        return reduce(lambda x, y: '{}{}{}'.format(x, pattern, y), attrs)


class User(Model):
    __table__ = 'User_info'

    id = IntegerField(primary_key = True)
    name = StringField(max_length=50)
    email = StringField(max_length=50, default='xx@qq.com')


if __name__ == '__main__':
    u = User(id=123, name='xhb')
    u.save()
