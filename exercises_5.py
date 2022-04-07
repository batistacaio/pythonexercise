#Functions

def my_function():
    print("Hello World!")
    
my_function()

#Arguments

def my_function2(fname):
    print(fname + " Batista")
    
my_function2("Caio")

#Arbitrary Arguments

def my_function3(*kids):
    print("The youngest child is " + kids[2])
    
my_function3("Emil", "Tobias", "Linus")

#List of arguments

def my_function4(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function4(fruits)

#Recursion

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)
print("\n\n")

#Lambda

x = lambda a : a + 10
print(x(5))

z = lambda a, b : a * b
print(z(5, 2))

def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)

print(mydoubler(11))

#Classes

class myClass:
    x = 5
    
c1 = myClass()
print(c1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myfunc(self):
        print("Hello my name is " + self.name)
        
p1 = Person("Caio", 25)
p1.myfunc()

#Inheritance

class myPerson:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        
    def printname(self):
        print(self.firstname, self.lastname)

class Student(myPerson):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
        
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Caio", "Batista", 2014)

x.welcome()