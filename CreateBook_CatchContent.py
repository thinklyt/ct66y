''''' 
伪装浏览器 

对于一些需要登录的网站，如果不是从浏览器发出的请求，则得不到响应。 
所以，我们需要将爬虫程序发出的请求伪装成浏览器正规军。 
具体实现：自定义网页请求报头。 
'''

#实例二：依然爬取豆瓣，采用伪装浏览器的方式
import os
import os.path
import urllib.request
import time
import re

servicedir = "D:\\李雨田的桌面\\mine\\python\\Spider\\"
savedir = "D:\\李雨田的桌面\\mine\\python\\Spider\\Booklist_Source\\"
savedir2 = "D:\\李雨田的桌面\\mine\\python\\Spider\\Booklist_Content\\"
#定义保存函数
def saveFile(data,i):
	path = savedir2 + i + ".content"
	f = open(path,'w',encoding='UTF-8')
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

		
file = open(servicedir + "booklist.txt")
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
'Chrome/51.0.2704.63 Safari/537.36'
}


list = os.listdir(savedir) #列出文件夹下所有的目录与文件
for i in range(0,len(list)):
	path = os.path.join(savedir,list[i])
	if os.path.isfile(path):
		#你想对文件的操作
		file = open(path,"r",encoding='UTF-8')
		print(path)
		ii = 1
		strs = ""
		while 1:
			line = file.readline()
			print(line)
			if not line:
				break
			pass # do something
			if len(line) > 4:
				url = "https://shici.chazidian.com" + line
				print(url)
				try:
					req = urllib.request.Request(url=url,headers=headers)
					res = urllib.request.urlopen(req)
					data = res.read().decode('gbk')
					data = data.encode('utf8')
				
					title = txt_wrap_by("<title>"," - 查字典诗词网</title>",data)
					content = txt_wrap_by('<div id="print_content">','<p id="pages_next">',data)
					print(title)
					title = "第" + '%d'%ii + "首：" + title + "\n"
					strs = strs + "\n" + title + content + "\n"
					ii = ii + 1
					print("ok")
				except Exception:
					pass
					time.sleep(20)
			time.sleep(1)
		saveFile(strs,list[i])
		
		print(list[i]+"ok")
		print(path+"抓取完毕")
		'''
		
		'''
		
'''

i = 0
while 1:
	line = file.readline()
	if not line:
		break
	pass # do something
	url = line
	print(line)
	req = urllib.request.Request(url=url,headers=headers)
	res = urllib.request.urlopen(req)

	data = res.read().decode()	#读取二进制流并转为str
	#如果出错怎么处理？
	
	title = txt_wrap_by("<title>"," - 查字典诗词网</title>",data)
	
	#取出唐诗名字列表
	content = txt_wrap_by('<div class="list100">','<div class="clear"></div>',data)
	content = content.replace('</li><li>','</li>\n<li>')
	content = content.replace('<ul>','')
	content = content.replace('</ul>','')
	#print(content)
	content = content.replace(" ","")
	urls = re.findall(r'\/shi\d*\/',content,re.I)
	strs = ""
	for i in urls:
		#print(i)
		strs = strs + i + "\n"
	else:
		#print('this is over')
		pass

	#也可以把爬取的内容保存到文件中
	saveFile(strs,title)
	#i = i + 1
	print(title)
	
	time.sleep(1)
'''