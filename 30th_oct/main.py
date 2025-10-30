# class Calculator():
#     def __init__(self, a, b):
#         self.a=a
#         self.b=b

#     def add(self):
#         print(self.a+self.b)

#     def subtract(self):
#         print(self.a-self.b)

#     def multiply(self):
#         print(self.a*self.b)

#     def divide(self):
#         print(self.a/self.b) 

# var1=Calculator(10,20)
# var1.add()
# var1.subtract()
# var1.multiply()
# var1.divide()

# parent
class Factory():
    def __init__(self):
        pass
    def make_veh(self):
        print("I am making a general vehicle")

# class child_class_name(parent_class_name1, parent)
class CarFactory(Factory):
    def __init__(self):
        pass

    # manufacturing  cars
    def make_cars(self):
        print("I am manufacturing only cars")

    def make_veh(self):
        print("I am changing my grandparent class to my own")

class BikeFactory(Factory) :
    def __init__(self):
        pass

    # manufacturing bikes
    def make_bikes(self):
        print("I am manufacturing only bike")

    def make_veh(self):
        print("I am changing my grandparent class to my own") 
           


new_car_factory = CarFactory()
# self property 
new_car_factory.make_cars()

# parent property
new_car_factory.make_veh()


