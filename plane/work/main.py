# -*- coding:utf-8 -*-
from pygame.locals import *
import pygame
import time
import random


# 改造成面向对象的程序： 我方飞机HeroPlane    我方子弹 HeroBullet       |     敌机EnemyPlane   敌方子弹 EnemyBullet
class Plane(object):
    # 初始化
    def __init__(self, screen, x, y, image_path):
        self.x = x
        self.y = y
        self.screen = screen
        self.plane = pygame.image.load(image_path)
        self.bullet_list = []  # 存放多颗子弹列表

    def display(self):
        # 6.将飞机添加到窗口中
        self.screen.blit(self.plane, (self.x, self.y))

        # 准一个空列表
        empty_list = []

        # 遍历子弹列表
        for bullet in self.bullet_list:
            bullet.display()
            # 子弹移动
            bullet.bullet_move()
            # 判定出界否
            if bullet.judge():
                empty_list.append(bullet)

        # 删除子弹
        for b in empty_list:
            self.bullet_list.remove(b)


# 我方飞机HeroPlane
class HeroPlane(Plane):

    # 初始化
    def __init__(self, screen):
        x = (240 - 27) / 2
        y = 400 - 50
        image_path="./feiji/hero.png"
        super().__init__(screen,x,y,image_path)

    def display(self):
        Plane.display(self)

    # 添加左右上下移动的动作
    def move_left(self):
        if self.x <= 0:
            self.x = 0
        else:
            self.x -= 5

    def move_right(self):
        print(self.x)
        if self.x >= 240-27:
            self.x = 240-27
        else:
            self.x += 5

    def move_up(self):
        self.y -= 5

    def move_down(self):
        self.y += 5

    # 定义开火 发射
    def fire(self):
        self.bullet_list.append(HeroBullet(self.screen, self.x, self.y))
        # bullet.display()


# 敌方飞机
class EnemyPlane(Plane):

    # 初始化
    def __init__(self, screen):
        Plane.__init__(self,screen,0,0,"./feiji/enemy3.png")
        self.direction = "right"

        # 定义爆炸效果的内容
        self.bomb_image_list = []
        self.__get_bomb_image()
        self.isbomb = False

        self.image_num = 0  # 显示过得图片  数量
        self.image_index = 0 # 要显示的图片 数量

    #加载爆炸图片函数
    def __get_bomb_image(self):
        for i in range(1,7):
            image_path = "./planeboom/Plane_Boom_0"+str(i)+".png"
            self.bomb_image_list.append(pygame.image.load(image_path))
         # 记录图片列表的长度
        self.image_length = len(self.bomb_image_list)

    def display(self):
        if self.isbomb:
            bomb_image=self.bomb_image_list[self.image_index]
            # 将图片显示在窗口上
            self.screen.blit(bomb_image, (self.x,self.y))
            # 改变遍历image_num
            self.image_num += 1
            # 判断image_num 是否在列表长度范围内
            if self.image_num == (self.image_length+1):
                self.image_num = 0
                self.image_index += 1

                if self.image_index > (self.image_length-1):
                    self.image_index = 5

                    time.sleep(2)
                    exit()

        else:
            Plane.display(self)

    # 添加左右上下移动的动作
    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5

        # 判断是否应该改变方向了
        if self.x > 240-56:
            self.direction = "left"
        elif self.x <= 0:
            self.direction = "right"

    # 定义开火 发射
    def fire(self):
        ran = random.randint(1, 80)
        if ran == 26 or ran == 60:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))


# 定义子弹的父类
class Bullet(object):
    # 初始化的动作
    def __init__(self, screen, x, y, image_path):
        self.x = x
        self.y = y
        self.screen = screen
        self.bullet = pygame.image.load(image_path)

    # 父类的显示
    def display(self):
        self.screen.blit(self.bullet, (self.x, self.y))


# 敌方子弹
# 敌方子弹类 ----》创建子弹类对象 ----》敌方飞机开火 -----》添加到飞机中的子弹列表中
class EnemyBullet(Bullet):
    # 初始化的动作
    def __init__(self, screen, x, y):
        Bullet.__init__(self, screen, x+28, y+35, "./feiji/EnemyBullet1.png")

    def display(self):
        Bullet.display(self)

    # 定义子弹移动的动作
    def bullet_move(self):
        self.y += 5

    # 判断子弹是否出边界
    def judge(self):
        if self.y >= 400:
            return True
        else:
            return False


# 定义我方子弹
# 子弹类----》子弹对象----》将子弹对象显示到窗口
class HeroBullet(object):
    # 初始化的动作
    def __init__(self, screen, x, y):
        Bullet.__init__(self, screen, x+10, y-30, "./feiji/HeroBullet1.png")

    def display(self):
        Bullet.display(self)

    # 定义子弹移动的动作
    def bullet_move(self):
        self.y -= 5

    # 判断我方子弹出界
    def judge(self):
        if self.y < -25:
            return True
        else:
            return False


# 控制键盘动作函数
def control_key(hero):
    # 获取事件，比如按键等
    for event in pygame.event.get():
        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero.move_left()
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero.move_right()
            # 检测按键是否是w或者top
            elif event.key == K_w or event.key == K_UP:
                print('top')
                hero.move_up()
            # 检测按键是否是s或者down
            elif event.key == K_s or event.key == K_DOWN:
                print('bottom')
                hero.move_down()
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero.fire()



def main():
    # 1. 创建窗口  set_mode(元组，flags,depth)   元组 窗口的大小
    screen = pygame.display.set_mode((240, 400), 0, 32)
    # 2. 创建背景
    background = pygame.image.load("./feiji/background.png")
    # 添加一个我方飞机对象
    hero = HeroPlane(screen)
    # 创建一个敌人飞机对象
    enemy = EnemyPlane(screen)

    while True:
        # 3. 将背景添加到窗口
        screen.blit(background, (0, 0))
        # 将飞机对象显示在窗口中
        hero.display()
        # 显示敌方的飞机
        enemy.display()
        enemy.fire()
        # 敌方飞机开始移动
        enemy.move()
        # 4. 更新显示内容
        pygame.display.update()
        # 通过键盘控制飞机
        control_key(hero)
        # 休息一会儿
        time.sleep(0.02)


if __name__ == "__main__":
    main()