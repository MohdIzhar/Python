import  math
from traceback import print_tb

class InclinationError(Exception):
    pass

def inclination(dx, dy):
    try:
        return math.degrees(math.atan(dy/dx))
    except ZeroDivisionError as e:
        raise InclinationError("Slope cannot be vertical") from e
# using from keyword for explicit chaining  from e suffix when we create the exception. 
# This associates the new exception object with the original exception e
# Like implicit chaining associates the exception through __context__
# explicit associates through __cause__

def main():
    try:
        inclination(0,5)
    except InclinationError as e:
        print(e.__traceback__)
        print_tb(e.__traceback__)

    print("Finished")