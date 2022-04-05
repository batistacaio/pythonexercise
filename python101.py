#This is a comment

if 5 > 2:
    print("Five is greater than two!")

x = 5
y = "John"
print(x)
print(y)

#Now we are gonna specify the data types
z = str(3)
w = float(3)
print(type(z))
print(type(w))

#Multiple values to variables
#a, b, c = "Orange", "Banana", "Cherry"
#print(a)
#print(b)
#print(c)

#Unpacking

#fruits = ["apple", "banana", "cherry"]
#a, b, c = fruits
#print(a, b, c)
#print(a)

#Functions, local scope and global scope
a = "awesome"

def myfunc():
    print("Python is " + a)
    
myfunc()

def newfunc():
    global var1
    var1 = "fantastic"
    
newfunc()

print("Python is " + var1)


#Data Types
data1 = 5
data2 = 2.5
data3 = "Example"
data4 = True

print(type(data1), type(data2), type(data3), type(data4))

#Useful tips

#*Boolean statements starts with capital letters -> True, False
#*Lists and tuples are equivalents to arrays, but tuples are immutable
#*Null equivalent is None