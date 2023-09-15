"""
based on example code from Cisco DevOps class - chapter three
code modified from example provided to be PEP8 and have clear errors in tests
variable names changed to be clear and eliminate need for additional comments
"""


def add5(input_number):
    """
    takes a number and adds 5 to it and returns the new value
    """
    assert (isinstance(input_number, int)), 'ERROR! need integer as input to function'
    # make sure the numer is an integer, test is now built into the function
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
    check_value = add5(10.102645)
    assert check_value == 15.102645
    # they should probably add a tolerance to this as floats are weird - try adding 0.2 to 0.3

tests_add5()
# add5('potato')
# uncomment to trigger custom message with Assertion Error. 
