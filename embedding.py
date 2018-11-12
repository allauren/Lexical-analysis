import gzip
import gensim
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def read_input(input_file):
    """This method reads the input file which is in gzip format"""

    logging.info("reading file {0}...this may take a while".format(input_file))
    with gzip.open(input_file, 'rb') as f:
        for i, line in enumerate(f):

            if (i % 10000 == 0):
                logging.info("read {0} reviews".format(i))
            yield gensim.utils.simple_preprocess(line)


input_file = 'reviews_data.txt.gz'
documents = list (read_input (input_file))
logging.info ("Done reading data file")
model = gensim.models.Word2Vec (documents, size=150, window=10, min_count=100, workers=10)
model.train(documents,total_examples=len(documents),epochs=10)
model.save("word2vec100.model")