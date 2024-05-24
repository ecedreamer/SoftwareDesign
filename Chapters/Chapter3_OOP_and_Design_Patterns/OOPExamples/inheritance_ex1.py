"""
Inheritance: process of deriving attributes and behaviors of parent class to child classes
- Parent Class | Base Class | Super class
- Child Class | Derived Class | Sub class


IS A RULE is inheritance
HAS A RULE is not inheritance, it is Composition(Association)
"""

class Car:  # parent class
    def __init__(self, brand, model, color, milage):
        self.car_brand = brand
        self.car_model = model
        self.color = color
        self.milage = milage

    def get_car_intro(self):
        return self.car_brand + " " + self.car_model

class ElectricCar(Car):
    def __init__(self, brand, model, color, milage, charg_time):
        super().__init__(brand, model, color, milage)
        self.charging_time = charg_time

    def get_electric_car_intro(self):
        return self.car_brand + " Charge Time: " + str(self.charging_time)


def main():
    car1 = Car("TATA", model="Nexon", color="white", milage=10)
    car_intro = car1.get_car_intro()
    print(car_intro)

    mycar2 = ElectricCar("MG", "Model 4", "Blue", 150, 5)
    mycar_intro = mycar2.get_electric_car_intro()
    print(mycar_intro)

main()
