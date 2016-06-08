# -*- coding: UTF-8 -*-
# import requests
# html = requests.get('http://tieba.baidu.com/f?ie=utf-8&kw=python')
# print (html.text)

import requests
import re
import sys
# reload(sys)
# sys.setdefaultencoding("gb18030")
type = sys.getfilesystemencoding()

# head = {'User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
# html = requests.get('http://jp.tingroom.com/yuedu/yd300p/',headers = head)
html = requests.get('http://jp.tingroom.com/yuedu/yd300p/')
html.encoding = 'utf-8'
# print(html.text)
title = re.findall('color:#666666;">(.*?)</span></p></li>',html.text,re.S)
for each in title:
    print(each)





