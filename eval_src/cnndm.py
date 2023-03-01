import os
import sys

sys.path.insert(0, 'metrics')

from redun import unique_ngrams_ratio, normal_inver_diver

def cnndm_redun(path):
  filelist = os.listdir(path)
  uniq_unigram_list = []
  uniq_bigram_list = []
  uniq_trigram_list = []
  nid_list = []
  print("Number of file: ", len(filelist))

  for file in filelist:
    if file.endswith(".story"): 
      file_path = f"{path}\{file}"
      with open(file_path, 'r', encoding="utf8") as f:
        text = f.read()
        text = text.lower()

        src = text.split('@highlight')[0]
        # sum = text.split('@highlight')[1:len(text.split('@highlight'))]
        # summary = ''
        # summary = summary.join(sum)

        # Unique ngrams ratio
        uniq_unigram = unique_ngrams_ratio(src, 1)
        uniq_bigram = unique_ngrams_ratio(src, 2)
        uniq_trigram = unique_ngrams_ratio(src, 3)
        uniq_unigram_list.append(uniq_unigram)
        uniq_bigram_list.append(uniq_bigram)
        uniq_trigram_list.append(uniq_trigram)
        # print("uniq_unigram: ", uniq_unigram)
        # print("uniq_bigram: ", uniq_bigram)
        # print("uniq_trigram: ", uniq_trigram)

        #NID
        nid = normal_inver_diver(src)
        nid_list.append(nid)
        # print("NID: ", nid)

  mean_uniq_unigram = sum(uniq_unigram_list)/len(uniq_unigram_list)
  mean_uniq_bigram = sum(uniq_bigram_list)/len(uniq_bigram_list)
  mean_uniq_trigram = sum(uniq_trigram_list)/len(uniq_trigram_list)
  mean_nid = sum(nid_list)/len(nid_list)

  return mean_uniq_unigram, mean_uniq_bigram, mean_uniq_trigram, mean_nid, len(filelist)

def cnndm_sum(cnn_path, dm_path):
  cnn_uni, cnn_bi, cnn_tri, cnn_nid, cnn_count = cnndm_redun(cnn_path)
  dm_uni, dm_bi, dm_tri, dm_nid, dm_count = cnndm_redun(dm_path)

  total_doc = cnn_count + dm_count
  uniq_uni = (cnn_uni+dm_uni)/total_doc
  uniq_bi = (cnn_bi+dm_bi)/total_doc
  uniq_tri = (cnn_tri+dm_tri)/total_doc
  nid = (cnn_nid+dm_nid)/total_doc

  return uniq_uni, uniq_bi, uniq_tri, nid, total_doc


cnn_path = r"raw_data\cnndm\cnn_stories\stories"
dm_path = r"raw_data\cnndm\dailymail_stories\stories"

uniq_uni, uniq_bi, uniq_tri, nid, total_doc = cnndm_sum(cnn_path, dm_path)

