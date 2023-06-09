import pygame

hero_rect = pygame.Rect(100, 500, 120, 125)
print("角色原点 %d %d" % (hero_rect.x, hero_rect.y))
print("角色尺寸 %d %d" % (hero_rect.width, hero_rect.height))
print("%d %d" % hero_rect.size)
