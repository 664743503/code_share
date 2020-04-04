#!/usr/bin/python3 python3
# coding=utf-8
import pygame

pygame.init()

# 创建游戏的窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像:加载图片-->绘制图像-->刷新显示
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))
pygame.display.update()

# 绘制英雄图像
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 定义rect记录英雄的初始位置
hero_rect = pygame.Rect(200, 500, 102, 126)

# 游戏循环
while True:
    # 设置循环体内部代码执行的频率
    clock.tick(60)
    hero_rect.y -= 1
    if hero_rect.y <= - hero_rect.height:
        hero_rect.y = 700
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    pygame.display.update()

pygame.quit()
