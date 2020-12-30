#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys 
import time 

f = None
try:
    f = open('poem.md')
    while True:
        line = f.readline()
        if len(line) == 0:
            break 
        print(line, end = '')
        sys.stdout.flush()
        print('Press ctrl+c now')
        time.sleep(1)
except IOError:
    print('Could not find the file')
except KeyboardInterrupt:
    print('!!You cancelled the reading from the file.')
finally:
    if f:
        f.close()
    print('Closed the file.')
