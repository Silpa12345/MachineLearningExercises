import sys
import numpy as np

x = np.array([1,2,3,4,5,6,7,8])
print(x.shape, x.dtype)

z=np.array(list('Hello World'))
print(z, z.dtype)

print(np.zeros((2,4)))

print(np.random.rand(8))

c = np.arange(start=1, stop=9)
print(np.all(x==c))