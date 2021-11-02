"""
Given the input data of points [(1, 2), (3,4), (5,6), (8, 8), (7, -1)], fit a line of the form
Y = A * X + B. Return the values (A, B) as a tuple
"""
import numpy as np

def lin_interpolate(data):
    """
    :param data: List of points to linearly interpolate, each of which is provided as a tuple.
    :return: The optimal A and B of your fit line
    """
    # We recognize that if we are trying to solve the equation XM = y (where M = [A, b])
    # then we use matrix algebra to find the solution is M = (X^T*X)^{-1}*X^T*y
    # Here X is a 2d array with the first column being all our X-values and the
    # second column being a column of all 1s. Convince yourself why this is an equivalent representation
    # to our desired problem.
    data = np.array(data)
    X = np.ones_like(data)
    X[:, 0] = data[:, 0]
    inverted = np.linalg.inv(np.dot(X.transpose(), X))
    coeff = np.dot(inverted, np.dot(X.transpose(), data[:, 1]))
    return tuple(coeff)

a=lin_interpolate([(1, 2), (3,4), (5,6), (8, 8), (7, -1)])
print(a)