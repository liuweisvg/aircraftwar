# 画出屏幕，和静止的飞机
import pygame, sys
 
# 初始化
pygame.init()
size = screen_width, screen_height = 600, 800
BLACK= 0, 0, 0
screen = pygame.display.set_mode(size) #初始化屏幕

# 初始化角色 
hero_image = pygame.image.load('hero.png')
herorect = (200,660,400,150)

# 获取飞机的长度
hero_image_width =  hero_image.get_width()
# 获取飞机的宽度
hero_image_height = hero_image.get_height()
# 飞机的起始位置，应该在下面的正中间
x = screen_width/2 - hero_image_width/2
y = screen_height - hero_image_height

# 定义常量
MOVE_DIR_LEFT = 0    # 向左移动
MOVE_DIR_RIGHT = 1	 # 向右移动

pygame.display.set_caption("AircraftGame")  # 初始化标题


# 设置初始坐标
 

# 事件与更新
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BLACK)
    screen.blit(hero_image, herorect)
    pygame.display.update() # 更新


