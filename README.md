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

```
### 1. Siapkan Directori dan  Install package yang diperlukan 
```
mkdir data_dashboard_project
cd data_dashboard_project
pipenv install
pipenv shell
echo -e "streamlit==1.25.0\npandas==1.5.3\nmatplotlib==3.7.1\nseaborn==0.12.2\nnumpy==1.24.3" > requirements.txt
pip install -r requirements.txt
```

### 2. Menjalankan Streamlit dengan dashboard
```
streamlit run dashboard.py
```
