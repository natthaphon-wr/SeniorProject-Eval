import os
from metrics import unique_ngrams_ratio, normal_inver_diver, word_sent_count

# Avg. doc/summary length Metrics
def open_src_count(path):
  filelist = os.listdir(path)
  doc_sents_list = []
  doc_words_list = []
  summ_sents_list = []
  summ_words_list = []

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
        doc_sents_list.append(doc_sents)
        doc_words_list.append(doc_words)
        summ_sents_list.append(summ_sents)
        summ_words_list.append(summ_words)

  result_dict = {'mean_doc_sents': sum(doc_sents_list)/len(doc_sents_list),
                 'mean_doc_words': sum(doc_words_list)/len(doc_words_list),
                 'mean_summ_sents': sum(summ_sents_list)/len(summ_sents_list),
                 'mean_summ_words': sum(summ_words_list)/len(summ_words_list)}

  return result_dict, len(filelist)

# Redundancy Metrics
def open_src_redun(path):
  filelist = os.listdir(path)
  uniq_unigram_list = []
  uniq_bigram_list = []
  uniq_trigram_list = []
  nid_list = []
  # print("Number of file: ", len(filelist))

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
        uniq_unigram_list.append(uniq_unigram)
        uniq_bigram_list.append(uniq_bigram)
        uniq_trigram_list.append(uniq_trigram)
        # print("Unique 1/2/3 grams: ", uniq_unigram, " ", uniq_bigram, " ", uniq_trigram)

        #NID
        nid = normal_inver_diver(src)
        nid_list.append(nid)
        # print("NID: ", nid)

  result_dict = {'mean_uniq_unigram': sum(uniq_unigram_list)/len(uniq_unigram_list),
                 'mean_uniq_bigram': sum(uniq_bigram_list)/len(uniq_bigram_list),
                 'mean_uniq_trigram': sum(uniq_trigram_list)/len(uniq_trigram_list),
                 'mean_nid': sum(nid_list)/len(nid_list)}

  return result_dict, len(filelist)

# Include cnn/dm and bbc/eest to CNNDM and Finance
def sum_result(path1, path2, redun_metric):
  if redun_metric:
    dict1, count1 = open_src_redun(path1)
    dict2, count2 = open_src_redun(path2)
    total_doc = count1 + count2
  else:
    dict1, count1 = open_src_count(path1)
    dict2, count2 = open_src_count(path2)
    total_doc = count1 + count2
  
  dict_result = {}
  if list(dict1.keys()) == list(dict2.keys()):
    for key in dict1:
      dict_result[key] = ((dict1[key] * count1) + (dict2[key] * count2)) / total_doc

  return dict_result, total_doc

# Compare Redundancy of cnndm and financial
def compare_redun():
  cnn_path = r"raw_data\cnndm\cnn_stories\stories"
  dm_path = r"raw_data\cnndm\dailymail_stories\stories"
  bbc_path = r"raw_data\finance_preprocessed\BBC_News"
  eest_path = r"raw_data\finance_preprocessed\eest"

  dict_cnndm, total_cnndm = sum_result(cnn_path, dm_path)
  dict_fin, total_fin = sum_result(bbc_path, eest_path)





  return 1






