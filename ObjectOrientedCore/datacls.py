from position import Position, EarthPosition
from dataclasses import dataclass

# class decorators
@dataclass(eq=True, frozen=True)
class Location:
    name: str
    position: Position

    # used to validate data before construction
    def __post_init__(self):
        if self.name == "":
            raise ValueError("Location name cannot be empty")

    
hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.16))
stockholm = Location("Stockholm", EarthPosition(59.33, 18.06))
cape_town = Location("Cape town", EarthPosition(-33.93, 18.42))
rotterdam = Location("Rotterdam", EarthPosition(51.96, 4.47))
maracaibo = Location("Maracaibo", EarthPosition(10.65, -71.65))

# >>> from datacls import *
# >>> paris = Location("Paris", Position(48.8, 2.3))
# >>> paris
# Location(name='Paris', position=Position(latitude=48.8, longitude=2.3))

# Run before passing frozen = True
# >>> from datacls import *
# >>> cities = {hong_kong, stockholm, cape_town, maracaibo}

# Run after passing frozen = True
# >>> from datacls import *
# >>> cities = {hong_kong, stockholm, cape_town, maracaibo}
