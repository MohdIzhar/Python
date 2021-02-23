# def -> binds a function object to a name, used to define new functions, executed at runtime

# local functions

def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]

    return sorted(strings, key=last_letter)

print(
sort_by_last_letter(['hello', 'from', 'a', 'local','function'])
)
########
# LEGB #
########

g = 'global'
def outer(p="parameter"):
    l = "local"
    def inner():
        print(g,p,l)
    inner()

outer()

# -> Local function are not members of enclosing functions
# outer.inner() try to run this

# Returning local function

def enclosing():
    def local_func():
        print("local func")
    return local_func


lf = enclosing()
lf()

############
# CLOSURES # -> records object from enclosing scopes, keeps record until enclosing scope is gone, uses __closure__
############

def enclosing():
    x = "closed over"
    def local_func():
        print(x)
    return local_func

lf = enclosing()
lf()
print(lf.__closure__)

######################
# Function Factories # -> Function that return other functions, returned function uses both their own arguments
######################    as well as arguments to the factory

def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp

square = raise_to(2)
print(square.__closure__)
print(square(5))
print(square(9))

cube = raise_to(3)
print(cube(10))
print(cube(4))


# Binding name in enclosing scope

message = "global"

def enclosing():
    message = "enclosing"
    def local():
        message = "local"

    print("enclosing message: ", message)
    local()
    print("enclosing message: ", message)
    
print("global message: ", message)
enclosing()
print("global message: ", message)

##########
# GLOBAL # -> introduce binding from the global scope into another scope
##########


message = "global"

def enclosing():
    message = "enclosing"
    def local():
        global message
        message = "local"

    print("enclosing message: ", message)
    local()
    print("enclosing message: ", message)
    
print("global message: ", message)
enclosing()
print("global message: ", message)

############
# nonlocal # -> insert name binding from enclosig scope to local scope
############


message = "global"

def enclosing():
    message = "enclosing"
    def local():
        nonlocal message
        message = "local"

    print("enclosing message: ", message)
    local()
    print("enclosing message: ", message)
    
print("global message: ", message)
enclosing()
print("global message: ", message)