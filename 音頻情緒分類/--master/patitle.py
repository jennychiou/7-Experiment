import urllib.request
from bs4 import BeautifulSoup
#如果不加上下面的这行出现会出现urllib2.HTTPError: HTTP Error 403: Forbidden错误
    #主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问User-Agent,具体的信息可以通过火狐的FireBug插件查询
import requests
from bs4 import BeautifulSoup


article_title = []
article_class = []
re=requests.get("https://www.ptt.cc/bbs/index.html",cookies={'over18': '1'})
soup= BeautifulSoup(re.text, "html.parser")
# https://www.ptt.cc/bbs/Gossiping/index.html
results=soup.find_all("div",{"class":"board-name"})
# print(results)#抓index title
resultss=soup.find_all("div",{"class":"board-class"})




# https://www.ptt.cc/bbs/Gossiping/index.html
#print(results)#抓index title


for item in results:
	item_title=item.text
	article_title.append(item_title)
	
for item in resultss:
	item_class=item.text
	article_class.append(item_class)

dictionary = dict(zip(article_class, article_title))
# print (dictionary)/01
for i in dictionary.items():
    print(i[0],i[1])


abc=input("請輸入你要進入的看板:(參考上面選項)")
aurl="https://www.ptt.cc/bbs/"+abc+"/index.html"
print(aurl)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(aurl, headers=headers)
response=urllib.request.urlopen(req).read()

soup =  BeautifulSoup(response,"html.parser")

container = soup.select('.r-ent')
for each_item in container:
     print ("日期："+each_item.select('div.date')[0].text, "作者："+each_item.select('div.author')[0].text)
     print (each_item.select('div.title')[0].text)
     print ("---------------------------------")
results=soup.find_all("div",{"class":"title"})
article_href=[]
article_href_url=[]
for item in results:
	item_href=item.find("a")
	#print(item_href)
	if item_href is None:
		print('No  value supplied')
	else:
		article_href.append(item_href.text)
		item_href_url=item.find("a").attrs['href']
		article_href_url.append(item_href_url)
		
		print(item_href.text)
		# print(item_href_url)
input_two=int(input("請輸入想看的內容值"))
#input_two=1
title_href="https://www.ptt.cc"+article_href_url[input_two]


a=title_href

