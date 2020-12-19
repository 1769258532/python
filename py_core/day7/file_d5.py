#-*-coding:utf-8 -*-
#!/usr/bin/python3
# @Author:liulang

with open(r'xxx.docx', 'rb') \
		as src, open('test_new.docx', 'wb') as dst:
	dst.write(src.read())
