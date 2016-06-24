# -coding:utf-8 -*-
from lxml import etree
html = '''
<html class="">
<head>
    <meta charset="UTF-8">
    <title>福建顺昌</title>
</head>
<body>
<div id="contents">
    <ul id="countrys">
        <li>中国</li>
        <li>美国</li>
    </ul>
    <ul id="cities">
        <li>顺昌</li>
        <li>南平</li>
    </ul>
    <div id="url">
        <a href="http://www.jikexueyuan.com/course/practice/">zhangyihui</a>
        <a href="http://www.jikexueyuan.com/course/practice/" title="项目实战">点我点开</a>
    </div>
</div>

</body>
</html>
'''
selector = etree.HTML(html)
#提取文本
# content = selector.xpath('//ul[@id="countrys"]/li/text()')
# for each in content:
#     print(each)
#提取属性
link = selector.xpath('//*[@id="url"]/a/@href')
for each in link:
    print(each)
#
title = selector.xpath('//*[@id="url"]/a/@title')
print(title[0])#注意虽然列表只有一个数也要加【0】
