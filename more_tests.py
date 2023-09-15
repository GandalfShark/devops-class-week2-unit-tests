"""
unit tests based on chapter 3 Cisco DevOPs class, which is written for people
who already know how to program and write tests .. so yea... and
https://docs.python.org/3/library/unittest.html
"""
import unittest


class Tests(unittest.TestCase):
    # create class test based on the superclass unitest.TestCase
    def test_add3(self):
        # make a method to test the function add3, created below
        self.assertEqual(add3(4), 7), 'ERROR in math'
        # check to see if passing 4 into add3 returns 7, and these are the SAME TYPE
        self.assert_(add3(100), 103)
        # check if this function returns the value
        self.assertIs(add3(-4), -1)
        # check to see if these are the same object, I don't think they are

        # this could be done with assert_, assertIs, or assertEqual(a, b)
        # they all check if a is the same as b, but in different ways
        # all three tests pass but there is a warning


def add3(number):
    """
    returns the number input plus three
    """
    return number + 3
    # no point in making a var to hold a number we are just returning,
    # change added number to fail test


if __name__ == 'main':
    # check to see if this file is being run directly, as opposed to called from an import
    unittest.main()
    # run the tests if it is
