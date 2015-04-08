# -*- encoding=utf8 -*-
# 二值化去噪
from PIL import Image
import os
def Binarization(filepath='code/0000.jpg'):
	img = Image.open(filepath) # 读入图片
	img = img.convert("RGBA")
	pixdata = img.load()
	#二值化
	for y in xrange(img.size[1]):
	    for x in xrange(img.size[0]):
	        if pixdata[x, y][0] < 90:
	            pixdata[x, y] = (0, 0, 0, 255)
	for y in xrange(img.size[1]):
	    for x in xrange(img.size[0]):
	        if pixdata[x, y][1] < 136: #解决绿色字符问题从136调整到176
	            pixdata[x, y] = (0, 0, 0, 255)
	for y in xrange(img.size[1]):
	    for x in xrange(img.size[0]):
	        if pixdata[x, y][2] > 0:
	            pixdata[x, y] = (255, 255, 255, 255)
	img.save("re"+filepath+".gif", "GIF")
	#放大图像 方便识别
	im_orig = Image.open("re"+filepath+".gif")
	big = im_orig.resize((1000, 500), Image.NEAREST)

if __name__=="__main__":
	dir="code/"
	for f in os.listdir(dir):
		Binarization(dir+f)
