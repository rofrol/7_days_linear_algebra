# matrix dot product
import numpy
from numpy import array
A = array([[1, 2], [3, 4], [5, 6]])
B = array([[6, 5], [4, 3], [2, 1]])

#implement more matrix arithmetic operations such as subtraction, division, the Hadamard product, and vector-matrix multiplication.


def substraction (m1, m2):
    a = array([])
    for (x,y), value in numpy.ndenumerate(m1):
        a = numpy.append(a, value - m2[x, y])
    return a

print(substraction(A, B))
