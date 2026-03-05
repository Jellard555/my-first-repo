import pygame.font
class Button:
    def __init__(self,ai_game,msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()                 #设置初始属性

        self.width,self.height = 200,50                           #设置按钮尺寸和基本属性
        self.button_color = (0,135,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        self.rect = pygame.Rect(0,0,self.width,self.height)       #创建rect按钮，并居中
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)                                       #按钮的标签只创建一次

    def _prep_msg(self,msg):
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)    #将msg渲染为图像
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)         #fill用于绘制时填充颜色
        self.screen.blit(self.msg_image,self.msg_image_rect)  #blit用于绘制文本