import syllables
import re

punc = '[,.!\'?]'
##text = "Tale as old as time True as it can be Barely even friends then somebody bends unexpcetedly"
##text = "Every night in my dreams I see you, I feel you, That is how I know you go on Far across the distance And spaces between us You have come to show you go on Near, far, wherever you are I believe that the heart does go on Once more you open the door And you're here in my heart And my heart will go on and on"
##text = "I can show you the world Shining, shimmering, splendid Tell me, princess Now when did you last let your heart decide? I can open your eyes Take you wonder by wonder Over, sideways, and under On a magic carpet ride"
text = "Row, row, row your boat Gently down the stream Merrily merrily, merrily, merrily Life is but a dream"
text_re = re.sub(punc,'',text)
print(text_re)

#另外寫法
##replace = ','
##if "," in text:
##    print('contains',replace,'!')
##    print()
##text_re = text.replace(replace,'')
##print(text_re)
##

a = text_re.split()
##print(a)
for i in range (0,len(a)):
    word = a[i]
    count = syllables.estimate(a[i])
    msg = 'Word : {:>2}  |  Count : {}'.format(word, count)
    print(msg)
