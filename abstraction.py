class Car:
    def __init__(self):
        self.clutch = False
        self.brk = False
        self.accelerate = False
        self.car = False

    def start(self,car):
        if car == "start" :       
            self.car = True
            self.clutch = True
            self.accelerate = True
            print("Car started..")
        else :
            print("Car already start or unable to start")
 #abstract all the essential details and showing only relevant information
c1 = Car()
c1.start("start")
