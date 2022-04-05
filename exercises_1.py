import random

#Using for in

cities = ["São Paulo", "Campinas", "Guarulhos"]

#for city in cities:
#    print(city, end=", ")
    
#Adding a new city to the list cities
cities.append("Santo André")

for city in cities:
    print(city)
    
#Numbers
a = int(1)
b = float(3.4)
c = float(3.5e20)
d = complex(5j)
print(a, b, c, d)
    
#Using random module
print(random.randrange(1, 10))

#Check String
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
    
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
    
#Slicing and modifying strings
name = "Caio Batista "
print(name.upper()[:4])
print(name.lower()[5:])
print(name.strip())

#Combine strings with format method
age = 25
shirts = 9
price = 29.95
txt2 = "My name is Caio, and I am {} years old. I've sold {} shirts for {} dollars each."
print(txt2.format(age , shirts, price))

#Escape character
#Backslash is required when there are quotes inside a string
txt3 = "We are the so-called \"Vikings\" from the north."
#Like C, we can use "\n" for a new line

#Useful string methods
name2 = "caio"
print(name2.capitalize()) #Converts the first character to upper case
print(name2.strip()) #Returns a trimmed version of the string
#Extended list of methods at https://www.w3schools.com/python/python_strings_methods.asp