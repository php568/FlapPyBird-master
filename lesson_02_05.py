# 课程2 目标
    # 1.了解Python之什么是函数
    #   函数就是最基本的一种代码抽象的方式

    # 2.了解Python之调用函数
    #   Python内置了很多有用的函数，我们可以直接调用。
    #   要调用一个函数，需要知道函数的名称和参数
    #    调用函数的时候，如果传入的参数数量不对，会报TypeError的错误
    #    如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误
    #    Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数：
    #    >>> int('123')
    #    123
    #    >>> int(12.34)
    #    12
    #    >>> float('12.34')
    #    12.34
    #    >>> str(1.23)
    #    '1.23'
    #    >>> str(100)
    #    '100'
    #    >>> bool(1)
    #    True
    #    >>> bool('')
    #    False

    # 3.了解Python之编写函数
    #   定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
    #   然后，在缩进块中编写函数体，函数的返回值用return语句返回。
    #   def my_abs(x):
    #       if x >= 0:
    #           return x
    #       else:
    #           return -x

    # 4.了解Python函数之返回多值
    #   import math
    #   def move(x, y, step, angle=0):
    #       nx = x + step * math.cos(angle)
    #       ny = y - step * math.sin(angle)
    #       return nx, ny
    #    >>> x, y = move(100, 100, 60, math.pi / 6)
    #    >>> print(x, y)
    #    >>> r = move(100, 100, 60, math.pi / 6)
    #    >>> print(r)
    #(151.96152422706632, 70.0)
    #   在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

    # 5.了解Python之递归函数
    # 6.了解Python之定义默认参数
    # 7.了解Python之定义可变参数