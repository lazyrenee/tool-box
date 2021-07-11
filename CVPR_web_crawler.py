import urllib.request
import re
import os
from bs4 import BeautifulSoup
import requests

os.chdir('/Users/reneejia/Desktop') 

url='http://openaccess.thecvf.com/CVPR2018.py'
response=requests.get(url)
a='http://openaccess.thecvf.com/'

results_page = BeautifulSoup(response.content,'lxml')
text=results_page.find_all('div',class_="bibref")
names=[]
for i in text:
    single='[CVPR2018]'+re.findall(r"(?<=^title = {).*(?=})",str(i),flags=re.MULTILINE)[0]+'.pdf'
    names.append(single)
#print(names)

def getFile(url,count):
    file_name = names[count]
    u = urllib.request.urlopen(url)
    f = open(file_name, 'wb')
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        f.write(buffer)
    f.close()
    print ("Sucessful to download" + " " + file_name)

results_page = BeautifulSoup(response.content,'lxml')
all_tags = results_page.find_all(href=re.compile("content_cvpr_2018/papers"))

os.mkdir('paper2')
os.chdir(os.path.join(os.getcwd(), 'paper2'))
list=[]
for b in all_tags:
    list.append(b.get('href'))
for i in range(47,len(list)+1):
    print(i)
    m=a+list[i-1]
    getFile(m,i)
    i+=1

os.chdir('/Users/reneejia/Desktop') 
os.getcwd()