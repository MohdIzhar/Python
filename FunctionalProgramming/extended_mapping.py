# def color(red, green, blue, **kwargs):
#     print("r =", red)
#     print("g =", green)
#     print("b =", blue)
#     print(kwargs)

# k = {'red': 21, 'green': 68, 'blue': 120, 'alpha': 52}
# color(**k)

# # dict() uses **kwargs in its initializer
# k = dict(red=21, green=68, blue=120, alpha=52)
# color(**k)


# Argument Forwarding

def trace(f, *args, **kwargs):
    """f =  will take a function"""
    print("args = ", args)
    print("kwargs =", kwargs)
    result = f(*args, **kwargs)
    print("result =", result)


trace(int, "ff", base=16)