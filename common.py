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
		

#定义保存函数
def saveFile(data,i):
	path = savedir + i + ".out"
	f = open(path,'w')
	f.write(data)
	f.close()