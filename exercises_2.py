#Booleans

class myclass():
    def __len__(self):
        return 0
    
myobj = myclass()
print(bool(myobj)) #Returns False

#Almost any value is evaluated True, except empty strings, number 0, empty lists, tuples, sets and dicts.

def myFunction():
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")
    
x = 200
print(isinstance(x, int))

#Operators

y = 25
z = 4
print(y ** z) #Exponentiation
print(y // z) #Floor division

#Lists

mylist = ["apple", "banana", "cherry"]
print(mylist)
print(len(mylist))
#Constructor method
thislist = list(("apple", 1, False, "banana"))
print(thislist)

#-----
#Four types of collections (arrays) => 
#1 - list (ordered and changeable - allow duplicates), 
#2 - tuple (ordered and unchangeable - allow duplicates), 
#3 - set (unordered and unchangeable, but can add/remove items - do not allow duplicates) and 
#4 - dictionary (ordered and changeable - do not allow duplicates)
#-----

#Check if

if "apple" in thislist:
    print("Found some apples")
    
#Change values
    
thislist[2] = True
print(thislist)

#Insert items

thislist.insert(4, 43.2)
print(thislist)
#-Use append to add to the end of the list

#Extend list

thislist.extend(mylist)
print(thislist)

#Remove last item

thislist.pop()
print(thislist)