# coding: utf-8

"""
@author: 武明辉 
@time: 17-9-16 下午4:02
"""
import string

from PIL import Image
import argparse

chars = string.printable

parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o', '--output')
parser.add_argument('--width', type=int, default=80)
parser.add_argument('--height', type=int, default=80)

args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(chars)
    gray = int(0.2126*r+0.7152*g+0.0722*b)

    unit = (256.0 + 1)/length
    return chars[int(gray/unit)]


if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open('output.txt', 'w') as f:
            f.write(txt)

