import gensim
import matplotlib.pyplot as plt
import math
from sklearn.manifold import TSNE
import numpy as np
import matplotlib.pyplot as plt

def closestwords_tsnescatterplot(model, words, num, state):
    word_presents = []
    word_labels = []
    list = []
    for wrd in words :
        if wrd in model.wv.vocab :
            word_presents.append(wrd)
    close_words = model.wv.most_similar(positive=word_presents, topn=num)

    for wrd_score in close_words:
        wrd_vector = np.array(model.wv[wrd_score[0]])
        word_labels.append(wrd_score[0])
        list.append(wrd_vector)

    for wrd_score in word_presents:
        wrd_vector = model.wv[wrd_score]
        word_labels.append(wrd_score)
        list.append(wrd_vector)

    arr = np.array(list)

    tsne = TSNE(n_components=2, random_state=0)
    np.set_printoptions(suppress=True)
    Y = tsne.fit_transform(arr)

    x_coords = Y[:, 0]
    y_coords = Y[:, 1]
    plt.scatter(x_coords, y_coords)

    for label, x, y in zip(word_labels, x_coords, y_coords) :
        plt.annotate(label, xy=(x, y), xytext=(-5, 5), textcoords='offset points')
    plt.xlim(x_coords.min() + 20.00005, x_coords.max() + 20.00005)
    plt.ylim(y_coords.min() + 20.00005, y_coords.max() + 20.00005)
    plt.scatter(0, 0)
    plt.title(state)
    return word_labels


