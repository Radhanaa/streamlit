import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')

# setting icon > streamlit-emoji-shortcode
st.set_page_config(page_title="Global Store", page_icon=":computer:",layout="wide")

st.title(" :chart_with_upwards_trend: Penyewaan Sepeda")
st.markdown('<style>div.block-container{padding-top:5rem;}</style>',unsafe_allow_html=True)

st.sidebar.image("dicoding.jpeg", width = 200)
st.sidebar.header("Belajar Analisis Data dengan Python")

st.write("""
**Menentukan pertanyaan bisnis**:
- Musim apakah yang memiliki jumlah penyewa sepeda terbanyak dan tersedikit?
- Bagaimana hubungan atau korelasi suhu (temp dan atemp), kelembapan, dan kecepatan angin terhadap jumlah pengguna sepeda?
- Cuaca apakah yang memiliki jumlah penyewa sepeda terbanyak dan tersedikit?
- Bagaimana pola perubahan jumlah penyewa pada setiap bulan pada tahun 2011 dan 2012?
""")
st.markdown(
    """
    <hr style="height:4px; border:none; background-color:grey;">
    """, 
    unsafe_allow_html=True
)

data_musim = pd.read_csv("D:\\Semester 6\\Bangkit\\Data\\data_musim.csv")

st.write("1. Musim yang memiliki jumlah penyewa sepeda terbanyak dan tersedikit")
# Membuat dua kolom di Streamlit
col1, col2 = st.columns(2)

# Atur tinggi dan lebar yang sama
fig_size = (6, 6)

# Kolom 1: Bar Chart
with col1:
    fig1, ax1 = plt.subplots(figsize=fig_size)
    sns.barplot(x='season', y='cnt', data=data_musim, color='blue', ax=ax1)
    ax1.set_xlabel('Musim')
    ax1.set_ylabel('Total CNT')
    ax1.set_title('Total CNT per Musim')
    ax1.grid(axis='y')
    st.pyplot(fig1)

# Kolom 2: Pie Chart
with col2:
    fig2, ax2 = plt.subplots(figsize=fig_size)
    ax2.pie(data_musim['cnt'], 
            labels=data_musim['season'], 
            autopct='%1.1f%%', 
            startangle=140, 
            colors=['lightcoral', 'lightgreen', 'lightskyblue', 'plum'])
    ax2.set_title('Proporsi Total CNT per Musim')
    st.pyplot(fig2)

st.markdown('---')
st.write('2. Korelasi suhu (temp dan atemp), kelembapan, dan kecepatan angin terhadap jumlah pengguna sepeda')
data2 = pd.read_csv("D:\\Semester 6\\Bangkit\\Data\\data2.csv")

# Mencari nilai korelasi antara Usia dan Akreditasi
plt.figure(figsize=(6, 4))  # Ukuran heatmap yang lebih kecil
sns.heatmap(data2.corr(), annot=True, cmap='coolwarm', annot_kws={"size": 8}, cbar_kws={"shrink": 0.5})

# Mengatur ukuran font untuk sumbu dan judul
plt.title('Korelasi', fontsize=10)  # Ukuran font judul
plt.xticks(fontsize=8)  # Ukuran font untuk sumbu x
plt.yticks(fontsize=8)  # Ukuran font untuk sumbu y

st.pyplot(plt)  # Menampilkan heatmap di Streamlit

st.markdown('---')

st.write('3. Cuaca yang memiliki jumlah penyewa sepeda terbanyak dan tersedikit')

data_cuaca = pd.read_csv("D:\\Semester 6\\Bangkit\\Data\\data_cuaca.csv")

# Membuat dua kolom di Streamlit
col1, col2 = st.columns(2)

# Kolom 1: Bar Chart
with col1:
    plt.figure(figsize=(5, 5))  # Ukuran figure bar chart
    plt.bar(data_cuaca['weathersit'], data_cuaca['cnt'], color='green')
    plt.xlabel('Cuaca')
    plt.ylabel('Total CNT')
    plt.title('Total CNT per Cuaca')
    plt.grid(axis='y')
    st.pyplot(plt)  # Menampilkan bar chart

# Kolom 2: Pie Chart
with col2:
    plt.figure(figsize=(5, 5))  # Ukuran figure pie chart
    plt.pie(data_cuaca['cnt'], labels=data_cuaca['weathersit'], autopct='%1.2f%%', startangle=140, colors=['red', 'green', 'blue', 'yellow'])
    plt.title('Proporsi Total CNT per Cuaca')
    st.pyplot(plt)  # Menampilkan pie chart

st.markdown('---')

st.write('4. Pola perubahan jumlah penyewa pada setiap bulan pada tahun 2011 dan 2012')

data_2011 = pd.read_csv("D:\\Semester 6\\Bangkit\\Data\\data_2011.csv")
data_2012 = pd.read_csv("D:\\Semester 6\\Bangkit\\Data\\data_2012.csv")

st.write("Data pada tahun 2011:")

# Membentuk data dalam format panjang (tidy format)
df_long_2011 = pd.melt(data_2011, id_vars=['mnth'], value_vars=['casual', 'registered', 'cnt'],
                  var_name='Kategori', value_name='Jumlah')

# Plot menggunakan Seaborn dan mengecilkan ukurannya
plt.figure(figsize=(8, 4))  # Mengubah ukuran figure menjadi lebih kecil
sns.lineplot(x='mnth', y='Jumlah', hue='Kategori', data=df_long_2011, marker='o')

# Menambahkan label dan judul dengan font yang lebih kecil
plt.xlabel('Bulan', fontsize=10)
plt.ylabel('Jumlah', fontsize=10)
plt.title('Diagram Garis Casual, Registered, dan CNT per Bulan pada Tahun 2011', fontsize=12)

# Mengubah ukuran font pada legenda
plt.legend(title='Kategori', title_fontsize=10, fontsize=8)

# Mengubah ukuran font pada ticks (label sumbu x dan y)
plt.xticks(fontsize=6.5)
plt.yticks(fontsize=6.5)

# Menambahkan grid untuk visualisasi yang lebih baik
plt.grid(True)

# Menampilkan plot di Streamlit
st.pyplot(plt)

st.write("Data pada tahun 2012:")

# Membentuk data dalam format panjang (tidy format)
df_long_2012 = pd.melt(data_2012, id_vars=['mnth'], value_vars=['casual', 'registered', 'cnt'],
                  var_name='Kategori', value_name='Jumlah')

# Plot menggunakan Seaborn dan mengecilkan ukurannya
plt.figure(figsize=(8, 4))  # Mengubah ukuran figure menjadi lebih kecil
sns.lineplot(x='mnth', y='Jumlah', hue='Kategori', data=df_long_2012, marker='o')

# Menambahkan label dan judul dengan font yang lebih kecil
plt.xlabel('Bulan', fontsize=10)
plt.ylabel('Jumlah', fontsize=10)
plt.title('Diagram Garis Casual, Registered, dan CNT per Bulan pada Tahun 2011', fontsize=12)

# Mengubah ukuran font pada legenda
plt.legend(title='Kategori', title_fontsize=10, fontsize=8)

# Mengubah ukuran font pada ticks (label sumbu x dan y)
plt.xticks(fontsize=6.5)
plt.yticks(fontsize=6.5)

# Menambahkan grid untuk visualisasi yang lebih baik
plt.grid(True)

# Menampilkan plot di Streamlit
st.pyplot(plt)

st.markdown('***Conclusion***')

st.write('''- Conclution pertanyaan 1 : Musim apakah yang memiliki jumlah penyewa sepeda terbanyak dan tersedikit?
  
  Jawab: Musim yang memiliki jumlah penyewa sepeda terbanyak adalah musim gugur dan musim yang memiliki jumlah penyewa tersedikit adalah musim semi

- Conclution pertanyaan 2 : Bagaimana hubungan atau korelasi suhu (temp dan atemp), kelembapan, dan kecepatan angin terhadap jumlah pengguna sepeda?

  Jawab: didapat 3 kesimpulan dari pertanyaan ini yaitu:
  - Hubungan/Korelasi suhu memiliki pengaruh positif sedang atau korelasi positif sedang terhadap jumlah penyewa
  - Hubungan/Korelasi Kelembapan udara memiliki pengaruh negatif lemah atau korelasi negatif lemah terhadap jumlah penyewa
  - Hubungan / Korelasi Kecepatan angin (windspeed) memiliki pengaruh positif sangat lemah atau korelasi poitif sangat lemah terhadap jumlah penyewa.

- Conclusion Pertanyaan 3: Cuaca apakah yang memiliki jumlah penyewa sepeda terbanyak dan tersedikit?
  
  Jawab: cuaca yang paling banyak didatangi penyewa adalah cuaca cerah, dan cuaca yang paling sedikit di datangi penyewa adalah cuaca Hujan lebat

- Conclusion Pertanyaan 4: Bagaimana pola perubahan jumlah penyewa pada setiap bulan pada tahun 2011 dan 2012?

  Jawab: Pola perubahan pada jumlah penyewa pada tahun 2011 adalah dari awal tahun sampai pertengahan tahun, jumlah penyewa mengalami peningkatan. akan tetapi dari pertengahan tahun sampai akhir tahun jumlah penyewa mengalami penurunan berlanjut sampai tahun 2012 yang mana polanya memiliki pola yang mirip dengan tahun 2011 yaitu dari awal tahun sampai pertengahan tahun, jumlah penyewa mengalami peningkatan. akan tetapi dari pertengahan tahun sampai akhir tahun jumlah penyewa mengalami penurunan.
         
Recomendation : 

    1. Sebaiknya untuk usaha penyewaan difokuskan pada sekitar musim Gugur yaitu pada bulan Juli-Oktober 
         karena memiliki jumlah penyewa banyak berdasarkan data 2011 dan 2012. 
         
    2.Untuk penyewaan sebaiknya difokuskan pada cuaca cerah dan berawan. 
         
    3. Berdasarkan korelasi dapat disarankan beberapa hal berikut:
         - Menawarkan diskon pada suhu ideal
         - Meningkatkan operasional dan ketersediaan sepeda
         - Memberikan opsi bersepeda dalam ruangan saat cuaca ekstream''')