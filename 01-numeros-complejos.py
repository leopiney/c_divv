import numpy as np


def im_equals(value, modulo=1, argument=np.pi):
    return np.allclose(value, modulo * np.e ** (argument * 1j))

