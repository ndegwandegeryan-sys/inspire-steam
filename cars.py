#Name : ndegwandegeryan
#Date : 23/02/2026
# program to show classes in python

class Car():
    #attributes of the car 
    def __init__(self,model,make,color,year):
        self.model = model
        self.make = make 
        self.color = color
        self.year = year

    #print car details
    def print_details(self,model,make,color,year ):
        print(f"The {make} {model} of color {color} was mnufactured in {year}")


#instantiate a class object

my_car = Car("Atenza","Mazda","White",2022)
dads_car = Car("Landcruiser","Toyota","Black",2025)

my_car.print_details("Atenza","Mazda","White",2022)
dads_car.print_details("Landcruiser","Toyota","Black",2025)





