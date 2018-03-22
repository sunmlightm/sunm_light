# 导入ｐｙｇａｍｅ和ｔｉｍｅ模块
import pygame
import time
from pygame.locals import *

# 飞机
class HeroPlan(object):
    # 设置飞机初始化信息
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("./image/hero.png")
        self.x = 110
        self.y = 300
        # 子弹列表
        self.bullet_list=[]

    # 显示飞机
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            # 显示子弹
            bullet.display()
            # 子弹移动
            bullet.move()

    # 生成子弹
    def send_bullet(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))

    # 左移动
    def move_left(self):
        self.x -= 5

    # 右移动　
    def move_right(self):
        self.x += 5

    # 向上移动
    def move_up(self):
        self.y -= 5

    # 向下移动
    def move_down(self):
        self.y += 5

# 子弹类
class Bullet(object):
    def __init__(self,screen,x,y):
        self.screen = screen
        self.image = pygame.image.load("./image/HeroBullet1.png")
        self.x = x+9
        self.y = y-15

    # 显示子弹
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    def move(self):
        self.y -= 5

# 敌机
class EnemyPlane(object):
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load("./image/enemy3.png")
        self.x = 10
        self.y = 10
        self.direction = "right"
    # 显示敌机
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

    # 敌机移动
    def move(self):
        if self.direction == "right":
            self.x += 2
        elif self.direction == "left":
            self.x -= 2
        #　判断是否超出范围
        if self.x > 175:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"


# 键盘控制模块
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

# 主函数
def main():
    # 创建一个窗口
    screen = pygame.display.set_mode((240,400),0,32)
    # 创建一个窗口大小的图片做背景填充
    background = pygame.image.load("./image/BackScr1.png")
    # 加载英雄飞机图片
    hero = HeroPlan(screen)
    # 飞机坐标
    enemy = EnemyPlane(screen)


    while True:
        # y -= 1
        # 调用键盘控制
        key_control(hero)
        # 背景图贴到窗口上
        screen.blit(background,(0,0))
        # ｈｅｒｏ飞机贴到窗口上
        # screen.blit(hero,(x,y))
        hero.display()
        # 显示敌机
        enemy.display()
        enemy.move()
        # 更新窗口重新绘制
        pygame.display.update()
        # ｃｐｕ休息０．０１ｓ
        time.sleep(0.01)


if __name__ == "__main__":
    main()
