import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dashboard\df_final.csv')

st.set_page_config(layout='wide', initial_sidebar_state = 'expanded')

# Fungsi untuk membuat bar plot
def create_bar_plot(data, title, x_label, y_label):
    plt.figure(figsize=(10, 6))
    data.plot(kind='bar', color=('blue', 'blue', 'blue', 'skyblue', 'skyblue', 'skyblue', 'skyblue', 'skyblue', 'skyblue', 'skyblue'))
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=90)
    plt.tight_layout()
    return plt

# Fungsi untuk membuat line plot
def create_line_plot(data, title, x_label, y_label):
    plt.figure(figsize=(10, 6))
    data.plot(kind='line', color='lightgreen', marker='o')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt

# Fungsi untuk membuat diagram donat
def plot_donut_chart(data, title):
    plt.figure(figsize=(8, 8))
    plt.pie(data, labels=data.index, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.3))
    plt.xticks(rotation=45)
    plt.title(title)
    return plt

# Sidebar
with st.sidebar:
    st.title('Analisis Data \n Listmerce')
    st.image('Logo.png')
    st.write('Nama\t: Abdurrahman Al-Adalah')
    st.write('Email\t: adilaladalah@gmail.com')
    st.write('ID Dicoding\t: marrabae')

    st.write("""
    # Pertanyaan
    1. Apa saja top 3 kategori barang yang paling sering dipesan?
    2. Pada hari apa yang memiliki jumlah transaksi paling banyak?
    3. Metode pembayaran apa yang paling banyak digunakan?
    """)

# Menghitung data untuk visualisasi
cat_count = df['product_category_name_english'].value_counts().head(10)

order_counts = df['ord_day_count'].value_counts()

most_payment = df['payment_type'].value_counts()
payment_percentage = (most_payment / most_payment.sum()) * 100

# Main Content
st.title('Dashboard Analisis Data')

# Menampilkan data

if st.checkbox('Tampilkan Data'):
    st.header('Data Frame yang digunakan')
    st.write(df)

col1, col2= st.columns(2)
with col1:
# Menampilkan visualisasi untk pertanyaan pertama menggunakan diagram bar
    st.subheader('Top 3 Kategori Barang Paling Sering Dipesan')
    st.pyplot(create_bar_plot(cat_count, 'Top 3 Kategori Barang Paling Sering Dipesan', 'Kategori Barang', 'Jumlah Pesanan'))

with col2:
    cat_count = df['product_category_name_english'].value_counts()
    st.write(cat_count)

# Menampilkan visualisasi untuk pertanyaan kedua mengggunakan diagram line
col1, col2= st.columns(2)

with col1:
    st.subheader('Jumlah Transaksi per Hari')
    st.pyplot(create_line_plot(order_counts, 'Total Jumlah Transaksi Berdasarkan Hari', 'Hari', 'Jumlah Transaksi'))

with col2:
    order_counts = df['ord_day_count'].value_counts()
    st.write(order_counts)

# Menampilkan visualisasi untuk pertanyaan ketiga menggunakan diagram donat
col1, col2 = st.columns(2)
with col1:
    st.subheader("Metode pembayaran yang paling sering digunakan")
    st.pyplot(plot_donut_chart(payment_percentage, 'Metode Pembayaran Paling Banyak Digunakan'))

with col2:
    most_payment = df['payment_type'].value_counts()
    payment_count = df['payment_type'].value_counts().sum()
    st.write(most_payment)

st.write("""
    # Conclusion
    ##### Conclusion pertanyaan 1: Apa saja top 3 kategori barang yang paling sering dipesan?
    Dari data yang telah dilihat, terdapat 3 kategori barang yang memiliki jumlah pesanan paling banyak yaitu dalam kategori perlengkapan rumah tangga, barang-barang kesehatan dan kecantikan, dan perlatan olahraga. Dari sini kita bisa melihat tren pasar saat ini dan juga melihat kebiasaan pelanggan yang ada di platform tersebut. Dari informasi tersebut perusahaan bisa melakukan fokus untuk pengembangan terhadap penjualan pada ketegori-kategori tersebut.

    ##### Conclusion pertanyaan 2: Pada hari apa yang memiliki jumlah transaksi paling banyak?
    Pada analisis ini saya ingin melihat bagaimana pola pembelian berdasarkan hari, dimana ternyata kebanyakan pelanggan melakukan transaksi pada hari kerja. Dari informasi yang didapat bisa mengambil langkah bisnis seperti optimalisasi stok logistik, penjadwalan shift kerja, dan melakukan promosi pada weekend untuk meningkatkan penjualan.

    ##### Conclusion pertanyaan 3: Metode pembayaran apa yang paling banyak digunakan?
    Melihat dari banyaknya pelanggan yang melakukan pembayaran menggunakan kartu kredit, saya menyimpulkan bahwa konsumen menghargai kemudahan dalam kemudahan dan kecepatan transaksi. Dari informasi yang sudah didapat kita bisa tahu bahwa penggunaan pembayaran menggunakan kartu kredit menjadi metode transaksi utama untuk sebagian besar pelanggan. Hal ini bisa menjadi langkah bisnis yang berdampak pada loyalitas pelanggan dengan mengadakan reward spesial ataupun melakukan diskon untuk setiap pembayran menggunakan kartu kredit.
"""

)