#PART 1 OOP one
# knowing some basic concepts of OOP
# Classes.Objects.Data attributes.Class attributes
#Methods.Inheritance

# two
class InputOutString:
    def __init__(self):
        self.string = ""
    def get_string(self):
        a = input("please enter a string")
        self.string = a
        return self.string
    def print_string(self):
        print(self.string)
b = InputOutString()
b.get_string()
b.print_string()

#three(a)
import math
class Shape():
    def __init__(self,colour):
        self.colour = colour
    def get_colour(self):
        return self.colour
    
class Cricle(Shape):
    def __init__(self,colour,radius):
        super().__init__(colour)
        self.radius = radius
    def get_radius(self):
        return self.radius
    def get_area(self):
        return math.pi * self.radius ** 2
    
    def __str__(self):
        print(f"The {self.colour} circle has area {self.get_area()} ")

class Rectangle(Shape):
    def __init__(self,colour,length,width):
        super().__init__(colour)
        self.length = length
        self.width = width
    def get_area(self):
        return self.length * self.width
    def get_parimeter(self):
        return 2 * (self.width + self.length)
    def __str__(self):
        print(f"The {self.colour} rectangle has area {self.get_area()} and parimeter {self.get_parimeter()}")

class Cylinder(Cricle):
    def __init__(self,colour,height):
        super().__init__(colour)
        self.height = height
    def get_area(self):
        return 2 * math.pi * self.radius  * (self.radius + self.height)
    def get_volumn(self):
        return math.pi * self.radius ** 2 * self.height
    def __str__(self):
        print(f"The {self.colour} cylinder has area {self.get_area()} and volumn {self.get_volumn()}")

#three(b)
def test_shapes():
    c1 = Cricle("blue" , 4)
    c1.__str__()

    r1 = Rectangle("yellow",4,4)
    r1.__str__()

    cy1 = Cylinder("red" , 5)
    cy1.__str__()
d = test_shapes() 
#three(c) unfinished
#four 
class Counter():
    total_instances = 0
    total_increment = 0
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.count = 0
        Counter.total_instances += 1
    def increment(self,amount = None):
        if amount is None:
            self.count += 1
        else:
            self.count += amount
        Counter.total_increment += 1
    def decrement(self,amount = None):
        if amount is None:
            self.count -= 1
        else:
            self.count -= amount
        
#five
class Exception():
    def __init__(self,message):
        self.message = message
    def __str__(self):
        return self.message
    
#six
