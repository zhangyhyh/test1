#for i in range(1, 10):
 #   print("team{0},{1},{2}" .format(i, "nihao", "gg"))

# class Hello:
#     def __init__(self, name): #构造方法
#         self._name = name
#     def sayHello(self):
#         print("Hello{0}".format(self._name))
#
# class Hi(Hello):
#     def __init__(self, name):  # 构造方法
#         Hello.__init__(self,name)
#
# h = Hello("nihao")
# h.sayHello()
# h1 = Hi("hh")
# h1.sayHello()

# -*- coding: UTF-8 -*-
#导入re库文件
import re
old_url = 'http://www.jikexueyuan.com/course/android/?pageNum=2'
total_page = 20

f = open('jikexueyuan.html','r',encoding='utf-8') #以指定的编码类型（即文件本身的编码）打开文件，
# chardet库可以判断文件编码类型
html = f.read()
f.close()

title = re.search('<title>(.*?)</title>', html, re.S) .group(0)
print(title)