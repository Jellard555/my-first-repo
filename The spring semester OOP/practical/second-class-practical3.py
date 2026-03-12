def Counter(*arg):
    result = 0
    for item in arg:
        result += item
    return result
b = range(1,101)
a = Counter(*b)
print(a) 


class Point():
    def __init__(self,x,y,**kwargs):
        super().__init__(**kwargs)
        self.x = x
        self.y = y
        self.location = (self.x,self,y)
    def distance_to_other(self,other):
        distance = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return distance
    def __str__(self):
        return self.location
    def __eq__(self,other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

class Shape():
    total_shape = 0
    def __init__(self,color,center,**kwargs):
        super().__init__(**kwargs)
        self.color = color
        self.center = center
    def get_area(self):
        pass
    def move_center(self,new_point):
        self.center = new_point

import math

class Circle(Shape):
    def __init__(self,color,center,radius):
        super().__init__(color,center)
        self.radius = radius
    def get_area(self):
        area = math.pi * self.radius ** 2
        return area
    def is_inside(self,point):
        dis = ((self.center.x - point.x) ** 2 + (self.center.y - point.y) ** 2) ** 0.5
        if dis <= self.radius:
            return True
        else:
            return False
class Cylinder():
    def __init__(self,base_circle,height):
        self.base_circle = Circle(base_circle.color,base_circle.center,base_circle.radius)
        self.height = height
    def get_surface_area(self):
        sa = 2 * math.pi * self.base_circle.radius * (self.height + self.base_circle.radius)
        return sa
    def get_volume(self):
        vo = math.pi * self.height * self.base_circle.radius ** 2
        return vo