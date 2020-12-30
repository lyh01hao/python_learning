#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@Author : Yihao Lin

'''
favourite_language = {
    'jen': 'python',
    'edward': 'ruby',
    'phil': 'python',
     }
for name, lang in favourite_language.items():
    print(f"{name.title()}'s favourite language is {lang.title()}\n")

for name in favourite_language.keys():
    print(name)

for name in favourite_language:
    print(name.title(), end = '\t')
    print(favourite_language[name].title())

print('not repeated')
for lang in set(favourite_language.values()):
    print(lang.title())

print(favourite_language.values())