# Unpack Operator

# **kwargs -> use for dictionaries

def func(x, y):
    print(x, y)


pairs = [(1,2), (3,4)]

# print(*x) # unpack into individual elements

for pair in pairs:
    # func(pair[0], pair[1])
    func(*pair)

print()
func(**{'y': 5,'x': 2})