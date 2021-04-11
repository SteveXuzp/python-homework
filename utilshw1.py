#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.icourse.club/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/55.0.2883.87 Safari/537.36'}
html = requests.get(url, headers=headers)
bs = BeautifulSoup(html.content, "lxml")
comments = bs.find_all(class_="col-sm-11 col-xs-10")
#print(comments)
a = re.findall('<a href=".*?">(.*?)</a>', str(comments))
time = re.findall('<span class="float-right">(.*?)</span>', str(comments))
contents = re.findall('<p class="text-muted">(.*?)<a', str(comments))
length = len(time)
name=[]
course=[]
for i in range(0,length):
    name.append(a[3*i])
    course.append(a[3*i+1])

