# imports needed and logging
import gzip
import gensim 
import logging
import sys 
from gensim.models import Word2Vec

def read_input(input_file):
    logging.info("reading file {0}...this may take a while".format(input_file))
    with gzip.open(input_file, 'rb') as f:
        for i, line in enumerate(f):
            if (i % 10000 == 0):
                logging.info("read {0} reviews".format(i))
            # do some pre-processing and return list of words for each review
            # text
            yield gensim.utils.simple_preprocess(line)

def main():
#    documents = list(read_input(sys.argv[1]))
    
    # build vocabulary and train model
#    print("Beginning to train model\n")
#    model = gensim.models.Word2Vec(
#        documents,
#        size=150,
#        window=10,
#        min_count=2,
#        workers=10)
#    model.train(documents, total_examples=len(documents), epochs=10)
#    model.save("word2vec.model")
    model = Word2Vec.load("word2vec.model")
    w1 = "nice"
    print(model.wv.most_similar(positive=w1))

if __name__ == "__main__":
    main()
