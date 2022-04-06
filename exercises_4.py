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