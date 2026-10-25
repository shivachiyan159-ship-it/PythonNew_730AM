# public
# protected
# private

# bus, tarin - public transport
# car , bike - (protected)
# mobile - (private)


class Bike:
    # attributes (variables)
    # methods (functions)
    # special method (constrcutor) - to inialize the data
    def __init__(self, color, price, keys):
        self.color = color  # public
        self._price = price  # protected - parent and child class
        # private - within the class (changing name)  _classname__attributename
        self.__keys = keys

    def display(self):
        print(self.__keys)

    @property
    def keys(self):
        # if subcscription
        user = "admin"
        if user == "admin":
            return self.__keys
        else:
            return "you dont have access mykeys"

    @keys.setter
    def keys(self, value):
        # if subcscription
        user = "admin"
        if user == "admin":
            self.__keys = value
        else:
            return "you dont have access mykeys"

    @property
    def getcolor(self):
        # if subcscription
        return self.color

    @getcolor.setter
    def setcolor(self, value):
        # if subcscription
        self.color = value


class Apachi(Bike):
    def __init__(self, color, price, keys, mileage):
        Bike.__init__(self, color, price, keys)
        self.pricenew = self._price  # protected memvbers can access child class
        self.mileage = mileage



splenderobj = Apachi("red", 75000, "yes", 70)

print(splenderobj.color)
# you are adult so you have maturity dont use protected and private members outside the class.
# print(splenderobj._price)
# accessing private members using using nam mangling
# print(splenderobj._Bike__keys)

# we have to give access to controlled way
# lock
# id pwd

# 1. thrugh public method
# splenderobj.display()
# 2. through name mangling
# print(splenderobj._Bike__keys)
# 3. through getters and setters properties
print(splenderobj.keys)
print(splenderobj.color)
splenderobj.color = "green"
splenderobj.keys = "no"
print(splenderobj.keys)
splenderobj.getcolor
splenderobj.setcolor = "black"
