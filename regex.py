#!/bin/env python
# -*- coding: utf-8 -*-

import re

# s = 'javapythonc++php'
# print(re.findall('a', s))
#
# s = "<html><h1>hello world<h1></html>"
# print(re.findall('<h1>(.*)<h1>', s))
#
# s = '我喜欢身高为170的女孩'
# print(re.findall('\d+', s))
#
# s = 'http://www.baidu.com and https://boob.com'
# print(re.findall('https?://', s))

# s = 'lalala<hTml>hello</HtMl>hahah'
# print(re.findall('<.*>(.*)<.*>', s))
#

# string = '''Fall in love with you
# i love you very much
# i love she
# i love her'''
#
# print(re.findall('^.*', string, re.M))

s = 'bobo@hit.edu.com'
print(re.findall('(h.*?)\.', s))

s = 'saas and sas and saaas'
print(re.findall('sa{1,2}s', s))

s = """<div>静夜思
窗前明月光
疑是地上霜
举头望明月
低头思故乡
</div>"""

print(re.findall('[\u4e00-\u9fa5]+', s, re.S))