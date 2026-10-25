class Father:
    # attributes
    # methods
    # special member method(constructor)
    def __init__(self, bike, house, money):
        print("Father class constructor called")
        self.bike = bike
        self.money = money
        self.house = house

    def assets(self):
        return f"i have money {self.money} and bike {self.bike} and house {self.house}"


class Son(Father):
    # attributes
    # methods
    # special member method(constructor)
    def __init__(self, bike, house, money, age, name):
        print("son class constructor called")
        # explicitly we calledd father class constructor
        Father.__init__(self, bike, house, money)
        self.age = age
        self.name = name

    def play(self):
        return f"my name is {self.name} and i am {self.age} years old and i can play cricket"


class Daughter(Father):
    # attributes or data
    # methods or behaviors
    # special member method(constructor)
    def __init__(self, bike, house, money, name):
        print("daughter callss construcotr called")
        Father.__init__(self, bike, house, money)
        self.name = name

    def dance(self):
        return f" my name is {self.name} and i can dance"


raviobj = Son("herohonda", "bighouse", "10lakhs", 23, "ravi")
res = raviobj.assets()
print(res)
print(raviobj.play())

print("================================================")

saiobj = Daughter("herohonda", "bighouse", "10lakhs", "sai")
res3 = saiobj.dance()
print(res3)
print(saiobj.assets())

# praveenobj = Son()
# res1 = praveenobj.assets()
# print(res1)
# res4 = praveenobj.play()
# print(res4)
