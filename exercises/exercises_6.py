from modules import person1

#Modules

def greeting(at1, at2, at3):
    print("Hello, my name is " + at1 + ", i'm " + at2 + " years old and i'm a " + at3)
    
greeting(person1["name"], str(person1["age"]), person1["profession"])