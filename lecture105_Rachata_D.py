class Vehicle:
    licenseCode =""
    serialCode =""
    DNA = ""
    def turnonair(self):
        print("Turn on")

class car(Vehicle):
    def sayhell(self):
        print("hello world:car")

class van(Vehicle):
    def sayhell(self):
        print("hello world:van")

class pickup(Vehicle):
    def sayhell(self):
        print("hello world:pickup")

class estatecar(Vehicle):
    def sayhell(self):
        print("hello world:estatecar")

car1 = car()
car1.turnonair()
car1.sayhell()

van1 = van()
van1.turnonair()
van1.sayhell()

pickup1 = pickup()
pickup1.turnonair()
pickup1.sayhell()

estatecar1 = estatecar()
estatecar1.turnonair()
estatecar1.sayhell()