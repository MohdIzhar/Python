# def lookups():
#         s = [1,4,6]
#         try:
#             items = s[5]
#         except IndexError:
#             print("Handled IndexError")

#         d = dict(a=72, b=99, c=31)
#         try:
#             value = d['x']
#         except KeyError:
#             print("Handled KeyError")

def lookups():
    s = [1,4,6]
    try:
        items = s[5]
    except LookupError:
        print("Handled IndexError")

    d = dict(a=72, b=99, c=31)
    try:
        value = d['x']
    except LookupError:
        print("Handled KeyError")

