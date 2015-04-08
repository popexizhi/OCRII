#-*- coding=UTF-8 -*-
import os, Image,re,time
import unittest
import urllib
from img_to_string import img_do,img_to_string #添加字符库图片处理库
from Binarization import Binarization #二值去噪
import string_list #波动方式匹配

class diff_rob():
	def __init__(self):
		#点阵大小定义
		self.y_long=25 #y轴范围
		self.x_long=16 #x轴范围
	
	def doing(self,mod,target):
		#全图对比
		diffs=0
		for yi in range(self.y_long):
			for xi in range(self.x_long):
				t=(225 == (mod.get_img()[0].getpixel((xi, yi))) and (0 ==target.get_img()[0].getpixel((xi, yi))))#由于此方式可能引起n被识别为m的问题，所以使用basic的严格匹配方式
				basic =(mod.get_img()[0].getpixel((xi, yi)) != target.get_img()[0].getpixel((xi, yi)))
				if (basic):
					diffs += 1
				
		return diffs


	def doing_startdiff(self,mod,target):
		#起点对比
		diffs=0 #对比结果
		d_point=0 #比较过的点数记录
		(xi_mod,yi_mod)=mod.not_black_point()
		(xi_target,yi_target)=target.not_black_point()
		if(((-1,-1) == (xi_target,yi_target)) or ( (-1,-1) ==(xi_mod,yi_mod) ) ):
			return -1 # 存在无对比点的img
		
		xi_T=xi_target-xi_mod #x轴差距
		yi_T=yi_target-yi_mod #y轴差距
		while((yi_target < self.y_long) and (yi_mod < self.y_long) ):
			while ((xi_target < self.x_long) and (xi_mod < self.x_long)):
				d_point=d_point+1
				#差异位置
				t=((225 == mod.getxy_pixel(xi_mod,yi_mod)) and (0 == target.getxy_pixel(xi_target,yi_target)))
				u=(mod.getxy_pixel(xi_mod,yi_mod) != target.getxy_pixel(xi_target,yi_target) )
				if (u):
					diffs += 1
				
				xi_mod=xi_mod+1
				xi_target=xi_target+1
			#y轴位置修改
			yi_mod=yi_mod+1
			yi_target=yi_target+1
			#x轴位置修改
			if( xi_T>= 0): #x偏移量是目标图向右时，移动target的起点
				xi_mod=0
				xi_target=xi_T
			else:#x偏移量是目标图向左时,移动mod的起点
				xi_target=0
				xi_mod=0-xi_T

		#print "mod stop is"+str(xi_mod)+" "+str(yi_mod)
		#print "target stop is"+str(xi_target)+" "+str(yi_target)
		#print "d_point is "+str(d_point)
		return diffs

def recognize_mave(f):	
    	"""mave 方式获得内容 """
	#print "%s get is :" % f
	#print string_list.mave_xy(f)
	return string_list.mave_xy(f)

				
def recognize_x(f):
    fontMods ={}
    x=img_to_string() 
    fontMods = x.get_charslib() #字符库
 
    #加载被分析字符
    img = img_do(f)
    font=[]
    font.append(img)

    result=""
    for i in font:
	    target=i
	    points=[]
	    for mod in fontMods:
		    diffs=diff_rob()
		    points.append((diffs.doing(fontMods[mod],i),mod))
		    #print "mod is %s" % mod
	
	    #比较结果排序
	    points.sort()
	    #print "points list is:"
	    #print points

	    #保存识别结果
	    sourecode=re.findall(r"\d+",target.get_filename())[0]
	    if (int(points[0][0])<=35):
		result += points[0][1][0]  #满足对比值保存
	    	saveimg(target.get_img()[0],"goodres/"+sourecode+"_"+points[0][1]+"_"+str(points[0][0]))
	    else:
		"""#基本对比算法小于分析接受值时,使用偏移方式对比 [popexizhi:使用波动对比放弃此偏移计算]
		points=[]
		for mod in fontMods:
			diffs=diff_rob()
			points.append((diffs.doing_startdiff(fontMods[mod],i),mod))
	 	#比较结果排序
	        points.sort()
	        #print "startdiff points list is:"
	        #print points

     	        result += points[0][1][0]
		if (int(points[0][0])<=35):
	    	    saveimg(target.get_img()[0],"goodres/"+sourecode+"_str"+"_"+points[0][1]+"_"+str(points[0][0]))
	        else:
		    saveimg(target.get_img()[0],"badres/"+sourecode+"_"+points[0][1]+"_"+str(points[0][0]))
		"""
		#recognize_mave 波动方式对比处理
		mave_res=recognize_mave(f)
		print "%s is " % f 
		print mave_res
		result +=mave_res[1][0]
    #print "fontMode is "
    #print fontMods

    return result

def saveimg(img,filename):
	img.save(filename+".gif","GIF")

def loadnewpic(getnum=200):
	#下载原始文件
	print "start loadpic"
	for i in range(getnum):
		url="http://checkin.99114.com/getVcode"
		print "downloade:", i
		file("./code/%04d.jpg" % i, "wb").write(urllib.urlopen(url).read())

def binarization_do():
	#去噪处理
	dir="code/"
	print "start binarization_do"
	for f in os.listdir(dir):
		print f
		Binarization(dir+f)
def split_img(dir="recode/"):
	#分割字符
	print "start split_img"
	j = 1
	for f in os.listdir(dir):
	    if f.endswith(".gif"):
	        img = Image.open(dir+f)
	        for i in range(4): 
	            x = 7 + i*15
	            y = 1
	            img.crop((x, y, x+16, y+25)).save("font/%d.gif" % j) 
	
	            print "j=",j 
	            j += 1

def change_to_string():
	#对比字库转换为对应内容
	t="res is:"
	filepath="./font/"
	#filepath="./que/"
	print "start change_to_string "
	for f in os.listdir(filepath):
		if f.endswith(".gif"):
			#print "-"*20
			#print f
			t=t+recognize_x(filepath+f)

	print t

if __name__=="__main__":
	loadnewpic(1)#下载原始文件
	binarization_do() #二值去噪
	split_img() #原图分割
	change_to_string() #转换为字符


