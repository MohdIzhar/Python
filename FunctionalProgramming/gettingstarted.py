import socket

def resolve(host):
    return socket.gethostbyname(host)

# >>> resolve
# <function resolve at 0x7faa4938e488>
# >>> resolve('mohdizhar')
# >>> resolve('localhost')


