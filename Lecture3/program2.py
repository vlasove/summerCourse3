class Machine:
    poop = 20
    def __init__(self, nw = 0 , c = "black"):
        self.n_wheels = nw
        self.color = c

    def friction(self):
        return self.n_wheels*150


class Auto(Machine):
    def __init__(self, eng = 1, vol = 1, mark = "JiGuyl"):
        super().__init__(self)
        self.engine = eng
        self.volume = vol
        self.mark = mark

    def horse_power(self):
        return self.engine/self.volume*1000

class Bike:
    def __init__(self, mspd = 1000, n_pas = 1):
        self.max_speed = mspd
        self.n_passengers = n_pas

    def horse_power(self):
        return "Many many many HP!"

    

