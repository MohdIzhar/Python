import os

class PhoneBook:

    def __init__(self, cache_directory) -> None:
        self._numbers = {}
        self.filename = os.path.join(cache_directory, 'phonebook.txt')
        self.cache = open(self.filename,'w')

    def add(self, name, number):
        self._numbers[name] = number

    def lookup(self, name):
        return self._numbers[name]

    def names(self):
        return set(self._numbers.keys())

    def clear(self):
        self.cache.close()
        os.remove(self.filename)
