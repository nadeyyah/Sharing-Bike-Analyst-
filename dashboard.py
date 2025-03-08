import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import gdown

# Download data menggunakan gdown
file_id = "1lS10up4nts5Efpwj8cIEaEf3U_FBBHZM" 
url = f"https://drive.google.com/uc?id={file_id}&export=download"
output = "all_data.csv"
gdown.download(url, output, quiet=False)

# Load data
data = pd.read_csv(output)

# Streamlit Dashboard
st.title("Dashboard Interaktif: Analisis Penyewaan Sepeda")
# Load Dataset
combined_df = data

# Identifikasi Variabel
combined_df['dteday'] = pd.to_datetime(combined_df['dteday'])
combined_df['year'] = combined_df['dteday'].dt.year
combined_df['month'] = combined_df['dteday'].dt.month

# Sidebar
st.sidebar.header("Filter Data")
st.sidebar.markdown("""
**Catatan Kode Musim**:
- 1: Spring  
- 2: Summer  
- 3: Fall  
- 4: Winter  
""")
st.sidebar.markdown("""
**Catatan Kode Cuaca**:
- 1: Clear, Few clouds, Partly cloudy, Partly cloudy  
- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist  
- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds  
- 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog  
""")

selected_year = st.sidebar.multiselect("Pilih Tahun:", combined_df['year'].unique(), default=combined_df['year'].unique())
selected_season = st.sidebar.multiselect("Pilih Musim:", combined_df['season'].unique(), default=combined_df['season'].unique())
selected_weather = st.sidebar.multiselect("Pilih Cuaca:", combined_df['weathersit'].unique(), default=combined_df['weathersit'].unique())
selected_month = st.sidebar.multiselect("Pilih Bulan:", combined_df['month'].unique(), default=combined_df['month'].unique())

# Filters
filtered_data = combined_df[(combined_df['year'].isin(selected_year)) &
                            (combined_df['season'].isin(selected_season)) &
                            (combined_df['weathersit'].isin(selected_weather)) &
                            (combined_df['month'].isin(selected_month))]

st.subheader("Dataset Setelah Filter")
st.dataframe(filtered_data)

# Statistika Deskriptif
st.subheader("Statistik Deskriptif")
st.write(filtered_data.describe())

# Visualisasi: Tren Penyewaan Sepeda berdasarkan Bulan
st.subheader("Tren Penyewaan Sepeda Bulanan")
monthly_trend = filtered_data.groupby('month')[['cnt_day', 'cnt_hour']].mean().reset_index()

fig1, ax1 = plt.subplots(figsize=(8, 4))
sns.lineplot(data=monthly_trend, x='month', y='cnt_day', marker='o', label='Cnt Day', ax=ax1)
sns.lineplot(data=monthly_trend, x='month', y='cnt_hour', marker='o', label='Cnt Hour', ax=ax1)
for i, row in monthly_trend.iterrows():
    ax1.annotate(f"{row['cnt_day']:.0f}", (row['month'], row['cnt_day']), textcoords="offset points", xytext=(0, 2), ha='center')
    ax1.annotate(f"{row['cnt_hour']:.0f}", (row['month'], row['cnt_hour']), textcoords="offset points", xytext=(0, 2), ha='center')
ax1.set_title("Rata-rata Penyewaan Sepeda Bulanan")
ax1.set_xlabel("Bulan")
ax1.set_ylabel("Rata-rata Penyewaan")
ax1.legend()
st.pyplot(fig1)

# Visualisasi: Distribusi Penyewaan Berdasarkan Pengguna
st.subheader("Distribusi Penyewaan Berdasarkan Pengguna")
user_distribution = filtered_data.groupby('season')[['casual', 'registered']].mean().reset_index()

fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.barplot(data=user_distribution, x='season', y='casual', color='#ABC8FD', label='Casual', ax=ax2)
sns.barplot(data=user_distribution, x='season', y='registered', color='#F6A788', label='Registered', bottom=user_distribution['casual'], ax=ax2)
for i, row in user_distribution.iterrows():
    ax2.text(i, row['casual'] / 2, f"{row['casual']:.0f}", ha='center', color='white')
    ax2.text(i, row['casual'] + row['registered'] / 2, f"{row['registered']:.0f}", ha='center', color='white')
ax2.set_title("Distribusi Penyewaan Berdasarkan Pengguna dan Musim")
ax2.set_xlabel("Musim")
ax2.set_ylabel("Rata-rata Penyewaan")
ax2.legend()
st.pyplot(fig2)

# Visualisasi: Korelasi Antar Variabel
st.subheader("Korelasi Antar Variabel")
numerical_columns = ['temp', 'atemp', 'hum', 'windspeed', 'cnt_hour', 'casual', 'registered']
correlation_matrix = filtered_data[numerical_columns].corr()

fig3, ax3 = plt.subplots(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax3)
ax3.set_title("Heatmap Korelasi Variabel")
st.pyplot(fig3)

# Analisis Klaster Manual
# Grup Manual Berdasarkan Suhu
def categorize_temp(temp):
    if temp < 0.3:
        return "Dingin"
    elif 0.3 <= temp < 0.7:
        return "Sedang"
    else:
        return "Panas"

# Grup Manual Berdasarkan Kelembapan
def categorize_hum(hum):
    if hum < 0.4:
        return "Rendah"
    elif 0.4 <= hum < 0.7:
        return "Sedang"
    else:
        return "Tinggi"

# Grup Manual Berdasarkan Kecepatan Angin
def categorize_windspeed(windspeed):
    if windspeed < 0.2:
        return "Lambat"
    elif 0.2 <= windspeed < 0.5:
        return "Sedang"
    else:
        return "Cepat"

# Tambahkan Kolom Grup ke Data
combined_df['temp_group'] = combined_df['temp'].apply(categorize_temp)
combined_df['hum_group'] = combined_df['hum'].apply(categorize_hum)
combined_df['windspeed_group'] = combined_df['windspeed'].apply(categorize_windspeed)

# Pivot Table: Analisis Penyewaan Berdasarkan Grup
group_analysis = combined_df.pivot_table(
    values='cnt_day',
    index=['temp_group', 'hum_group', 'windspeed_group'],
    aggfunc='mean'
).sort_values('cnt_day', ascending=False)

st.subheader("Penyewaan Sepeda Berdasarkan Grup")

grouped_data = group_analysis.reset_index()

fig1, ax1 = plt.subplots(figsize=(12, 6))
sns.barplot(
    data=grouped_data,
    x="temp_group",
    y="cnt_day",
    hue="hum_group",
    palette="coolwarm",
    ci = None,
    ax=ax1
)
ax1.set_title("Rata-rata Penyewaan Berdasarkan Suhu dan Kelembapan")
ax1.set_xlabel("Kategori Suhu")
ax1.set_ylabel("Rata-rata Penyewaan Harian")
ax1.legend(title="Kategori Kelembapan")
for container in ax1.containers:
    ax1.bar_label(container, fmt="%.1f", label_type="edge", fontsize=9)
st.pyplot(fig1)