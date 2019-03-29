from turtle import*

def eyes(x,y):
    goto(x,y)
    color("black")
    penup()
    setheading(90)
    forward(-10)
    setheading(0)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    color("white")
    penup()
    setheading(-180)
    forward(5)
    setheading(-270)
    forward(8)    
    setheading(0)
    pendown()
    begin_fill()
    circle(3)
    end_fill()
    penup()

def head(x,y):
    goto(x,y)
    pensize(2)
    color("black")
    setheading(0)
    pendown()
    forward(200)
    setheading(90)
    forward(-60)
    setheading(180)
    forward(160)
    setheading(0)
    circle(5,-90)
    penup()
    goto(200,-30)
    pendown()
    forward(20)
    setheading(180)
    forward(160)
    setheading(0)
    right(105)    
    forward(50)
    setheading(180)  
    forward(120)
    setheading(75)
    forward(180)
    setheading(0)
    right(60)
    forward(50)
    setheading(0)
    left(60)
    forward(50)
    setheading(0)
    right(90)
    forward(45)
    penup()

def nose(x,y):
    goto(x,y)
    pensize(2)   
    setheading(0)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    penup()
    

def main():
    pensize(4)
    colormode(255)      #将其设置为1.0或255.随后 颜色三元组的r，g，b值必须在0 .. cmode范围内
    #color((250,128,10),"orange")
    #setup(840,500)
    #screensize(500,500)
    speed(5)

    #眼睛
    eyes(0,0)

    #头
    head(0,30)

    #鼻子
    nose(185,30)

    hideturtle()
    
if __name__ == '__main__':
	main()
