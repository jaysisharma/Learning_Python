class Vehicle:
    #Constructor that executes when the program runs
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        print("Vehicle Started")


# initialzing the Car Class
class Car(Vehicle):

    total_cars = 0 # Creating a varaible inside the class to count the total objects
    def __init__(self, brand, model, year, car_type):
        super().__init__(brand, model, year)
        self.car_type = car_type
        Car.total_cars +=1

    def Car_info(self): # Function to print the Car value
        print(f"Car Brand is {self.brand}, Model is {self.model}, Released year is {self.year} {self.car_type} Type")

# Creating Objects

car1 = Car('Audi', 'S3', 2004, 'Diesel')
car2 = Car('BMW', 'M10', 2010, 'Petrol')
car3 = Car('Hyndai', 'T20', 2020, 'Electric')

#Function Call

car1.Car_info()
car2.Car_info()
car3.Car_info()
print(Car.total_cars) # Accessing the Class variable



# Inheritance
# Passing the main class to the Subclass as parameter

class ElectricCar(Vehicle):
    def __init__(self, brand, model, year,battery_capacity):
        super().__init__(brand, model, year) # Accessing the Parent Class values using super()
        self.batter_capacity = battery_capacity

    def Car_Data(self):
        print(f"The Electric Car Specification are {self.brand} Brand {self.model} Model {self.year} year {self.batter_capacity} Battery Capacity")
    

car4 = ElectricCar('Lamborghini', 'Urus', 1998, '12000mAh')

car4.Car_Data()

#Polymorphism

class Truck(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
    
    def start(self):
        print('Truck Started')


truck = Truck('Mahindra', 'S2', 2004)
car4 = ElectricCar('Lamborghini', 'Urus', 1998, '12000mAh')


def drive(Vehicle):
    Vehicle.start()

drive(truck)
drive(car4)

