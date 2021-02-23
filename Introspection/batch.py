from itertools import chain

class Batch:
    def __init__(self, iterables = ()):
        self._iterables = list(iterables)

    def append(self, iterable):
        self._iterables.append(iterable)

    def __iter__(self):
        return chain(*self._iterables)

# >>> import inspect
# >>> import batch
# >>> inspect.ismodule(batch)
# True

# inspect.getmembers(batch) -> result in all outputs including builts-in
# inspect module contains 16 predicates to identify different object types from isabstract to istraceback.
# >>> dir(inspect)

# inspect.getmembers() - takes second argument as function to filter the result
# >>> inspect.getmembers(batch, inspect.isclass)
# [('Batch', <class 'batch.Batch'>), ('chain', <class 'itertools.chain'>)]

# Note:- you can import another module from current module
# This is because import binds the imported module into current import namespace.
# >>> from batch import chain
# >>> list(chain([1,2,3],[4,5,6]))
# [1, 2, 3, 4, 5, 6]
# This is surprising output

# >>> inspect.getmembers(batch.Batch, inspect.isfunction)
# [('__init__', <function Batch.__init__ at 0x7f390d6cd400>), ('__iter__', <function Batch.__iter__ at 0x7f390d6cd510>), ('append', <function Batch.append at 0x7f390d6cd488>)

# >>> init_sig = inspect.signature(batch.Batch.__init__)
# >>> init_sig
# <Signature (self, iterables=())>
# this is to get attributes of class

# with this signature we can get list of parameters and each parameter can query individually for attributes such as their default values
# >>> init_sig.parameters
# mappingproxy(OrderedDict([('self', <Parameter "self">), ('iterables', <Parameter "iterables=()">)]))
# >>> repr(init_sig.parameters['iterables'].default)
# '()'
# we can convert signature into string to get nice output
# >>> str(init_sig)
# '(self, iterables=())'

# Note :- inspect.signature doesn't always work


