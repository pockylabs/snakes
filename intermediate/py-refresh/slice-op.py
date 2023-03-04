# slice operator
x = [0,1,2,3,4,5,6,7,8]
y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
s = "hello"

# sliced = [start:stop:step]
sliced = x[0:4:2]
print(sliced)

sliced2 = x[4:2:-1]
print(sliced2)

sliced3 = (1,2,3,4,4,2,2,1)[::2]
print(sliced3)