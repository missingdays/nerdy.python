
def are_close(n1, n2, precision=0.001):
    """
    Checks whether two numbers are equal up to precision
    Note that because of rounding errors some results can be unexpected
    """

    return abs(n1-n2) <= precision
