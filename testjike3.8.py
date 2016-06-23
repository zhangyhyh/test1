# -coding:utf-8 -*-
import requests
import re
import sys
reload(sys)
# sys.setdefaultencoding("utf-8")
class spider(object):
    def changepage(self, url, total_page): #换页功能
        now_page = int(re.search('pageNum=(\d+)', url, re.S).group(1))
        page_group = []
        for i in range(now_page, total_page+1):
            link = re.sub('pageNum=\d+', 'pageNum=%s'%i, url, re.S)
            page_group.append(link)
        return page_group
    def getsource(self, url):
        html = requests.get(url)
        html.encoding = "utf-8"
        return html.text
    def geteveryclass(self, source):
        everyclass = re.findall('(<li id=.*?</li>)', source, re.S)
        return everyclass
    def getinfo(self, eachclass):
        info = {} #定义一个字典
        #课程标题和介绍
        info1 = re.search('title="(.*?)" alt="', eachclass, re.S).group(1)
        info2 = re.search('none;">(.*?)</p>', eachclass, re.S).group(1)
        i1 = info1.encode("utf-8")   ########这边很重要重要 重要 重要 重要
        i2 = info2.encode("utf-8")
        info["title"] = str(i1)
        info["content"] = str(i2)
        #课程时间和等级
        info3 = re.findall('<em>(.*?)</em>', eachclass, re.S)
        i3 = info3[0].encode("utf-8")
        i4 = info3[1].encode("utf-8")
        info["class time"] = str(i3)
        info["class level"] = str(i4)

        # asciistring = unicodestring.encode("ascii")
        return info
    def saveinfo(self, classinfo):
        f = open('info.txt', 'w')
        for each in classinfo:
            seq1 = ["title: ",each["title"],"\n"]
            seq2 = ["content: ", each["content"],"\n"]
            seq3 = ["class time: ", each["class time"], "\n"]
            seq4 = ["class level: ", each["class level"], "\n"]

            f.writelines(seq1)
            f.writelines(seq2)
            f.writelines(seq3)
            f.writelines(seq4)
        f.close()






if __name__ == '__main__':
    classinfo = []
    url = 'http://www.jikexueyuan.com/course/?pageNum=1'
    jikespider = spider()
    all_links = jikespider.changepage(url, 20)
    for link in all_links:
        print("正在处理的页面： " +link)
        html = jikespider.getsource(link)
        everyclass = jikespider.geteveryclass(html)
        for each in everyclass:
            info = jikespider.getinfo(each)
            classinfo.append(info)
    jikespider.saveinfo(classinfo)
