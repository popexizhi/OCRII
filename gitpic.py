import urllib
for i in range(150):
    url = 'http://checkin.99114.com/getVcode'
    print "download", i
    file("./code/%04d.jpg" % i, "wb").write(urllib.urlopen(url).read())
