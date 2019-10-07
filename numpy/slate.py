import numpy as np

# matrix with 1 to 15
a = np.arange(15).reshape(3, 5)
print(a)
print(a.ndim)
print(a.size)
print(a.shape)

b = np.random.randn(3, 5)
c = np.array((1,3,2))
print(c)

print(b)
