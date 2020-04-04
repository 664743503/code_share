#!/usr/bin/python3 python3
# coding=utf-8

import pygame
from plane_sprites import *

class PlaneGame(object):
    "飞机大战主游戏"
    def __init__(self):
        print("游戏初始化")
        # 1.创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，创建精灵和精灵组
        self.__create_sprites()
        # 4.设置定时器事件，创建敌机，1s一个
        pygame.time.set_timer(ENEMY_EVENT, 1000)
        # 5.设置定时器事件，发射子弹，0.5s一个
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)


    def __create_sprites(self):
        # 1.创建背景精灵和精灵组，实现滚动效果
        bg1 = Background()
        bg2 = Background(True)
        self.bg_group = pygame.sprite.Group(bg1, bg2)
        # 2.创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 3.创建英雄的精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)


    def start_game(self):
        print("游戏开始...")
        while True:
            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2.事件监听
            self.__event_handle()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制精灵组
            self.__update_sprites()
            # 5.刷新显示
            pygame.display.update()

    def __event_handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == ENEMY_EVENT:
                # print("敌机出场...")
                # 创建敌机精灵
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动...")
        # 使用键盘提供的方法获取键盘按键
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应的按键索引值 1
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 3
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
        else:
            self.hero.speed = 0


    def __check_collide(self):
        # 1.子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 2.敌机撞毁英雄
        hero_collision = pygame.sprite.groupcollide(self.hero_group, self.enemy_group, True, True)
        # 3.判断列表有无内容
        if len(hero_collision) > 0:
            # 1.让英雄牺牲
            self.hero.kill()
            # 2.结束游戏
            PlaneGame.__game_over()
    
    def __update_sprites(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)
        
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    # 因为不需要调用类成员变量和类成员方法，所以改成静态方法
    @staticmethod
    def __game_over():
        print("游戏结束...")
        pygame.quit()
        exit()


if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
