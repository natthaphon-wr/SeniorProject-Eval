import pandas as pd
from read_src import open_src_count, open_src_redun

cnn_path = r"raw_data\cnndm\cnn_stories\stories"
dm_path = r"raw_data\cnndm\dailymail_stories\stories"

bbc_path = r"raw_data\finance_preprocessed_final\BBC"
bloomberg_path = r"raw_data\finance_preprocessed_final\Bloomberg"
eest_path = r"raw_data\finance_preprocessed_final\eest"

# # CNN dataset
# mean_cnn, count_cnn, df_cnn = open_src_redun(cnn_path, False)
# print("Total CNN Documents: ", count_cnn)
# print(mean_cnn)
# df_cnn.to_csv(r"eval_src\result/cnn_summ_redun.csv", sep=',', index=False)

# DM dataset
mean_dm, count_dm, df_dm = open_src_redun(dm_path, False)
print("Total DM Documents: ", count_dm)
print(mean_dm)
df_dm.to_csv(r"eval_src\result/dm_summ_redun.csv", sep=',', index=False)

# # BBC dataset
# mean_bbc, count_bbc, df_bbc = open_src_redun(bbc_path, False)
# print("Total BBC Documents: ", count_bbc)
# print(mean_bbc)
# df_bbc.to_csv(r"eval_src\result/bbc_summ_redun.csv", sep=',', index=False)

# # Bloomberg dataset
# mean_bloom, count_bloom, df_bloom = open_src_redun(bloomberg_path, False)
# print("Total Bloomberg Documents: ", count_bloom)
# print(mean_bloom)
# df_bloom.to_csv(r"eval_src\result/bloomberg_summ_redun.csv", sep=',', index=False)

# # EEST dataset
# mean_eest, count_eest, df_eest = open_src_redun(eest_path, False)
# print("Total EEST Documents: ", count_eest)
# print(mean_eest)
# df_eest.to_csv(r"eval_src\result/eest_summ_redun.csv", sep=',', index=False)
