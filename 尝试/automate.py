class Cat:
    def __init__(self,name,color):
        self.name = name
        self.color = color
cat1 = Cat("lihhai","green")
a = f"这是一只猫，名字叫{cat1.name},颜色是{cat1.color}"
print(a)

import sys
import pygame    #怎么绘制屏幕？
class BlueSky:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Blue Sky")
        self.bg_color = (0,0,300)