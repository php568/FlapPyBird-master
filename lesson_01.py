# 课程1 目标
    # 1.了解什么是编程语言
    # 2.了解什么是编程
    # 3.了解都有哪些编程语言 介绍世界上有多少编程语言
    # 4.了解python语言目前在语言排行
    # 5.了解python语言的概念和特点
    #   解释型、面向对象、动态数据类型的高级程序设计语言
    #   目前有两个主流的大版本：2.7   3.x  (3.x在语法上有升级)
    #   语言轻量化，依赖python包做开发
    #   生态库完善
    # 6.如何安装python
    #   下载 https://www.python.org/downloads  选择python3.7 for windows
    #   https://docs.python.org/3/tutorial/index.html
    #   https://docs.python.org/3/index.html
    #   https://docs.python.org/3/library/turtle.html
    # 7.如何输出一条如何 Hello World
    #    print("Hello World")
    # 8.做一个加法运算
    #   print(5+3)
    # 9.保存文件，执行python
    # 10.碰到错误怎么办

###############################

import random

secret = random.randint(1,6)
guess = 0 
tries = 0
while guess != secret and tries < 6:
    guess = int(input("What's You guess? "));
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    tries = tries + 1
if guess == secret:
    print("You got it")
else:
    print("Better lucky next time")
    print("The secret number was", secret)
    
###############################
# homework

# 编y写代码

# 1. Who created the python language?   You need Google.

# 2.Print 3 lines of string, your name, your birthday, your favorite color
# 9i8i8i8i8i8打印3行字符串，你的名字，你的生日，你最欢的颜色

# 3.How many minutes are there in a week?

# 3.打印过程中出现的都有什么错误，你是如何解决的