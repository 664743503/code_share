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

# 游戏循环
while True:
    pass

pygame.quit()
