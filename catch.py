#--*--coding:utf-8--*--
import urllib
import urllib.request
import config

def catch(url):
	req = urllib.request.Request(url=url,headers=headers)
	res = urllib.request.urlopen(req)
	data = res.read().decode('gbk')
	return data




if __name__ == "__main__":
	str = catch("http://www.runoob.com/python3/python3-dictionary.html")
	print(str)