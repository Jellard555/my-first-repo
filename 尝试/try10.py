#面向对象编程
class fruit:
    def _init_ (self,fresh,color,size):
        self.fresh = fresh
        self.color = color
        self.size = size

color = ("red","green","blue")
color_iter = iter(color)
print(next(color_iter))
print(next(color_iter))


class CuteCat :
    def __init__(self, cat_name,cat_age,cat_color):
        self. name = cat_name 
        self. age = cat_age
        self. color = cat_color 
    def speak(self):
        print('miao'*self.age)
    def think(self,content):
        print(f'xiaomao{self.name}zaisikao{content}')
cat1 = CuteCat("sun",2,"red")
cat1.think("quganma")
cat1.speak()
cat2 = CuteCat("bright",6,"pink")

#for循环的复习
course = "JC1001"
for i in course:
    print(i)
