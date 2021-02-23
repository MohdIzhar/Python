class Base:

    def __init__(self):
        print("Base Initializer")

    def f(self):
        print("Base.f()")

class Sub(Base):
    
    def __init__(self):
        super().__init__()
        print("Sub Initializer")

    def f(self):
        print('Sub.f()')