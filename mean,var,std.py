import numpy as np
#np.set_printoptions(legacy="1.13")
n,m=map(int,input().split())
arr1=np.array([[i for i in input().split()]for k in range(n)],int)

print(np.mean(arr1,axis=1))
print(np.var(arr1,axis=0))
print(np.std(arr1,axis=None))