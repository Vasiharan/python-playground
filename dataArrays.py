import array
import numpy as np

L = list(range(10))
A = array.array('i', L)
print(A)

print(np.array([1,2,3,4]))

# explicitly set the data type of the resulting array
print(np.array([1,2,3,4], dtype='float32'))


# nested lists in multi-dimensional arrays
multiArray = np.array([range(i, i + 3) for i in [2, 4, 6]])
print(multiArray)

# create an array of five values evenly spaced between 0 and 1
print(np.linspace(0, 1, 5))


# create a 3x3 array of random values between 0 and 1
print(np.random.random((3,3,)))

# create a 3x3 indentity matrix
print(np.eye(4))













