from read_src import open_src_count, open_src_redun, sum_result, compare_redun

cnn_path = r"raw_data\cnndm\cnn_stories\stories"
dm_path = r"raw_data\cnndm\dailymail_stories\stories"
bbc_path = r"raw_data\finance_preprocessed\BBC_News"
eest_path = r"raw_data\finance_preprocessed\eest"

# Fiancial700 unique ngrams ratio and NID
dict_fin_count, total_fin = sum_result(bbc_path, eest_path, redun_metric=True)
print("Total Financial700 Documents: ", total_fin)
for key in dict_fin_count:
  print(key, ": ", dict_fin_count[key])

# CNN/DM unique ngrams ratio and NID
dict_cnndm_count, total_cnndm = sum_result(cnn_path, dm_path, redun_metric=True)
print("Total CNN/DM Documents: ", total_cnndm)
for key in dict_cnndm_count:
  print(key, ": ", dict_cnndm_count[key])
