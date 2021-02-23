# Working with float in python can lead to problem even in small values

import decimal

print(decimal.getcontext())
# prec =  28, this tells by default decimal system is configured with 28 points of decimal precision.

print(decimal.Decimal(5))
# Note when run it return the repr of decimal with string
print(decimal.Decimal('0.8'))
# Decimal also accepts string

# Now run the below example as we run in float
print(decimal.Decimal('0.8') - decimal.Decimal('0.7'))


# Construction with Fractional Values
# Passing the literal value to the constructor as string can be very important

# Now run this
print(decimal.Decimal(0.8) - decimal.Decimal(0.7))
# now notice the difference between the two

# Lets understand whats happening, behind the scene the repl is treating literal type as float
# check using type(0.8) and internally with base 10 representation. and some rounding occurs then these values are then passed to the decimal constructor
# So, it is recommended that always specify fractional decimal literals as string.
# Then the it treat it as Decimal value.

# To avoid float operation
decimal.getcontext().traps[decimal.FloatOperation] = True
# print(decimal.Decimal(0.8))
# this will raise an exception between decimal and float operations

# try this as well
# print(decimal.Decimal('0.8') > 0.7)

# Preserving Decimal Precision and has significant role

a = decimal.Decimal(3)
b = decimal.Decimal('3.0')
c = decimal.Decimal('3.00')
print(a)
print(b)
print(c)

print(a*2)
print(b*2)
print(c*2)

# we have the precession setting in the module context
# lets reduce the precision to six significant figures 
decimal.getcontext().prec = 6
# and preform the computation that exceeds and you will see the limited context precision kick in.
d = decimal.Decimal('1.234567')
print(d)
print(d+decimal.Decimal(1))

# Decimal also supports special values for infinity and Not a Number

print(decimal.Decimal('Infinity'))
print(decimal.Decimal('NaN'))

print(decimal.Decimal('NaN') + decimal.Decimal('1.414'))

# Decimal can be combine safely with Python integers
# and not generally tru for float and other numeric types

# Arithmetic operation with floats will raise a type error.
# print(decimal.Decimal('1.4') + 0.6)
# since it prevents inadverent precision and representation from creeping into programs 
decimal.getcontext().traps[decimal.FloatOperation] = False
# we can compare decimal with floats
print(decimal.Decimal('0.6') > 0.4)

# The result of modulus with Decimal takes its sign from the first operand
print((-7) % 3)
# For int the modulus has the same sign as divisor

# Decimal has different result

print(decimal.Decimal(-7) % decimal.Decimal(3))

# Broken Expectations

def is_odd(n):
    return n % 2 == 1

print(is_odd(2))
print(is_odd(3))
print(is_odd(-2))
print(is_odd(-3))
print(is_odd(2.0))
print(is_odd(3.0))
print(is_odd(-2.0))
print(is_odd(-3.0))

# but it fails with Decimal
print(is_odd(decimal.Decimal(2)))
print(is_odd(decimal.Decimal(3)))
print(is_odd(decimal.Decimal(-2)))
print(is_odd(decimal.Decimal(-3)))
print(decimal.Decimal(-3) % 2)

# to maintain the decimal result
# use this
# def is_odd(n):
    # return n % 2 != 0

# This identity is preserved
# x == (x//y) * y + x % y

# Floor Division with int
print(-7//3)
# this is because integer always tends to infinity so in this case next multiple of 3 is -9 which completely divides
# so the output is -3
# and with decimal it is negative two
print(decimal.Decimal(-7)//decimal.Decimal(3))
# because it divides next multiple of 3 with -2 i.e 6


# Decimal type uses base 10 floating point number representation
# Function in math dont work with Decimal

