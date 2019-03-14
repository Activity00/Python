# coding: utf-8

"""
@author: 武明辉 
@time: 19-3-14 下午9:56
"""
import collections


class Validated:
    pass


class EntityMeta(type):
    def __prepare__(metacls, name, bases):
        return collections.OrderedDict()

    def __init__(cls, name, base, attr_dict):
        super().__init__(name, base, attr_dict)
        cls._field_names = []
        for key, attr in attr_dict.items():
            if isinstance(attr, Validated):
                type_name = type(attr).__name__
                attr.storage_name = '_{}#{}'.format(type_name, key)
                cls._field_names.append(key)


class Entity(metaclass=EntityMeta):
    """ Business entity"""
    @classmethod
    def field_names(cls):
        for name in cls._field_names:
            yield name




if __name__ == '__main__':
    pass
