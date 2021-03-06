#!/usr/bin/env python3

import re
import time
import os

NAMES = ['\u6c88\u7956\u51e1', '\u9648\u96ef\u5a77', '\u9ebb\u7440\u8c0c', '\u51af\u7085', '\u9a6c\u6653\u6db5', '\u9676\u5b9b\u742a']

out = open('output.csv', 'w', encoding='utf-8-sig', newline='\r\n')
out.write(','.join(['Time'] + NAMES))
out.write('\n')
filenames = sorted([i for i in os.listdir() if re.match('crawl-([0-9]+).html$', i)])
for filename in filenames:
    try:
        out.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(re.findall('crawl-([0-9]+).html', filename)[0]))))
        out.write(',')
        with open(filename, 'r', encoding='gbk') as f:
            s = f.read()
            sep = re.findall('<font color=#FF0000>([0-9]+)</font>', s)
            out.write(','.join(sep))
    except Exception as e:
        print('Error: %s' % e)
    out.write('\n')
print('Output has been written to output.csv')
