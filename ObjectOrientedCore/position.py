class Position:

    def __init__(self, latitude, longitude):
        if not (-90 <= latitude<= +90):
            raise ValueError(f"Latitude {latitude} out of range")

        if not (-180 <= longitude <= +180):
            raise ValueError(f"Longitude {longitude} out of range")

        self._latitude = latitude
        self._longitude = longitude


    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return  self._longitude

    @property
    def latitude_hemisphere(self):
        return "N" if self.latitude >= 0 else "S"

    @property
    def longitude_hemisphere(self):
        return "E" if self.longitude >= 0 else "W"

    def __repr__(self):
        # return f"Position(latitude={self.latitude}, longitude={self.longitude})"
        return f"{typename(self)}(latitude={self.latitude}, longitude={self.longitude})"

    # __str__ for user which hide technical details
    def __str__(self):
        return format(self)
        # return (f"{abs(self.latitude)} {self.latitude_hemisphere},"
        # f"{abs(self.longitude)} {self.longitude_hemisphere}")

    def __format__(self, format_spec):
        component_format_spec = ".2f"
        prefix, dot, suffix = format_spec.partition(".")
        if dot:
            num_decimal_places = int(suffix)
            component_format_spec = f".{num_decimal_places}f"
        latitude = format(abs(self.latitude), component_format_spec)
        longitude = format(abs(self.longitude), component_format_spec)
        return (f"{latitude} {self.latitude_hemisphere},"
        f"{longitude} {self.longitude_hemisphere}")

class EarthPosition(Position):
    pass

class MarsPosition(Position):
    pass

def typename(obj):
    return type(obj).__name__



# >>> from position import *
# >>> oslo = Position(60.0, 10.7)
# >>> r = repr(oslo)
# >>> p = eval(r)
# >>> p

# >>> from position import *
# >>> mauna_kea = EarthPosition(latitude = 19.82, longitude = -155.47)
# >>> mauna_kea
# >>> olympus_mons = MarsPosition(latitude = 18.65, longitude = -133.8)
# >>> olympus_mons

# >>> from position import *
# >>> mount_erebus = EarthPosition(-77.5, 167.2)
# >>> str(mount_erebus)
# >>> repr(mount_erebus)

# >>> from position import *
# >>> aconcagua = EarthPosition(-32.7, -70.1)
# >>> repr(aconcagua)
# 'EarthPosition(latitude=-32.7, longitude=-70.1)'
# >>> str(aconcagua)
# '32.7 S,70.1 W'
# >>> format(aconcagua)
# 'FORMATTED POSITION'
# >>> f"The highest mountain is located in South America at {aconcagua}"
# 'The highest mountain is located in South America at FORMATTED POSITION'
# >>> "The highest mountain is located in South America at {}".format(aconcagua)
# 'The highest mountain is located in South America at FORMATTED POSITION'

# >>> from position import *
# >>> matterhorn = EarthPosition(45.9763, 7.6586)
# >>> format(matterhorn)
# '45.98 N,7.66 E'

# >>> from position import *
# >>> matterhorn = EarthPosition(45.9763, 7.6586)
# >>> format(matterhorn, ".1")
# '46.0 N,7.7 E'
# >>> format(matterhorn, ".0")
# '46 N,8 E'
# >>> format(matterhorn)
# '45.98 N,7.66 E'

