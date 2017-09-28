# coding: utf-8

"""
@author: 武明辉 
@time: 17-9-28 上午8:40
"""


class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column = column_type

    def __str__(self):
        return '<%s:%s>'%(self.__class__,self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                mappings[k] = v

        for k in mappings.iterkeys():
            attrs.pop(k)

        attrs['__table__'] = name
        attrs['__mappings__'] = mappings

        return type.__new__(cls, name, bases, attrs)


class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError('Model object has no attribute %s'%item)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        arags = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            arags.append(getattr(self,k,None))
        sql = 'insert into %s (%s) values (%s)'%(self.__table__,','.join(fields),','.join(params))
        print(sql)


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


u = User(id=12345, name='wmh', email='xxx.xx',password='****')
u.save()
