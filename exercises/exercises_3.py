#Loops

mylist = ["apple", "banana", "cherry", "grape", "mango", "pineapple"]

for x in mylist:
    print(x)
#or by referring their index numbers
for i in range(len(mylist)):
    print(mylist[i])
#List comprehension - shortest syntax for looping
[print(x) for x in mylist]
    
#While

z = 0
while z <= 10:
    print(z)
    z = z + 1
    
#Creating a new list using List Comprehension with parameters (contains letter "a")

newlist = [x for x in mylist if "a" in x]
print(newlist)

#Iterable

numberlist = [x for x in range(10)]

#Sort list

mylist.sort()
#Reverse
mylist.sort(reverse = True)
#Customize sort by using key argument
#Reverse order regardless of the alphabets
mylist.reverse()

#Tuple

mytuple = ("red", "blue", "green", "purple", "orange")
#The order is defined and may not change, we also can't add or remove items
#You can change items by converting it into a list, and then convert back to a tuple
convertedlist = list(mytuple)
convertedlist[2] = "white"
mytuple = tuple(convertedlist)
print(mytuple)
#You can use any list method with this
#You are allowed to add tuples to tuples, and remove them with del keyword
anothercolor = ("black",)
mytuple += anothercolor
print(mytuple)

#Sets

myset = {"pencil", "notebook", "eraser", "scale"}
print(myset)
#Sets are unindexed and duplicate values will be ignored
myset.add("pen")
print(myset)
#You can update a set with any iterable objects
myset.update(mytuple)
print(myset)
#Remove by using the remove() or discard() methods (discard doest not return error if not exists)
#Important set methods in https://www.w3schools.com/python/python_sets_methods.asp