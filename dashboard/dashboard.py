from matplotlib import axis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe
# Menghitung Jumlah Penyewa Keseluruhan
def create_daily_counts_df(df):
    daily_counts_df = df.resample(rule='D', on='dteday').agg({
        "counts": "sum",
    })
    daily_counts_df = daily_counts_df.reset_index()
    daily_counts_df["unique_days"] = range(1, len(daily_counts_df) + 1)
    return daily_counts_df

# Menghitung Rentang Waktu Dari Awal Sampai Akhir
def create_rentang_tahun_df(df, dteday):
    tahun_awal_df = df['dteday'].dt.year.min()
    tahun_akhir_df = df['dteday'].dt.year.max()
    return tahun_awal_df, tahun_akhir_df

# Membuat Analisis Tren Dari Waktu ke Waktu
def create_analisis_tren_waktu(df, dteday, counts):
    analisis_tren_waktu_df = df.set_index(dteday)[counts]
    return analisis_tren_waktu_df

# Menghitung Jumlah Penyewa Berdasarkan Tahun
def create_byyear_df(df):
    byyear_df = df.groupby(df['dteday'].dt.year)['counts'].sum().reset_index()
    byyear_df.rename(columns={
        "dteday": "year",
        "counts": "counts"
    }, inplace=True)
    return byyear_df

# Menghitung Jumlah Penyewa Berdasarkan Hari kerja vs Hari Libur
def create_day_type_counts_plot(df):
    day_type_counts_df = df['workingday'].value_counts()
    return day_type_counts_df

# Membuat Jumlah Penyewa Berdarakna KOndisi Cuaca
def create_weathersit_counts_plot(df):
    weathersit_counts_df = df.groupby('weathersit').size().sort_values(ascending=True)
    return weathersit_counts_df

# Load cleaned data
all_df = pd.read_csv("dashboard/all_data.csv")

datetime_columns = ["dteday"]
all_df.sort_values(by="dteday", inplace=True)
all_df.reset_index(inplace=True)
 
for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

# Filter data tanggal
min_date = all_df["dteday"].min()
max_date = all_df["dteday"].max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4d/Bicycle_icon_MUV.png")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input( # type: ignore
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    ) # type: ignore

main_df = all_df[(all_df["dteday"] >= str(start_date)) & 
                (all_df["dteday"] <= str(end_date))]

# Menyiapkan berbagai dataframe
daily_counts_df = create_daily_counts_df(main_df)
analisis_tren_waktu_df = create_analisis_tren_waktu(main_df, 'dteday', 'counts')
rentang_tahun_awal, rentang_tahun_akhir = create_rentang_tahun_df(main_df, 'dteday')
byyear_df = create_byyear_df(main_df)
day_type_counts_df = create_day_type_counts_plot(main_df)
weathersit_counts_df = create_weathersit_counts_plot(main_df)

# plot number of daily Bike sharing (2011-2012)
st.header('Bike Sharing Dashboard :sparkles:')
st.subheader('Daily Bike Sharing Trends')
 
col1, col2 = st.columns(2)
 
with col1:
    total_counts = daily_counts_df.counts.sum()
    st.metric("Total of Bike Rental Users", value=total_counts)

with col2:
    total_tahun = rentang_tahun_akhir - rentang_tahun_awal
    output_rentang_tahun = f"{rentang_tahun_awal} - {rentang_tahun_akhir}"
    st.metric("Rentang Waktu", value=output_rentang_tahun)

# Visualisasi Tren penyewaan sepeda dari waktu ke waktu
st.subheader('Tren penyewaan sepeda dari waktu ke waktu')
fig, axis = plt.subplots(figsize=(16, 8))
sns.lineplot(
    x=analisis_tren_waktu_df.index,
    y=analisis_tren_waktu_df.values,
    marker='o', 
    linewidth=2,
    color="#90CAF9",
    ax=axis
)
axis.tick_params(axis='y', labelsize=20)
axis.tick_params(axis='x', labelsize=15)

axis.set_title("Grafik Tren Harian", loc="center", fontsize=20)
axis.set_ylabel("Jumlah Peminjaman Sepeda", fontsize=15)
axis.set_xlabel("Tanggal", fontsize=15)
st.pyplot(fig)

# Total Penyewaan Sepeda Per-Tahun
st.subheader('Jumlah Penyewa Sepeda Tiap Tahun')
fig, axis = plt.subplots(figsize=(16, 8))
sns.barplot(
    y="counts", 
    x="year",
    data=byyear_df.sort_values(by="year", ascending=True),
    ax=axis
)
axis.set_title("Total Penyewaan Sepeda Per-Tahun", loc="center", fontsize=20)
axis.set_ylabel("Jumlah Penyewa", fontsize=15)
axis.set_xlabel("Year", fontsize=15)
axis.tick_params(axis='x', labelsize=12)
axis.tick_params(axis='y', labelsize=12)
st.pyplot(fig)

# Jumlah Penyewaa Sepeda pada Hari Kerja vs Hari Libur
st.subheader('Jumlah Penyewa Sepeda pada Hari kerja & Hari Libur')
fig, axis = plt.subplots(figsize=(8, 6))
sns.barplot(
    x=day_type_counts_df.index, 
    y=day_type_counts_df.values, 
    palette='viridis', ax=axis)

axis.set_xlabel('Hari')
axis.set_ylabel('Jumlah Penyewaan')
axis.set_title('Jumlah Penyewaa Sepeda pada Hari Kerja vs Hari Libur')
st.pyplot(fig)

#Jumlah Penyewaan Berdasarkan Kondisi Cuaca
st.subheader('Jumlah Penyewaan Berdasarkan Kondisi Cuaca')
fig, axis = plt.subplots(figsize=(10, 6))
sns.barplot(
    x=weathersit_counts_df.values, 
    y=weathersit_counts_df.index, 
        palette='Dark2', ax=axis)

axis.set_xlabel('Jumlah Penyewaan')
axis.set_ylabel('Kondisi Cuaca')
axis.set_title('Jumlah Penyewaan Berdasarkan Kondisi Cuaca')
st.pyplot(fig)

# Copyright saya
st.caption('Copyright (c) Muhammad Irsyad Fikri Azhar 2024')