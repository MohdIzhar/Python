# Float - 64 bit Representation
# 1 sign bit
# 11 bits exponent (the value to which the fraction is raised)
# 52 bits mantissa (dedicated to represent fractions)

# Python floats of 15-17 digits of decimal precision 
# We can convert decimals with 15 figures intp python floats and back without loss of information.

import sys

# print(sys.float_info)
most_negative_float = -sys.float_info.max
greatest_negative_float = -sys.float_info.min

print("most_negative_float: ", most_negative_float)
print("greatest_negative_float: ", greatest_negative_float)

# Loss of Precision
print("--------Loss of Precision--------")
print(float(10))
print(2**53)
print(float(2**53))
print(float(2**53+1))
print(float(2**53+2))
print(float(2**53+3))
print(float(2**53+4))

# Some fractional values cant be accurately represented with float

print(0.8 - 0.7)

# To know more about float see David Goldberg's classic "What Every Computer Scientist Should know about Floating Point Arithmetic"
