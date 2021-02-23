# Complex number in python

print(2j)
print(type(2j))

print(3+4j)
# we can use complex constructor also

print(complex(3))
print(complex(3, -2))

# can bu used with string delimited with no spacing
print(complex('-2+3j'))

# if give whitespaces will throw error
# print(complex('-2 + 3j'))

c = 3 + 5j
# extracting real and imaginary component from complex number
print(c.real)
print(c.imag)

# also support the conjugate
print(c.conjugate())

# math function can't be used with complex we have another module called
# cmath for different operations

# import math
# math.sqrt(-1) will give error

import cmath

print(cmath.sqrt(-1))

# obtain the phase of complex number
print(cmath.phase(1+1j))
print(abs(1+1j))

# these value together can be return in tuple format

print(cmath.polar(1+1j))
modulus, phase = cmath.polar(1+1j)
print(modulus, phase)

# to reverse modulus and phase use rect function
print(cmath.rect(modulus, phase))

# Practical Example of COmplex Number in Electrical Engineering
# Circuit Analysis -> AC circuit Analyse phase, current, voltage

def inducive(ohms):
    return complex(0.0, ohms)

def capacitive(ohms):
    return complex(0.0, -ohms)

def resistive(ohms):
    return complex(ohms)

def impedance(components):
    z = sum(components)
    return z

imp = impedance([inducive(10), resistive(10), capacitive(5)])

import cmath
p = cmath.phase(imp)
print(p)

# converting radian to degree i.e phase value
import math
d = math.degrees(p)
print(d)


# inbuilt numeric functions
# round()
# abs()
# note float uses binary representation and may yield different results
print(round(2.675, 2))
from decimal import Decimal
print(round(Decimal('2.675'), 2))


# Base Conversion -> Int

int("val", base=2) # base range 2-36 inclusive
