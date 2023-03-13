from read_src import open_src_count, open_src_redun, sum_result

cnn_path = r"raw_data\cnndm\cnn_stories\stories"
dm_path = r"raw_data\cnndm\dailymail_stories\stories"
bbc_path = r"raw_data\finance_preprocessed\BBC_News"
eest_path = r"raw_data\finance_preprocessed\eest"

# CNN dataset
dict_cnn, count_cnn = open_src_count(cnn_path)
print("Total CNN Documents: ", count_cnn)
for key in dict_cnn:
  print(key, ": ", dict_cnn[key])

# Dailymail dataset
dict_dm, count_dm = open_src_count(dm_path)
print("Total Dailymail Documents: ", count_dm)
for key in dict_dm:
  print(key, ": ", dict_dm[key])



# Fiancial700 avg. doc/summary length
# dict_fin_count, total_fin = sum_result(bbc_path, eest_path, redun_metric=False)
# print("Total Financial700 Documents: ", total_fin)
# for key in dict_fin_count:
#   print(key, ": ", dict_fin_count[key])

# # BBC dataset
# dict_bbc, count_bbc = open_src_count(bbc_path)
# print("Total BBC Documents: ", count_bbc)
# for key in dict_bbc:
#   print(key, ": ", dict_bbc[key])

# # EEST dataset
# dict_eest, count_eest = open_src_count(eest_path)
# print("Total EEST Documents: ", count_eest)
# for key in dict_eest:
#   print(key, ": ", dict_eest[key])


