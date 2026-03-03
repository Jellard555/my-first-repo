import pygame
import sys

class TestGame:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Test")
        self.bg_color = (30, 50 , 50)  # 浅灰色背景

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 绘制背景+红色矩形（模拟飞船）
            self.screen.fill(self.bg_color)
            pygame.draw.rect(self.screen, (255, 0, 0), (400, 550, 50, 80))  # 底部中间的红色矩形
            pygame.display.flip()

if __name__ == '__main__':
    test = TestGame()
    test.run_game()