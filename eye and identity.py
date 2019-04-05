# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 20:51:12 2019

@author: Tanujdeep
"""

###eye and identity

import numpy as np

m,n=list(map(int,input().split()))

arr1=np.eye(m,n)
#np.set_printoptions(legacy='1.13')
# OR
#numpy.set_printoptions(sign=' ')
print (arr1)