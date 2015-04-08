#-*- coding:UTF-8 -*-
import os,Image,re
class img_to_string():
	def get_charslib(self,path_charslib="char-code/"):
		"""加载字符库,path_charslib为字符库路径 """
		fontMods={}
	        charpath=path_charslib 
	        #加载字库
		getname_r=r".*(?=\.gif)"
	        for i in os.listdir(charpath):
			if i.endswith(".gif"):
				#获得字符名称
	    			charname=re.findall(getname_r,i)[0]
	    			#print "charname is %s " % charname
	            		fontMods[charname]=img_do(charpath+i)
	    
	    	return fontMods

class img_do():
	def __init__(self,filepath):
		#点阵大小定义
		self.y_long=25 #y轴范围
		self.x_long=16 #x轴范围
		
		self.filepath=filepath
		img=Image.open(filepath)
		self.img_xy=[]
		self.img_xy.append(img)

	def not_black_point(self):
		"""提供可对比的像素起点"""
		font = self.img_xy
		for i in font:
			#print i
			for yi in range(self.y_long):
				for xi in range(self.x_long):
					if ( "225" == str(i.getpixel((xi,yi)))):#如果为空白继续查找
							pass
					else:
						return (xi,yi)
		return (-1,-1)
	def getxy_pixel(self,x,y):
		"""返回xy的指定值 """
		return self.img_xy[0].getpixel((x,y))	

	def get_img(self):
		return self.img_xy

	def get_filename(self):
		return self.filepath

if __name__=="__main__":
	a= img_to_string()
	print a.get_charslib()


