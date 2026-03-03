import math

def areaParallelogram(b,h):
    area = b * h
    return area
area1 = areaParallelogram(4,6)
print(area1)

def areaTrapezium(b1,b2,a):
    trapezoid = (b1 + b2) / 2 * a 
    return trapezoid
trapezoid1 = areaTrapezium(6,6,4)
print(trapezoid1)

def areaTriangle(base,height):
    area_of_a_triangle = 1/2 * base * height
    return area_of_a_triangle
triangle1 = areaTriangle(4,3)
print(triangle1)

def areaCircleD(diameter):
    area_of_a_circle =  (math.pi / 4) * diameter ** 2
    return area_of_a_circle
circle1 =  areaCircleD(4)
print(circle1)

def  volCuboid(length,width,height):
    cubiod = length * width * height
    return cubiod
volCuboid1 = volCuboid(6,6,6)
print(volCuboid1)

def sAreaCuboid(l,w,h):
     surface_area_of_a_cuboid = (2 * w * l + 2 * l * h + 2 * h * w)
     return  surface_area_of_a_cuboid
volCuboid2 = sAreaCuboid(6,6,6)
print(volCuboid2)

def  sAreaTriPyr(ba,p,sl):
    surface_area_of_a_triangular_pyramid = (ba + 1/2 * p * sl)
    return surface_area_of_a_triangular_pyramid
TriPyr1 = sAreaTriPyr(1,2,3)
print(TriPyr1)

def volSphere(radius):
    volume_of_a_sphere = ((4/3) * math.pi * radius**3)
    return volume_of_a_sphere
Sphere1 = volSphere(4)
print(Sphere1)