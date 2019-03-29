# 课程2 目标
    # 1.了解Python之if语句
    #   计算机之所以可以做很多事情，是因为自己做条件判断。
    #   比如，输入用户年龄，根据年龄打印不同的内容，在Python程序中，用if语句实现
    #    age = 20
    #    if age >= 18:
    #        print('your age is', age)
    #        print('adult')
    #
    #   根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。
    #   注意: Python代码的缩进规则。
    #   具有相同缩进的代码被视为代码块，上面的3，4行 print 语句就构成一个代码块
    #   （但不包括第5行的print）。如果 if 语句判断为 True，就会执行这个代码块。
    #   缩进请严格按照Python的习惯写法：4个空格，不要使用Tab，更不要混合Tab和空格，
    #   否则很容易造成因为缩进引起的语法错误。
    #   注意: if 语句后接表达式，然后用:表示代码块开始。
    #   如果你在Python交互环境下敲代码，还要特别留意缩进，并且退出缩进需要多敲一行回车

    # 2.了解Python之if-else
    #   也可以给if添加一个else语句，意思是，如果if判断是False，不要执行if的内容，去把else执行了：
    #    age = 3
    #    if age >= 18:
    #        print('your age is', age)
    #        print('adult')
    #    else:
    #        print('your age is', age)
    #        print('teenager')
    #   冒号不要忘记
    #
    # 3.了解Python之if-elif-else
    #   我们还可以用elif做更细致的判断
    #   age = 3
    #   if age >= 18:
    #       print('adult')
    #   elif age >= 6:
    #       print('teenager')
    #   else:
    #       print('kid')
    #
    # elif是else if的缩写，完全可以有多个elif，所以if语句的完整形式就是：
    # if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else，
    # if判断条件还可以简写，比如写：
    #    if x:
    #       print('True')
    #   只要x是非零数值（not 0）、非空字符串（not ''）、非空list(not [])等，就判断为True，否则为False。
    #
    #  Demo 结合我们之前学的input
    #  birth = input('birth: ')
    #   if birth < 2000:
    #       print('before 2000')
    #   else:
    #       print('after 2000')

    # 4.了解Python之for循环
    #   要计算1+2+3，我们可以直接写表达式：
    #    >>> 1 + 2 + 3
    #    6   #输出
    #   但是，要计算1+2+3+...+10000呢，我们的界面可能写不完
    #   所以Python提供了两种循环，一种是for...in循环，依次把list或tuple中的每个元素迭代出
    #
    #   names = ['Michael', 'Bob', 'Tracy']
    #   for name in names:
    #       print(name)
    #   依次打印names的每一个元素
    #
    #   sum = 0
    #   for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    #       sum = sum + x
    #   print(sum)
    #   计算1-10的整数之和，可以用一个sum变量做累加
    #
    #   那刚才我们的10000呢，不还是要写10000个数么？
    #   所以 Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。
    #   比如range(5)生成的序列是从0开始小于5的整数
    #   list(range(5))
    #   [0, 1, 2, 3, 4, ...]
    #   list(range(1000))
    #   [0, 1, 2, 3, 4, ...]

    # 5.了解Python从while循环
    #   另一种是while循环，只要条件满足，就不断循环，条件不满足时退出循环。
    #   sum = 0  # 保存累加结果
    #   n = 1
    #   while n <= 10:
    #       sum = sum + n
    #       n = n + 1
    #   print(sum)

    # 6.了解Python之break退出循环
    #   如果要提前结束循环，可以用break语句
    #   sum = 0  # 保存累加结果
    #   n = 1
    #   while n <= 10:
    #       if n==5:
    #           break
    #       sum = sum + n
    #       n = n + 1
    #   print(sum)

    # 7.了解Python之continue继续循环
    #   在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。
    #   sum = 0  # 保存累加结果
    #   n = 1
    #   while n <= 10:
    #       if n==5:
    #           continue
    #       sum = sum + n
    #       n = n + 1
    #   print(sum)



#homework
    #  Number-guessing Game  写一个猜数字游戏
    #  规则，在[1,6]之间选一个数字，然后让玩家输入数字，猜是否是这个数字，如果是提示猜中啦
    #   如果不是，提示是猜大了，还是猜小了，最多允许猜3次的机会，3次都没有猜中，提示下次加油

import random

secret = random.randint(1,6)
guess = 0
tries = 0

print("It is a number from 1 to 6. I'll give you 3 tries.")
while guess!= secret and tries < 3:
    guess = int(input("What's your guess?"))
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")

    tries = tries + 1

if guess == secret:
    print("You got it")
else:
    print("Better lucky next time, the number is", secret)