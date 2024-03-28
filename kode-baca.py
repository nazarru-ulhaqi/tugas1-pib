import pandas as pd

# Baca file CSV
df_csv = pd.read_csv("nama_file_csv.csv")

# Baca file Excel
df_excel = pd.read_excel("nama_file_excel.xlsx")

# Tampilkan data
print(df_csv.head())
print(df_excel.head())
