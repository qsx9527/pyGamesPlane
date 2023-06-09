import pygame
from game01_Sprite import *

pygame.init()

screen = pygame.display.set_mode((480, 700))

# 背景
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))


# 角色
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (190, 500))

# 统一update
pygame.display.update()

# 时钟对象设置帧率
clock = pygame.time.Clock()

# rect记录角色初始记录
hero_rect = pygame.Rect(190, 500, 102, 126)

i = 0
# 游戏循环
while True:
    # 代码执行频率决定
    clock.tick(99)
    # 监听事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出。。。")
            pygame.quit()
            exit()
    # 捕获事件
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)



    hero_rect.y -= 3

    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    pygame.display.update()



pygame.quit()
