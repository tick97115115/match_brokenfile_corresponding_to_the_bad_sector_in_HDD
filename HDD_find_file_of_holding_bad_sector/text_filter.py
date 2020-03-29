#!/usr/bin/env python3 
# -*- coding:utf-8 -*-

import os

def arangement(text,separator):
    
    n = 0
    def alignment(text_0):
        nonlocal n
        n = n + 1
        return str(n) + text_0
    try:
        result =  map(alignment,text.split(separator))
        print(result)
    except TypeError:
        print('The argument \'text\' of function arangement receive the obejct \'str\' ,instead of %s' % type(text))





if __name__ == "__main__":
    t = '华北水利水电大学、郑州大学、河南理工大学、郑州轻工业学院、河南工业大学、河南科技大学、中原工学院、河南农业大学、河南师范大学、信阳师范学院、周口师范学院、安阳师范学院、许昌学院、南阳师范学院、商丘师范学院、郑州航空工业管理学院、黄淮学院、平顶山学院、安阳工学院、南阳理工学院、河南城建学院、黄河科技学院、郑州科技学院、郑州工业应用技术学院、商丘工学院、河南师范大学新联学院、信阳学院、安阳学院、新乡医学院三全学院、河南科技学院新科学院、郑州工商学院、商丘学院、郑州成功财经学院、郑州升达经贸管理学院'
    s = '、'
    #map(ord,t)
    arangement(t,s)
    #print(t.split(s))
    #print(t)