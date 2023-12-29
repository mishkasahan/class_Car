class Car:
    def __init__(self, make, model, year, mileage):
        self.__make = make
        self.__model = model
        self.year = year
        self.mileage = mileage

    def drive(self, lenght):
        if self.mileage + lenght > 300000:
            print("Якщо ви здійсните цю поїздку, то перевищите максимальний пробіг авто")
        else: self.mileage += lenght

    def setmake(self, make1):
        self.__make = make1

    def setmodel(self, model1):
        self.__model = model1

    def setyear(self, year1):
        self.year = year1

    def setmileage(self, mileage1):
        self.mileage = mileage1

mash = Car("Opel", "Astra", 2010, 298000)
mash.drive(2100)
mash.setyear(2011)
print(mash.year)
