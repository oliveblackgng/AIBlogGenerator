class Car:
    def __init__(self, brand):
        # 'self.brand' is an instance variable tied to the specific object
        self.brand = brand

    def show_brand(self):
        # Accessing the brand of the current object using 'self'
        print("The brand is", self.brand)

# Create an object of Car
my_car = Car("Toyota")

# Call the method to show the brand
my_car.show_brand()