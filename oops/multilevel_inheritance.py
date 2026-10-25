class BaseMobile:
    # attributes
    # methods
    # special method

    def __init__(self, brand, battery):
        print("base mobile constructor called")
        self.brand = brand
        self.battery = battery

    def call(self):
        print("calling")

    def msg(self):
        print("calling")


class SmartMobile(BaseMobile):
    # attributes
    # methods
    # special method

    def __init__(self, camera):
        print("smartmobile constructor called")
        self.camera = camera

    def take_photo(self):
        print("i can take photo")


class GamingMobile(SmartMobile):
    # attributes
    # methods
    # special method

    def __init__(self, ram, brand, battery, camera):
        print("gaming mobile constructor called")
        BaseMobile.__init__(self, brand, battery)
        SmartMobile.__init__(self, camera)
        self.ram = ram

    def playgame(self):
        print(" i can play pubg")


gamemobobj = GamingMobile("16gb", "samsung", "1000mah", "12mp")
# gamemobobj1 = GamingMobile("12gb", "samsung", "1500mah")
# gamemobobj.call()
# gamemobobj.take_photo()
# gamemobobj.playgame()
print(gamemobobj.battery)
print(gamemobobj.camera)
# print(GamingMobile.__mro__)


# output
# gaming mobile constructor called
# base mobile constructor called
# 1000mah
