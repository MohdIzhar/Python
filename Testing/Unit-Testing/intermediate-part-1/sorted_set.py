from collections.abc import Sequence, Set
from itertools import chain

class SortedSet(Sequence, Set):
    def __init__(self, items = None):
        self._items = sorted(set(items)) if items is not None else []

    def __contains__(self, item):
        return item in self._items

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        result = self._items[index]
        return SortedSet(result) if isinstance(index, slice) else result

    def __repr__(self):
        return "SortedSet({})".format(
            repr(self._items) if self._items else ''
        )

    def __eq__(self,rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items == rhs._items

    def __ne__(self,rhs):
        if not isinstance(rhs, SortedSet):
            return NotImplemented
        return self._items != rhs._items

    def __add__(self, rhs):
        return SortedSet(chain(self._items, rhs._items))
        
    def __mul__(self, rhs):
        return self if rhs > 0 else SortedSet()

    def __rmul__(self, lhs):
        return self * lhs

    # use self on left hand side always in these set protocol cases
    def issubset(self,iterable):
        return self <= SortedSet(iterable)

    def issuperset(self,iterable):
        return self >= SortedSet(iterable)
    
    def intersection(self, iterable):
        return self & SortedSet(iterable)

    def union(self, iterable):
        return self | SortedSet(iterable)

    def symmetric_differnce(self, iterable):
        return self ^ SortedSet(iterable)

    def differnce(self, iterable):
        return self - SortedSet(iterable)
