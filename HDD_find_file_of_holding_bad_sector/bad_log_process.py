#!/usr/bin/env python3
# -*- coding:utf-8 -*-

text = open(r'C:\Users\APboi\Desktop\bads_WDC WD10SDZW-11UMGS0_WD-WXN1AA7K3Z8N.txt',mode='r',encoding='utf-8')
a = text.read()
b = a.split('\n')
c = [x for x in b if x != '']
d = [x for x in c if x[-1] == 'd']
e = [x.split(',')[0] for x in d]

from map_broken_files import *

mapping(LBA_to_CHS(4096,512,e))