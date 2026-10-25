# inheritance - resuability
# encapsulation - data security
# abstarction - show simplicity or hide complexity
# polymorphism - many forms


# means hiding the implementation but providing the service
# show only neccessary features
# hide complexity and make simplicity

# what you can do
# you dont want how it works

# real life examples in abstarction
# listening songs
# start car
# restaraunt
# washing machine
# atm machine


class FaceBook:
    # attributes
    # methods
    def login(self):
        # validation
        self.__validate()
        # authentication
        self.__authenticate()
        # displayhome
        self.__displayhome()

    def __displayhome(self):
        print("welcome to facebook")

    def __validate(self):
        print("doing validation")

    def __authenticate(self):
        print("doing authentication")


faobj = FaceBook()
faobj.login()  # show only neccessary features (hiding validation and authentication)
# faobj.__validate()
# faobj.__authenticate()
