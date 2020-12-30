#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
poem = ''' \
        Programme is fun
        When the work is done
        if you wanna make your work also fun:
            use Python!
'''

f = open('poem.md', 'w')
f.write(poem)
f.close()

f = open('poem.md')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end = '')
f.close()
