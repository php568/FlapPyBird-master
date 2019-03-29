from itertools import cycle
import random
import sys

# 将pygame库导入到python程序中
import pygame
# 需要引入pygame中的所有常量。
from pygame.locals import *

# 每秒传输帧数(Frames Per Second)
FPS = 30
SCREENWIDTH  = 288   #屏幕宽度
SCREENHEIGHT = 512   #屏幕高度
# amount by which base can maximum shift to left
# 管道上下之间的间隙
PIPEGAPSIZE  = 200 # gap between upper and lower part of pipe
# base那个条条所在的高度 注意以左上角为坐标起始点  所以这个高度是往下为正
BASEY        = SCREENHEIGHT * 0.79
# image, sound and hitmask  dicts
# 图像，声音，撞击的文件
IMAGES, SOUNDS, HITMASKS = {}, {}, {}

# list of all possible players (tuple of 3 positions of flap)
# 三种小鸟造型
PLAYERS_LIST = (
    # red bird
    (
        'assets/sprites/redbird-upflap.png',
        'assets/sprites/redbird-midflap.png',
        'assets/sprites/redbird-downflap.png',
    ),
    # blue bird
    (
        # amount by which base can maximum shift to left
        'assets/sprites/bluebird-upflap.png',
        'assets/sprites/bluebird-midflap.png',
        'assets/sprites/bluebird-downflap.png',
    ),
    # yellow bird
    (
        'assets/sprites/yellowbird-upflap.png',
        'assets/sprites/yellowbird-midflap.png',
        'assets/sprites/yellowbird-downflap.png',
    ),
)

# list of backgrounds
BACKGROUNDS_LIST = (
    'assets/sprites/background-day.png',
    'assets/sprites/background-night.png',
)

# list of pipes
PIPES_LIST = (
    'assets/sprites/pipe-green.png',
    'assets/sprites/pipe-red.png',
)


try:
    xrange
except NameError:
    xrange = range


def main():
    global SCREEN, FPSCLOCK
    # 经过初始化以后我们就可以尽情地使用pygame了。
    pygame.init()


    # 使用Pygame时钟之前，必须先创建Clock对象的一个实例，
    # 控制每个循环多长时间运行一次。这就像一个定时器在控制时间进程，指出“现在开始下一个循环”！现在开始下一个循环！……
    FPSCLOCK = pygame.time.Clock()

    # 通常来说我们需要先创建一个窗口，方便我们与程序的交互。
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

    # 设置窗口标题
    pygame.display.set_caption('Flappy Bird')

    # numbers sprites for score display
    # 加载并转换图像
    # 在pygame中可以使用pygame.image.load（）函数来加载位图 （支持jpg,png,gif,bmp,pcx,tif,tga等多种图片格式）。
    # convert_alpha()方法会使用透明的方法绘制前景对象。
    # 因此在加载一个有alpha通道的素材时（比如PNG TGA），需要使用convert_alpha()方法，当然普通的图片也是可以使用这个方法的，用了也不会有什么副作用。
    IMAGES['numbers'] = (
        pygame.image.load('assets/sprites/0.png').convert_alpha(),
        pygame.image.load('assets/sprites/1.png').convert_alpha(),
        pygame.image.load('assets/sprites/2.png').convert_alpha(),
        pygame.image.load('assets/sprites/3.png').convert_alpha(),
        pygame.image.load('assets/sprites/4.png').convert_alpha(),
        pygame.image.load('assets/sprites/5.png').convert_alpha(),
        pygame.image.load('assets/sprites/6.png').convert_alpha(),
        pygame.image.load('assets/sprites/7.png').convert_alpha(),
        pygame.image.load('assets/sprites/8.png').convert_alpha(),
        pygame.image.load('assets/sprites/9.png').convert_alpha()
    )

    # game over sprite
    # 游戏结束显示的图像
    IMAGES['gameover'] = pygame.image.load('assets/sprites/gameover.png').convert_alpha()

    # message sprite for welcome screen
    # 欢迎界面显示的图像
    IMAGES['message'] = pygame.image.load('assets/sprites/message.png').convert_alpha()

    # base (ground) sprite
    # 始终显示的base图像
    IMAGES['base'] = pygame.image.load('assets/sprites/base.png').convert_alpha()

    # sounds
    # WAV版 OGG版是指游戏的音频格式
    # WAV版是属于游戏原版
    # OGG是大大们通过转换器把音频格式的WAV改成OGG，这样游戏的配置提高要求使游戏本身的体积而缩小节省了空间。
    # 可以看一下同一个音频 ogg版的是比wav版的文件小很多
    # if 'win' in sys.platform:
        # soundExt = '.wav'
    # else:
        # soundExt = '.ogg'

    # 音效:pygame.mixer
    # sound = pygame.mixer.Sound('/home/liumin/love.wav')使用指定文件名载入一个音频文件，并创建一个Sound对象。 音频文件可以是wav,ogg等格式。
    # 音频文件的内容会被全部载入到内存中。
    # SOUNDS['die']    = pygame.mixer.Sound('assets/audio/die' + soundExt)
    # SOUNDS['hit']    = pygame.mixer.Sound('assets/audio/hit' + soundExt)
    # SOUNDS['point']  = pygame.mixer.Sound('assets/audio/point' + soundExt)
    # SOUNDS['swoosh'] = pygame.mixer.Sound('assets/audio/swoosh' + soundExt)
    # SOUNDS['wing']   = pygame.mixer.Sound('assets/audio/wing' + soundExt)

    while True:
        # select random background sprites
        # 加载随机背景  （白天或者黑夜）
        # 随机选择0或者1
        randBg = random.randint(0, len(BACKGROUNDS_LIST) - 1)
        # 加载随机背景
        IMAGES['background'] = pygame.image.load(BACKGROUNDS_LIST[randBg]).convert()

        # select random player sprites
        # 加载随机角色 （红色、蓝色、黄色小鸟）
        randPlayer = random.randint(0, len(PLAYERS_LIST) - 1)
        IMAGES['player'] = (
            pygame.image.load(PLAYERS_LIST[randPlayer][0]).convert_alpha(),
            pygame.image.load(PLAYERS_LIST[randPlayer][1]).convert_alpha(),
            pygame.image.load(PLAYERS_LIST[randPlayer][2]).convert_alpha(),
        )

        # select random pipe sprites
        # 加载随机管道样式
        pipeindex = random.randint(0, len(PIPES_LIST) - 1)
        # 一个上面的管道 一个下面的管道
        IMAGES['pipe'] = (
            # 旋转180度
            pygame.transform.rotate( pygame.image.load(PIPES_LIST[pipeindex]).convert_alpha(), 180 ),
            pygame.image.load(PIPES_LIST[pipeindex]).convert_alpha(),
        )

        # hismask for pipes
        # 得到管道的边界mask
        HITMASKS['pipe'] = (
            getHitmask(IMAGES['pipe'][0]),
            getHitmask(IMAGES['pipe'][1]),
        )

        # hitmask for player
        # 得到player的边界mask
        HITMASKS['player'] = (
            getHitmask(IMAGES['player'][0]),
            getHitmask(IMAGES['player'][1]),
            getHitmask(IMAGES['player'][2]),
        )
        # 返回'playery'（player所在位置）,'basex'（base图像所在位置）'playerIndexGen'（飞行姿势index）
        movementInfo = showWelcomeAnimation()
        crashInfo = mainGame(movementInfo)
        showGameOverScreen(crashInfo)


def showWelcomeAnimation():
    """Shows welcome screen animation of flappy bird"""
    # index of player to blit on screen
    playerIndex = 0
    playerIndexGen = cycle([0, 1, 2, 1])
    # iterator used to change playerIndex after every 5th iteration
    loopIter = 0
    # player所在位置
    playerx = int(SCREENWIDTH * 0.2)
    playery = int((SCREENHEIGHT - IMAGES['player'][0].get_height()) / 2)
    # 欢迎图像所在位置
    messagex = int((SCREENWIDTH - IMAGES['message'].get_width()) / 2)
    messagey = int(SCREENHEIGHT * 0.12)

    basex = 0
    # amount by which base can maximum shift to left
    # 可以最大限度地向左移动的距离
    baseShift = IMAGES['base'].get_width() - IMAGES['background'].get_width()

    # player shm for up-down motion on welcome screen
    # 角色在欢迎屏幕上进行上下移动
    playerShmVals = {'val': 0, 'dir': 1}

    while True:
        # 使用pygame.event.get()来处理所有的事件,
        for event in pygame.event.get():
            # 如果 quit 或者 按键之后又按下esc，就结束游戏
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            # 如果按键之后点击或者按下
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                # make first flap sound and return values for mainGame
                # 播放飞的特效声音
                # SOUNDS['wing'].play()
                return {
                    'playery': playery + playerShmVals['val'],
                    'basex': basex,
                    'playerIndexGen': playerIndexGen,
                }

        # adjust playery, playerIndex, basex
        # 获得匹配元素集合中每个元素紧邻的同胞元素 调整飞行姿势图片
        if (loopIter + 1) % 5 == 0:
            playerIndex = next(playerIndexGen)
        loopIter = (loopIter + 1) % 30
        basex = -((-basex + 4) % baseShift)
        playerShm(playerShmVals)

        # draw sprites
        # screen.blit(space, (0,0))可以绘制位图 第一个参数是加载完成的位图，第二个参数是绘制的起始坐标。
        SCREEN.blit(IMAGES['background'], (0,0))
        SCREEN.blit(IMAGES['player'][playerIndex],
                    (playerx, playery + playerShmVals['val']))
        SCREEN.blit(IMAGES['message'], (messagex, messagey))
        SCREEN.blit(IMAGES['base'], (basex, BASEY))
        # 更新整个窗口
        pygame.display.update()
        # 循环应该多长时间运行一次
        FPSCLOCK.tick(FPS)


def mainGame(movementInfo):
    # 初始得分以及初始player的姿态以及迭代次数都为0
    score = playerIndex = loopIter = 0
    # 得到飞行姿势
    playerIndexGen = movementInfo['playerIndexGen']
    # player所在位置
    playerx, playery = int(SCREENWIDTH * 0.2), movementInfo['playery']

    # base图像所在位置
    basex = movementInfo['basex']
    baseShift = IMAGES['base'].get_width() - IMAGES['background'].get_width()

    # get 2 new pipes to add to upperPipes lowerPipes list
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # list of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1[0]['y']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[0]['y']},
    ]

    # list of lowerpipe
    lowerPipes = [
        {'x': SCREENWIDTH + 200, 'y': newPipe1[1]['y']},
        {'x': SCREENWIDTH + 200 + (SCREENWIDTH / 2), 'y': newPipe2[1]['y']},
    ]

    pipeVelX = -4

    # player velocity, max velocity, downward accleration, accleration on flap
    # 角色速度，最大速度，向下加速度，襟翼加速度
    playerVelY    =  -9   # player's velocity along Y, default same as playerFlapped
    playerMaxVelY =  10   # max vel along Y, max descend speed
    playerMinVelY =  -8   # min vel along Y, max ascend speed
    playerAccY    =   1   # players downward accleration
    playerRot     =  45   # player's rotation
    playerVelRot  =   3   # angular speed
    playerRotThr  =  20   # rotation threshold
    playerFlapAcc =  -9   # players speed on flapping
    playerFlapped = False # True when player flaps


    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            #如果点击
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > -2 * IMAGES['player'][0].get_height():
                    playerVelY = playerFlapAcc #上升
                    playerFlapped = True
                    # SOUNDS['wing'].play()

        # check for crash here
        crashTest = checkCrash({'x': playerx, 'y': playery, 'index': playerIndex},
                               upperPipes, lowerPipes)
        # 如果掉在地上或者撞击到了管道，就返回结束游戏
        if crashTest[0]:
            return {
                'y': playery,
                'groundCrash': crashTest[1],
                'basex': basex,
                'upperPipes': upperPipes,
                'lowerPipes': lowerPipes,
                'score': score,
                'playerVelY': playerVelY,
                'playerRot': playerRot
            }

        # check for score
        playerMidPos = playerx + IMAGES['player'][0].get_width() / 2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + IMAGES['pipe'][0].get_width() / 2
            # 当角色达到管道缝隙的中间+4时，score+1，并且在此时播放得分音效
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 1
                # SOUNDS['point'].play()

        # playerIndex basex change
        if (loopIter + 1) % 3 == 0:
            playerIndex = next(playerIndexGen)
        loopIter = (loopIter + 1) % 30
        basex = -((-basex + 100) % baseShift)

        # rotate the player
        if playerRot > -90:
            playerRot -= playerVelRot

        # player's movement
        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY
        if playerFlapped:
            playerFlapped = False

            # more rotation to cover the threshold (calculated in visible rotation)
            playerRot = 45

        playerHeight = IMAGES['player'][playerIndex].get_height()
        playery += min(playerVelY, BASEY - playery - playerHeight)

        # move pipes to left
        # 管道移动
        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            uPipe['x'] += pipeVelX
            lPipe['x'] += pipeVelX

        # add new pipe when first pipe is about to touch left of screen
        # 当第一个管道移动到屏幕左侧边缘时，生成下一个管道
        if 0 < upperPipes[0]['x'] < 5:
            newPipe = getRandomPipe()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])

        # remove first pipe if its out of the screen
        # 当管道移动到屏幕外侧后，删除它
        if upperPipes[0]['x'] < -IMAGES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        # draw sprites
        SCREEN.blit(IMAGES['background'], (0,0))

        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(IMAGES['pipe'][0], (uPipe['x'], uPipe['y']))
            SCREEN.blit(IMAGES['pipe'][1], (lPipe['x'], lPipe['y']))

        SCREEN.blit(IMAGES['base'], (basex, BASEY))
        # print score so player overlaps the score
        # 显示得分
        showScore(score)

        # Player rotation has a threshold
        visibleRot = playerRotThr
        if playerRot <= playerRotThr:
            visibleRot = playerRot
        # 旋转角色
        playerSurface = pygame.transform.rotate(IMAGES['player'][playerIndex], visibleRot)
        # 显示旋转后的角色
        SCREEN.blit(playerSurface, (playerx, playery))

        # 更新窗口
        pygame.display.update()
        # 循环应该多长时间运行一次
        FPSCLOCK.tick(FPS)


def showGameOverScreen(crashInfo):
    """crashes the player down ans shows gameover image"""
    # 获取得分
    score = crashInfo['score']
    playerx = SCREENWIDTH * 0.2
    playery = crashInfo['y']
    playerHeight = IMAGES['player'][0].get_height()
    playerVelY = crashInfo['playerVelY']
    playerAccY = 2
    playerRot = crashInfo['playerRot']
    playerVelRot = 7

    basex = crashInfo['basex']

    upperPipes, lowerPipes = crashInfo['upperPipes'], crashInfo['lowerPipes']

    # play hit and die sounds
    # SOUNDS['hit'].play()
    # 如果没有撞击到地面，就播放die音效就可以了
    # if not crashInfo['groundCrash']:
        # SOUNDS['die'].play()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery + playerHeight >= BASEY - 1:
                    return

        # player y shift
        if playery + playerHeight < BASEY - 1:
            playery += min(playerVelY, BASEY - playery - playerHeight)

        # player velocity change
        if playerVelY < 15:
            playerVelY += playerAccY

        # rotate only when it's a pipe crash
        if not crashInfo['groundCrash']:
            if playerRot > -90:
                playerRot -= playerVelRot

        # draw sprites
        SCREEN.blit(IMAGES['background'], (0,0))

        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(IMAGES['pipe'][0], (uPipe['x'], uPipe['y']))
            SCREEN.blit(IMAGES['pipe'][1], (lPipe['x'], lPipe['y']))

        SCREEN.blit(IMAGES['base'], (basex, BASEY))
        showScore(score)

        playerSurface = pygame.transform.rotate(IMAGES['player'][1], playerRot)
        SCREEN.blit(playerSurface, (playerx,playery))

        FPSCLOCK.tick(FPS)
        pygame.display.update()


def playerShm(playerShm):
    """oscillates the value of playerShm['val'] between 8 and -8"""
    if abs(playerShm['val']) == 8:
        playerShm['dir'] *= -1

    if playerShm['dir'] == 1:
         playerShm['val'] += 1
    else:
        playerShm['val'] -= 1


def getRandomPipe():
    """returns a randomly generated pipe"""
    # y of gap between upper and lower pipe
    # 随机生成随机高度的管道
    gapY = random.randrange(0, int(BASEY * 0.6 - PIPEGAPSIZE))
    gapY += int(BASEY * 0.2)
    pipeHeight = IMAGES['pipe'][0].get_height()
    pipeX = SCREENWIDTH + 10

    return [
        {'x': pipeX, 'y': gapY - pipeHeight},  # upper pipe
        {'x': pipeX, 'y': gapY + PIPEGAPSIZE}, # lower pipe
    ]


def showScore(score):
    """displays score in center of screen"""
    scoreDigits = [int(x) for x in list(str(score))]
    totalWidth = 0 # total width of all numbers to be printed

    for digit in scoreDigits:
        totalWidth += IMAGES['numbers'][digit].get_width()

    Xoffset = (SCREENWIDTH - totalWidth) / 2

    # 显示得分
    for digit in scoreDigits:
        SCREEN.blit(IMAGES['numbers'][digit], (Xoffset, SCREENHEIGHT * 0.1))
        Xoffset += IMAGES['numbers'][digit].get_width()


def checkCrash(player, upperPipes, lowerPipes):
    """returns True if player collders with base or pipes."""
    # 飞行姿势
    pi = player['index']
    player['w'] = IMAGES['player'][0].get_width()
    player['h'] = IMAGES['player'][0].get_height()

    # if player crashes into ground
    # 掉在地上
    if player['y'] + player['h'] >= BASEY - 1:
        return [True, True]
    else:

        playerRect = pygame.Rect(player['x'], player['y'],
                      player['w'], player['h'])
        pipeW = IMAGES['pipe'][0].get_width()
        pipeH = IMAGES['pipe'][0].get_height()

        for uPipe, lPipe in zip(upperPipes, lowerPipes):
            # upper and lower pipe rects
            uPipeRect = pygame.Rect(uPipe['x'], uPipe['y'], pipeW, pipeH)
            lPipeRect = pygame.Rect(lPipe['x'], lPipe['y'], pipeW, pipeH)

            # player and upper/lower pipe hitmasks
            pHitMask = HITMASKS['player'][pi]
            uHitmask = HITMASKS['pipe'][0]
            lHitmask = HITMASKS['pipe'][1]

            # if bird collided with upipe or lpipe
            uCollide = pixelCollision(playerRect, uPipeRect, pHitMask, uHitmask)
            lCollide = pixelCollision(playerRect, lPipeRect, pHitMask, lHitmask)
            # 如果撞击到了上管道或者下管道 返回
            if uCollide or lCollide:
                return [True, False]

    return [False, False]

def pixelCollision(rect1, rect2, hitmask1, hitmask2):
    """Checks if two objects collide and not just their rects"""
    # 角色和管道之间重合的情况
    rect = rect1.clip(rect2)

    # 没重合就是没撞击到
    if rect.width == 0 or rect.height == 0:
        return False

    x1, y1 = rect.x - rect1.x, rect.y - rect1.y
    x2, y2 = rect.x - rect2.x, rect.y - rect2.y

    for x in xrange(rect.width):
        for y in xrange(rect.height):
            # 撞击到了
            if hitmask1[x1+x][y1+y] and hitmask2[x2+x][y2+y]:
                return True
    return False

def getHitmask(image):
    """returns a hitmask using an image's alpha."""
    # 得到撞击mask
    mask = []
    for x in xrange(image.get_width()):
        mask.append([])
        for y in xrange(image.get_height()):
            mask[x].append(bool(image.get_at((x,y))[3]))
    return mask

if __name__ == '__main__':
    main()
