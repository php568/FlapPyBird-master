# 课程2 目标
    # 1.了解Python创建list
    #   Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
    #   numbers = [1, 2, 3]
    #   classmates = ['Michael', 'Bob', 'Tracy']
    #   len(classmates)
    #   type(classmates)
    #   type(classmates[1])

    # 2.了解Python按照索引访问list
    #   classmates[0]
    #   classmates[1]
    #   classmates[2]
    #   当索引超出了范围时，Python会报一个IndexError错误，所以，要确保索引不要越界，记得最后一个元素的索引是len(classmates) - 1
    #   classmates[3]

    # 3.了解Python之倒序访问list
    #   如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
    #   classmates[-1]
    #   classmates[-2]
    #   classmates[-3]
    #   classmates[-4]

    # 4.了解Python之添加新元素
    #   list是一个可变的有序表
    #   classmates.append('Adam')
    #   也可以把元素插入到指定的位置，比如索引号为1的位置：
    #   classmates.insert(1, 'Jack')
    #   classmates.insert(1, ['Jack1','Jack2'])
    #   classmates.insert(-1, ['Jack1','Jack2'])

    # 5.了解Python从list删除元素
    #   要删除list末尾的元素，用pop()方法
    #   classmates.pop()
    #   要删除指定位置的元素，用pop(i)方法，其中i是索引位置
    #   classmates.pop(1)

    # 6.了解Python中替换元素
    #   要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
    #   classmates[1] = 'Sarah'
    #   classmates[2] = 'Doge'
    #   classmates[4] = 'Small Doge' #如果写4

    # 7.list里面的元素的数据类型也可以不同
    #   L = ['Apple', 123, True]
    #   list元素也可以是另一个list
    #   s = ['python', 'java', ['asp', 'php'], 'scheme']
    #   等价
    #   p = ['asp', 'php']
    #   s = ['python', 'java', p, 'scheme']
    #   如果取php这个值呢
    #   p[1]
    #   s[2][1]
    #   来看下，这个s变量里面的元素个数是多少
    #   len(s)
    #   L = []  # 空list
    #   len(L)  # 看下长度

    # 7.了解Python之创建tuple
    #   另一种有序列表叫元组，和list非常相似
    #   classmates = ('Michael', 'Bob', 'Tracy')
    #   一旦初始化后，就不能修改，没有了append() insert()
    #   而且也没法使用 classmates[2] = 'Doge' 这种赋值成另外的元素
    #
    # 8.了解Python之创建单元素tuple
    #   t = (1)    # 输出t看看是什么结果
    #   定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
    #   t = (1, )  # 输出t看看是什么结果
    #    Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。

    # 9.了解Python之“可变”的tuple
    #   t = ('a', 'b', ['A', 'B'])
    #   t[2][0] = 'X'
    #   t[2][1] = 'Y'
    #   t   #输出t
    #   结果看到的是什么？
    #   表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！




#homework
    # -*- coding: utf-8 -*-
    # L = [
    #     ['Apple', 'Google', 'Microsoft'],
    #     ['Java', 'Python', 'Ruby', 'PHP'],
    #     ['Adam', 'Bart', 'Lisa']
    # ]

    # 打印Apple:
    # print(?)
    # 打印Python:
    # print(?)
    # 打印Lisa:
    # print(?)

    # 把 Doge 追加到L[3][2]的位置

    # 将 L[2][2]的值 修改为 Doge