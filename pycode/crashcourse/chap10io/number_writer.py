#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@Author : Yihao Lin

'''
import json

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)