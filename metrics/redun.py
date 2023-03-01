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
  uniq_ngram_list = []

  for sent in text_sent:
    # Word tokenize with removing stopwords: punctuations
    stoplist = set(list(punctuation)) #( + stopwords.words('english') )
    tokens = [token for token in word_tokenize(sent) if token not in stoplist]

    ngram = ngrams(tokens, n)
    ngram_list = []

    for grams in ngram:
      ngram_list.append(grams) 

    print("\nN-grams: ")
    print(ngram_list)

    if(len(ngram_list) > 0):
      print("Count ngram: ", len(ngram_list))
      print("Count Unique n-grams: ", len(np.unique(np.array(ngram_list), axis=0)))

      uniq_ng_ratio = len(np.unique(np.array(ngram_list), axis=0)) / len(ngram_list)
      uniq_ngram_list.append(uniq_ng_ratio)

  if(len(uniq_ngram_list) > 0):
    mean_uniq = sum(uniq_ngram_list)/len(uniq_ngram_list)
    return mean_uniq
  else:
    return 0


def normal_inver_diver(text):
  text_sent = sent_tokenize(text) #split sentence
  diversity_list = []

  for sent in text_sent:
    unigram = ngrams(word_tokenize(sent), 1)
    unigram_list = []

    for grams in unigram:
      unigram_list.append(grams)

    # Calculate diversity of unigrams
    counts_dict = Counter(unigram_list)
    counts = np.array(list(counts_dict.values())) 
    prob = counts/len(unigram_list)

    diversity = entropy(prob)    
    diversity_list.append(diversity)

    #print("Diversity: ", diversity)
    #print("len(unigram_list): ", len(unigram_list))
    #print("Diversity: ", diversity)
    # It's supported assumption: The longer document (or sentence), the higher entropy (diversity) 

  #print("sum(diversity_list): ", sum(diversity_list))

  # nid = 1 - (avg(diversity) / log(sum(diversity)))
  nid = 1 - ((sum(diversity_list)/len(diversity_list))/(np.log(sum(diversity_list))))

  return nid


