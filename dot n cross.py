import numpy as np

n = int(input())

arr1=np.array([[e for e in input().split()]for i in range(n)],int)

arr2=np.array([[e for e in input().split()]for i in range(n)],int)

print(np.dot(arr1,arr2))

