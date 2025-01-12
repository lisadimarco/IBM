import numpy as np

a = np.array([0, 1, 2, 3, 4])

print(a)
print(type(a))
print(a.dtype)
print(a.size)
print(a.ndim)
print(a.shape)

c = np.array([20, 1, 2, 3, 4])
c[0] = 100
d = c[1:4]
c[4] = 0
c[3:5] = 300, 400

print(c)