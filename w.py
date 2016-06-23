# -*-coding:utf-8 -*-
import requests
import re
import sys
reload(sys)

class spider(object):
    def getinfo(self):
        info = {} #定义一个字典
        info["title"] = "class1"
        info["content"] = "C++"
        return info
    def saveinfo(self,classinfo):
        f = open('w.txt', 'w')
        for each in classinfo:
            seq1 = ["title: ",each["title"],"\n"]
            seq2 = ["content: ", each["content"],"\n"]
            f.writelines(seq1)
            f.writelines(seq2)
        f.close()
jikespider = spider()
classinfo = []
in1 = jikespider.getinfo()
classinfo.append(in1)
jikespider.saveinfo(classinfo)