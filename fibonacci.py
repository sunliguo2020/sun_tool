# -*- coding: utf-8 -*-
"""
@author: sunliguo
@contact: QQ376440229
@Created on: 2022/2/20 13:14
"""


def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1


if __name__ == '__main__':
    fib = fibonacci(100)
    print(type(fib))
    for i in fib:
        print(i, end="  ")
