import requests
import json
import jieba
import jieba.analyse
import imp
from bs4 import BeautifulSoup
from sklearn.feature_extraction import DictVectorizer #用於轉換 dict 為 sklearn estimators 可用的向量
from sklearn.feature_extraction.text import TfidfTransformer #將矩陣轉換為 TF 或 TF-IDF 表示
from sklearn.svm import LinearSVC #以 LinearSVC 分類演算法為例
from collections import defaultdict #使用 dict 儲存資料
import re
import random
import urllib3
urllib3.disable_warnings()



# 	else:
# 	# 	# print(tempstr[0])
# print('angry','\n',sadlist)
# print('happy', '\n', happylist)
# print('sad', '\n', sadlist)
# print('relax', '\n', relaxlist)

import urllib.request
from bs4 import BeautifulSoup
#如果不加上下面的这行出现会出现urllib2.HTTPError: HTTP Error 403: Forbidden错误
    #主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问User-Agent,具体的信息可以通过火狐的FireBug插件查询
import requests
from bs4 import BeautifulSoup


article_title = []
article_class = []
re1=requests.get("https://www.ptt.cc/bbs/index.html",cookies={'over18': '1'})
soup= BeautifulSoup(re1.text, "html.parser")
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
# abc="LOL"
aurl="https://www.ptt.cc/bbs/"+abc+"/index.html"
print(aurl)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(aurl, headers=headers)
response=urllib.request.urlopen(req).read()

soup =  BeautifulSoup(response,"html.parser")

container = soup.select('.r-ent')
# print(container)
for each_item in container:
     print ("日期："+each_item.select('div.date')[0].text, "作者："+each_item.select('div.author')[0].text,"貼文數:"+each_item.select('div.nrec')[0].text)
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
# input_two=0
title_href="https://www.ptt.cc"+article_href_url[input_two]


a1=title_href


r=requests.get(a1,cookies={'over18': '1'})
soup= BeautifulSoup(r.text, "html.parser")
results=soup.find_all("div",{"class":"title"})
# # print(results)#抓網址LOL群組內

for item in results:
	item_href=item.find("a").attrs['href']
	article_href.append(item_href)
# 	# print(item_href)
# 	# print("========================================================")

author=soup.select('span.article-meta-value')[0].text #作者
board=soup.select('span.article-meta-value')[1].text
title=soup.select('span.article-meta-value')[2].text
time=soup.select('span.article-meta-value')[3].text
user_tag=soup.select('span.push-tag')
user_id = soup.select('span.push-userid')
user_content = soup.select('span.push-content')
user_ipdatetime = soup.select('span.push-ipdatetime')

print("作者:",author)
print("看板:",board)
print("時間:",time)
print("標題:",title)
print("===================")
push_tag_len=len(user_tag)

tag_shh=0
tag_tag=0
count=0
cut_word =[]
content=[]


while (count<push_tag_len):
	comment=(user_tag[count].text+user_id[count].text+user_content[count].text+" "+user_ipdatetime[count].text)
# 	# # comment=comment.strip();
	print(comment);
	count=count+1
# 	#  for comment in post['comments']: #取得八卦文文章之鄉民留言
total_comments = defaultdict(int)
total_pushes = defaultdict(int)
total_hates = defaultdict(int)
couunt =0 
noob=0
neutral=0
push=0
while (couunt<push_tag_len):
	user = user_id[couunt].text
	total_comments[user] += 1
	push_tag=user_tag[couunt].text
	total_pushes[push_tag] += 1        
	# print(total_pushes)
	push=total_pushes['推 ']
	neutral=total_pushes['→ ']
	noob=total_pushes['噓 ']
   	
	couunt=couunt+1
	if ((push==0) and (neutral==0) and (noob==0)):
		print("無法判斷情緒並預設為快樂")   
# # print("noob",noob)
# # print(neutral,"neutral")
# # print(push,"push")
ptt_result1=[]
tag_sum=noob+neutral+push
if (push>(tag_sum*0.95)):
	print("happy")
	ptt_result1.append("happy")
elif (push>(tag_sum*0.75) and push<(tag_sum*0.95)):
	print("relax")
	ptt_result1.append("relax")
elif (push>(tag_sum*0.5) and push<(tag_sum*0.75)):
	print("sad")
	ptt_result1.append("sad")
elif(push<(tag_sum*0.5)):
	print("angry")
	ptt_result1.append("angry")

# print(ptt_result1)
# url=str(angrylist[random.randint(0,10)]).strip(" ")
sadlist=[]
angrylist=[]
relaxlist=[]
happylist=[]
resultmusic=open("C:/Users/NUTC/Desktop/music-mood-classifier-master/result2.txt","r")
resultmusic1=resultmusic.readlines()
len(resultmusic1)

		
for i in range(len(resultmusic1)):
# 	# print(resultmusic1[i])
	tempstr = str(resultmusic1[i]).split(',')
	if ((tempstr[0]=="happy")  ):
		happylist.append(tempstr[1])
		# print(tempstr[0])
		#url=str(happylist[3]).strip(" ")
	elif( (tempstr[0]=="sad")):
		sadlist.append(tempstr[1])
		# print(tempstr[0])
		#url=str(sadlist[0]).strip(" ")
	elif( (tempstr[0]=="relax")):
	    relaxlist.append(tempstr[1])
		#print(tempstr[0])
		#url=str(relaxlist[3]).strip(" ")
	elif( (tempstr[0]=="angry")):
		angrylist.append(tempstr[1])
		
# print(tempstr[0])
		#url=str(angrylist[3]).strip(" ")
	# if((ptt_result1[0]=="angry") and (tempstr[0]=="angry")):
	# url=str(angrylist[random.randint(0,10)]).strip(" ")
	# print(url)
	# elif((ptt_result1[0]=="happy") and (tempstr[0]=="happy")):
	# url=str(happylist[random.randint(0,11)]).strip(" ")
if((ptt_result1[0]=="angry")):
	url=str(angrylist[random.randint(0,10)]).strip(" ")
	print(url)
elif((ptt_result1[0]=="happy")):
	url=str(happylist[random.randint(0,11)]).strip(" ")
	# print(url)
elif((ptt_result1[0]=="relax")):
	url=str(relaxlist[random.randint(0,9)]).strip(" ")
	# print(url)
elif((ptt_result1[0]=="sad")):
	url=str(sadlist[random.randint(0,11)]).strip(" ")
	# print(url)
	# print(url)
	# elif((ptt_result1[0]=="relax") and (tempstr[0]=="relax")):
	# url=str(relaxlist[random.randint(0,9)]).strip(" ")
	# print(url)
	# elif((ptt_result1[0]=="sad") and (tempstr[0]=="sad")):
	# url=str(sadlist[random.randint(0,11)]).strip(" ")
	# print(url)



res = requests.get(url, verify=False)
soup = BeautifulSoup(res.text,'html.parser')

last = None
youtubeurl=[]
for entry in soup.select('a'):
	m = re.search("v=(.*)", entry['href'])
	
	if m:	
		target = m.group(1)
		if target == last:
			continue
		if re.search("list",target):
			continue
		last = target
		youtubeurl.append(target)


youtube_playlist="https://www.youtube.com/watch?v="+ youtubeurl[0]
# print(happylist)

# print(relaxlist)
# print(sadlist)
# print(angrylist)

# #分類 四個if else分在array裡面
# #youtube爬網址爬第一首
# # url=str(happylist[0]).strip(" ")
# # url = "https://www.youtube.com/results?search_query=sugar+maroon5"
# print (url)
# 		# print(youtubeurl)#檢視碼
# 		# print (target)

# print(youtube_playlist)

from selenium import webdriver
import time
youtube_playlist1=str(youtube_playlist)
chrome_path = "C:/Users/NUTC/Desktop/music-mood-classifier-master/chrome/chromedriver.exe" #chromedriver.exe執行檔所存在的路徑
web = webdriver.Chrome(chrome_path)
newweb=webdriver.Chrome(chrome_path)
web.get(a1)
newweb.get(youtube_playlist)
js='window.open("youtubeurl1");'
web.execute_script(js)

print (web.current_window_handle) # 输出当前窗口句柄（百度）
handles = web.window_handles # 获取当前窗口句柄集合（列表类型）
print (handles) # 输出句柄集合

for handle in handles:# 切换窗口（切换到搜狗）
    if handle!=web.current_window_handle:
        print ('switch to ',handle)
        web.switch_to_window(handle)
        print (web.current_window_handle) # 输出当前窗口句柄（搜狗）
        break


#关闭当前窗口（搜狗）
# web.switch_to_window(handles[0]) #切换回百度窗口

# web.set_window_position(0,0) #瀏覽器位置
# web.set_window_size(5000,5000) #瀏覽器大小
# newweb.set_window_size(10,10) #瀏覽器大小


# web.find_element_by_link_text('天氣預報').click() #點擊頁面上"天氣預報"的連結
# time.sleep(5)

# web.close()
		# 不重複的網頁
# https://www.youtube.com/watch?v=

# import mpv
# player = mpv.MPV(ytdl=True)
# player.play('https://youtu.be/DOmdB7D-pUU')

# import time
# words = ""
# for item in words.split():
#     print('\n'.join([''.join([(item[(x-y) % len(item)] 
#     if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') 
#     for x in range(-30, 30)]) 
#     for y in range(12, -12, -1)]))
#     time.sleep(1.5);
	
	# word = jieba.cut(user_content[count].text.strip(),cut_all=False)
	
	# cut_word.append("/".join(word).strip());
	# print(cut_word);
	#去頭去尾換行之類的字符
	# print ("/".join(word))#結疤段詞	
	# print(user_tag[count].text)
	
	# print("==========================================================================")




 
# print ('word_len{%d}' % len(list(cut_word)))
# jieba_extract=[]
# for cut_word in cut_word:
# 	keywords = jieba.analyse.extract_tags(cut_word, topK=20, withWeight=True, allowPOS=())
# 	# 访问提取结果
# 	for item in keywords:
# 	    # 分别为关键词和相应的权重
# 	    print (item[0],item[1])
# 	    jieba_extract.append(item[0])
# 	    print("====================")
	    
	    # print('keyword{%d}'%len(list(keywords)))
		
	 
	# 同样是四个参数，但allowPOS默认为('ns', 'n', 'vn', 'v')
	# 即仅提取地名、名词、动名词、动词
	# keywords = jieba.analyse.textrank(cut_word, topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v'))
	# # 访问提取结果
	# for item in keywords:
	#     # 分别为关键词和相应的权重
	#     print (item[0], item[1]);
	    
	#     print("1==================="+cut_word)
	#     # print('1keyword{%d}'%len(list(keywords)))

				
# from sklearn.feature_extraction import DictVectorizer #用於轉換 dict 為 sklearn estimators 可用的向量
# from sklearn.feature_extraction.text import TfidfTransformer #將矩陣轉換為 TF 或 TF-IDF 表示
# from collections import defaultdict #使用 dict 儲存資料


# 				# convert to vectors
# c_dvec = DictVectorizer()
# c_tfidf = TfidfTransformer()
# c_vector = c_dvec.fit_transform(jieba_extract)
# c_X = c_tfidf.fit_transform(c_vector) #將一千篇所有鄉民留言的斷詞文字矩陣轉成向量並計算tf-idf
#分類留言的情緒
 # get pushes

# build and train the classifier
