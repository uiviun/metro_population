from bs4 import BeautifulSoup
import requests
import re
import time
import urllib
import sys

headers={
			'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
		}

fo = open("list_raw.txt", "w")
for i in range(1,2):
    for j in ["heping","nankai","hebei","hexi","hedong","hongqiao","xiqing","dongli","jinnan","beichen","binhaixinqu"]:
        i=str(i)
        j=str(j)
        s="https://tj.lianjia.com/xiaoqu/"+j+"/pg"+i+"/"
        time.sleep(1)
        print (s+"\n")
        response = requests.get(url=s,headers=headers)
        html = response.text
        soup = BeautifulSoup(html)
       # print(soup)
        ditinct2 = soup.find_all("li", "clear xiaoquListItem")
        ditinct2=str(ditinct2)
        print(ditinct2)
      #  l=re.search(r"resblockPosition:'(.*)',",ditinct2).group(1)
      # p=l.split("'")
      #  fo.write(p[0]+"\n")
    


fo.close()
