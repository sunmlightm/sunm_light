import pygame
import time
from pygame.locals import *
import random

class HeroPlan(object):
    def __init__(self,screen):
        self.screen=screen
        self.x=100
        self.y=300
        self.image=pygame.image.load("image/hero.png")
        self.bullet_list = []
    # 显示飞机
    def display(self):
        empty_list=[]
        # screen.blit(plane, (x, y))
        self.screen.blit(self.image,(self.x,self.y))
        # 显示子弹
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                empty_list.append(bullet)
        for bullet in empty_list:
            empty_list.remove(bullet)
    # 发射子弹
    def send_bullet(self):
        # 生成子弹并放进列表
        self.bullet_list.append(HeroBullet(self.screen,self.x,self.y))

class EnemyPlane(object):
    def __init__(self,screen):
        self.screen=screen
        self.x=0
        self.y=0
        self.image=pygame.image.load("image/EnemyBoss2.png")
        self.bullet_list = []
        self.flg="right"
    # 显示飞机
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        empty_list=[]
        # 显示子弹
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                # 移除列表中的当前这个子弹
                empty_list.append(bullet)
        # 根据空列表中存的元素，删除bullet_list
        for b in empty_list:
            self.bullet_list.remove(b)
    # 发射子弹
    def send_bullet(self):
        # 生成子弹并放进列表
        num=random.randint(1,200)
        if num==20 or num==150:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y,"image/Goods01.png"))
        if num==30 or num==180:
            self.bullet_list.append(EnemyBullet(self.screen,self.x-50,self.y,"image/HeroBullet2.png"))
        if num==60 or num==188:
            self.bullet_list.append(EnemyBullet(self.screen,self.x+50,self.y,"image/HeroBullet2.png"))

    def move(self):
        if self.flg=="right":
            self.x=self.x+1
        elif self.flg=="left":
            self.x=self.x-1
        if self.x<=0:
            self.flg="right"
        elif self.x>=130:
            self.flg="left"

#子弹
class HeroBullet(object):
    def __init__(self,screen,x,y):
        self.screen=screen
        self.image=pygame.image.load("image/HeroBullet2.png")
        self.x=x+9
        self.y=y-20
    # 显示子弹
    def display(self):
        # 显示子弹
        self.screen.blit(self.image, (self.x, self.y))
    # 子弹移动
    def move(self):
        self.y = self.y-5
    # 判断是否越界
    def judge(self):
        if self.y<-25:
            return True
        else:
            return False

# 敌机子弹
class EnemyBullet(object):
    def __init__(self,screen,x,y,images):
        self.screen=screen
        self.image=pygame.image.load(images)
        self.x=x+52
        self.y=y+80
    # 显示子弹
    def display(self):
        # 显示子弹
        self.screen.blit(self.image, (self.x, self.y))
    # 子弹移动
    def move(self):
        self.y = self.y+5

    # 判断子弹是否出边界
    def judge(self):
        if self.y >= 400:
            return True
        else:
            return False

def key_control(hero):
    # 监听键盘代码
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit")
            exit()
        if event.type == KEYDOWN:
            # 左
            if event.key == K_LEFT or event.key == K_a:
                print("left")
                hero.x -= 5
            # 右
            elif event.key == K_RIGHT or event.key == K_d:
                print("right")
                hero.x += 5
            # 上
            elif event.key == K_UP or event.key == K_w:
                print("up")
                hero.y -= 5
            # 下
            elif event.key == K_DOWN or event.key == K_s:
                print("down")
                hero.y += 5
            # 空格
            elif event.key == K_SPACE:
                print("space")
                hero.send_bullet()

def main():
    # 创建窗口  set_mode(元组，flags,depth)   元组 窗口的大小
    screen = pygame.display.set_mode((240, 400), 0, 32)
    # 创建背景
    background = pygame.image.load("image/BackScr3.png")
    # 添加一个我方飞机
    plane=HeroPlan(screen)
    enemy_plan=EnemyPlane(screen)

    while True:
        # 将背景添加到窗口
        screen.blit(background, (0, 0))
        # 将飞机添加到窗口中
        plane.display()
        enemy_plan.display()
        enemy_plan.move()
        enemy_plan.send_bullet()
        # 更新显示内容
        pygame.display.update()
        # 键盘控制飞机移动
        key_control(plane)
        # cpu休息
        time.sleep(0.01)

if __name__ == "__main__":
    main()
