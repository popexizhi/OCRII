#-*- coding:UTF-8 -*-
import os, Image,re,time
class img_to_string():
	def get_charslib(self,path_charslib="char-code/"):
		"""加载字符库,path_charslib为字符库路径 """
		fontMods={}
	        charpath=path_charslib 
	        #加载字库
		getname_r=r"^."
	        for i in os.listdir(charpath):
			if i.endswith(".gif"):
				#获得字符名称
	    			charname=re.findall(getname_r,i)[0]
	    			#print "charname is %s " % charname
	            		fontMods[charname]=Image.open(charpath+i)
	    
	    	return fontMods

def recognize(f):
    fontMods ={}
    x=img_to_string() 
    fontMods = x.get_charslib() #字符库
    
    #加载被分析字符
    img = Image.open(f)
    font=[]
    font.append(img)
    
    result=""
    for i in font:
        target=i
        points = []
        for mod in fontMods:
            diffs = 0
	    #print "mod is %s" % mod
            for yi in range(25):
                for xi in range(16):
                    if fontMods[mod].getpixel((xi, yi)) != target.getpixel((xi, yi)):
                        diffs += 1
            points.append((diffs, mod[0]))
        points.sort()
	print "points lists is:"
	print points
        result += points[0][1]
	
	#保存识别结果
	if (int(points[0][0])<=35):
		saveimg(target,"goodres/"+points[0][1]+"_"+str(points[0][0]))
	else:
		saveimg(target,"badres/"+points[0][1]+"_"+str(points[0][0]))


    return result

def saveimg(img,filename):
	img.save(filename+"__"+str(time.time())+".gif","GIF")

if __name__=="__main__":
	#filepath="./font/"
	filepath="./que/"
	for f in os.listdir(filepath):
		if f.endswith(".gif"):
			#print "-"*20
			#print f
			recognize(filepath+f)
		
	
