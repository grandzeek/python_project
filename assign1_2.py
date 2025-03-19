# Assignment 1: Designing a Smartphone Class
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price  # Encapsulated attribute
    
    def get_price(self):  # Encapsulation: getter method
        return self.__price
    
    def set_price(self, new_price):  # Encapsulation: setter method
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price cannot be negative!")
    
    def specs(self):
        return f"{self.brand} {self.model} costs ${self.__price}"

# Child class with additional method
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, price, gpu):
        super().__init__(brand, model, price)
        self.gpu = gpu
    
    def gaming_specs(self):
        return f"{self.brand} {self.model} has a {self.gpu} GPU, great for gaming!"

# Creating objects
phone1 = Smartphone("Apple", "iPhone 14", 999)
phone2 = GamingSmartphone("Asus", "ROG Phone 6", 1299, "Adreno 730")

print(phone1.specs())
print(phone2.specs())
print(phone2.gaming_specs())

# Activity 2: Polymorphism with move() method
class Vehicle:
    def move(self):
        pass  # This method will be overridden by subclasses

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# Creating objects
car = Car()
plane = Plane()
boat = Boat()

# Demonstrating polymorphism
vehicles = [car, plane, boat]
for v in vehicles:
    print(v.move())
