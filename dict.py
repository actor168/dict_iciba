__author__ = 'actor168'
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re



#使用爱词霸查询单词中文意思
class DICT:

    #初始化，传入基地址
    def __init__(self,baseUrl):
        #base链接地址
        self.baseURL = baseUrl

    #传入页码，获取该页帖子的代码
    def getPage(self):
        try:
            #构建URL
            url = self.baseURL
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            #返回UTF-8格式编码内容
            return response.read().decode('utf-8')
        #无法连接，报错
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
               print u"连接失败,错误原因",e.reason
	       return None

    
    def getContent(self,page):
        #匹配所有楼层的内容
        pattern = re.compile('<span class='+"'"+'prop'+"'"+'>.*?</span>.*?<p>(.*?)</p>',re.S)
        result = re.search(pattern,page)
    	if result:
        #print result.group(1)  #测试输出
        	return result.group(1).strip()
    	else:
        	return None


    def writeData(self,contents):
        #向文件写入每一楼的信息
        print contents;


    def start(self):
        try:
	    page = self.getPage();
            contents = self.getContent(page)
            self.writeData(contents)
        #出现异常
        except IOError,e:
            print "查询异常，原因" + e.message
        finally:
            print "------"
	   

print u"please input"
baseURL = 'http://www.iciba.com/' + str(raw_input(u'http://www.iciba.com/'))
dict_ac = DICT(baseURL)
dict_ac.start()
