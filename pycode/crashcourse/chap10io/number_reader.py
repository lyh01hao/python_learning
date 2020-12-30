#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@Author : Yihao Lin

'''

import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)
print(numbers)