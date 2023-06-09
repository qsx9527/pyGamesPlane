import random
import pygame

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SEC = 99
# 定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 子弹
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    
    def __init__(self, image_name, speed=1):
        # 调用父类初始化
        super().__init__()

        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        pygame.display.update()
        self.rect.y += self.speed


# 派生子类背景精灵
class Background(GameSprite):

    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        super().update()
        # 背景精灵图片滚动实现
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.speed = random.randint(1, 3)
        # bottom底部
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            print("飞出屏幕删除")
            self.kill()

    def __del__(self):
        print("飞机死了")


class Hero(GameSprite):
    """英雄精灵"""
    # 横纵坐标控制
    xy = 0

    def __init__(self):
        super().__init__("./images/me1.png", 0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        if self.xy == 0 or self.xy == 1:
            self.rect.x += self.speed
        elif self.xy == 2 or self.xy == 3:
            self.rect.y += self.speed

        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.bottom >= SCREEN_RECT.bottom:
            self.rect.bottom = SCREEN_RECT.bottom

    def fire(self):
        print("tututu。。。")

        bullet = Bullet()

        bullet.rect.bottom = self.rect.y - 20
        bullet.rect.centerx = self.rect.centerx

        self.bullets.add(bullet)


class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        super().__init__("./images/bullet1.png", -3)
        pass

    def update(self):
        super().update()

        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("子弹死了")