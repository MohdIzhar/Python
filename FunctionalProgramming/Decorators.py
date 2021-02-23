##############
# Decorators # -> implemented as callable that accepts a callable and returns a callable
##############

    # -------   # @my_decorator    <----| pass to decorator  
    # |         # def my_func():        |
    # |         #     ....              | function object
    # |         #      |-----------> compiles ^     ^
    # | new function object-------------------------|

# Decorators allows us to modify existing function without changing their definition
# callers dont need to change when decorators are applied

# Ex: Ensure that functions only return ASCII strings
    # Sol: we can use ascii() to do that
        # this is intrusive and hard to maintain

from ast import walk


def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

def northern_city():
    return 'Tromsø'

print(northern_city())

@escape_unicode
def northern_city():
    return 'Tromsø'

print(northern_city())

# Classes as Decorators -> classes are callable objects

class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)

@CallCount
def hello(name):
    print('Hello {}'.format(name))


hello('Mohammad')
hello('Izhar')
hello('Pythoners')
print(hello.count)


# instances as decorators -> python calls an instance's __call__() when it is used as decorators
# __call__()'s value is used as new function
# creates groups of callable that you can dynamically control as a group

class Tracer:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap


tracer = Tracer()
@tracer
def rotate_list(l):
    return l[1:] + [l[0]]


l = [1,2,3]
l = rotate_list(l)
print(l)
l = rotate_list(l)
print(l)
tracer.enabled = False
l = rotate_list(l)
print(l)
l = rotate_list(l)
print(l)

# we can use multiple decorator
# @decorator1
# @decorator2
# @decorator3

# we can use decorator method with class and decorator class with methods

# functools.wrap() replace metadata with that of decorated callable
# It is decorator that apply to our wrapper function.
# __name__, __doc__ of inner function get wrapped to outer function

###########################
# Parametrized Decorators #
########################### 

def check_non_negative(index):
    def validator(f):
        def wrap(*args):
            if args[index] < 0:
                raise ValueError('Argument {} must be non-negative.'.format(index))
            return f(*args)
        return wrap

    return validator

@check_non_negative(1)
def create_list(value, size):
    return [value] * size

print(create_list('a', 3))
print(create_list(123, -6))