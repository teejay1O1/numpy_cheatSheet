import numpy as np

#np.set_printoptions(legacy='1.13')
# OR
#numpy.set_printoptions(sign=' ')
arr1= np.array([(i) for i in input().split()],float)

print (np.floor(arr1))
print (np.ceil(arr1))
print (np.rint(arr1))
