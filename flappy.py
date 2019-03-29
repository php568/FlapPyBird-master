from itertools import cycle
import random
import sys

# 将pygame库导入到python程序中
import pygame
# 需要引入pygame中的所有常量。 导入一些常用的函数和常量
from pygame.locals import *
#向sys模块借一个exit函数用来退出程序
# from sys import exit

# 每秒传输帧数(Frames Per Second)
FPS = 30
SCREENWIDTH  = 288   #屏幕宽度
SCREENHEIGHT = 512   #屏幕高度
SCREEN_SIZE = (SCREENWIDTH, SCREENHEIGHT)

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
    'assets/sprites/redbird-downflap.png',
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
    SCREEN = pygame.display.set_mode(SCREEN_SIZE)

    # 设置窗口标题
    pygame.display.set_caption('Flappy Bird')

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

    x, y = 0, 0
    move_x, move_y = 0, 0

    font = pygame.font.SysFont("arial", 16);
    font_height = font.get_linesize()
    event_text = []

    #游戏主循环
    while True:
        event = pygame.event.wait()
        event_text.append(str(event))
        #获得时间的名称
        event_text = event_text[-SCREEN_SIZE[1]//font_height:]
        #这个切片操作保证了event_text里面只保留一个屏幕的文字
     
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            # 接收到退出事件后退出程序
            sys.exit()
    
        SCREEN.fill((255, 255, 255))
     
        y = SCREEN_SIZE[1]-font_height
        #找一个合适的起笔位置，最下面开始但是要留一行的空
        for text in reversed(event_text):
            SCREEN.blit( font.render(text, True, (0, 0, 0)), (0, y) )
            #以后会讲
            y-=font_height
            #把笔提一行
        
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


# 事件	            产生途径	                    参数
# QUIT	            用户按下关闭按钮	            none
# ATIVEEVENT	    Pygame被激活或者隐藏	        gain, state
# KEYDOWN	        键盘被按下	                    unicode, key, mod
# KEYUP	            键盘被放开	                    key, mod
# MOUSEMOTION	    鼠标移动	                    pos, rel, buttons
# MOUSEBUTTONDOWN	鼠标按下	                    pos, button
# MOUSEBUTTONUP	    鼠标放开	                    pos, button
# JOYAXISMOTION	    游戏手柄(Joystick or pad)移动	joy, axis, value
# JOYBALLMOTION	    游戏球(Joy ball)?移动	        joy, axis, value
# JOYHATMOTION	    游戏手柄(Joystick)?移动	        joy, axis, value
# JOYBUTTONDOWN	    游戏手柄按下	                joy, button
# JOYBUTTONUP	    游戏手柄放开	                joy, button
# VIDEORESIZE	    Pygame窗口缩放	                size, w, h
# VIDEOEXPOSE	    Pygame窗口部分公开(expose)?	    none
# USEREVENT	        触发了一个用户事件	            code


# KEYDOWN和KEYUP的参数描述如下：
# key – 按下或者放开的键值，是一个数字，估计地球上很少有人可以记住，所以Pygame中你可以使用K_xxx来表示，比如字母a就是K_a，还有K_SPACE和K_RETURN等。
# mod – 包含了组合键信息，如果mod & KMOD_CTRL是真的话，表示用户同时按下了Ctrl键。类似的还有KMOD_SHIFT，KMOD_ALT。
# unicode – 代表了按下键的Unicode值，这个有点不好理解，真正说清楚又太麻烦，游戏中也不太常用，说明暂时省略，什么时候需要再讲吧。