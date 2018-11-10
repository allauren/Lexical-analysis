import gensim
import matplotlib.pyplot as plt
import math
from sklearn.manifold import TSNE
import numpy as np
import matplotlib.pyplot as plt

model = gensim.models.Word2Vec.load("word2vec.model")
model['beautiful']
value = model.wv.most_similar (positive=['beautiful'], topn=10)
arr = []
word_labels = []
i = 0
for wrd_score in value:
    wrd_vector = model[wrd_score[0]]
    print(wrd_vector)
    word_labels.append(wrd_score[0])
    arr.append(np.array([wrd_vector]))
# find tsne coords for 2 dimensions
tsne = TSNE(n_components=2, random_state=0)
np.set_printoptions(suppress=True)
Y = tsne.fit_transform(arr)

x_coords = Y[:, 0]
y_coords = Y[:, 1]
# display scatter plot
plt.scatter(x_coords, y_coords)

for label, x, y in zip(word_labels, x_coords, y_coords):
    plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')
plt.xlim(x_coords.min() + 0.00005, x_coords.max() + 0.00005)
plt.ylim(y_coords.min() + 0.00005, y_coords.max() + 0.00005)
plt.show()
print(value)

