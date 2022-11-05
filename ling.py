from pymystem3 import Mystem
import pymorphy2
import nltk as nltk
import string
from nltk.corpus import stopwords
from stop_words import get_stop_words
import jsonlines
from nltk.probability import FreqDist


m = Mystem()
morph = pymorphy2.MorphAnalyzer()
res = open('res.txt', 'w', encoding='utf-8')
stop_words = list(get_stop_words('ru'))
spec_chars = string.punctuation + '\n\xa0«»\t—…'

'''sw = open('stopwords.txt', 'w', encoding='utf-8')
for word in stop_words:
    sw.write(word)
    sw.write('\n')'''


def write_in_file(name):
    with open("stopwords.txt", encoding="utf-8") as sw, open(name, encoding="utf-8") as f, open("new.txt", "w",
                                                                                        encoding="utf-8") as no_sw:
        stopwords = sw.readlines()
        no_sw.writelines(line + "\n" for line in f.readlines() if line not in stopwords)

    no_sw = open('new.txt', 'r', encoding='utf-8')
    no_sw = "".join([ch for ch in no_sw if ch not in spec_chars])

    lemmas = m.lemmatize(no_sw)

    res.writelines(lemmas)
    return res


write_in_file('my.txt')
write_in_file('1984.txt')
write_in_file('farm.txt')
write_in_file('world.txt')
write_in_file('ulitka.txt')
