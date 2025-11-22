class Car:
    runs = True
    def __init__(self,name,model):
        self.name = name
        self.model = model

    def start(self):
        if self.runs:
            print(f"Name is: {self.name} modal is: {self.model} car is starting")
        else:
            print(f"{self.name} car is not starting somwthing went wrong!")

my_car = Car("Hundai","2020")
# my_car.runs = False
my_car.start()  
print(isinstance(my_car,Car))