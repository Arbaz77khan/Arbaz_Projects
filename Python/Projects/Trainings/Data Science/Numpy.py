import numpy as np

# 1D Array
a = np.array([1,2,3])   #Also know as vector

# 2D Array
b = np.array([[1,2,3],[4,5,6]])   #Also know as metrics

# 3D Array
c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])   #Also know as tensor

d = np.array([1,2,4], dtype=float)  # By default it is int. However we can change the type using dtype.

print(a.dtype)

a.astype(np.int64)

print(a.dtype)

e = np.arange(1, 11) #Same as range function in python

f = np.arange(1, 13).reshape(3, 4) # To change the shape of array.

# To Intialize the array.
g = np.ones((2,3))
h = np.zeros((2,3))
i = np.random.random((2,3))

j = np.linspace(1, 10, 4) #lower range, upper range, number of items -> It will create an array of item which are equidistance within the range.

k = np.identity(3)

print(type(a))

print(a)

print(b)

print(c)

print(d)

print(e)

print(f)

print(g,h,i)

print(j)

print(k)