import os ,Image
j = 1
dir="recode/"
for f in os.listdir(dir):
    if f.endswith(".gif"):
        img = Image.open(dir+f)
        for i in range(4): 
            x = 7 + i*15
            y = 1
            img.crop((x, y, x+16, y+25)).save("font/%d.gif" % j) 

            print "j=",j 
            j += 1
