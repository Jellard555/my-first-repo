import pygame
from pygame.sprite import Sprite


class Ship(Sprite):  #这个.get_rect()是什么意思？   rect是pygame中矩形的表示，pygame可以将所有的
    def __init__(self,ai_game):  #self.ai-game 都只是这个ship中的两个参数，
        super().__init__()
        self.screen = ai_game.screen  #初始化飞船设置 这是总的self设定
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()  #初始化飞船位置
        self.image = pygame.image.load('C:/Users/Jellard/Desktop/python_word/alien_invasion/images/ship.bmp')  #load后面是下载好的内容 加文件的名字
        self.image = pygame.transform.scale(self.image,(50,50))                   #缩小图片
        self.rect = self.image.get_rect()        #这是图片的位置固定？
        self.rect.midbottom = self.screen_rect.midbottom  #让每一个新生成的飞船都在底部中央
        self.x = float(self.rect.x)                      #在飞船的属性x中储存一个浮点数
        self.moving_right = False                     #当按右键的动作不存在，则为False
        self.moving_left = False 
    def update(self):                                 #向右的动作更新，按一下则向右走一个单位
        if self.moving_right and self.rect.right < self.screen_rect.right:
           self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x                  #根据self.x更新rect对象
    def blitme(self):   #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

