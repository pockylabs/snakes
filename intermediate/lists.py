# Lists: ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple"]
print(mylist)

# item = mylist[-1]
# print(item)

# for i in mylist:
#     print(i)

if "lemon" in mylist:
    print("yes")
else: 
    print("no")

print(f"We have {len(mylist)} items in list")

mylist.append("lemon")
print(mylist)

mylist.insert(1, "blueberry")
print(mylist)

item = mylist.pop()
print(item)

print(mylist)

item = mylist.remove("cherry")
print(mylist)

item = mylist.reverse()
print(mylist)

numlist = [4, 3, 1, -1, -5, 10]
# item = numlist.sort()

new_list = sorted(numlist)
print(numlist)
print(new_list)

numlist2 = [0] * 5
print(numlist2)

numlist3 = [1, 2, 3, 4, 5]

newest = numlist2 + numlist3
print(newest)

print("\n")

# SLICING
listbaru = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = listbaru[1:5]
b = listbaru[:5]
c = listbaru[1:]
d = listbaru[::2] #all the way from beginning with the step 2
print(a)
print(b)
print(c)
print(d)

# nice trick to reverse list
revlist = listbaru[::-1]
print(revlist)
print("\n")

# COPYING a list
list_org = ["banana", "cherry", "apple"]

#list_cpy = list_org || #both list refer to same list inside memory - BE CAREFUL!
list_cpy = list_org.copy()
## or
# list_cpy = list(list_org)
# list_cpy = list_org[:] #slicing all the way from the beginning to the end

list_cpy.append("lemon")

print(list_cpy)
print(list_org)

# LIST COMPREHENSION
# an elegant and fast way to create a new list from an existing list with one line.
alist = [1, 2, 3, 4, 5, 6]
blist = [i*i for i in alist] # expression and for in loop over your list

print(alist)
print(blist)