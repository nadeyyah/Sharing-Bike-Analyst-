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
### Download Python melalui BREW (MacOS)
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
python3 --version
```
### Siapkan Directori dan  Install package yang diperlukan 
```
mkdir data_dashboard_project
cd data_dashboard_project
pipenv install
pipenv shell
echo -e "streamlit==1.43.0\npandas==2.2.3\nmatplotlib==3.10.1\nseaborn==0.13.2\nnnumpy==2.2.3\ngdown==5.2.0" > requirements.txt
pip install -r requirements.txt
```
### Menjalankan Streamlit dengan dashboard
```
streamlit run dashboard.py
```
