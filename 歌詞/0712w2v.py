from __future__ import print_function
import six
from gensim.corpora import WikiCorpus

if __name__ == '__main__':
    inp = "../enwiki-latest-pages-articles1.xml-p10p30302.bz2"
    outp = "../out_wiki.en.txt"
    space = " "
    i = 0

    output = open(outp, 'w', encoding="utf-8")
    wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        if(i % 1000 == 0):
            print(i)
        if six.PY3:
            output.write(' '.join(text) + '\n')
        else:
            output.write(space.join(text) + "\n")
        i = i + 1
    output.close()
