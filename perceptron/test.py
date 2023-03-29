from base import *

def test_base():
    a = ([[1, 1, -1.5], [1, 1, -0.5]])
    b = ([0, 1, 1])
    print(dot(a, b), 'our')

    a = np.array([[1, 1, -1.5], [1, 1, -0.5]])
    b = np.array([0, 1, 1])
    print(np.dot(a, b), 'np')



test_base()