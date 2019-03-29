# 课程2 目标 goals
    #   计算机不仅可以处理各种数值，还可以处理文本、图形、音频、视频、网页等各种各样的数据
    #   不同的数据，需要定义不同的数据类型
    #   Computers can handle not only all kinds of values, but also text, graphics, audio, video, web pages and other kinds of data.
    #   Different data, need to define different data types
    # 1.了解Python的数据类型以及基本的数学运算
    #   There are several basic types of python
    #   一、整数(int、integer),  can achieve binary, decimal, and hexadecimal conversions between.
    #       二进制(binary)：0, 1
    #       十进制(decimal)：1, 100, -8080, 0 等
    #       十六进制(hexadecimal)：0x前缀和0-9，a-f表示，如：0xff00, 0xa5b4c3d2
    #   二、浮点数(float)
    #       1.23, 3.14, -9.01, 1.23e9(1.23x10^9), 1.2e-5(0.000012)
    #   三、字符串(string),
    #       'abc', "xyz"
    #   四、布尔值(boolean)
    #       True, False
    #   五、空值(empty\null)
    #       None(一个特殊的空值)
    #
    #   四大基本运算：Four basic operations , plus(+) minus(-) times(*) and divide(/)
    #   In computers, they're called operators.
    #   2 and 5 are called operands
    #   x = (2 + 5) * 3 - 4/2
    #   运算顺序，遵循数学规则的计算顺序，先()，再*，再/，最后-

    # 2.了解Python之print语句
    #   交互环境，>>> 是Python解释器的提示符, 文本编辑器不需要
    #   print()打印字符串
    #       print('The quick brown fox')
    #       print('The quick brown fox', 'jumps over', 'the lazy dog') # 遇到逗号会输出一个空格
    #       print(300)
    #       print(100 + 200)  or  print('100 + 200 =', 100 + 200)

    # 2.了解Python之input语句
    #   可以让用户输入字符串，并存放到一个变量里。
    #   name = input()
    #   name = input('please enter your name: ')

    # 3.了解Python的注释(comment)
    #   作用1.用来说明代码 方便别人能够看懂
    #   作用2.一些代码不想运行又不想删除
    #   单行注释以#开头，后面的文字直到行尾
    #   多行注释以一对''' 123123 '''
    #   多行注释以一对""" 123123 """

    # 4.了解Python中什么是变量(variable)
    #   变量的概念基本上和初中代数的方程变量是一致的
    #   变量是用一个变量名表示，变量名必须是大小写英文、数字和下划线（_）的组合，且不能用数字开头
    #   a=2  a x a = 2 x 2 = 4
    #   width = 20
    #   height = 5 * 9
    #   width * height
    #   在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
    #   a = 123 # a是整数
    #   print(a)
    #   a = 'ABC' # a变为字符串
    #   print(a)

    # 5.了解Python中定义字符串
    #   计算机最早只有127个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为ASCII编码，比如大写字母A的编码是65，小写字母z的编码是122。
    #   中国制定了GB2312编码，用来把中文编进去。
    #   全世界有上百种语言，日本把日文编到Shift_JIS里，
    #   韩国把韩文编到Euc-kr里，各国有各国的标准，就会不可避免地出现冲突，
    #   结果就是，在多语言混合的文本中，显示出来会有乱码。(想看乱码是什么样子么)
    #   字符串是以Unicode编码的
    #   print('包含中文的str')
    #   print('The quick brown fox')
    #   print("I'm OK")
    #   print('Learn "Python" in website')
    #   print(' Bob said \"I\'m OK\".')    #  \ can be used to escape quotes  注意：转义字符 \ 不计入字符串的内容中。

    # 6.了解Python中raw字符串与多行字符串...
    #   如果一个字符串包含很多需要转义的字符，对每一个字符都进行转义会很麻烦。为了避免这种情况，我们可以在字符串前面加个前缀 r ，表示这是一个 raw 字符串，里面的字符就不需要转义了

    # 7.了解Python中的Unicode字符串
    #   由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
    #   #!/usr/bin/env python3
    #   # -*- coding: utf-8 -*-
    #   第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
    #   第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。

    # 8.了解Python中的整数和浮点数
    # 9.了解Python中的布尔类型



# -*- coding: utf-8 -*-
# 昨日课程复习

print('包含中文的str')
print('The quick brown fox', 'jumps over', 'the lazy dog')
print('Learn "Python" in website')
print("Learn 'Python' in website")
print('Bob said \"I\'m OK\".')
print("Bob said \"I\'m OK\".")
# 常用的转义字符
# \n 表示换行
# \t 表示一个制表符  tab键按下去显示的字符
# \\ 表示 \ 字符本身

print('''line1
... line2
... line3''')

print('''
\(~_~)/ \(~_~)/,\n
\(~_~)/ \(~_~)/,\n
\(~_~)/ \(~_~)/,\n
''')


name = input()
name = input('please enter your name: ')
print('hello,', name)


print(True)
print(False)
print(3 > 2)
print(3 > 5)






