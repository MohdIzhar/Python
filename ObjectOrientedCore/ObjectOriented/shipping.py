import iso6346

class ShippingContainer:

    # class attributes
    next_serial = 1337
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0
    
    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    # declaring static to remove instance (self)
    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code = owner_code, 
            serial = str(serial).zfill(6)
            )

    @classmethod
    def create_empty(cls, owner_code, length_ft, **kwargs):
        return cls(owner_code, length_ft, contents = [], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, **kwargs):
        return cls(owner_code, length_ft, contents = list(items), **kwargs)

    def __init__(self, owner_code, length_ft, contents, **kwargs):
        self.owner_code = owner_code
        self.length_ft = length_ft
        self.contents = contents
        # self.serial = self._generate_serial() 
        # self.serial = ShippingContainer._generate_serial()
        # ShippingContainer this will not work in case inheritance because we are calling specific class
        # to use polymorphism behaviour of static method use self
        self.bic = self._make_bic_code(
            owner_code = owner_code,
            serial= ShippingContainer._generate_serial()
            )

    @property
    def volume_ft3(self):
        return self._calc_volume()
        
    def _calc_volume(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft

class RefregratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100

    def __init__(self, owner_code, length_ft, contents,* , celsius, **kwargs):
        super().__init__(owner_code, length_ft, contents, **kwargs)
        if celsius > RefregratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temprature too hot!")
        self._celsius = celsius

    # @property
    # def volume_ft3(self):
    def _calc_volume(self):
        return super()._calc_volume() - RefregratedShippingContainer.FRIDGE_VOLUME_FT3
        # return (self.length_ft * ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT - RefregratedShippingContainer.FRIDGE_VOLUME_FT3)
        # return super().volume_ft3 - RefregratedShippingContainer.FRIDGE_VOLUME_FT3

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32)* 5/9

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._set_celsius(value)

    def _set_celsius(self, value):
        if value > RefregratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return RefregratedShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = RefregratedShippingContainer._f_to_c(value)

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code = owner_code,
            serial = str(serial).zfill(6),
            category = 'R'
        )

class HeatedRefrigeratedShippingContainer(RefregratedShippingContainer):
    MIN_CELSIUS = -20

    # @RefregratedShippingContainer.celsius.setter
    # def celsius(self, value):
    def _set_celsius(self, value):
        # if not (HeatedRefrigeratedShippingContainer.MIN_CELSIUS <= value <= RefregratedShippingContainer.MAX_CELSIUS):
        #     raise ValueError("Temperature out of range")
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temparature too cold!")
        # self._celsius = value
        super()._set_celsius(value)
        # RefregratedShippingContainer.celsius.fset(self, value)
