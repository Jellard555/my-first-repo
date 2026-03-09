class Settings:
    def __init__(self):   #游戏初始化的设置
        self.screen_width = 1200  #对于屏幕的设计
        self.screen_height = 1000
        self.bg_color = (230,230,230)

        self.ship_speed = 1.5
        self.ship_limit = 3


        self.bullet_speed = 6.0
        self.bullet_width = 30
        self.bullet_height = 1.5
        self.bullet_color = (160,60,10)
        self.bullets_allowed = 5  #限制子弹数量


        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 5

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.alien_speed = 1.5
        self.bullet_speed = 2.5

        self.fleet_direction = 1

        self.alien_score = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_score = int(self.alien_score * self.score_scale)
        print(self.alien_score)