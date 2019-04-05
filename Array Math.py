import numpy as np

n,m=list(map(int,input().split()))
#n is no. of rows and m is no. of clumns
arr1=np.array([[int(e) for e in input().split()]for k in range(n)])
arr2=np.array([[int(e) for e in input().split()]for k in range(n)])    

print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1//arr2)
print(arr1%arr2)
print(arr1**arr2)