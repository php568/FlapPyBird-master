from turtle import*

def nose(x,y):#鼻子
    penup()#提起笔
    goto(x,y)#定位
    pendown()#落笔，开始画
    setheading(-30)#将乌龟的方向设置为to_angle/为数字（0-东、90-北、180-西、270-南）
    begin_fill()#准备开始填充图形
    a=0.4
    for i in range(120):
        if 0<=i<30 or 60<=i<90:
            a=a+0.08
            left(3) #向左转3度
            forward(a) #向前走a的步长
        else:
            a=a-0.08
            left(3)
            forward(a)
    end_fill()#填充完成

    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    pencolor(255,155,192)#画笔颜色
    setheading(10)
    begin_fill()
    circle(5)
    color(160,82,45)#返回或设置pencolor和fillcolor
    end_fill()

    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255,155,192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160,82,45)
    end_fill()

def head(x,y):#头
    color((255,155,192),"pink")
    penup()
    goto(x,y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(180)
    circle(300,-30)
    circle(100,-60)
    circle(80,-100)
    circle(150,-20)
    circle(60,-95)
    setheading(161)
    circle(-300,15)
    penup()
    goto(-100,100)
    pendown()
    setheading(-30)
    a=0.4
    for i in range(60):
        if 0<=i<30 or 60<=i<90:
            a=a+0.08
            lt(3) #向左转3度
            fd(a) #向前走a的步长
        else:
            a=a-0.08
            lt(3)
            fd(a)
    end_fill()

def ears(x,y): #耳朵
    color((255,155,192),"pink")
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50,50)
    circle(-10,120)
    circle(-50,54)
    end_fill()

    penup()
    setheading(90)
    forward(-12)
    setheading(0)
    forward(30)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50,50)
    circle(-10,120)
    circle(-50,56)
    end_fill()

def eyes(x,y):#眼睛
    color((255,155,192),"white")
    penup()
    setheading(90)
    forward(-20)
    setheading(0)
    forward(-95)
    pendown()
    begin_fill()
    circle(15)
    end_fill()

    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()

    color((255,155,192),"white")
    penup()
    setheading(90)
    forward(-25)
    setheading(0)
    forward(40)
    pendown()
    begin_fill()
    circle(15)
    end_fill()

    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()

def cheek(x,y):#腮
    color((255,155,192))
    penup()
    goto(x,y)
    pendown()
    setheading(0)
    begin_fill()
    circle(30)
    end_fill()

def mouth(x,y): #嘴
    color(239,69,19)
    penup()
    goto(x,y)
    pendown()
    setheading(-80)
    circle(30,40)
    circle(40,80)

def body(x,y):#身体
    color("red",(255,99,71))
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    setheading(-130)
    circle(100,10)
    circle(300,30)
    setheading(0)
    forward(230)
    setheading(90)
    circle(300,30)
    circle(100,3)
    color((255,155,192),(255,100,100))
    setheading(-135)
    circle(-80,63)
    circle(-150,24)
    end_fill()

def hands(x,y):#手
    color((255,155,192))
    penup()
    goto(x,y)
    pendown()
    setheading(-160)
    circle(300,15)
    penup()
    setheading(90)
    forward(15)
    setheading(0)
    forward(0)
    pendown()
    setheading(-10)
    circle(-20,90)

    penup()
    setheading(90)
    forward(30)
    setheading(0)
    forward(237)
    pendown()
    setheading(-20)
    circle(-300,15)
    penup()
    setheading(90)
    forward(20)
    setheading(0)
    forward(0)
    pendown()
    setheading(-170)
    circle(20,90)

def foot(x,y):#脚
    pensize(10)
    color((240,128,128))
    penup()
    goto(x,y)
    pendown()
    setheading(-90)
    forward(40)
    setheading(-180)
    color("black")
    pensize(15)
    fd(20)

    pensize(10)
    color((240,128,128))
    penup()
    setheading(90)
    forward(40)
    setheading(0)
    forward(90)
    pendown()
    setheading(-90)
    forward(40)
    setheading(-180)
    color("black")
    pensize(15)
    fd(20)

def tail(x,y):#尾巴
    pensize(4)
    color((255,155,192))
    penup()
    goto(x,y)
    pendown()
    setheading(0)
    circle(70,20)
    circle(10,330)
    circle(70,30)

def test(x,y):#测试
    clear()
    pensize(4)
    color((255,155,192))
    penup()
    goto(x,y)
    pendown()
    pencolor(255, 155, 192)
    setheading(0)
    begin_fill()
    circle(70) #画一个半径70的圆
    color(160, 82, 45)
    end_fill()

    penup()
    goto(x,y+70)
    pendown()
    pencolor(255, 155, 192)
    dot(30, "blue")

    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255,155,192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160,82,45)
    end_fill()


def setting():          #参数设置
    pensize(4)
    # hideturtle()        #使乌龟无形（隐藏）
    colormode(255)      #将其设置为1.0或255.随后 颜色三元组的r，g，b值必须在0 .. cmode范围内
    color((255,155,192),"pink")
    setup(840,500)
    speed(10)

def main():
    setting()           #画布、画笔设置
    # test(50,50)

    nose(-100,100)      #鼻子
    head(-69,167)       #头
    ears(0,160)         #耳朵
    eyes(0,140)         #眼睛
    cheek(80,10)        #腮
    mouth(-20,30)       #嘴
    body(-32,-8)        #身体
    hands(-56,-45)      #手
    foot(2,-177)        #脚
    tail(148,-155)      #尾巴

    done()

if __name__ == '__main__':
	main()


# https://docs.python.org/3/library/turtle.html#introduction
# 控制画笔绘制状态方法
# pendown()         Pull the pen down – drawing when moving. 放下画笔，移到指定点后继续绘制
# penup()           Pull the pen up – no drawing when moving. 提起画笔，用于另起一个地方绘制时用，与pendown()配对使用
# pensize(width)    Set the line thickness to width or return it. 设置画笔线条的粗细为指定大小

# Turtle运动方法
# forward()         Move the turtle forward by the specified distance, in the direction the turtle is headed. 沿着当前方向前进指定距离
# backward()        Move the turtle backward by distance, opposite to the direction the turtle is headed. 沿着当前相反方向后退指定距离
# right(angle)      Turn turtle right by angle units. 向右旋转angle角度
# left(angle)       Turn turtle left by angle units. 向左旋转angle角度
# goto(x,y)         Move turtle to an absolute position. If the pen is down, draw line.  移动到绝对坐标(x,y)处
# setx()            Set the turtle’s first coordinate to x, leave second coordinate unchanged. 将当前x轴移动到指定位置
# sety()            Set the turtle’s second coordinate to y, leave first coordinate unchanged. 将当前y轴移动到指定位置
# setheading(angle) Set the orientation of the turtle to to_angle. 设置当前朝向为angle角度
# home()            Move turtle to the origin – coordinates (0,0) – and set its heading to its start-orientation (which depends on the mode,) 设置当前画笔位置为原点，朝向东
# circle()          Draw a circle with given radius.  绘制一个指定半径，角度、以及步骤的圆圈
# dot(r)            Draw a circular dot with diameter size, using color.  绘制一个指定直径和颜色的圆点
# undo()            Undo (repeatedly) the last turtle action(s). 撤销画笔最后一步动作
# speed()           Set the turtle’s speed to an integer value in the range 0..10. 设置画笔的绘制速度，参数为0-10之间

# Turtle颜色和字体绘制方法
# color()           Return or set pencolor and fillcolor. 设置画笔的颜色
# begin_fill()      To be called just before drawing a shape to be filled. 填充图形前，调用该方法
# end_fill()        Fill the shape drawn after the last call to begin_fill(). 填充图形结束
# filling()         Return fillstate (True if filling, False else). 返回填充的状态，True为填充，False为未填充
# clear()           Delete the turtle’s drawings from the screen.Do not move turtle. State and position of the turtle as well as drawings of other turtles are not affected. 清空当前窗口，但不改变当前画笔的位置
# reset()           Delete the turtle’s drawings from the screen, re-center the turtle and set variables to the default values. 清空当前窗口，并重置位置等状态为默认值
# screensize()      Resize the canvas the turtles are drawing on. 设置画布的长和宽
# hideturtle()      Make the turtle invisible.  隐藏画笔的turtle形状
# showturtle()      Make the turtle visible. 显示画笔的turtle形状
# isvisible()       Return True if the Turtle is shown, False if it’s hidden. 如果turtle可见，则返回True
# write()           Write text - the string representation of arg - at the current turtle position according to align (“left”, “center” or right”) and with the given font. 输出font字体的字符串


# 作业
#   画个等腰三角形、正方向、菱形、五边形、六边形、圆形
#
# turtle.pensize(3)
# turtle.penup()
# turtle.goto(-200, -50)
# turtle.pendown()
# turtle.begin_fill()
# turtle.color("red")
# turtle.circle(40, steps=3)
# turtle.end_fill()
#
# turtle.penup()
# turtle.goto(-100, -50)
# turtle.pendown()
# turtle.begin_fill()
# turtle.color("blue")
# turtle.circle(40, steps=4)
# turtle.end_fill()
#
# turtle.penup()
# turtle.goto(0, -50)
# turtle.pendown()
# turtle.begin_fill()
# turtle.color("green")
# turtle.circle(40, steps=5)
# turtle.end_fill()
#
# turtle.penup()
# turtle.goto(100, -50)
# turtle.pendown()
# turtle.begin_fill()
# turtle.color("yellow")
# turtle.circle(40, steps=6)
# turtle.end_fill()
#
# turtle.penup()
# turtle.goto(200, -50)
# turtle.pendown()
# turtle.begin_fill()
# turtle.color("purple")
# turtle.circle(40)
# turtle.end_fill()
#
# turtle.color("green")
# turtle.penup()
# turtle.goto(-100, 50)
# turtle.pendown()
# turtle.write(("Cool Colorful shapes"),
#              font=("Times", 18, "bold"))
# turtle.hideturtle()
