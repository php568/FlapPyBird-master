from itertools import cycle
import random
import sys

# 将pygame库导入到python程序中
import pygame
# 需要引入pygame中的所有常量。 导入一些常用的函数和常量
from pygame.locals import *
#向sys模块借一个exit函数用来退出程序
from sys import exit

# 每秒传输帧数(Frames Per Second)
FPS = 30
SCREENWIDTH  = 288   #屏幕宽度
SCREENHEIGHT = 512   #屏幕高度

# base那个条条所在的高度 注意以左上角为坐标起始点  所以这个高度是往下为正
BASEY        = SCREENHEIGHT * 0.79

# image, sound and hitmask  dicts
# 图像，撞击的文件
IMAGES = {}

# list of backgrounds
BACKGROUNDS_LIST = (
    'assets/sprites/background-day.png',
)

MOUSE_LIST = (
    #'assets/sprites/doge01_org.png',
    'assets/sprites/erha01_org.png',
)


def main():
    global SCREEN, FPSCLOCK
    # 初始化pygame,为使用硬件做准备  经过初始化以后我们就可以尽情地使用pygame了。
    pygame.init()

    # 使用Pygame时钟之前，必须先创建Clock对象的一个实例，
    #  Before you can use the Pygame clock, you must first create an instance of the clock object,
    # 控制每个循环多长时间运行一次。这就像一个定时器在控制时间进程，指出“现在开始下一个循环”！现在开始下一个循环！……
    # Controls how often each loop runs. It's like a timer controlling the time process, saying "now start the next loop"! now start the next loop!.
    FPSCLOCK = pygame.time.Clock()

    # 通常来说我们需要先创建一个窗口，方便我们与程序的交互。
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

    # 设置窗口标题
    pygame.display.set_caption('Doge')

    # select random background sprites
    # 加载随机背景  （白天或者黑夜）
    # 随机选择0或者1
    randBg = 0
    # 加载随机背景
    IMAGES['background'] = pygame.image.load(BACKGROUNDS_LIST[randBg]).convert()
    
    randMs = 0
    IMAGES['mouse'] = pygame.image.load(MOUSE_LIST[randMs]).convert_alpha()

    #游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                # 接收到退出事件后退出程序
                exit()
    
        # 将背景图画上去
        # screen.blit(space, (0,0))可以绘制位图 第一个参数是加载完成的位图，第二个参数是绘制的起始坐标。
        SCREEN.blit(IMAGES['background'], (0,0))

        # 获得鼠标位置
        x, y = pygame.mouse.get_pos()
        # 计算光标的左上角位置
        x-= IMAGES['mouse'].get_width() / 2
        y-= IMAGES['mouse'].get_height() / 2
        # 把光标画上去
        SCREEN.blit(IMAGES['mouse'], (x, y))
        
        # 刷新一下画面  更新整个窗口
        pygame.display.update()


if __name__ == '__main__':
    main()
