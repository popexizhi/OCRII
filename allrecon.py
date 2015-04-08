# -*- coding: UTF-8 -*-
import os, Image
def binary(f):
    img = Image.open(f)
    #img = img.convert('1')
    pixdata = img.load()
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][0] < 90:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][1] < 136:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][2] > 0:
                pixdata[x, y] = (255, 255, 255, 255)
    return img
def division(img):
    font=[]
    for i in range(4):
        x=7+i*15
        y=1
        font.append(img.crop((x,y,x+16,y+25)))
    return font
def recognize(img):
    fontMods = []
    for i in range(10):
        fontMods.append((str(i), Image.open("./num/%d.bmp" % i)))
    result=""
    font=division(img)
    for i in font:
        target=i
        points = []
        for mod in fontMods:
            diffs = 0
            for yi in range(13):
                for xi in range(9):
                    if mod[1].getpixel((xi, yi)) != target.getpixel((xi, yi)):
                        diffs += 1
            points.append((diffs, mod[0]))
        points.sort()
        result += points[0][1]
    return result
if __name__ == '__main__':
    codedir="./code/"
    for imgfile in os.listdir(codedir):
        if imgfile.endswith(".jpg"):
            dir="./result/"
            img=binary(codedir+imgfile)
            num=recognize(img)
            dir += (num+".png")
            print "save to", dir
            img.save(dir)
