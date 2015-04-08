#-*- coding:UTF-8 -*-
import os, Image,re,time
class string_list():
	"""序列串的处理，max+-的波动情况"""
	def __init__(self,lists):
		self.string_list=[]
		self.string_list=lists

	def get_max(self):
		#返回序列中的最大值和所在位置
		res=(0,0)
		Max=0
		step=0
		#doing
		for i in self.string_list:
			#print "i=%d,Max=%d" % (i[0],Max)
			if (i[0]>Max):
				Max=i[0]
				res=(i[0],step)
			step=step+1 #当前使用给出的序列中的位置记录，而不是i中的存储位置，testcase构建方便调整
		#get value
		self.max_size=res[1] #存储最大值所在位置
		return res 

	def left_diff(self,size=2):
		#返回maxsize结点为起点的left及-x轴的size位置内的趋势值
		maxsize=self.max_size #最大值点的
		res=[]
		#doing
		for i in range(size):
			#左边界处理
			if ((maxsize-i-1) <0):
				res.append("null")
				break
			diff=self.string_list[maxsize-i][0]-self.string_list[maxsize-i-1][0]
			res.append(diff)
			
		return res

	def right_diff(self,size=2):
		#返回maxsize结点为起点的right及+x轴的size位置内的趋势值
		maxsize=self.max_size #最大值点的
		res=[]
		#doing
		for i in range(size):
			#左边界处理
			if ((maxsize+i+1) >(len(self.string_list)-1)):
				res.append("null")
				break
			diff=self.string_list[maxsize+i][0]-self.string_list[maxsize+i+1][0]
			res.append(diff)
			
		return res

class char_img():
	"""序列串的相似程度对比 """
	def __init__(self,wave=3,move_range=3):
		self.wave=wave #波动容忍度，默认为+-3，取img中一个点的大小
		self.move_range=move_range #比较峰值附近的三个点的位置变化趋势

	def samelike(self,st_a,st_b):
		"""两个序列串的波动相似程度samelike越大越相似 """
		samelike=1
		refind_flag=0 #检查比对结果判断是否启用新匹配方式
		#doing
		#max对比
		a_max=st_a.get_max()[0]
		b_max=st_b.get_max()[0]
		#print "a max is %d" % st_a.get_max()[1]
		#print "b max is %d" % st_b.get_max()[1]
		if ( abs(a_max-b_max)<(self.wave+1) ):#最大值在容忍范围上的偏差比较
			samelike=10-abs(a_max-b_max) #偏差范围的绝对值设置为samelike的基数
			refind_flag=samelike
		else:
			#重新查找a,b开始点,起点位置标记
			refind_flag=10
		#print "samelike is %d" % samelike
		#x+3对比
		str_a_right_diff=st_a.right_diff(size=self.move_range) #st_a x+3列表
		str_b_right_diff=st_b.right_diff(size=self.move_range) #st_b x+3列表
		#print "a is"
		#print str_a_right_diff
		#print "b is"
		#print str_b_right_diff
		for i in range(self.move_range):
			#"null"处理
			if (("null"==str_a_right_diff[i]) or ("null" == str_b_right_diff[i])):
				samelike=samelike * 1 #超出范围处理为波动外的值
				refind_flag=refind_flag + 100
				break

			#比较
			#print "samelike is %d" % samelike
			if( abs(str_a_right_diff[i]-str_b_right_diff[i]) < (self.wave + 1 )):
				samelike=samelike * (10-abs(str_a_right_diff[i]-str_b_right_diff[i]))
			else:
				samelike=samelike * 1


		#x-3对比
		str_a_left_diff=st_a.left_diff(size=self.move_range) #st_a x+3列表
		str_b_left_diff=st_b.left_diff(size=self.move_range) #st_b x+3列表
		#print "a is"
		#print str_a_left_diff
		#print "b is"
		#print str_b_left_diff
		for i in range(self.move_range):
			#"null"处理
			if (("null"==str_a_left_diff[i]) or ("null" == str_b_left_diff[i])):
				samelike=samelike * 1 #超出范围处理为波动外的值
				break
			#比较
			#print "samelike is %d" % samelike
			if( abs(str_a_left_diff[i]-str_b_left_diff[i]) < (self.wave + 1 )):
				samelike=samelike * (10-abs(str_a_left_diff[i]-str_b_left_diff[i]))
			else:
				samelike=samelike * 1
		#print "samelike is %d" % samelike
		return samelike
	def rob_left_right(self,samelike,range_v=3):
		"""如果最大值出现在左右边距的+3内(range_v)位置，处理噪声问题 """
		pass



class get_file_st():
	def getY_img(self,f):
		"""获得从行角度看y轴波动情况 """
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
		return x_Max

	def getX_img(self,f):
		"""获得从列角度看x轴波动情况 """
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
	
			#y_Max.sort()
		return y_Max
	

def char_xyMax(filespath="./"):
	char_list_x=[]
	char_list_y=[]
	for f in os.listdir(filespath):
		if f.endswith(".gif"):
			u=get_file_st()
			t=u.getY_img(filespath+f)
			ty=u.getX_img(filespath+f)
			char_list_x.append((f,t))
			char_list_y.append((f,ty))
			#print f
			#print getXMax_img(f)
			#print getY_img(f)
	
	return char_list_x,char_list_y

def mave_xy(filepath="1.gif"):
	test_x=get_file_st()
	f=filepath
	x=test_x.getY_img(f)
	y=test_x.getX_img(f)
	target_x=string_list(x)
	target_y=string_list(y)

	use_diff=char_img(move_range=4) #比较者
	reslist_x=[]
	reslist_y=[]
	xy_list=[]
	(x_list,y_list)=char_xyMax("../")
	for i in x_list:
		mod_x=string_list(i[1])
		reslist_x.append((use_diff.samelike(target_x,mod_x),i[0]))
	j=0
	for i in y_list:
		mod_y=string_list(i[1])
		diff_y=use_diff.samelike(target_y,mod_y)
		reslist_y.append((diff_y,i[0]))

		#总权值
		total=diff_y*reslist_x[j][0]
		xy_list.append((total,i[0]))
		j=j+1	
	
	print "~" *20
	reslist_x.sort()
	print reslist_x[-1]
	reslist_y.sort()
	print reslist_y[-1]
	xy_list.sort()
	print xy_list[-1]


if __name__=="__main__":
	filespath="res/"
	for f in os.listdir(filespath):
		if f.endswith(".gif"):
			print "*"*40
			print f
			mave_xy(filespath+f)



