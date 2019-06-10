import numpy
# multiply vectors
from numpy import array
a = array([1, 2, 3])
print(a)
b = array([1, 2, 3])
print(b)
c = a * b
print(c)


# implement other vector arithmetic operations such as addition, division, subtraction, and the vector dot product.

def addition (v1, v2):
    a = array([])
    for idx, val in enumerate(v1):
        a = numpy.append(a, val + v2[idx])
    return a

print(addition(a, b))

def division (v1, v2):
    a = array([])
    for idx, val in enumerate(v1):
        a = numpy.append(a, val / v2[idx])
    return a

print(division(a, b))

def substraction (v1, v2):
    a = array([])
    for idx, val in enumerate(v1):
        a = numpy.append(a, val - v2[idx])
    return a

print(substraction(a, b))

def dotproduct (v1, v2):
    a = 0
    for idx, val in enumerate(v1):
        a = a + val * v2[idx]
    return a

print(dotproduct(a, b))
