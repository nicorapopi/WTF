class car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def drive(self):
        print(f"{self.brand} is driving")

mycar = car("toyota","red")
mycar.drive()