import pygame, sys
import time
import random
import os

'''
Change log
1.0.5 - Today I learned KidsCanCode's pygame template!
http://patreon.com/kidscancode
1.0.4 - enemies are automatically spawned!
1.0.3 - fixed bullet initial position!
1.0.2 - you can shoot bullets with space key!
1.0.1 - you can move the aircraft with arrow keys!
1.0.0 - initial version
'''

WIDTH = 600
HEIGHT = 800
FPS = 30

TITLE = "Aircraft Game"

BLACK = (0, 0, 0)

HERO_SPEED = 3

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

class Hero(pygame.sprite.Sprite):
    # sprite for the Hero
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "hero.png")).convert()
        # self.image.fill(GREEN)
        #self.image.set_colorkey(BLACK) # command to ignore the background black color
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - self.rect.height / 2)
        self.x_speed = 0
        self.y_speed = 0
    
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

# 初始化
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
hero = Hero()
all_sprites.add(hero)

# 子弹类
bullet_surf = pygame.image.load('bullet_hero.png')
bullet_width = bullet_surf.get_width()
bullet_height = bullet_surf.get_height()
bullet_speed = 3
bullets = []

# 敌机
enemy1_surf = pygame.image.load('enemy1.png')
enemy1_width = enemy1_surf.get_width()
enemy1_height = enemy1_surf.get_height()
enemy1_speed = 3
enemy1s = []

last_enemy_generation_tick = 0

# 事件与更新
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # process input(events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.x_speed = -HERO_SPEED
            elif event.key == pygame.K_RIGHT:
                hero.x_speed = HERO_SPEED
            elif event.key == pygame.K_UP:
                hero.y_speed = -HERO_SPEED
            elif event.key == pygame.K_DOWN:
                hero.y_speed = HERO_SPEED
            elif event.key == pygame.K_SPACE:
                pass
                #new_bullet = [x + hero_width/2 - bullet_width/2, y - bullet_height]
                #bullets.append(new_bullet)

        elif event.type == pygame.KEYUP:
            # 某个方向的键盘被松开，这个方向的偏移量为0
            if event.key == pygame.K_LEFT:
                hero.x_speed = 0
            elif event.key == pygame.K_RIGHT:
                hero.x_speed = 0
            elif event.key == pygame.K_UP:
                hero.y_speed = 0
            elif event.key == pygame.K_DOWN:
                hero.y_speed = 0

    # 自动产生敌机
    tick = pygame.time.get_ticks()
    if tick - last_enemy_generation_tick >= 1000:
        last_enemy_generation_tick = tick
        if random.random() < 0.5:
            enemy_x = int(WIDTH * random.random())
            enemy_y = -enemy1_height
            new_enemy = [enemy_x, enemy_y]
            enemy1s.append(new_enemy)

    all_sprites.update()

    # 子弹移动后的位置
    for bullet in bullets:
        bullet[1] -= bullet_speed

    # 敌人移动后的位置
    for enemy in enemy1s:
        enemy[1] += enemy1_speed

    # 画图
    screen.fill(BLACK)
    all_sprites.draw(screen)

    for bullet in bullets:
        screen.blit(bullet_surf, (bullet[0], bullet[1]))
    for enemy in enemy1s:
        screen.blit(enemy1_surf, (enemy[0], enemy[1]))

    pygame.display.flip()

pygame.quit()
