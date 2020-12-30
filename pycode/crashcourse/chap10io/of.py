#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@Author : Yihao Lin

'''
with open('digit.txt') as opened_file:
    s = opened_file.read()
print(s)

with open('digit.txt') as opened_file:
    for line in opened_file:
        print(line.rstrip())

with open('digit.txt') as opened_file:
    lines = opened_file.readlines()

for line in lines:
    print(line.rstrip())
