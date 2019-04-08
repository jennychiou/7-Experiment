import requests		#引入requests普通模組
from bs4 import BeautifulSoup


article_title = []
article_class = []
re=requests.get("https://www.ptt.cc/bbs/index.html",cookies={'over18': '1'})
#使用普通get拿取網頁碼存在re,後面用cookie判定大於18歲
soup= BeautifulSoup(re.text, "html.parser")
# https://www.ptt.cc/bbs/Gossiping/index.html
results=soup.find_all("div",{"class":"board-name"})
# print(results)#抓index title
resultss=soup.find_all("div",{"class":"board-class"})




# https://www.ptt.cc/bbs/Gossiping/index.html
# print(results)#抓index title


for item in results:
	item_title=item.text
	article_title.append(item_title)
	
for item in resultss:
	item_class=item.text
	article_class.append(item_class)


# print(article_title,article_class)
	


dictionary = dict(zip(article_class, article_title))
# print (dictionary)/01
for i in dictionary.items():
    print(i[0],i[1])

#input_one=input("請輸入你要的版面")
input_one=4
board_ptt=article_title[input_one]
print(board_ptt)
article_href = []
r=requests.get("https://www.ptt.cc/bbs/"+board_ptt+"/index.html",cookies={'over18': '1'})
soup= BeautifulSoup(r.text, "html.parser")
# https://www.ptt.cc/bbs/Gossiping/index.html
results=soup.find_all("div",{"class":"title"})
# print(results)#抓ptt /gossoping/url



article_href_url=[]
for item in results:
	item_href=item.find("a")
	print(item_href)
	if item_href is None:
		print('No  value supplied')
	else:
		article_href.append(item_href.text)
		item_href_url=item.find("a").attrs['href']
		article_href_url.append(item_href_url)
		
		print(item_href.text)
		# print(item_href_url)
#input_two=input("請輸入想看的內容值")
input_two=1
title_href="https://www.ptt.cc"+article_href_url[input_two]
print(title_href)

	# 64/65 39/40