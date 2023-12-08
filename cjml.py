import pygame
from pygame.locals import *

# 初始化游戏
pygame.init()

# 设置窗口大小和标题
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Super Mario")

# 加载图像
bg_image = pygame.image.load("background.png")
player_image = pygame.image.load("player.png")

# 设置玩家的初始位置和速度
player_x = 100
player_y = 400
player_speed = 5

# 游戏循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # 更新玩家位置
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player_x -= player_speed
    if keys[K_RIGHT]:
        player_x += player_speed

    # 绘制背景和玩家
    screen.blit(bg_image, (0, 0))
    screen.blit(player_image, (player_x, player_y))

    # 刷新屏幕
    pygame.display.flip()

# 退出游戏
pygame.quit()
