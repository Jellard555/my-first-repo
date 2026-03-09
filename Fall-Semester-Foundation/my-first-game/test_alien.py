import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self):
        super().__init__()
        # 用纯色矩形替代图像（排除图像问题）
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # 红色矩形
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

pygame.init()
screen = pygame.display.set_mode((1200, 800))
aliens = pygame.sprite.Group()
aliens.add(Alien())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((30, 50, 50))
    aliens.draw(screen)
    pygame.display.flip()