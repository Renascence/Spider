import urllib
import re


response = urllib.urlopen('http://tieba.baidu.com/p/2460150866')  
html = response.read()
reg = r'src="(.+?\.jpg)"'
imgre = re.compile(reg)
imglist = re.findall(imgre,html)
x=0
for imgurl in imglist:
  urllib.urlretrieve(imgurl,'%s.jpg' % x)
  x+=1
