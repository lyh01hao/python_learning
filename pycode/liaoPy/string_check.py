#!/usr/bin/env python
# -*- coding: utf-8 -*-

inputstr = input('Please input your information')
itemstr = inputstr.split(';')

for one in itemstr:
    if ',' not in one:
        continue
    sentence = one.split(',')
    name = sentence[1].replace('the name is').strip()
