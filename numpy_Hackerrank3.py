# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 00:41:22 2019

@author: Tanujdeep
"""

import numpy as np

n,m=map(int,input().split(" "))

l=[[int(e) for e in input().split()] for i in range(n)]

arr1=np.array(l)

arrt=np.transpose(arr1)

arrf=arr1.flatten()

print(arrt)
print(arrf)