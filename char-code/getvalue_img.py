#-*- coding:UTF-8 -*-
import os, Image,re,time
def getYMax_img(f):
	#加载文件
	img = Image.open(f)
    	font=[]
    	font.append(img)

	x_Max=[]
	#打印对应的img点内容
	for i in font:
		for xi in range(16):
			oldmax=Max=0
			for yi in range(24):
				if(0 == i.getpixel((xi,yi)) and 0 ==i.getpixel((xi,yi+1))):
					oldmax=oldmax+1
				else:
					if (Max<oldmax):
						Max=oldmax
					oldmax=0
			if(Max<oldmax):
				Max=oldmax

			x_Max.append((Max,xi))

		#x_Max.sort()
		return x_Max


def getXMax_img(f):
	#加载文件
	img = Image.open(f)
    	font=[]
    	font.append(img)

	y_Max=[]
	#打印对应的img点内容
	for i in font:
		for yi in range(25):
			oldmax=Max=0
			for xi in range(15):
				if(0 == i.getpixel((xi,yi)) and 0 ==i.getpixel((xi+1,yi))):
					oldmax=oldmax+1
				else:
					if (Max<oldmax):
						Max=oldmax
					oldmax=0
			if(Max<oldmax):
				Max=oldmax

			y_Max.append((Max,yi))

		y_Max.sort()
		return y_Max
def show_img(f):
	#加载文件
	img = Image.open(f)
    	font=[]
    	font.append(img)

	#打印对应的img点内容
	for i in font:
		for yi in range(25):
			u=""
			for xi in range(16):
				u=u+"\t"+str(i.getpixel((xi,yi)))
			print u
def pr_xyMax(mod,target):
	#显示xy排序效果
	print getYMax_img(mod)
	print getYMax_img(target)
	print "~"*20
	print getXMax_img(mod)
	print getXMax_img(target)

def char_xyMax(filespath="./"):
	for f in os.listdir(filespath):
		if f.endswith(".gif"):
			print f
			#print getXMax_img(f)
			print getYMax_img(f)


if __name__=="__main__":
	modfile="h_2.gif"
	targfile="h.gif"
	#show_img(modfile)
	#pr_xyMax(modfile,targfile)
	char_xyMax()

