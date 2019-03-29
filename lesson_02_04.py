# 课程2 目标
    # 1.了解Python之什么是dict
    # Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
    # >>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

    # 2.了解Python之访问dict
    # >>> d['Michael']
    # 95
    #   把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
    # >>> d['Adam'] = 67
    # >>> d['Adam']
    # 67

    # 3.了解Python中dict的特点
    #   假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list：
    #   names = ['Michael', 'Bob', 'Tracy']
    #   scores = [95, 75, 85]
    #   给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从scores取出对应的成绩，list越长，耗时越长。
    #   如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢

    # 4.了解Python更新dict
    # 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
    # >>> d['Jack'] = 90
    # >>> d['Jack']
    # 90
    # >>> d['Jack'] = 88
    # >>> d['Jack']
    # 88

    # 5.了解Python之遍历dict
    # 如果key不存在，dict就会报错：
    #  >>> d['Thomas']
    # Traceback (most recent call last):
    #   File "<stdin>", line 1, in <module>
    # KeyError: 'Thomas'
    # 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
    #
    # >>> 'Thomas' in d
    # False
    #
    # 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
    #
    # >>> d.get('Thomas')
    # >>> d.get('Thomas', -1)
    # -1
    # 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
    # >>> d.pop('Bob')
    # 75
    # >>> d
    # {'Michael': 95, 'Tracy': 85}
    #
    # 和list比较，dict有以下几个特点：
    # 查找和插入的速度极快，不会随着key的增加而变慢；
    # 需要占用大量的内存，内存浪费多。
    # 而list相反：
    # 查找和插入的时间随着元素的增加而增加；
    # 占用空间小，浪费内存很少。

    # 6.了解Python中什么是set
    # set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，
    # 所以，在set中，没有重复的key。
    # 要创建一个set，需要提供一个list作为输入集合：
    # >>> s = set([1, 2, 3])
    # >>> s
    # {1, 2, 3}
    # 重复元素在set中自动被过滤：
    # >>> s = set([1, 1, 2, 2, 3, 3])
    # >>> s
    # {1, 2, 3}

    # 7.了解Python之访问set
    # 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
    # >>> s.add(4)
    # >>> s
    # {1, 2, 3, 4}
    # >>> s.add(4)
    # >>> s
    # {1, 2, 3, 4}
    #
    # 通过remove(key)方法可以删除元素：
    # >>> s.remove(4)
    # >>> s
    # {1, 2, 3}