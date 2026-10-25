# variables
# functions


# without inheritance

class Father:
    # attributes
    # constructor (special member method)
    # methods

    def __init__(self, color, eyes, name, age):
        self.name = name
        self.eyes = eyes
        self.clr = color
        self.age = age

    def eat(self):
        print("i can eat")

    def walk(self):
        print("i can walk")


class Son:
    # attributes
    # methods
    # constructor
    def __init__(self, name, age, color, eyes, school, grade):
        self.name = name
        self.eyes = eyes
        self.clr = color
        self.age = age
        self.school = school
        self.grade = grade

    def eat(self):
        print("i can eat")

    def walk(self):
        print("i can walk")

    def enjoy_life():
        print("enjoy life")


# fatherobj = Father("red", 2, "sai", 44)
# print(fatherobj.name)
# print(fatherobj.clr)
# fatherobj.eat()


# with Inheritance

class FatherNew:
    # attributes
    # constructor (special member method)
    # methods

    def __init__(self, color, eyes, name, age):
        print("father class constrcutor called")
        self.name = name
        self.eyes = eyes
        self.clr = color
        self.age = age

    def eat(self):
        print("i can eat")

    def walk(self):
        print("i can walk")


class SonNew(FatherNew):
    # attributes
    # methods

    # constructor
    def __init__(self, son_name, son_age, color, eyes, name, age):
        print("son class constrcutor called")
        FatherNew.__init__(self, color, eyes, name, age)
        self.son_name = son_name
        self.son_age = son_age

    def enjoy_life(self):
        print("i can enjoy life")


raviobj = SonNew("ravi", 24, "red", 2, "ramarao", 47)
print(raviobj.name)
print(raviobj.clr)
print(raviobj.eyes)
print(raviobj.son_name)
raviobj.enjoy_life()
raviobj.eat()
raviobj.walk()


# son class constrcutor called
# father class constrcutor called
# ramaro
# red
# 2
# ravi
# i can enjoy life
# i can eat
# i can walk


print(SonNew.__mro__)

# print(raviobj.name)
# print(raviobj.clr)
# raviobj.eat()
# raviobj.enjoy_life()
