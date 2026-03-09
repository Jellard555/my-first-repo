import pygame
from pygame.sprite import Sprite
from settings import Settings


class Alien(Sprite,Settings):
    def __init__(self,ai_game):      #初始化外星人 和设置初始位置
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings        
        self.image = pygame.image.load('C:/Users/Jellard/Desktop/python_word/alien_invasion/images/fleet.bmp')  #设置rect属性
        self.image = pygame.transform.scale(self.image,(80,80))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)  #储存外星人精确水平位置
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0 )
    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction    #向右移动外星人
        self.rect.x = self.x 
