import syllables
text = "Tale as old as time True as it can be Barely even friends then somebody bends unexpcetedly"
a = text.split()
##print(a)
for i in range (0,len(a)):
    word = a[i]
    count = syllables.estimate(a[i])
    msg = 'Word : {:>2}  |  Count : {}'.format(word, count)
    print(msg)
