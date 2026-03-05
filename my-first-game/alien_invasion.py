import sys
import random
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship      
from bullet import Bullet
from alien import Alien
from button import Button



class AlienInvasion:                                 #管理游戏资源和行为的类
    def __init__(self):                              #初始化游戏并创建游戏资源 基本上都是调用pygame中的函数功能
        pygame.init()
        self.clock = pygame.time.Clock()             #调用计时功能保持帧率
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens  = pygame.sprite.Group()      #这个group是什么意思？
        self._create_fleet()                      #这创建了一个舰队的编组，下面编写舰队的方法
        self.bg_color = (230,230,230)                #设置背景色 括号内分别为（红，绿，蓝）
        self.bullet_color = (60,60,60)            #子弹颜色的设定
        self.game_active = False
        self.play_button = Button(self,"play")

#上面是设置游戏基本的属性，下面是对属性进行游戏内的设计与赋值

    def run_game(self):                              #开始游戏的主循环
        while True:                                  #判断键盘和鼠标的事件
            self._check_events()                     #注意代码的顺序
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            #self._create_fleet()                    #每次都会生成新的外星人，从而掩盖了移动中的外星人，才有只向一边移动的问题
            self.clock.tick(60)
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
             if bullet.rect.bottom <= 0:
                  self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
        #   print(len(self.bullets))                 #用于检查是否子弹有消失
    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)   #检查子弹和飞船的rect是否接触，若接触就为True，告诉pygame删除对应的子弹和飞船
        if collisions:
            for aliens in collisions.values():   
                self.stats.score += self.settings.alien_score * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            self.stats.level += 1
            self.sb.prep_level()
   # def _check_aliens_collisions(self):
    #    collisions2 = pygame.sprite.groupcollide(self.aliens,self.aliens,True,True)
     #   self.aliens.empty()
    def _check_events(self):                         #响应按键和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:        #这个QUIT是不是结束的指令？ 是在pygame中的常量 用于捕获用户关闭游戏窗口的行为
                    sys.exit()
                elif event.type == pygame.KEYDOWN:   #飞船的位置变化，用pygame中的KEYDOWN进行实现
                    self._check_keydown_events(event)
                elif  event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
    def _check_keydown_events(self,event):
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:           #按q键退出
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()
    def _check_keyup_events(self,event):
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False    
            #self.screen.fill(self.bg_color)         #每次循环都重新绘制屏幕
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:  #限制子弹数量
            new_bullet = Bullet(self)                  #创建一颗子弹，并加入编组bullets  
            self.bullets.add(new_bullet)     
    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)#更新屏幕内容
            for bullet in self.bullets.sprites():
                 bullet.draw_bullet()
            self.aliens.draw(self.screen)
            self.sb.show_score()
            if not self.game_active:
                 self.play_button.draw_button()
            self.ship.blitme()                       #ship类后加.blitme(),是属性ship的重新绘制，这是一个函数绘制
            pygame.display.flip()                    #让最近绘制的屏幕可见，用新生成的屏幕替代旧的，元素更新，达成一种平滑过渡的动画效果
            #self.clock.tick(60)
    def _create_fleet(self):                         #重构createfleet，便于后续应用于创建更多外星飞船
         alien = Alien(self)
         alien_width,alien_height = alien.rect.size
        # current_x,current_y = alien_width,alien_height    #外星人的位置固定
         #while current_y < (self.settings.screen_height - 3 * alien_height):
          #  while current_x < (self.settings.screen_width - 2 * alien_width):
          #      self._create_alien(current_x,current_y)
           #     current_x += 2 * alien_width
           # current_x = alien_width
           # current_y += 2 * alien_height
         max_aliens_x = (self.settings.screen_width - 2 * alien_width)  //  (2 * alien_width)
         max_aliens_y = (self.settings.screen_height - 3 * alien_height)  //  (2 * alien_height)
         num_aliens = random.randint(6,max_aliens_x * max_aliens_y // 1)

         for _ in range(num_aliens):
              x1_position = random.randint(alien_width,self.settings.screen_width - 2 * alien_width)
              y1_position = random.randint(alien_height,self.settings.screen_height // 2 )
              self._create_alien(x1_position,y1_position)
    def _create_alien(self,x_position,y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)                   #添加外星飞船，但还要其显示
    def _update_aliens(self):
         self._check_fleet_edges()
         self.aliens.update()
         if pygame.sprite.spritecollideany(self.ship,self.aliens):  #spritecollideany函数接收两个实参，检查是否有成员和精灵发生了碰撞
              #print("Hitting!")
              self._ship_hit()
         self._check_aliens_bottom()
    def _check_fleet_edges(self):                    #在外星人碰到边缘时做出措施
         for alien in self.aliens.sprites():
              if alien.check_edges():
                   self._change_fleet_direction()
                   break
    def _change_fleet_direction(self):               #整个飞船向下移动，并改变它们的方向
         for alien in self.aliens.sprites():
              alien.rect.y += self.settings.fleet_drop_speed
         self.settings.fleet_direction *= -1
    def _ship_hit(self):
         if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
         else:
            self.game_active = False
            pygame.mouse.set_visible(True)
    def _check_aliens_bottom(self):            #飞船碰到屏幕底部，也当撞击处理
         for alien in self.aliens.sprites():
              if alien.rect.bottom >= self.settings.screen_height:
                   self._ship_hit()
                   break
    def _check_play_button(self,mouse_pos):
         #if self.play_button.rect.collidepoint(mouse_pos):
          #    self.stats.reset_stats()
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.settings.initialize_dynamic_settings()
            pygame.mouse.set_visible(False)
            self.game_active = True
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()