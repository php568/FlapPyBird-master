import time
from turtle import *



write(position())
pensize(4)
write(position())
#forward(-150)
backward(150)
write(position())
right(25)
forward(150)
write(position())
left(25)
forward(-150)
write(position())
penup()
goto(0,0)
pendown()
goto(20,20)
home()
circle(100)  #逆时针
time.sleep(5)
dot(100)
time.sleep(5)
undo()


# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
done()