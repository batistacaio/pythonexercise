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

