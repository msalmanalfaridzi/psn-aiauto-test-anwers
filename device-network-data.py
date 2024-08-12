import pandas as pd

# Membaca data dari file CSV
df = pd.read_csv('device_network_data.csv')

# Mengisi nilai Null dan kosong dengan nilai non-null terakhir
df['Value'] = df['Value'].replace('Null', pd.NA).ffill()

# Mengonversi kolom 'Value' ke tipe integer
df['Value'] = df['Value'].astype(int)

# Menghitung waktu downtime
total_downtime = 0
start_time = None

for index, row in df.iterrows():
    if row['Value'] == 1:
        if start_time is None:
            start_time = row['Epoch Time']
    else:
        if start_time is not None:
            total_downtime += row['Epoch Time'] - start_time
            start_time = None

# Menangani kasus di mana periode downtime berlanjut hingga akhir data
if start_time is not None:
    total_downtime += df.iloc[-1]['Epoch Time'] - start_time

# Mengonversi milidetik ke detik
total_downtime_seconds = total_downtime / 1000

print(f"Total downtime: {total_downtime_seconds:.2f} detik")