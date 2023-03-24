import pandas as pd
from read_src import open_src_count, open_src_redun

cnn_path = r"raw_data\cnndm\cnn_stories\stories"
dm_path = r"raw_data\cnndm\dailymail_stories\stories"

bbc_path = r"raw_data\finance_preprocessed_final\BBC"
bloomberg_path = r"raw_data\finance_preprocessed_final\Bloomberg"
eest_path = r"raw_data\finance_preprocessed_final\eest"

# CNN dataset
mean_cnn, count_cnn, df_cnn = open_src_count(cnn_path)
print("Total CNN Documents: ", count_cnn)
print(mean_cnn)
df_cnn.to_csv(r"eval_src\result/cnn_count.csv", sep=',', index=False)

# Dailymail dataset
mean_dm, count_dm, df_dm = open_src_count(dm_path)
print("Total Daily Mail Documents: ", count_dm)
print(mean_dm)
df_dm.to_csv(r"eval_src\result/dm_count.csv", sep=',', index=False)

# BBC dataset
mean_bbc, count_bbc, df_bbc = open_src_count(bbc_path)
print("Total BBC Documents: ", count_bbc)
print(mean_bbc)
df_bbc.to_csv(r"eval_src\result/bbc_count.csv", sep=',', index=False)

# Bloomberg dataset
mean_bloom, count_bloom, df_bloom = open_src_count(bloomberg_path)
print("Total Bloomberg Documents: ", count_bloom)
print(mean_bloom)
df_bloom.to_csv(r"eval_src\result/bloomberg_count.csv", sep=',', index=False)

# EEST dataset
mean_eest, count_eest, df_eest = open_src_count(eest_path)
print("Total EEST Documents: ", count_eest)
print(mean_eest)
df_eest.to_csv(r"eval_src\result/eest_count.csv", sep=',', index=False)
