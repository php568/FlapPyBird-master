# coding=utf-8

from turtle import *
from datetime import *

# 抬起画笔，向前运动一段距离放下
def Skip(step):
    penup()
    forward(step)
    pendown()

def mkHand(name, length):
    # 注册Turtle形状，建立表针Turtle
    reset()
    Skip(-length * 0.1)
    # 开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
    begin_poly()
    forward(length * 1.1)
    # 停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
    end_poly()
    # 返回最后记录的多边形。
    handForm = get_poly()
    register_shape(name, handForm)

def Init():
    global secHand, minHand, hurHand, printer
    # 重置Turtle指向北
    mode("logo")
    # 建立三个表针Turtle并初始化
    mkHand("secHand", 135)
    mkHand("minHand", 125)
    mkHand("hurHand", 90)
    secHand = Turtle()
    secHand.shape("secHand")
    minHand = Turtle()
    minHand.shape("minHand")
    hurHand = Turtle()
    hurHand.shape("hurHand")

    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)

    # 建立输出文字Turtle
    printer = Turtle()
    # 隐藏画笔的turtle形状
    printer.hideturtle()
    printer.penup()

def SetupClock(radius):
    # 建立表的外框
    reset()
    pensize(7)
    for i in range(60):
        Skip(radius)
        if i % 5 == 0:
            forward(20)
            Skip(-radius - 20)

            Skip(radius + 20)
            if i == 0:
                write(int(12), align="center", font=("Courier", 14, "bold"))
            elif i == 30:
                Skip(25)
                write(int(i/5), align="center", font=("Courier", 14, "bold"))
                Skip(-25)
            elif (i == 25 or i == 35):
                Skip(20)
                write(int(i/5), align="center", font=("Courier", 14, "bold"))
                Skip(-20)
            else:
                write(int(i/5), align="center", font=("Courier", 14, "bold"))
            Skip(-radius - 20)
        else:
            dot(5)
            Skip(-radius)
        right(6)

def Week(t):
    #week = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
    week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return week[t.weekday()]

def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s %d%d" % (y, m, d)

def Tick():
    # 绘制表针的动态显示
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0
    secHand.setheading(6 * second)
    minHand.setheading(6 * minute)
    hurHand.setheading(30 * hour)

    tracer(False)
    printer.forward(65)
    printer.write(Week(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.back(130)
    printer.write(Date(t), align="center",
                  font=("Courier", 14, "bold"))
    printer.home()
    tracer(True)

    # 100ms后继续调用tick
    ontimer(Tick, 100)

def main():
    # 打开/关闭龟动画，并为更新图纸设置延迟。
    tracer(False)
    Init()
    SetupClock(160)
    tracer(True)
    Tick()
    mainloop()

if __name__ == "__main__":
    main()
