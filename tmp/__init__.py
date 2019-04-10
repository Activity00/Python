# coding: utf-8

"""
@author: 武明辉 
@time: 19-4-8 下午10:38
"""


class Format:
    def __init__(self, path_name, rw):
        self.content = self._get_content(path_name)

    def _get_content(self, path_name):
        with open(path_name, 'r') as f:
            return f.read()


class FreeMindFormat(Format):
    pass


class MarkdownFormat:
    pass


class BaseConvert:
    source_format_class = None
    target_format_class = None

    def __init__(self, source_path, target_path):
        self._check_format()
        self.source_format = self.source_format_class(source_path, 'r')
        self.target_format = self.target_format_class(target_path, 'w')

    def convert(self):
        raise NotImplemented

    def _check_format(self):
        assert self.source_format_class is not None
        assert self.target_format_class is not None


class FreeMind2MDConvert(BaseConvert):
    source_format_class = FreeMindFormat
    target_format_class = MarkdownFormat

    def convert(self):
        self.source_format


class MD2FreeMindConvert(BaseConvert):
    source_format_class = MarkdownFormat
    target_format_class = FreeMindFormat


if __name__ == '__main__':
    convert = FreeMind2MDConvert('./xxx.mm')
    convert.convert()

