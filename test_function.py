import os
import nltk
import numpy as np
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize, word_tokenize

from metrics.redun import unique_ngrams_ratio, normal_inver_diver


cnn_path = r"raw_data\cnndm\cnn_stories\stories"
file_path = f"{cnn_path}/0ec4fb22f189f34e80f4e78812d04f0b40c9c57b.story"

with open(file_path, 'r') as f:
    text = f.read()
    text = text.lower()
    src = text.split('@highlight')[0]

    # uniq_unigram = unique_ngrams_ratio(src, 1)
    # uniq_bigram = unique_ngrams_ratio(src, 2)
    # uniq_trigram = unique_ngrams_ratio(src, 3)
    # print("\nUnique unigram ratio: ", uniq_unigram)
    # print("Unique bigram ratio: ", uniq_bigram)
    # print("Unique trigram ratio: ", uniq_trigram)

    nid = normal_inver_diver(src)
    print("NID: ", nid)
