# coding: utf-8

"""
@author: 武明辉 
@time: 17-9-28 上午8:40
"""


class Model(dict):
    """
    Model从dict继承，所以具备所有dict的功能，同时又实现了特殊方法__getattr__()和__setattr__()，所以又可以像引用普通字段那样写：
    >>> user['id']
    123
    >>> user.id
    123
    """
    __metaclass__ = ModelMetaclass

    def insert(self):
        params = {}
        for k, v in self.__mappings__.iteritems():
            params[v.name] = getattr(self, k)
        db.insert(self.__table__, **params)
        return self

    @classmethod
    def get(cls, pk):
        d = db.select_one('select * from %s where %s=?' % (cls.__table__, cls.__primary_key__.name), pk)
        return cls(**d) if d else None

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        mapping = ... # 读取cls的Field字段
        primary_key = ... # 查找primary_key字段
        __table__ = cls.__talbe__ # 读取cls的__table__字段
        # 给cls增加一些字段：
        attrs['__mapping__'] = mapping
        attrs['__primary_key__'] = __primary_key__
        attrs['__table__'] = __table__
        return type.__new__(cls, name, bases, attrs)