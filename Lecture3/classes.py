class Film:

    def __init__(self, d= -1,megan = False, m = -1, t = ""):
        self.duration = d
        self.isMegan = megan
        self.money = m
        self.title = t
        self.protogonist = "Jacob Bang"

    def isPopular(self, stars = 0):
        if self.isMegan:
            return self.duration*10+stars
        else:
            return 0


f = Film(120, True, 80000, "The PIPEC")
f2 = Film()

print(f.isPopular(20))
print(f2.isPopular())
 

print(f.duration, f.isMegan, f.title, f.money)
print(f2.duration, f2.isMegan, f2.title, f2.money)


