''''' 
伪装浏览器 

对于一些需要登录的网站，如果不是从浏览器发出的请求，则得不到响应。 
所以，我们需要将爬虫程序发出的请求伪装成浏览器正规军。 
具体实现：自定义网页请求报头。 
'''

#抓取帖子列表
import os
import os.path
import urllib.request
import time
import re
import pymysql
import sys



servicedir = "D:\\python\\zt66y\\"
savedir = "D:\\python\\zt66y\\Booklist_Source\\"

#定义保存函数
def saveFile(data,i):
	path = savedir + i + ".out"
	f = open(path,'w')
	f.write(data)
	f.close()

#取字符串中两个符号之间的东东
def txt_wrap_by(start_str, end, html):
	start = html.find(start_str)
	if start >= 0:
		start += len(start_str)
		end = html.find(end, start)
		if end >= 0:
			return html[start:end].strip()
		else:
			return ""
	else:
		return ""

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
'Chrome/51.0.2704.63 Safari/537.36'
}

db = pymysql.connect("localhost","root","","catch_t66y",use_unicode=True, charset="utf8")

# 使用cursor()方法获取操作游标 
cursor = db.cursor()


i = 1
while 1:
	if i > 2:
		break
	pass # do something
	url = "http://cl.9io.xyz/thread0806.php?fid=16&search=&page=" + '%d'%i
	print(url)
	req = urllib.request.Request(url=url,headers=headers)
	res = urllib.request.urlopen(req)

	data = res.read().decode('gbk')
	#data = data.encode('utf8')
	
	#如果出错怎么处理？
	
	#提取帖子
	urls = re.findall(r'\<h3\>\<a href=\"(.*)\" target=\"\_blank\" id=\"\">(.*)\<\/a\>\<\/h3\>',data,re.I)
	
	'''
	
	<h3><a href="htm_data/16/1706/2443000.html" target="_blank" id=""><font color=green>[原创][cl分享团出品]衰男搞定奥迪老板娘丝袜诱惑给你看穴肥水多惹人眼[13P]</font></a></h3>
	cl_post
	`oid` int(11) NOT NULL,
	`title` varchar(512) COLLATE utf8_bin NOT NULL,
	`url` varchar(512) COLLATE utf8_bin NOT NULL,
	`create_time` int(11) NOT NULL,
	`content` text COLLATE utf8_bin NOT NULL,
	`flg_catch` int(11) NOT NULL,
	`flg_green` int(11) NOT NULL
	'''
	
	'''
	findall函数返回的总是正则表达式在字符串中所有匹配结果的列表，此处主要讨论列表中“结果”的展现方式，即findall中返回列表中每个元素包含的信息。
	
	@1.当给出的正则表达式中带有多个括号时，列表的元素为多个字符串组成的tuple，tuple中字符串个数与括号对数相同，字符串内容与每个括号内的正则表达式相对应，并且排放顺序是按括号出现的顺序。
	@2.当给出的正则表达式中带有一个括号时，列表的元素为字符串，此字符串的内容与括号中的正则表达式相对应（不是整个正则表达式的匹配内容）。
	@3.当给出的正则表达式中不带括号时，列表的元素为字符串，此字符串为整个正则表达式匹配的内容。
	'''
	
	
	strs = ""
	for urlli in urls:
		print(urlli[0])
		print(urlli[1])
		#urlli_s = re.findall(r'htm_data\/.*\"',urlli,re.I)
		
		#cl_post_title = txt_wrap_by('<a href="','" target="_blank"',urlli)
		#cl_post_url = txt_wrap_by('target="_blank" id="">','</a></h3>',urlli)
		#cl_post_create_time = time.time()
		
		
		
		'''
		sql = r"INSERT INTO cl_post(title, url, create_time) VALUES ('%s', '%s', %d)" % (cl_post_title, cl_post_url, cl_post_create_time)
		
		print(sql)
		if cl_post_title != "":
			try:
				cursor.execute(sql)
				db.commit()
			except:
				db.rollback()
		'''
	else:
		#print('this is over')
		pass
	 
	i = i + 1
	time.sleep(5)

# 关闭数据库连接
db.close()
