import numpy as np

n,m=map(int,input().split())
arr1=np.array([[i for i in input().split()]for k in range(n)],int)

print(np.max(np.min(arr1,axis=1)))