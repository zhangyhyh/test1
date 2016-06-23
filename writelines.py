#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开文件
fo = open("test.txt", "w")
print "文件名为: ", fo.name
classinfo ={}
classinfo["title"] = "class123"
classinfo["content"] = "c++"
i = 'c'
seq = ["title: ",classinfo["title"],"\n"]
seb = ["content: " , classinfo["content"],"\n"]

# i = 'c'
# seq = ["菜鸟教程 1\n", "菜鸟教程 2\n","%c"%i]
fo.writelines( seq )
fo.writelines(seb)
# 关闭文件
fo.close()
