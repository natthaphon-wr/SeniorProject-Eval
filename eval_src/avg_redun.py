from read_src import open_src_count, open_src_redun, sum_result

cnn_path = r"raw_data\cnndm\cnn_stories\stories"
dm_path = r"raw_data\cnndm\dailymail_stories\stories"
bbc_path = r"raw_data\finance_preprocessed\BBC_News"
eest_path = r"raw_data\finance_preprocessed\eest"

# CNN/DM 
# dict_cnndm_count, total_cnndm = sum_result(cnn_path, dm_path, redun_metric=True)
# print("Total CNN/DM Documents: ", total_cnndm)
# for key in dict_cnndm_count:
#   print(key, ": ", dict_cnndm_count[key])

# Fiancial700 
# dict_fin_count, total_fin = sum_result(bbc_path, eest_path, redun_metric=True)
# print("Total Financial700 Documents: ", total_fin)
# for key in dict_fin_count:
#   print(key, ": ", dict_fin_count[key])

# CNN dataset
dict_cnn, count_cnn = open_src_redun(cnn_path)
print("Total CNN Documents: ", count_cnn)
for key in dict_cnn:
  print(key, ": ", dict_cnn[key])

# DM dataset
dict_dm, count_dm = open_src_redun(dm_path)
print("Total DM Documents: ", count_dm)
for key in dict_dm:
  print(key, ": ", dict_dm[key])

# BBC dataset
dict_bbc, count_bbc = open_src_redun(bbc_path)
print("Total BBC Documents: ", count_bbc)
for key in dict_bbc:
  print(key, ": ", dict_bbc[key])

# EEST dataset
dict_eest, count_eest = open_src_redun(eest_path)
print("Total EEST Documents: ", count_eest)
for key in dict_eest:
  print(key, ": ", dict_eest[key])

