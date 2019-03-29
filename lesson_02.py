# 课程2 目标
    # 1.了解Python的基础数据结构
    # 2.掌握python中的str、list、tuple、set、dict
    #   字符串：str
    #       a_string = "I am a string"
    #       type(a_string)
    #   列表：list、tuple、set
    #       list 一种可变的数组
    #           a_list = [1,2,3,4]
    #           type(a_list)
    #           a_list.append(5)
    #       tuple 一种不可变的数组
    #           a_tuple = (1,2,3,4)
    #           type(a_tuple)
    #           a_tuple.append(5)   #error
    #           a_tuple[0] = 2      #error
    #       set 一种可变的数组元素唯一的数组
    #           a_set = set(a_list) # or set([1,2,1,2])
    #           type(a_set)
    #   字典：dict
    #       dict 简单的 key => value 存储结构
    #           a_dict = {'1':'a', '2':'b'}
    #           a_dict.keys()
    #           a_dict.values()
    # 3.了解高级特性简单介绍
    #   生成器 generator,比如range 生成10个元素，放到内存中供使用
    #       for i in range(10): # 一次执行完成 比较消耗内存
    #           print i
    #       for i in xrange(10): # 每执行一步产生一个 适合生成大数组
    #           print i
    #   迭代器 iterator
    #   切片
    #       a_list = [1, 4, 9, 16, 25, 36, 49, 64, 81]
    #       a_list[5: 7]
    #       a_list[-2:]