
from . import *

def test_are_close():

    assert are_close(0.1, 0.1)
    assert are_close(-1/3, -1/3)
    assert are_close(0, 0)
    assert are_close(1e20, 1e20)

    assert are_close(0.1320, 0.1315, 0.001)
    assert are_close(0.0002, -0.0002, 0.001)
    assert are_close(-0.0002, 0.0002, 0.001)

    assert are_close(1e-10, 1e-10, 1e-9)
    assert are_close(1e-10, 9e-10, 1e-9)
    assert are_close(-1e-10, 1e-10, 1e-9)
    assert are_close(1e-10, -1e-10, 1e-9)

    assert are_close(1000, 1010, 20)
    assert are_close(-10, 10, 30)
    assert are_close(10, -10, 30)

    assert are_close(1e20, 9e19, 2e19)
    assert are_close(-1e10, 1e10, 1e21)

def test_product():

    assert product([]) == 1
    assert product([1]) == 1
    assert product([0]) == 0
    assert product([-1]) == -1

    assert product([1, 2]) == 2
    assert are_close(product([1/2, 2]), 1)

    assert product([-1, -1]) == 1
    assert product([-2, -3, -4, -5]) == 120

    assert product(range(1, 11)) == factorial(10)
