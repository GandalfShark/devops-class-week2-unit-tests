"""
based on example code from Cisco DevOps class - chapter three
code modified from example provided to be PEP8 and have clear errors in tests
variable names changed to be clear and eliminate need for additional comments
"""
from math import isclose


def add5(input_number):
    """
    takes a number and adds 5 to it and returns the new value
    """
    assert (isinstance(input_number, int) or isinstance(input_number, float)), 'ERROR! need a number as input to function'
    # make sure the numer is number, test is now built into the function
    # makes more sense to me incase the vars passed in from another part of the program change, IMHO
    new_value = input_number + 5
    return new_value


def tests_add5():
    check_value = add5(1)
    assert check_value == 6
    # assert r == 7
    # if the test is wrong, then you will still get an error the
    # commented out code checks here to see if 1+5 = 7, BE CAREFUL WHEN WRITING
    check_value = add5(5)
    assert check_value == 10
    # duh
    check_value = add5(10.2034556)
    assert isclose(check_value, 15.2034556, rel_tol=1e-9)
    # modified to allow for floating point math errors
    # math.isclose(a, b, rel_tol, abs_tol) <-- syntax


#tests_add5()
add5(4)
# uncomment to trigger custom message with Assertion Error. 
