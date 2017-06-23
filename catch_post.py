#--*--coding:utf-8--*--
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







if __name__ == "__main__":



i = 1
while 1:
	if i > 2:
		break
	pass # do something
	url = "http://cl.9io.xyz/thread0806.php?fid=16&search=&page=" + '%d'%i
	print(url)
	'''
	req = urllib.request.Request(url=url,headers=headers)
	res = urllib.request.urlopen(req)

	data = res.read().decode('gbk')
	#data = data.encode('utf8')
	'''
	#如果出错怎么处理？
	
	#提取帖子
	urls = re.findall(r'\<h3\>\<a href=\"(.*)\" target=\"\_blank\" id=\"\">(.*)\<\/a\>\<\/h3\>',data,re.I)
	
	
	
	
	
	
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
