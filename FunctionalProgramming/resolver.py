import socket

class Resolver:
    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        
        return self._cache[host]

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache



# >>> from resolver import *
# >>> resolve = Resolver()
# >>> resolve('localhost')
# '127.0.0.1'
# >>> resolve.__call__('localhost')
# '127.0.0.1'
# >>> resolve._cache
# {'localhost': '127.0.0.1'}
# >>> resolve('pluralsight.com')
# '34.212.224.191'
# >>> resolve._cache


# DNS time lookup
# >>> from timeit import timeit
# >>> timeit(setup="from __main__ import resolve", stmt="resolve('google.com')",number=1)
# 0.06351308200100902
# next time when run will take less time
# >>> timeit(setup="from __main__ import resolve", stmt="resolve('google.com')",number=1)
# 6.470001608249731e-06

# checking the previous store result using underscore
# >>> print("{:f}".format(_))
# 0.000006


# from resolve import *
# >>> resolve = Resolver()
# >>> resolve.has_host("pluralsight.com")
# False
# >>> resolve._cache
# {}
# >>> resolve("pluralsight.com")
# '34.212.224.191'
# >>> resolve.has_host("pluralsight.com")
# True
# >>> resolve._cache
# {'pluralsight.com': '34.212.224.191'}
# >>> resolve.clear()
# >>> resolve._cache
# {}



