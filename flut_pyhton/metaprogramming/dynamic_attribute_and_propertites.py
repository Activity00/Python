# coding: utf-8

"""
@author: 武明辉 
@time: 19-3-10 上午10:54
"""
import keyword
from collections import abc
import json
import os
import warnings
from urllib.request import urlopen

URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = './data/osconfeed.json'


def load():
    if not os.path.exists(JSON):
        msg = 'download {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp)


class FrozenJson:
    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '-'
            self.__data[key] = value
        self.__data = dict(mapping)

    def __new__(cls, item, *args, **kwargs):
        if isinstance(item, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(item, abc.MutableSequence):
            return [cls(item) for item in item]
        else:
            return item

    def __getattr__(self, item):
        """对类及其实例未定义的属性有效。也就属性是说，如果访问的属性存在，就不会调用__getattr__方法。这个属性的存在，包括类属性和实例属性
        """
        if hasattr(self.__data, item):
            return getattr(self.__data, item)
        else:
            return FrozenJson(self.__data[item])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


DB_NAME = 'data/schedule1_db'
CONFERENCE = 'conference.115'


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __eq__(self, other):
        if isinstance(other, Record):
            return self.__dict__ == other.__dict__
        else:
            return NotImplementedError


class MissingDatabaseError(RuntimeError):
    pass


class DbRecord(Record):
    __db = None

    @staticmethod
    def set_db(db):
        DbRecord.__db = db

    @staticmethod
    def get_db():
        return DbRecord.__db

    @classmethod
    def fetch(cls, ident):
        db = cls.get_db()
        try:
            return db[ident]
        except TypeError:
            if db is None:
                msg = 'database'
                raise MissingDatabaseError(msg.format(cls.__name__))
            else:
                raise

    def __repr__(self):
        if hasattr(self, 'serial'):
            cls_name = self.__class__.__name__
            return '<{} serial={!r}>'.format(cls_name, self.serial)
        else:
            return super().__repr__()


class Event(DbRecord):
    @property
    def venue(self):
        key = 'venue.{}'.format(self.venue_serial)
        return self.__class__.fetch(key)

    @property
    def speakers(self):
        if not hasattr(self, '_speaker_obj'):
            spkr_serials = self.__dict__['speakers']
            fetch = self.__class__.fetch
            self._speaker_objs = [fetch('speaker.{}'.format(key)) for key in spkr_serials]
        return self._speaker_objs

def load_db(db):
    raw_data = load()
    warnings.warn('loading' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        for record in rec_list:
            key = '{}.{}'.format(record_type, rec_list['serial'])
            record['serial'] = key
            db[key] = Record(**record)


if __name__ == '__main__':
    feed = load()
    print(sorted(feed['Schedule']))
