import os
import pandas as pd
from metrics import unique_ngrams_ratio, normal_inver_diver, word_sent_count

# Avg. doc/summary length Metrics
def open_src_count(path):
  filelist = os.listdir(path)
  result_all = pd.DataFrame(columns = ['doc_sents',
                                      'doc_words',
                                      'summ_sents',
                                      'summ_words'])

  for file in filelist:
    if file.endswith(".story"): 
      file_path = f"{path}\{file}"
      with open(file_path, 'r', encoding="utf8") as f:
        text = f.read()
        text = text.lower()

        doc = text.split('@highlight')[0]
        summ = text.split('@highlight')[1:len(text.split('@highlight'))]
        summary = ''
        summary = summary.join(summ)

        doc_sents, doc_words = word_sent_count(doc)
        summ_sents, summ_words = word_sent_count(summary)
        result_doc = pd.DataFrame([[doc_sents, doc_words, summ_sents, summ_words]], 
                                  columns=['doc_sents',
                                      'doc_words',
                                      'summ_sents',
                                      'summ_words'])
        result_all = pd.concat([result_all, result_doc])

  result_mean = result_all.mean(axis=0)

  return result_mean, len(filelist), result_all

# Redundancy Metrics
def open_src_redun(path):
  filelist = os.listdir(path)
  result_all = pd.DataFrame(columns = ['unique_unigram',
                                      'unique_bigram',
                                      'unique_trigram',
                                      'nid'])

  for file in filelist:
    if file.endswith(".story"): 
      file_path = f"{path}\{file}"
      with open(file_path, 'r', encoding="utf8") as f:
        text = f.read()
        text = text.lower()
        src = text.split('@highlight')[0]

        # Unique ngrams ratio
        uniq_unigram = unique_ngrams_ratio(src, 1)
        uniq_bigram = unique_ngrams_ratio(src, 2)
        uniq_trigram = unique_ngrams_ratio(src, 3)

        #NID
        nid = normal_inver_diver(src)

        result_doc = pd.DataFrame([[uniq_unigram, uniq_bigram, uniq_trigram, nid]],
                                  columns=['unique_unigram',
                                      'unique_bigram',
                                      'unique_trigram',
                                      'nid'])
        result_all = pd.concat([result_all, result_doc])

  result_mean = result_all.mean(axis=0)

  return result_mean, len(filelist), result_all

