# constructor is a special member method which will call automatically whenever you craete object.


class Father:
    # attributes (varaibles)
    # methods (functions)
    # constrcutor (to inilize the data)
    def __init__(self, charecter, color):
        print("father class consytructor called")
        self.chr = charecter
        self.clr = color

    def driving(self):
        print("i can drive")

    def eat(self):
        print("i learn eat from father")


class Mother:
    # attributes (varaibles)
    # methods (functions)
    # constrcutor (to inilize the data)
    def __init__(self, eyes):
        print("mother class constructor clalled")
        self.eyes = eyes

    def cooking(self):
        print("i can cook")

    def eat(self):
        print("i learn eat from mother")


class Son(Father, Mother):
    # attributes (varaibles)
    # methods (functions)
    # constrcutor (to inilize the data)
    def __init__(self, charecter, color, eyes, isBike):
        print("son class constructor called")
        Father.__init__(self, charecter, color)
        Mother.__init__(self, eyes)
        self.bike = isBike

    def pubg(self):
        print("i can play pubg")

    def eat(self):
        print("i can eat")

    def display(self):
        self.driving()
        self.cooking()
        self.eat()
        Father.eat(self)
        Mother.eat(self)
        print(f"i got charcter {self.chr} from my father and i got color {self.clr} from my fatther and i got eyes {self.eyes} from my mother and i have bike {self.bike}")


sonobj = Son("good", "red", "2", "yes")  # 46
sonobj.display()
# print(sonobj.chr)
# print(sonobj.eyes)
# print(sonobj.bike)


#  print("son class constructor called")
#  print("father class consytructor called")
#  print("mother class constructor clalled")
#  good
#  2
#  yes


# sonobj.driving()
# sonobj.cooking()
# sonobj.pubg()
# sonobj.eat()
# Father.eat(sonobj)
# Mother.eat(sonobj)

# print(Son.__mro__)
