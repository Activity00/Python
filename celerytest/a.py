# coding: utf-8

"""
@author: 武明辉 
@time: 18-10-8 下午7:09
"""
from celery import Celery
app = Celery(backend='redis://localhost', broker='redis://localhost/')


@app.task
def add(x, y):
    return x + y


if __name__ == '__main__':
    pass
