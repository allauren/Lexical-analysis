import gensim
import matplotlib.pyplot as plt
import math
from sklearn.manifold import TSNE
import numpy as np
import matplotlib.pyplot as plt

model = gensim.models.Word2Vec.load("word2vec.model")
value = model.wv.most_similar (positive=['beautiful'], topn=10)
#print(model.wv['computer'])
#print(value)


def display_closestwords_tsnescatterplot(model, word):
    word_labels = [word]
    print()
    close_words = model.wv.most_similar (positive=['beautiful'], topn=40)

    arr = [model.wv[word]]
    for wrd_score in close_words:
        wrd_vector = model.wv[wrd_score[0]]
        word_labels.append(wrd_score[0])
        arr = np.append(arr, [wrd_vector], axis=0)

    tsne = TSNE(n_components=2, random_state=0)
    np.set_printoptions(suppress=True)
    Y = tsne.fit_transform(arr)

    x_coords = Y[:, 0]
    y_coords = Y[:, 1]
    plt.scatter(x_coords, y_coords)

    for label, x, y in zip(word_labels, x_coords, y_coords):
        plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')
    plt.xlim(x_coords.min() + 0.00005, x_coords.max() + 0.00005)
    plt.ylim(y_coords.min() + 0.00005, y_coords.max() + 0.00005)

display_closestwords_tsnescatterplot(model, 'nice')
display_closestwords_tsnescatterplot(model, 'effective')

plt.show()
