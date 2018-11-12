import gensim
import matplotlib.pyplot as plt
import math
from sklearn.manifold import TSNE
import numpy as np
import matplotlib.pyplot as plt
from closest_words import closestwords_tsnescatterplot
from find_in_doc import check_words
import sys

def draw_plt(nummodel, personnality):
    wordlist1 = ['acceptance', 'broad-mindedness', 'impartiality','interest','observ', 'receptive', 'responsive', 'tolerant','understand']
    wordlist2 = ['ambitious', 'gentle', 'nice', 'bad', 'sad', 'new']
    wordlist3 = ['new', 'classy']
    wordlist4 = ['sad', 'christic']
    wordlist5 = ['woman', 'man']

    models = ['word2vec100.model', 'word2vec.model']

    person5 =[wordlist1, wordlist2, wordlist3, wordlist4, wordlist5]
    model = gensim.models.Word2Vec.load(models[nummodel])
    to_find = closestwords_tsnescatterplot(model, person5[personnality], 30, 'conscienscoutness')
    plt.savefig('haha.png')
    check_words('./letter.docx', to_find)

if __name__ == '__main__':
    print (sys.argv)
    if len(sys.argv) < 3 :
        print ('please put a model and a personallity trait')
    draw_plt(int(sys.argv[1]), int(sys.argv[2]))
