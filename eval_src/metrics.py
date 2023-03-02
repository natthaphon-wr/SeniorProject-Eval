import os
import nltk
import numpy as np
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
from scipy.stats import entropy
from string import punctuation

def word_sent_count(text):
  # Count sentences
  sentences = sent_tokenize(text)
  sent_count = len(sentences)
  
  # Count words
  stoplist = set(list(punctuation))
  words = [token for token in word_tokenize(text) if token not in stoplist]
  word_count = len(words)

  return sent_count, word_count

def unique_ngrams_ratio(text, n):
  text_sent = sent_tokenize(text) #split sentence
  ngram_list = []

  for sent in text_sent:
    # Word tokenize with removing stopwords: punctuations (+stopwords.words('english'))
    stoplist = set(list(punctuation))
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
    # Word tokenize with removing stopwords: punctuations (+stopwords.words('english'))
    stoplist = set(list(punctuation))
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

    # Calculate NID
    nid = 1- diversity / np.log(len(unigram_list))
    return nid

  else:
    return 0

