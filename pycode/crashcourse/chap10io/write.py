#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@Author : Yihao Lin

'''
filename = 'test.txt'

with open(filename, 'a') as opened_file:
    opened_file.write('ohayo')
    