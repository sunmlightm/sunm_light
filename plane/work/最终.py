import pygame
import time
from pygame.locals import *
import random
time_play=1

# 提取基类：
class Plan(object):
    def __init__(self,screen,x,y,image_path):
        self.screen=screen
        self.x=x
        self.y=y
        self.image=pygame.image.load(image_path)
        self.bullet_list = []
        self.bomb_image_list = []
        self.image_num = 0
        self.image_index = 0
        self.isbomb = False
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        empty_list=[]
        # 显示子弹
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                empty_list.append(bullet)
        for bullet in empty_list:
            empty_list.remove(bullet)


class Bullet(object):
    def __init__(self,screen,x,y,image_path):
        self.screen=screen
        self.image=pygame.image.load(image_path)
        self.x=x
        self.y=y


class HeroPlan(Plan):
    def __init__(self,screen):
        x=100
        y=300
        image_path="image/hero.png"
        super().__init__(screen,x,y,image_path)
        self.__get_bomb_image()
    # 加载爆炸图片
    def __get_bomb_image(self):
        for i in range(1, 7):
            im_path = "image/bossboom/Boss_Boom_0" + str(i) + ".png"
            self.bomb_image_list.append(pygame.image.load(im_path))
        self.image_length = len(self.bomb_image_list)
    # 显示飞机
    def display(self):
        for bullet in self.bullet_list:
        # 判断当前子弹是否击中飞机
            if bullet.judge_jizhong(self.enemy):
                self.enemy.isbomb=True
        # 爆炸
        if self.isbomb:
            bomb_image = self.bomb_image_list[self.image_index]
            self.screen.blit(bomb_image, (self.x, self.y))
            self.image_num += 1
            if self.image_num == (self.image_length + 1):
                self.image_num = 0
                self.image_index += 1
                if self.image_index > (self.image_length - 1):
                    self.image_index = 5
                    time.sleep(1)
                    main()  # 炸完了咋样？可以
        else:
            Plan.display(self)

    # 发射子弹
    def send_bullet(self,enemy):
        self.enemy=enemy
        # 生成子弹并放进列表
        self.bullet_list.append(HeroBullet(self.screen,self.x,self.y))


class EnemyPlane(Plan):
    def __init__(self,screen):
        x = 0
        y = 0
        image_path = "image/EnemyBoss2.png"
        super().__init__(screen, x, y, image_path)
        self.bullet_list = []
        self.flg = "right"
        self.__get_bomb_image()
        self.boom=0

    # 加载爆炸图片
    def __get_bomb_image(self):
        for i in range(1,7):
            im_path="image/bossboom/Boss_Boom_0"+str(i)+".png"
            self.bomb_image_list.append(pygame.image.load(im_path))
        self.image_length=len(self.bomb_image_list)

    # 显示飞机
    def display(self):
        # super().display()
        for bullet in self.bullet_list:
        # 判断当前子弹是否击中飞机
            if bullet.judge_jizhong(self.enemy):
                self.enemy.isbomb=True
        if self.isbomb:
            self.boom=1
            bomb_image = self.bomb_image_list[self.image_index]
            self.screen.blit(bomb_image, (self.x+50, self.y))
            self.image_num += 1
            if self.image_num == (self.image_length + 1):
                self.image_num = 0
                self.image_index += 1
                if self.image_index > (self.image_length - 1):
                    global time_play
                    time_play += 1
                    self.image_index = 5
                    time.sleep(1)
                    if time_play <= 3:
                        main()  # 炸完了咋样？可以
                    else:
                        exit()

        else:
            self.boom=0
            Plan.display(self)
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
    def send_bullet(self,enemy):
        self.enemy=enemy
        # 生成子弹并放进列表
        num=random.randint(1,200)
        if num==20 or num==150:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y,"image/Goods01.png"))
        if num==30 or num==180:
            self.bullet_list.append(EnemyBullet(self.screen,self.x-50,self.y,"image/HeroBullet2.png"))
        if num==60 or num==188:
            self.bullet_list.append(EnemyBullet(self.screen,self.x+50,self.y,"image/HeroBullet2.png"))

    def move(self):
        if self.boom==1:
            return
        if self.flg=="right":
            self.x=self.x+1
        elif self.flg=="left":
            self.x=self.x-1
        if self.x<=0:
            self.flg="right"
        elif self.x>=130:
            self.flg="left"

#子弹
class HeroBullet(Bullet):
    def __init__(self,screen,x,y):
        x=x+9
        y=y-20
        image_path="image/HeroBullet2.png"
        super().__init__(screen,x,y,image_path)

    def judge_jizhong(self, enemy):
        if self.x > enemy.x and self.x < enemy.x + 113:
            if self.y > enemy.y and self.y < enemy.y + 80:
                print("击中敌机了..")
                global boom_flog
                boom_flog=1
                return True
        else:
            return False

    # 显示子
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
class EnemyBullet(Bullet):
    def __init__(self,screen,x,y,images):
        x=x+52
        y=y+80
        super().__init__(screen,x,y,images)
    def judge_jizhong(self, enemy):
        if self.x > enemy.x and self.x < enemy.x + 27:
            if self.y > enemy.y and self.y < enemy.y + 32:
                print("被敌机击中了..")
                global boom_flog
                boom_flog=1
                return True
        else:
            return False
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

def key_control(self,enemy_plan):
    # 监听键盘代码
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit")
            exit()
        if event.type == KEYDOWN:
            # 左
            if event.key == K_LEFT or event.key == K_a:
                print("left")
                if self.x>=0:
                    self.x -= 5
            # 右
            elif event.key == K_RIGHT or event.key == K_d:
                print("right")
                if self.x<=210:
                    self.x += 5
            # 上
            elif event.key == K_UP or event.key == K_w:
                print("up")
                self.y -= 5
            # 下
            elif event.key == K_DOWN or event.key == K_s:
                print("down")
                self.y += 5
            # 空格发射子弹
            elif event.key == K_SPACE:
                print("space")
                self.send_bullet(enemy_plan)
            elif event.key == K_b:
                # 按b键了
                print("爆炸")
                enemy_plan.isbomb = True


def main():
    boom_flog = 0
    pygame.init()
    # 设置键盘重复键
    pygame.key.set_repeat(True)
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
        enemy_plan.send_bullet(plane)
        # 更新显示内容
        pygame.display.update()
        # 键盘控制飞机移动
        key_control(plane,enemy_plan)
        # cpu休息
        time.sleep(0.01)

if __name__ == "__main__":
    main()
