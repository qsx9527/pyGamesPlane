from game01_Sprite import *
import pygame


class PlaneGame(object):
    """打飞机主游戏"""

    def __init__(self):
        print("游戏初始化......")
        # 窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # 时钟
        self.clock = pygame.time.Clock()

        # 精灵
        self.__create_sprites()

        # 定时器  敌机定时器
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 100)

    def __create_sprites(self):
        # 创建背景精灵与精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 英雄精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始")

        while True:
            self.clock.tick(FRAME_PER_SEC)

            self.__event__handler()

            self.__check_collide()

            self.__update_sprites()

    # 监听事件
    def __event__handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌方飞机生成......")
                enemy = Enemy()
                self.enemy_group.add(enemy)
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右")
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.hero.speed = 4
            self.hero.xy = 0
        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed = -4
            self.hero.xy = 1
        elif key_pressed[pygame.K_UP]:
            self.hero.speed = -4
            self.hero.xy = 2
        elif key_pressed[pygame.K_DOWN]:
            self.hero.speed = 4
            self.hero.xy = 3

        else:
            self.hero.speed = 0

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    def __update_sprites(self):

        self.enemy_group.update()
        self.back_group.update()
        self.hero_group.update()
        self.hero.bullets.update()
        self.back_group.draw(self.screen)
        self.hero_group.draw(self.screen)
        self.enemy_group.draw(self.screen)
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == "__main__":

    game = PlaneGame()

    game.start_game()
