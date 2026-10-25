# polymorphism - many forms
# poly means many
# morph means forms

# types of polymorphism
# static polymorph or compile time poly morphism or method overloading
# dynamic poly morphism or runtime polymorphism or method overriding


# method overloading (method overloading not support python)
# method overloading - method name same but diffrent argumnets
# methid overriding - same method same argumnets


# python not support method overloading


class CustomMath:
    def add(self, a, b):
        return a+b

    def add(self, a, b, c):
        return a+b+c


# custobj = CustomMath()
# custobj.add(2, 3)
# print(custobj.add(2, 3, 6))


class CustomMathNew:
    # def add(self, a, b, c=0):
    #     return a+b+c

    def add(self, *a):
        total = 0
        for item in a:
            total = total+item
        return total


obj = CustomMathNew()
print(obj.add(23, 12))
print(obj.add(14, 7, 8))
print(obj.add(14, 7, 8, 7))
print(obj.add(14, 7, 8, 7, 16, 18, 19))


# method overriding

class Father:
    def sleep(self):
        print("father can sleep")

    def eat(self):
        print("father can eat")


class Son(Father):
    def eat(self):
        print("son can eat")

# pascal case -  FisrtName (class name)
# camel case  - firstNameIs
# snake case  - first_name (variable names)


sonobj = Son()
sonobj.eat()
