from typing import Mapping, MutableSequence


class JsonObj:
    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, item):
        if hasattr(self.__data, item):  # a = {'b': 1} hasattr(a, 'b') ->  False
            return getattr(self.__data, item)
        else:
            return JsonObj.build(self.__data[item])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, Mapping):
            return cls(obj)
        elif isinstance(obj, MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


if __name__ == '__main__':
    maps = {'a': 1, 'b': [{'c': '2'}]}
    jb = JsonObj(maps)
    print(jb.b)
