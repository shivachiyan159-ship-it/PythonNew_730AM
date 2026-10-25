# class
# object
# inheritance
# polymorphism
# abstarction
# encapsulation


class MahindraCar:
    # attributes (varibles or data)
    # methods (functions or behaviors)
    pass

tharobj=MahindraCar()
tharobj.name="thar"
tharobj.color="black"
tharobj.price="20laks"
print(tharobj.name)


xuvobj=MahindraCar()
xuvobj.name="xuv"
xuvobj.color="red"
xuvobj.price="25laks"
print(xuvobj.name)

scorpio=MahindraCar()
scorpio.name="scorpio"
scorpio.color="white"
scorpio.price="30laks"
print(scorpio.name)



class MahindraCarNew:
    # attributes (varibles or data)     
    # methods (functions or behaviors)
    # constructor (it is a special membor method which is used to initialize the data and it will call automatically whenever created object)
    def __init__(self,name,color,price):
        self.name=name
        self.clr=color
        self.price=price
        
    def start(self):
        print(f"{self.name} car started")
    
    def stop(self):
        print(f"{self.name} car stopped")

    
      
# def dispaly():
#     tharobj=MahindraCarNew("thar","red","20laks")
#     print(tharobj.clr)

# tharobj=MahindraCarNew("thar","red","20laks")
# print(tharobj.clr)
# tharobj.start()
# tharobj.stop()


# xuvobj=MahindraCarNew("xuv","black","25lakhs")
# print(xuvobj.clr)
# xuvobj.start()
# xuvobj.stop()

# dispaly()

# crud operation
# c - create
# r - read
# u - update
# d - delete


    
