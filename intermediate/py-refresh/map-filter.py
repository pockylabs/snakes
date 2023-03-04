x = [1,2,4,5,3,3,21,2,21,2,313,1,23,142,4]

mp = map(lambda i: i + 2, x)
fl = filter(lambda i: i % 2 == 0, x)
print(list(mp))
print(list(fl))