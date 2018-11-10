from graphics import *

def main():
    win = GraphWin("My Circle", 1000, 1000)
    c = Point(500,500)
    c.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
print(value)

vocab = list(model.wv.vocab)
X = model[vocab]
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X)
df = pd.DataFrame(X_tsne, index=vocab, columns=['x', 'y'])
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.scatter(df['x'], df['y'])
for word, pos in df.iterrows():
    ax.annotate(word, pos)
plt.show()