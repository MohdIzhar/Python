# To represent rational numbers
# 2/3 (numerator/denominator)
# denominator must not be zero

from decimal import Decimal
from fractions import Fraction

two_third = Fraction(2, 3)
print(two_third)
four_fifth = Fraction(4, 5)
print(four_fifth)
# Fraction(5,0) will give you zero division error

# Fraction can also be constructed from float object
print(Fraction(0.5))

# but not you will not get the exact result for all
# Example:
print(Fraction(0.1))

# fraction represent interoperatabiliy with Decimal and you will get exact result
print(Fraction(Decimal('0.1')))

# Fractions can be constructed with string
print(Fraction('22/7'))

# we can add, subtract, mul, div

print(Fraction(2,3) + Fraction(4,5))
print(Fraction(2,3) - Fraction(4,5))
print(Fraction(2,3) * Fraction(4,5))
print(Fraction(2,3) % Fraction(4,5))
print(Fraction(2,3) / Fraction(4,5))
print(Fraction(2,3) // Fraction(4,5))

# Fractions doesn't support methods for square roots and similar operations


# +-----------------+------------------+
# | Numeric Types   |     Qualities    |
# +-----------------+------------------+
# |    int                precission   |
# |   float               exactness    |
# |   Decimal             convenience  |
# |   Fraction            performance  |
# +------------------------------------+
