# def hyperVolume(*args):
#     print(args)
#     print(type(args))


# hyperVolume(3,4)
# hyperVolume(3,4,5)

# def hyperVolume(*lengths):
#     i = iter(lengths)
#     v = next(i)
#     for length in i:
#         v *= length

#     return v

# print(hyperVolume(2,4))
# print(hyperVolume(2,4,6))
# print(hyperVolume(2,4,6,8))
# print(hyperVolume())


def hyperVolume(length, *lengths):
    v = length
    for item in lengths:
        v *= item

    return v


print(hyperVolume(2,4))
print(hyperVolume(2,4,6))
print(hyperVolume(2,4,6,8))
print(hyperVolume())