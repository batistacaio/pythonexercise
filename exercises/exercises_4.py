#Dictionaries

mydict = {
    "name": "Caio",
    "surname": "Batista",
    "age": 25
}
print(mydict)
print(mydict["age"])
mydict["age"] = 26
#Changing a value
mydict.update({"name": "Kaio"})
print(mydict)
#Adding a new key
mydict["Favorite color"] = "blue"
#You can use update() method too
print(mydict)
#Removing items
mydict.pop("Favorite color")
print(mydict)

#Nesting dictionaries

brotherdict = {
    "name": "Lucas",
    "surname": "Batista",
    "age": 33
}

brosdict = {
    "bro1": mydict,
    "bro2": brotherdict
}
print(brosdict)

#Using elif

a = 33
b = 52
if a > b:
    print("A is greater than B")
elif a == b:
    print("A and B are equal")
else:
    print("B is greater than A")
    
#Short hand if else

z = 2
x = 330
print("Z") if z > x else print("X")

#Nested if

y = 41

if y > 10:
    print("Above ten, ")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
        
#While

i = 1
while i < 10:
    print(i)
    i += 1
    
#Break statement

t = 1
while t <= 10:
    print(t)
    if t == 5:
        break
    t += 1
    
#Using range with a condition

for f in range(5, 51, 5): #counts from 5 to 50 increasing by 5
    print(f)
    
#Else in a loop

for s in range(6):
    print(s)
else:
    print("Finished.")