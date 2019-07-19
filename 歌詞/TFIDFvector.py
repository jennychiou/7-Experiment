import numpy as np
import nltk
import math
import string
from scipy.linalg import norm
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.porter import *
from gensim.models import TfidfModel
from gensim.models.word2vec import Word2Vec
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

##def tfidf_similarity(s1, s2):
##    def add_space(s):
##        return ' '.join(list(s))
##
##    # 將字中間加入空格
##    s1, s2 = add_space(s1), add_space(s2)
##    # 轉化為TF矩陣
##    cv = TfidfVectorizer(tokenizer=lambda s: s.split())
##    corpus = [s1, s2]
##    print(corpus)
##    vectors = cv.fit_transform(corpus).toarray()
##    print('向量：','\n',vectors)
##    # 計算TF係數
##    return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))
##
##s1 = '你在幹嘛呢'
##s2 = '你在幹什麼呢'
##print('相似度：',tfidf_similarity(s1, s2))

#教學：https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/363018/

##nltk.download('punkt')
##nltk.download('stopwords')

text1 = ""
text2 = "I drove by all the places we used to hang out getting wasted\nI thought about our last kiss, how it felt the way you tasted\nAnd even though your friends tell me you|re doing fineAre you somewhere feeling lonely even though he|s right beside you?\nWhen he says those words that hurt you, do you read the ones I wrote you?Sometimes I start to wonder, was it just a lie?\nIf what we had was real, how could you be fine?|Cause I|m not fine at allI remember the day you told me you were leaving\nI remember the make-up running down your face\nAnd the dreams you left behind you didn|t need them\nLike every single wish we ever made\nI wish that I could wake up with amnesia\nAnd forget about the stupid little things\nLike the way it felt to fall asleep next to you\nAnd the memories I never can escape|Cause I|m not fine at allThe pictures that you sent me they|re still living in my phone\nI|ll admit I like to see them, I|ll admit I feel alone\nAnd all my friends keep asking why I|m not aroundIt hurts to know you|re happy, yeah, it hurts that you|ve moved on\nIt|s hard to hear your name when I haven|t seen you in so longIt|s like we never happened, was it just a lie?\nIf what we had was real, how could you be fine?|Cause I|m not fine at allI remember the day you told me you were leaving\nI remember the make-up running down your face\nAnd the dreams you left behind you didn|t need them\nLike every single wish we ever made\nI wish that I could wake up with amnesia\nAnd forget about the stupid little things\nLike the way it felt to fall asleep next to you\nAnd the memories I never can escapeIf today I woke up with you right beside me\nLike all of this was just some twisted dream\nI|d hold you closer than I ever did before\nAnd you|d never slip away\nAnd you|d never hear me sayI remember the day you told me you were leaving\nI remember the make-up running down your face\nAnd the dreams you left behind you didn|t need them\nLike every single wish we ever made\nI wish that I could wake up with amnesia\nAnd forget about the stupid little things\nLike the way it felt to fall asleep next to you\nAnd the memories I never can escape\n|Cause I|m not fine at all\nNo, I|m really not fine at all\nTell me this is just a dream\n|Cause I|m really not fine at all"
text3 = "I though we had a place, just our place, our home place, my headspace\nWas you and I always, but that phase has been phased in our place\nI see it on your face, a small trace, a blank slate, we been erased\nBut if we|re way too faded to drive, you can stay one more nightWe said we|d both love higher than we knew we could go\nBut still the hardest part is knowing when to let go\nYou wanted to go higher, higher, higher\nBurn too bright, now the fire|s gone, watch it all fall down, BabylonBabylon\nBurn too bright, now the fire|s gone, watch it all fall downI|m tired of the feud, your short fuse, my half turths are not amused\nI wish we had a clue to start new, a white moon, no residue\nThe color of our mood is so rude, a cold June, we|re not immune\nBut if we|re way too faded to fight, you can stay one more nightWe said we|d both love higher than we knew we could go\nBut still the hardest part is knowing when to let go\nYou wanted to go higher, higher, higher\nBurn too bright, now the fire|s gone, watch it all fall down, BabylonBabylon\nBurn too bright, now the fire|s gone, watch it all fall downWe said we|d both love higher than we knew we could go\nBut still the hardest part is knowing when to let go\nYou wanted to go higher, higher, higher\nBurn too bright, now the fire|s gone, watch it all fall down\nWe said we|d both love higher than we knew we could go\nBut still the hardest part is knowing when to let go\nYou wanted to go higher, higher, higher\nBurn too bright, now the fire|s gone, watch it all fall down, BabylonBabylon\nBurn too bright, now the fire|s gone, watch it all fall down"

#分詞
def get_tokens(text):
    lowers = text.lower()
    #remove the punctuation using the character deletion step of translate
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    no_punctuation = lowers.translate(remove_punctuation_map)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens

#過濾缺乏實際意義的 the, a, and 等詞
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

tokens1 = get_tokens(text1)
tokens2 = get_tokens(text2)
tokens3 = get_tokens(text3)

filtered1 = [w for w in tokens1 if not w in stopwords.words('english')]
filtered2 = [w for w in tokens2 if not w in stopwords.words('english')]
filtered3 = [w for w in tokens3 if not w in stopwords.words('english')]

print('未過濾')
count1_1 = Counter(tokens1) #未過濾
count2_1 = Counter(tokens2) #未過濾
count3_1 = Counter(tokens3) #未過濾
print ('count1_1：',count1_1.most_common(10))
print ('count2_1：',count2_1.most_common(10))
print ('count3_1：',count3_1.most_common(10))

#Counter() 函式用於統計每個單詞出現的次數。
print('已過濾(停用詞)')
count1_2 = Counter(filtered1) #已過濾
count2_2 = Counter(filtered2) #已過濾
count3_2 = Counter(filtered3) #已過濾
print ('count1_2：',count1_2.most_common(10))
print ('count2_2：',count2_2.most_common(10))
print ('count3_2：',count3_2.most_common(10))

stemmer = PorterStemmer()
stemmed1 = stem_tokens(filtered1, stemmer)
stemmed2 = stem_tokens(filtered2, stemmer)
stemmed3 = stem_tokens(filtered3, stemmer)

print('已過濾(保留字根)')
count1_3= Counter(stemmed1)
print('count1-3：',count1_3.most_common(30))
count2_3= Counter(stemmed2)
print('count2-3：',count2_3.most_common(30))
count3_3= Counter(stemmed3)
print('count3-3：',count3_3.most_common(30))

#計算 TF-IDF(t)=TF(t)×IDF(t)
#教學：https://stackabuse.com/implementing-word2vec-with-gensim-library-in-python/
def tf(word, count):
    return count[word] / sum(count.values())

def n_containing(word, count_list):
    return sum(1 for count in count_list if word in count)

def idf(word, count_list):
    return math.log(len(count_list) / (1+n_containing(word, count_list)))

def tfidf(word, count, count_list):
    return tf(word, count) * idf(word, count_list)

countlist = [count1_2, count2_2, count3_2]
for i, count in enumerate(countlist):
    print('------------------------------------------')
    print("Top words in document {}".format(i+1))
    scores = {word: tfidf(word, count, countlist) for word in count}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:10]:
        print("Word: {}, TF-IDF: {}".format(word, round(score, 5)))

##print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
##
##text = "I buy a new car for the bitch (for real)\nI tear down the mall with the bitch (for real)\nYou can|t even talk to the bitch (no)\nShe fucking with bosses and shit (oh God)\nI pull up in |rari|s and shit, with choppers and Harley|s and shit (for real)\nI be Gucci|d down, you wearing Lacoste and shit (bitch)\nYeah, Moncler, yeah, fur came off of that, yeah (yeah)\nTriple homicide, put me in a chair, yeah (in jail)\nTriple cross the plug, we do not play fair, yeah (Oh god)\nGot |em tennis chains on and they real blingy (blingy)\nDraco make you do the chicken head like Chingy (Chingy)\nWalk in Neiman Marcus and I spend a light fifty (fifty)\nPlease proceed with caution, shooters, they be right with me (21)\nBad bitch, cute face and some nice titties\n$7500 on a Saint Laurent jacket (yeah)\nBitch, be careful where you dumpin| your ashes (bitch)\nI ain|t no sucker, I ain|t cut for no action (nah)\nThe skreets raised me, I|m a ho bastard (wild, wild, wild, wild)\nI bought a |Rari just so I can go faster (skrrt)\nNiggas tryna copy me, they playin| catch up (21)\nI might pull up in a Ghost, no Casper (21)\nI been smoking gas and I got no asthmaI got 1-2-3-4-5-6-7-8 M|s in my bank account, yeah (Oh, God)\nIn my bank account, yeah (Oh God)\nIn my bank account, yeah (Oh God)\nIn my bank account, yeah (Oh God)\nIn my bank account, yeah (Oh God)\nIn my bank account, yeah (Oh God)\nI got 1-2-3-4-5-6-7-8 shooters ready to gun you down, yeah (fast)\nReady to gun you down, yeah (Oh God)\nReady to gun you down, yeah (Oh God)\nReady to gun you down, yeah (Oh God)\nReady to gun you down, yeah (Oh God)\nReady to gun you down, yeah (Oh God)Yeah dog I|m for real, dog (21)\nRegular, buy the seats, I got a house on the hill, dog (21)\nWanna see a body, nigga? Get you killed, dog (wet)\nWanna Tweet about me, nigga? Get you killed, dog (wet)\nKilled dog, I|m a real dog, you a lil| dog (21)\nBe a dog, wanna be a dog, chasing mil|s, dog\nDunk right in your bitch like O|Neal, dog\nI shoot like Reggie Mill|, dog (21)\nChopper sting you like a eel, dogI got 1-2-3-4-5-6-7-8 M|s in my bank account, yeah (Oh, God)\nIn my bank account, yeah (Oh God)\nIn my bank account, yeah (Oh God)\nIn my bank account, yeah (Oh God)\nIn my bank account, yeah (Oh God)\nIn my bank account, yeah (Oh God)\nI got 1-2-3-4-5-6-7-8 shooters ready to gun you down, yeah (fast)\nReady to gun you down, yeah (Oh God)\nReady to gun you down, yeah (Oh God)\nReady to gun you down, yeah (Oh God)\nReady to gun you down, yeah (Oh God)\nReady to gun you down, yeah (Oh God)Roulette clips, send a roulette hit\nPull up on your bitch, she say I got that ruler dick\nSpray your block down, we not really with that rural shit\nGlock cocked now, I don|t really give no fuck |bout who I hit\nYeah, your bitch, she get jiggy with me\nKeep that Siggy with me\nBitch, I|m Mad Max, you know I got Ziggy with me\nKeep a mad mag in case they wanna get busy with me\n|Rari matte black and I got a Bentley with meI got 1-2-3-4-5-6-7-8 M|s in my bank account, yeah (Oh, God)\nIn my bank account, yeah (Oh God)\nIn my bank account, yeah (Oh God)\nIn my bank account, yeah (Oh God)\nIn my bank account, yeah (Oh God)\nIn my bank account, yeah (Oh God)\nI got 1-2-3-4-5-6-7-8 shooters ready to gun you down, yeah (fast)\nReady to gun you down, yeah (Oh God)\nReady to gun you down, yeah (Oh God)\nReady to gun you down, yeah (Oh God)\nReady to gun you down, yeah (Oh God)\nReady to gun you down, yeah (Oh God)$7500 on a Saint Laurent jacket (yeah)\nBitch, be careful where you dumpin| your ashes (bitch)\nI ain|t no sucker, I ain|t cut for no action (nah)\nThe skreets raised me, I|m a ho bastard"
##tokens1 = get_tokens(text)
##filtered1 = [w for w in tokens1 if not w in stopwords.words('english')]
##print(filtered1)
##
#CountVectorizer是透過fit_transform函數將文本中的詞語轉換為詞頻矩陣
#矩陣元素a[i][j] 表示j詞在第i個文本下的詞頻，即各个詞語出現的次數。
#透過get_feature_names()可看到所有文本的關鍵字
#透過toarray()可看到詞頻矩陣的結果。
##cv = CountVectorizer(max_df=0.85)
##word_count_vector =cv.fit_transform(filtered1)
##word_count_array =word_count_vector.toarray()
##word_count_names =cv.get_feature_names()
##print(word_count_vector.shape,'\n')
##print(word_count_array,'\n')
##print(word_count_names,'\n')
##print(list(cv.vocabulary_.keys())[:30])
##
###TfidfTransformer統計vectorizer中每個詞語的tf-idf權重值
##tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
##tfidf_transformer.fit(word_count_vector)
##print(tfidf_transformer.idf_)
