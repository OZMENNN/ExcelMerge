# noinspection PyUnresolvedReferences
# -*- coding: utf-8 -*-

import pandas as pd
import os



# search
folder_path = 'C:\Users\MT\PycharmProjects\......'

# new DataFrame
combined_df = pd.DataFrame()

# check
for filename in os.listdir(folder_path):
    if filename.endswith('.xls') or filename.endswith('.xls'):
        file_path = os.path.join(folder_path, filename)

        # read
        df = pd.read_excel(file_path)

        # DataFrame merge
        combined_df = pd.concat([combined_df, df], ignore_index=True)

# write
combined_df.to_excel('combined_output.xlsx', index=False)

print("Excel dosyaları başarıyla birleştirildi!")
