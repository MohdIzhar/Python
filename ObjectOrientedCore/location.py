from position import *
import inspect

def auto_repr(cls):
    # print(f"Decorating {cls.__name__} with auto_repr")
    members = vars(cls) #vars is in built function that return mapping dict like object
    # for name, member in members.items():
    #     print(name, member) 

    if "__repr__" in members:
        raise TypeError(f"{cls.__name__} already defines __repr__")

    if "__init__" not in members:
        raise TypeError(f"{cls.__name__} does not override __init__")

    sig =  inspect.signature(cls.__init__)
    parameters_names = list(sig.parameters)[1:]
    # print("__init__ parameter names: ", parameters_names)

    if not all( isinstance(members.get(name, None), property) for name in parameters_names):
        raise TypeError(f"Cannot apply auto_repr to {cls.__name__} beacuse not all __init__ parameters have matching properties")

    def synthesized_repr(self):
        return "{typename}({args})".format(typename=typename(self), args=", ".join("{name}={value!r}".format(name=name, value=getattr(self,name)) for name in parameters_names))

    setattr(cls, "__repr__", synthesized_repr)
    return cls

@auto_repr
class Location:

    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    # def __str__(self):
    #     return self._name

    # def __eq__(self, other):
    #     if isinstance(other, type(self)):
    #         return NotImplemented
    #     return (self.name == other.name) and (self.position == other.position)

    # def __hash__(self):
    #     return hash(self.name, self.position)

    
hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.16))
stockholm = Location("Stockholm", EarthPosition(59.33, 18.06))
cape_town = Location("Cape town", EarthPosition(-33.93, 18.42))
rotterdam = Location("Rotterdam", EarthPosition(51.96, 4.47))
maracaibo = Location("Maracaibo", EarthPosition(10.65, -71.65))
