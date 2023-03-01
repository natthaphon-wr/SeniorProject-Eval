import os
import nltk
import numpy as np
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
from scipy.stats import entropy
from string import punctuation


def unique_ngrams_ratio(text, n):
  text_sent = sent_tokenize(text) #split sentence
  ngram_list = []

  for sent in text_sent:
    # Word tokenize with removing stopwords: punctuations
    stoplist = set(list(punctuation)) #( + stopwords.words('english') )
    tokens = [token for token in word_tokenize(sent) if token not in stoplist]

    ngram = ngrams(tokens, n)
    for grams in ngram:
      ngram_list.append(grams) 

  if(len(ngram_list) > 0):
    uniq_ng_ratio = len(np.unique(np.array(ngram_list), axis=0)) / len(ngram_list)
    return uniq_ng_ratio
  else:
    return 0


def normal_inver_diver(text):
  text_sent = sent_tokenize(text) #split sentence
  unigram_list = []

  for sent in text_sent:
    # Word tokenize with removing stopwords: punctuations
    stoplist = set(list(punctuation)) #( + stopwords.words('english') )
    tokens = [token for token in word_tokenize(sent) if token not in stoplist]

    unigram = ngrams(tokens, 1)
    for grams in unigram:
      unigram_list.append(grams)

  if len(unigram_list) > 0:
    # Calculate diversity of unigrams of document
    counts_dict = Counter(unigram_list)
    counts = np.array(list(counts_dict.values())) 
    prob = counts/len(unigram_list)
    diversity = entropy(prob)    

    # # Calculate nid (assumption that D in equation is Diversity)
    # nid = 1 - diversity / np.log(np.abs(diversity))
    # print("nid: ", nid)

    # # Calculate nid (assumption that D in equation is Document, abs(d) = no. of sentence)
    # nid2 = 1- diversity / np.log(len(text_sent))
    # print("nid2: ", nid2)

    # Calculate nid (assumption that D in equation is Document, abs(d) = no. of unigram)
    nid3 = 1- diversity / np.log(len(unigram_list))
    print("nid3: ", nid3)

    return nid3

  else:
    return 0

  



  

