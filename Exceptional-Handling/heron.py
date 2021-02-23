import sys
import math
import io

class TraingleError(Exception):
    def __init__(self, text, sides):
        super().__init__(text)
        self._sides = tuple(sides)

    @property
    def sides(self):
        return self._sides

    # using args from base class method and overriding stra method
    def __str__(self):
        return "'{}' for sides {}".format(self.args[0], self._sides)

    def __repr__(self):
        return "TriangleError({!r}, {!r})".format(self.args[0],self._sides)

    

def triangle_area(a,b,c):
    sides = sorted((a, b, c))
    if sides[2] > sides[0] + sides[1]:
        raise TraingleError("Illegal traingle", sides)

    p = (a + b + c) / 2
    a = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return a

def main():
    try:
        a = triangle_area(3,4,10)
        print(a)
    except TraingleError as e:
        # print(e, file=sys.stdin) # this is second bug file input
        try:
            print(e, file=sys.stdin)
        except io.UnsupportedOperation as f:
            print(e)
            print(f)
            print(f.__context__ is e)