import numpy as np

n,m=list(map(int,input().split()))

arr1=np.array([[int(e) for e in input().split()]for i in range(n)])

print( np.prod(np.sum(arr1,axis=0)))

