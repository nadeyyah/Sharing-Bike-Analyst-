# Dashboad Analisis Penyewaan Sepeda

Dashboard ini dirancang untuk menganalisis data penyewaan sepeda berdasarkan faktor lingkungan seperti suhu, kelembapan, dan kecepatan angin. Visualisasi yang disediakan meliputi grafik distribusi, analisis rata-rata penyewaan, dan time series untuk memberikan wawasan mendalam terkait pola penyewaan sepeda.

----
## Fitur Utama
- **Clusterisasi Berdasarkan Suhu, Kelembapan, dan Kecepatan Angin**:
  - Mengelompokkan data ke dalam kategori seperti **Dingin**, **Sedang**, **Panas** untuk suhu, serta kategori kelembapan dan kecepatan angin lainnya.
- **Visualisasi Data**:
  - Menyediakan berbagai grafik seperti **heatmap**, **bar chart**, dan **time series**.
- **Pivot Table**:
  - Menampilkan ringkasan analisis rata-rata penyewaan sepeda berdasarkan kategori suhu, kelembapan, dan kecepatan angin.
----

## Instalasi
### 1. Clone Repository
Clone repository ini ke lokal Anda dengan perintah:
```
git clone https://github.com/username/repository-name.git
   cd repository-name
```
### 2. Membuat dan Mengaktifkan enviroment Python
```
python -m venv env
source env/bin/activate    # Linux/MacOS
env\Scripts\activate       # Windows
```
### 3. Install package yang diperlukan 
```
pip install -r requirements.txt
```

### 4. Menjalankan Streamlit dengan dashboard
```
streamlit run dashboard.py
```
