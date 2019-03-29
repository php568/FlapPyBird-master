# 课程3 目标
    # 1.认识编程模型
    # 2.熟悉两种编程模型：函数式，面向对象
    #   函数式编程
    #       把运算过程尽量写成一系列嵌套的函数调用
    #       函数就是面向过程的程序设计的基本单元
    #       功能地位和数据变量一样重要
    #       参数不变，一次执行 == 多次执行
    #       Python 中的函数式
    #           def: 自定义函数
    #               def hi(name=''):
    #                   print 'Hello, {}'.format(name)
    #                   return None
    #               hi()
    #               hi('everyone')
    #           lambda: 匿名函数(使用lambda这种语法构造函数)
    #               func = lambda x:x**2
    #               func(20)
    #               a_list = range(10)
    #               map(func, a_list)
    #               map(lambda x:x**2, a_list)