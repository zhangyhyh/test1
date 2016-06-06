# -*- coding: UTF-8 -*-
#导入re库文件
import re
old_url = 'http://www.jikexueyuan.com/course/android/?pageNum=2'
total_page = 20

f = open('jikexueyuan.html','r',encoding='utf-8') #以指定的编码类型（即文件本身的编码）打开文件，
# chardet库可以判断文件编码类型
html = f.read()
f.close()
#爬取标题
# title = re.search('<title>(.*?)</title>', html, re.S) .group(1)
# print(title)
#爬取链接
# links = re.findall('href="(.*?)" ', html, re.S)
# for each in links:
#     print (each)
#提取部分文字，先大再小
# text_field = re.findall('<ul(.*?)</ul>', html, re.S)[1]
# text = re.findall('">(.*?)</a></li>', text_field, re.S)
# for each in text:
#     print (each)
#sub实现翻页
for i in range(2,total_page+1):
    newlink = re.sub('pageNum=\d+', 'pageNum=%d'%i,old_url,re.S)
    print(newlink)