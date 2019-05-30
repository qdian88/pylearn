# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 11:04:43 2019

@author: Administrator
"""
m=10**3
s_max=0
for i in range(m-1,m//10,-1):
    for j in range(m-1,i-1,-1):
        s=i*j
        if str(s)==str(s)[::-1] and s > s_max:
            s_max=s
            print(s)
print(s_max)