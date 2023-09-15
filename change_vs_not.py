"""
quirks of mutable vs immutable based on tech with tim vid
https://www.youtube.com/watch?v=mMv6OSuitWw
"""
print('\n ~~~ TUPLE ~~~')
x = (1, 2, 3)
# creates an immutable object x that is a tuple
y = x
# COPIES the value of the tuple
x = [7, 8, 'potato']
# assigns a new value to x making it a list
print(f'X is = {x}\nY is = {y}')
# note that the value of y does not change

# --- doing the same thing with a list --- #
print('\n ~~~ LIST ~~~')
a = [1, 2, 3]
# creates an mutable object a that is a list
b = a
# creates a REFERENCE to the a object
a[0] = 25
# assigns a new value to the 0th position
# but if you re-assign the entire var b will not change
print (f'a is = {a}\nb is = {b}')
'''
note:
the value of b CHANGES, because it is a LINK to a not a copy
any changes to the object stored in a will affect the things linked to it
that includes passing it into a function as an argument 
because the argument is another LINK back to the original object
'''
print('\n ~~~ passing mutable list above into a function ~~~')


def foo(input_argument):
    input_argument.sort()
    print(f'your sorted is is: {input_argument}')
    # note that this function does not return a value

foo(a)
print(f'a is now: {a} and b is now {b}')
# a changes but b does not

# # # more notes - DevOps cisco stuffs# # #
print('\nstяings doing wierd things:')
this_string = 'pasta '
print(this_string*3)
# you can multipy strings
this_string += 'and snail repellent'
# you can also concatenate them with + in some odd ways
print(this_string)

