# speed
import time
l1 = [i for i in range(10000000)]
l2 = [i for i in range(10000000, 20000000)]
l3 =[]

start = time.time()
for i in range(len(l1)):
    l3.append(l1[i]+l2[i])
print(time.time() - start)

import numpy as np
a = np.arange(10000000)
b = np.arange(10000000)
start = time.time()
c = a+b
print(time.time() - start)

# Memory

import sys

print(sys.getsizeof(l1))


print(sys.getsizeof(a))