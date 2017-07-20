# -*- coding:utf-8 -*-
"""
created on April 19th,2017
@author :Sherry
description:计算字符串最后一个单词的长度，单词以空格隔开。

"""
import sys
line = input('Please enter a string:')
words = line.split()
print (len(words[-1]))

"""
sample code:
import sys
while True:
    line=sys.stdin.readline().strip()
    if line=='':
        break
    str_t=line.split()[-1]
    print len(str_t)
"""