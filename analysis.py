#!/usr/bin/env python3

import re
import time
import os

NAMES = ['沈祖凡', '陈雯婷', '麻瑀谌', '冯炅', '马晓涵', '陶宛琪']

out = open('output.csv', 'w', encoding='utf-8')
out.write(','.join(['Time']+NAMES))
out.write('\n')
filenames = [i for i in os.listdir() if re.match('crawl-([0-9]+).html', i)]
filenames.sort()
for filename in filenames:
    out.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(re.findall('crawl-([0-9]+).html', filename)[0]))))
    out.write(',')
    with open(filename, 'r', encoding='gbk') as f:
        s = f.read()
        sep = re.findall('<font color=#FF0000>([0-9]+)</font>', s)
        out.write(','.join(sep))
    out.write('\n')
print('Output has been written to output.csv')
