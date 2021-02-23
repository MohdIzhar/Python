m = map(ord, 'The quick brown fox')
# maps are lazy
print(m)

class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wraps(*args, **kwargs):
            if self.enabled:
                print("Calling {}".format(f))
            return f(*args, **kwargs)
        return wraps

result = map(Trace()(ord), 'The quick brown fox')
print(result)
print(next(result))
print(next(result))

l1 = ['a', 'b', 'c']
l2 = ['1', '2', '3']
l3 = ['A', 'B', 'C']

def combine(a1, a2, a3):
    return '{} {} {}'.format(a1, a2, a3)

m = map(combine, l1,l2,l3)
print(list(m))


# Filter functions -> takes a function and iterable and terminate if any false condition is met
# are lazy
postives = filter(lambda x: x > 0, [1,-5, 0, 6, -2, 8])
postives
print(list(postives))

# functools.reduce()
from functools import reduce
import operator

print(reduce(operator.add, [1,2,3,4,5]))

numbers = [1,2,3,4,5]
accumulator = operator.add(numbers[0], numbers[1])
for item in numbers[2:]:
    accumulator = operator.add(accumulator ,item)

print(accumulator)
# Note -> if we pass empty iterable to reduce then it will return an error
#         if we pass only one element with iterable then it will return that element without calling reduce function

# reduce(operator.mul, [])
# reduce(operator.mul, [1])

# we can pass optional value or default value in reduce function
values = []
print(reduce(operator.add, values, 0))
values = [1,2,3]
print(reduce(operator.add, values, 0))
