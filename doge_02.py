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
SCREENWIDTH  = 5000   #屏幕宽度
SCREENHEIGHT = 5000   #屏幕高度

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
    'assets/sprites/doge.jpg',
    'assets/sprites/doge01_org.png',
    #'assets/sprites/erha01_org.png',
)


def main():
    global SCREEN, FPSCLOCK
    # 初始化pygame,为使用硬件做准备  经过初始化以后我们就可以尽情地使用pygame了。
    pygame.init()

    # 通常来说我们需要先创建一个窗口，方便我们与程序的交互。
    # set_mode会返回一个Surface对象，代表了在桌面上出现的那个窗口，三个参数第一个为元祖，代表分 辨率（必须）；第二个是一个标志位，具体意思见下表，如果不用什么特性，就指定0；第三个为色深。
    # 标志位
    # FULLSCREEN	创建一个全屏窗口
    # DOUBLEBUF	创建一个“双缓冲”窗口，建议在HWSURFACE或者OPENGL时使用
    # HWSURFACE	创建一个硬件加速的窗口，必须和FULLSCREEN同时使用
    # OPENGL	创建一个OPENGL渲染的窗口
    # RESIZABLE	创建一个可以改变大小的窗口
    # NOFRAME	创建一个没有边框的窗口
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

    # 设置窗口标题
    pygame.display.set_caption('Doge')

    # select random background sprites
    # 加载随机背景  （白天或者黑夜）
    # 随机选择0或者1
    randBg = 0
    # 加载随机背景
    # convert函数是将图像数据都转化为Surface对象，
    # 每次加载完图像以后就应该做这件事件（事实上因为 它太常用了，如果你不写pygame也会帮你做）；
    # convert_alpha相比convert，保留了Alpha 通道信息（可以简单理解为透明的部分），这样我们的光标才可以是不规则的形状。
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
        # blit是个重要函数，第一个参数为一个Surface对象，第二个为左上角位置。画完以后一定记得用update更新一下，否则画面一片漆黑。
        SCREEN.blit(IMAGES['background'], (0,0))

        # 获得鼠标位置
        x, y = pygame.mouse.get_pos()
        # 计算光标的左上角位置
        x = x - IMAGES['mouse'].get_width() / 2
        y = y - IMAGES['mouse'].get_height() / 2
        # 把光标画上去
        SCREEN.blit(IMAGES['mouse'], (x, y))
        
        # 刷新一下画面  更新整个窗口
        pygame.display.update()


if __name__ == '__main__':
    main()

    
# Pygame有很多的模块，下面是一张一览表：

# 模块名	功能
# pygame.cdrom	访问光驱
# pygame.cursors	加载光标
# pygame.display	访问显示设备
# pygame.draw	绘制形状、线和点
# pygame.event	管理事件
# pygame.font	使用字体
# pygame.image	加载和存储图片
# pygame.joystick	使用游戏手柄或者 类似的东西
# pygame.key	读取键盘按键
# pygame.mixer	声音
# pygame.mouse	鼠标
# pygame.movie	播放视频
# pygame.music	播放音频
# pygame.overlay	访问高级视频叠加
# pygame	就是我们在学的这个东西了……
# pygame.rect	管理矩形区域
# pygame.sndarray	操作声音数据
# pygame.sprite	操作移动图像
# pygame.surface	管理图像和屏幕
# pygame.surfarray	管理点阵图像数据
# pygame.time	管理时间和帧信息
# pygame.transform	缩放和移动图像