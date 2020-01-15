import pygame, sys
import time
# 令飞机能左右移动
  
# 初始化
pygame.init()
size = screen_width, screen_height = 600, 800
BLACK= 0, 0, 0
screen = pygame.display.set_mode(size) #初始化屏幕

# 初始化角色 
hero_image = pygame.image.load('hero.png')
# herorect = (200,660,400,150)

# 获取飞机的长度
hero_image_width =  hero_image.get_width()
# 获取飞机的宽度
hero_image_height = hero_image.get_height()

# 飞机的初始坐标，应该在下面的正中间
x = screen_width/2 - hero_image_width/2
y = screen_height - hero_image_height

# 定义常量
MOVE_DIR_LEFT = 0    # 向左移动
MOVE_DIR_RIGHT = 1	 # 向右移动

pygame.display.set_caption("AircraftGame")  # 初始化标题

# 飞机的移动偏移量，每个方向设置一个
move_L, move_R, move_U, move_D = 0, 0, 0, 0

 
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




    screen.fill(BLACK)
    screen.blit(hero_image, (x, y))
    pygame.display.update() #更新














