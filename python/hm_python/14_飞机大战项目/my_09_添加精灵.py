#!/usr/bin/python3 python3
# coding=utf-8
import pygame 
from plane_sprites import *

# pygame初始化
pygame.init()

# 创建游戏的窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像:加载图片-->绘制图像-->刷新显示
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

# 绘制英雄图像
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))

# 创建时钟对象
clock = pygame.time.Clock()

# 定义rect记录英雄的初始位置
hero_rect = pygame.Rect(200, 500, 102, 126)

# 创建敌机精灵和敌机精灵组
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy2.png", 2)
enemy_group = pygame.sprite.Group(enemy, enemy1)

# 游戏循环
while True:
    # 设置循环体内部代码执行的频率
    clock.tick(60)

    # 事件监听
    for event in pygame.event.get():
        # 判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            print("退出游戏...")
            pygame.quit()
            exit()

    # 修改飞机的位置
    hero_rect.y -= 1
    if hero_rect.y <= - hero_rect.height:
        hero_rect.y = 700

    # 绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法
    enemy_group.update()    # 让组中所有的精灵更新位置
    enemy_group.draw(screen)    # 在screen上绘制所有的精灵
    
    # 刷新显示
    pygame.display.update()


pygame.quit()
