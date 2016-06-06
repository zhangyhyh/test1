# -*- coding: UTF-8 -*-

# import main
# b = main.Hello()
# b.sayHello()
#
# from  main import Hello
# c = Hello()
# c.sayHello()


import re
a = 'adfhxxhaoxx123xxdexxjfojf'
b = re.findall('xx(.*?)xx', a)
print (b[0])