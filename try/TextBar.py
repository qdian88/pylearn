# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:13:04 2019

@author: Administrator
"""
#文本进度条
import time
scale = 50
print("执行开始".center(scale // 2,"-"))
start = time.perf_counter()
for i in range(scale+1):
    a = i / scale * 100
    b = "*" * i 
    c = "." * (scale-i)
    end = time.perf_counter()
    print("\r{:.2f}%[{}->{}]{:.2f}s".format(a,b,c,end-start),end="")
    time.sleep(0.1)
print("\n"+"执行结束".center(scale // 2,"-"))