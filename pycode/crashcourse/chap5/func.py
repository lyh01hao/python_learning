#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@Author : Yihao Lin

'''

def show(age, money, *book, **details):
    print(age)
    print(f"money is {money}")
    for boo in book:
        print(f"book is {boo}")
    print("\n")
    for key in details.keys():
        print(key)

info = {'name': 'lyh', 'subject': 'cs'}
age = 1
money = 10086
book = ('the', 'one')
show(age, money, book, info)
print('show2')
show(1, 78, 'the', 'two', name = 'lyh', subject = 'cdd')
print(book)
print(info)