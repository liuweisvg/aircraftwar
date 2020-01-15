import pygame, sys
import time

'''
Change log
1.0.3 - fixed bullet initial position!
1.0.2 - you can shoot bullets with space key!
1.0.1 - you can move the aircraft with arrow keys!
1.0.0 - initial version
'''

# 初始化
pygame.init()
size = screen_width, screen_height = 600, 800
BLACK= 0, 0, 0
screen = pygame.display.set_mode(size) #初始化屏幕

# 初始化角色 
hero_surf = pygame.image.load('hero.png')
# herorect = (200, 660, 400, 150)

# 获取飞机的长度
hero_width =  hero_surf.get_width()
# 获取飞机的宽度
hero_height = hero_surf.get_height()

# 飞机的初始坐标，应该在下面的正中间
x = screen_width/2 - hero_width/2
y = screen_height - hero_height
pos = [x, y]

pygame.display.set_caption("AircraftGame")  # 初始化标题

# 飞机的移动偏移量，每个方向设置一个
move_L, move_R, move_U, move_D = 0, 0, 0, 0

# 子弹类
bullet_surf = pygame.image.load('bullet_hero.png')
bullet_width = bullet_surf.get_width()
bullet_height = bullet_surf.get_height()

bullet_speed = 1

bullets = []

# 事件与更新
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_L = 1
            elif event.key == pygame.K_RIGHT:
                move_R = 1
            elif event.key == pygame.K_UP:
                move_U = 1
            elif event.key == pygame.K_DOWN:
                move_D = 1
            elif event.key == pygame.K_SPACE:
                new_bullet = [x + hero_width/2 - bullet_width/2, y - bullet_height]
                bullets.append(new_bullet)

        elif event.type == pygame.KEYUP:
            # 某个方向的键盘被松开，这个方向的偏移量为0
            if event.key == pygame.K_LEFT:
                move_L = 0
            elif event.key == pygame.K_RIGHT:
                move_R = 0
            elif event.key == pygame.K_UP:
                move_U = 0
            elif event.key == pygame.K_DOWN:
                move_D = 0

    # 飞机移动后的位置
    x = x + move_R - move_L    
    y = y + move_D - move_U

    # 子弹移动后的位置
    for bullet in bullets:
        bullet[1] -= bullet_speed

    tick = pygame.time.get_ticks()

    # 画图
    screen.fill(BLACK)
    screen.blit(hero_surf, (x, y))
    for bullet in bullets:
        screen.blit(bullet_surf, (bullet[0], bullet[1]))

    pygame.display.update() #更新
