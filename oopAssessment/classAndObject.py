class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car make: {self.make}, model: {self.model}, year: {self.year}")

my_car = Car("Audi", "BMW", "2021")
my_car.display_info()