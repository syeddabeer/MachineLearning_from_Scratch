"""
Given the input data of points [(1, 2), (3,4), (5,6), (8, 8), (7, -1)], fit a line of the form
Y = A * X + B using gradient descent. Provide the implementation of your algorithm in the function provided.
Then evaluate your linear regression fit on the provided point.
"""
import numpy as np

def linear_interpolate_point(data, test_points):
    """
    Fit a line to the provided data and then evaluate on the provided test point.
    :param data: Collection of points to fit provided as a list of tuples
    :param x: Point to interpolate using your fit line
    :return: The output of your point on the interpolated line
    """
    # fill in the function here
    data = np.array(data)
    print("data: ", data)
    X = np.ones_like(data)
    print("X: ", data)
    X[:, 0] = data[:, 0]
    print("X: ", data)
    inverted = np.linalg.inv(np.dot(X.transpose(), X))
    coeff = np.dot(inverted, np.dot(X.transpose(), data[:, 1]))
    t_arr=np.array(test_points)
    y= np.dot(coeff.transpose(), t_arr)
    return y


a=linear_interpolate_point(
    [(1, 2), (3,4), (5,6), (8, 8), (7, -1)],
    10.5
)

print(a)