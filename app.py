import streamlit as st

st.set_page_config(
    page_title="Portofolio Data Analyst Fian",
    page_icon="✨",
    layout="wide", # Bisa 'centered' atau 'wide'
    initial_sidebar_state="expanded" # Bisa 'auto', 'expanded', 'collapsed'
)

st.title("Selamat Datang di Portofolio Fian")
# Konten aplikasi lainnya

st.write("Ini adalah teks biasa menggunakan 'st.write()'")
st.write("12345")
st.write({"a": 1, "b": 2})

st.header("Bagian Proyek Data Analyst")

st.markdown("Ini adalah **Teks Tebal**, ini adalah *teks miring*")
st.markdown("Ini adalah [link ke Google](https://www.google.com).")

st.markdown("---") # Garis pembatas
st.markdown("""
* Item satu
* Item dua
    * Sub-item A
""")

st.code("code 123")

if st.button("Tekan Saya!"):
    st.write("Tombol berhasil ditekan!")

if st.checkbox("Tampilkan Detail"):
    st.write("Detail penting terlihat!")

pilihan_warna = st.radio(
    "Pilih warna favorit Anda:",
    ('Merah', 'Hijau', 'Biru')
)
st.write(f"Anda memilih warna: {pilihan_warna}")

pilihan_kota = st.selectbox(
    "Pilih kota asal Anda:",
    ('Jakarta', 'Bandung', 'Surabaya', 'Medan')
)
st.write(f"Anda berasal dari: {pilihan_kota}")

pilihan_skill = st.multiselect(
    "Pilih skill Anda:",
    ['Python', 'SQL', 'Excel', 'Tableau', 'Machine Learning']
)
st.write(f"Skill yang Anda pilih: {', '.join(pilihan_skill)}")

nilai_slider = st.slider(
    "Pilih tingkat kepuasan (1-10):",
    min_value=1, max_value=10, value=9, step=1
)
st.write(f"Tingkat kepuasan Anda: {nilai_slider}")

rating = st.select_slider(
    "Berikan rating untuk aplikasi ini:",
    options=['Sangat Buruk', 'Buruk', 'Cukup', 'Baik', 'Sangat Baik']
)
st.write(f"Anda memberi rating: {rating}")

nama = st.text_input("Masukkan nama Anda:")
if nama:
    st.write(f"Halo, {nama}!")

uploaded_file = st.file_uploader("Unggah file CSV Anda", type=['csv', 'txt', 'doc'])
if uploaded_file is not None:
    import pandas as pd
    df_uploaded = pd.read_csv(uploaded_file)
    st.write("Data berhasil diunggah:")
    st.dataframe(df_uploaded.head())

import streamlit as st
import pandas as pd
import numpy as np 

# data dummy
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
).cumsum()

# membuat line chart
st.area_chart(chart_data)
st.bar_chart(chart_data)
st.line_chart(chart_data)

# Data dummy lokasi di sekitar Jakarta
map_data = pd.DataFrame({
    'lat': [-6.2088, -6.1754, -6.9175],
    'lon': [106.8456, 106.8272, 107.6191]
})
# Membuat visualisasi map
st.map(map_data)

#import streamlit as st
import matplotlib.pyplot as plt
#import numpy as np

fig, ax = plt.subplots()
ax.hist(np.random.randn(100), bins=20)
ax.set_title("Histogram Contoh")
st.pyplot(fig)

# Contoh dari URL (Media)
st.image("https://www.python.org/static/community_logos/python-logo.png", 
         caption="Logo", width=400)

# Mengatur konfigurasi halaman Streamlit
st.set_page_config(
    # Judul halaman yang ditampilkan di tab browser
    page_title="Portfolio Data Analyst Fian",

    # Icon halaman yang ditampilkan di tab browser
    page_icon="📊",

    # Mengatur layout halaman menjadi lebar (wide)
    layout="wide",  #bisa "center"

    # Mengatur sidebar agar terbuka secara default
    initial_sidebar_state="expanded"
)

# Dekorator untuk meng-cache data dan tidak memuatnya ulang setiap kali
@st.cache_data
# Fungsi untuk menghasilkan data dashboard dan menyimpannya di cache
def generate_dashboard_data():
    # Membuat range tanggal dari 1 Januari 2024 selama 30 hari
    dates = pd.date_range('2024-01-01', periods=30)

    # Mengembalikan DataFrame dengan kolom Date, Sales, Visitors, dan Conversion
    return pd.DataFrame({
        # Kolom tanggal
        'Date': dates,

        # Kolom penjualan dengan nilai random antara 1000-5000
        'Sales': np.random.randint(1000, 5000, 30),

        # Kolom pengunjung dengan nilai random antara 500-3000
        'Visitors': np.random.randint(500, 3000, 30),

        # Kolom konversi dengan nilai random antara 0.01-0.1
        'Conversion': np.random.uniform(0.01, 0.1, 30)
    })

# Test: Lihat hasil data yang dihasilkan
# dashboard_data = generate_dashboard_data()
# dashboard_data.head()

# Dekorator untuk meng-cache data skills
@st.cache_data
# Fungsi untuk mengembalikan data skills/keahlian
def get_skills_data():
    # Mengembalikan DataFrame berisi daftar skill dan tingkat keahlian
    return pd.DataFrame({
        # Kolom nama skill
        'Skill': ['Python', 'SQL', 'Tableau', 'PowerBI', 'Excel', 'Statistics'],

        # Kolom profisiensi dengan nilai 0-100
        'Proficiency': [95, 90, 85, 80, 95, 85]
    })

# Dekorator untuk meng-cache data proyek
@st.cache_data
# Fungsi untuk mengembalikan data proyek dengan kemampuan filter
def get_projects_data():
    # Membuat list berisi data-data proyek
    projects = [
        # Proyek pertama: E-commerce Sales Analysis
        {
            # Judul proyek dengan emoji
            'title': '📊 Proyek 1: E-commerce Sales Analysis',
            # Kategori proyek
            'category': 'EDA',
            # Tahun proyek dibuat
            'year': 2023,
            # Deskripsi detail tentang proyek
            'description': '''**Deskripsi:**
Melakukan analisis mendalam terhadap data penjualan e-commerce untuk mengidentifikasi
trend dan peluang pertumbuhan.

**Tools:** Python, Pandas, Matplotlib, Streamlit

**Key Insights:**
- Total sales meningkat 45% YoY
- Kategori Electronics adalah top performer
- Waktu terbaik untuk promo adalah Q4''',
            # Flag apakah proyek memiliki gambar atau tidak
            'has_image': False
        },
        # Proyek kedua: Customer Segmentation Dashboard
        {
            # Judul proyek dengan emoji
            'title': '📈 Proyek 2: Customer Segmentation Dashboard',
            # Kategori proyek
            'category': 'Dashboard',
            # Tahun proyek dibuat
            'year': 2023,
            # Deskripsi detail tentang proyek
            'description': '''**Deskripsi:**
Interactive dashboard untuk segmentasi pelanggan berdasarkan RFM analysis.

**Tools:** SQL, Tableau, Python

**Key Metrics:**
- 5 customer segments identified
- Average CLV per segment
- Churn risk prediction''',
            # Flag apakah proyek memiliki gambar atau tidak
            'has_image': False
        },
        # Proyek ketiga: Churn Prediction Model
        {
            # Judul proyek dengan emoji
            'title': '🤖 Proyek 3: Churn Prediction Model',
            # Kategori proyek
            'category': 'Prediction',
            # Tahun proyek dibuat
            'year': 2024,
            # Deskripsi detail tentang proyek
            'description': '''**Deskripsi:**
Machine learning model untuk memprediksi customer churn dengan akurasi 85%.

**Tools:** Python, Scikit-learn, XGBoost

**Performance:**
- Accuracy: 85%
- Precision: 0.82
- Recall: 0.88''',
            # Flag apakah proyek memiliki gambar atau tidak
            'has_image': False
        }
    ]

    # Mengkonversi list projects menjadi DataFrame dan mengembalikannya
    return pd.DataFrame(projects)

# Fungsi untuk menampilkan navigasi di sidebar
def render_sidebar_nav():
    # Menampilkan judul navigasi di sidebar
    st.sidebar.markdown("# 📍 Navigasi")

    # Membuat tombol radio untuk memilih halaman
    page = st.sidebar.radio(
        # Label untuk radio button
        "Pilih halaman:",
        # Opsi halaman yang tersedia
        ["🏠 Beranda", "👤 Tentang Saya", "📁 Proyek", "📊 Dashboard", "📧 Contact"]
    )

    # Menampilkan pemisah di sidebar
    st.sidebar.markdown("---")

    # Menampilkan tautan media sosial di sidebar
    st.sidebar.markdown(
        """
        ### 🔗 Media Sosial
        - [LinkedIn](https://linkedin.com)
        - [GitHub](https://github.com)
        - [Email](mailto:email@example.com)
        """
    )

    # Menampilkan pemisah lagi di sidebar
    st.sidebar.markdown("---")

    # Menampilkan caption/teks kecil di sidebar
    st.sidebar.caption("© 2024 Portfolio Saya")

    # Mengembalikan halaman yang dipilih user
    return page

# Fungsi untuk menampilkan foto profil
def render_profile_image():
    # Mencoba untuk menampilkan foto profil
    try:
        # Menampilkan gambar dari file
        st.image(
            # Path ke file gambar profil
            "assets/profile_picc.png",
            # Caption yang ditampilkan di bawah gambar
            caption="Foto Profil",
            # Mengatur gambar menggunakan lebar container penuh
            use_container_width=True
        )
    # Jika file tidak ditemukan
    except FileNotFoundError:
        # Menampilkan pesan warning
        st.warning("⚠️ File 'assets/profpict.png' tidak ditemukan!")
        # Menampilkan pesan info/petunjuk
        st.info("💡 Buat folder 'assets/' dan masukkan foto Anda di sana.")

#page beranda
col1, col2 = st.columns([2, 1])
with col1:
        # Menampilkan judul besar dengan emoji
        st.title("🌟 Selamat Datang!")

        # Menampilkan teks markdown dengan pengenalan diri
        st.markdown(
            """
            Halo, nama saya **Muhammad Rizki**. Saya adalah seorang **Data Analyst**
            yang passionate tentang mengubah data menjadi insights yang actionable.

            Dalam portfolio ini, saya menampilkan beberapa proyek data yang telah saya kerjakan,
            dari exploratory data analysis hingga business intelligence dashboard.
            """
        )

# Menggunakan kolom kedua untuk foto profil
with col2:
        # Memanggil fungsi untuk menampilkan foto profil
    render_profile_image()

    def render_divider():
            st.markdown("---")
        # Menampilkan garis pemisah
    render_divider()

        # Menampilkan statistik singkat
    st.subheader("📈 Statistik Singkat")

        # Membuat 4 kolom untuk menampilkan metrik
    col1, col2, col3, col4 = st.columns(4)

        # Menampilkan metrik proyek selesai
    col1.metric("Proyek Selesai", 12, "+3")

        # Menampilkan metrik total dataset
    col2.metric("Total Dataset", 50, "-5")

        # Menampilkan metrik jumlah klien
    col3.metric("Clients", 8, "+2")

        # Menampilkan metrik tahun pengalaman
    col4.metric("Tahun Pengalaman", 3, "+1")

# def page_tentang_saya():
    # Menampilkan judul halaman dengan emoji
st.title("👤 Tentang Saya")

    # Menampilkan subheader untuk latar belakang
st.subheader("Latar Belakang")

    # Menampilkan teks tentang latar belakang dan keahlian
st.write(
        """
        Saya adalah data analyst dengan pengalaman 3+ tahun di industri e-commerce dan fintech.
        Saya berspesialisasi dalam:
        - **Data Exploration & Cleaning**: Menggunakan Pandas & NumPy
        - **Data Visualization**: Tableau, PowerBI, Streamlit
        - **Statistical Analysis**: A/B Testing, Hypothesis Testing
        - **Business Intelligence**: Dashboard development, KPI tracking
        """
    )

    # Menampilkan subheader untuk technical skills
st.subheader("🛠️ Technical Skills")

    # Memanggil fungsi untuk mendapatkan data skills dan menyimpannya dalam variable
skills_data = get_skills_data()

import plotly.express as px
    # Membuat bar chart menggunakan Plotly Express
fig = px.bar(
        # Data yang digunakan untuk chart
        skills_data,
        # Kolom yang ditampilkan di x-axis
        x='Skill',
        # Kolom yang ditampilkan di y-axis
        y='Proficiency',
        # Judul chart
        title='Tingkat Keahlian',
        # Kolom yang digunakan untuk warna
        color='Proficiency',
        # Skala warna yang digunakan
        color_continuous_scale='Viridis',
        # Menampilkan nilai di atas bar
        text='Proficiency'
    )

    # Menampilkan chart di Streamlit
st.plotly_chart(fig, use_container_width=True)

# Menampilkan subheader untuk sertifikasi
st.subheader("📚 Sertifikasi")

    # Membuat 3 kolom untuk menampilkan sertifikasi
cert_col1, cert_col2, cert_col3 = st.columns(3)

    # Menampilkan sertifikasi Google Analytics di kolom pertama
cert_col1.markdown(
        """
        **Google Analytics Certification**
        ✅ Certified, 2022
        """
    )

    # Menampilkan sertifikasi SQL di kolom kedua
cert_col2.markdown(
        """
        **SQL for Data Analysis**
        ✅ Certified, 2021
        """
    )

    # Menampilkan sertifikasi Tableau di kolom ketiga
cert_col3.markdown(
        """
        **Data Visualization with Tableau**
        ✅ Certified, 2023
        """
    )

# Menampilkan judul halaman dengan emoji
st.title("📁 Proyek Saya")

    # Menampilkan subheader untuk filter proyek
st.subheader("🔍 Filter Proyek")

    # Membuat 2 kolom untuk filter
col1, col2 = st.columns(2)

    # Menggunakan kolom pertama untuk filter kategori
with col1:
        selected_category = st.multiselect(
            "Kategori:",
            ['EDA', 'Dashboard', 'Prediction', 'Visualization'],
            default=['EDA', 'Dashboard', 'Prediction']
        )

        # Menggunakan kolom kedua untuk filter tahun
with col2:
        selected_year = st.slider(
            "Tahun:",
            2021,
            2024,
            (2021, 2024)
        )
render_divider()
projects_df = get_projects_data()
# Melakukan filter pada data proyek berdasarkan kategori dan tahun yang dipilih
filtered_projects = projects_df[
        # Filter berdasarkan kategori yang dipilih
        (projects_df['category'].isin(selected_category)) &
        #filter berdasarkan tahun minimum yang dipilih
        (projects_df['year'] >= selected_year[0]) &
        #filter berdasarkan tahun maksimum yang dipilih
        (projects_df['year'] <= selected_year[1])
    ]

# Mengecek apakah ada proyek yang sesuai dengan filter
if len(filtered_projects) == 0:
        #menampilkan pesan info jika tidak ada proyek yang sesuai dengan filter
        st.info("📭 Tidak ada proyek yang sesuai dengan filter Anda")
        #keluar dari fungsi

# Loop untuk menampilkan setiap proyek yang telah difilter
    # Gunakan enumerate untuk membuat key tombol unik (agar tidak bentrok jika index DataFrame bukan 0..n-1)
for i, (_, project) in enumerate(filtered_projects.iterrows()):
        # Membuat expander untuk setiap proyek (dapat diklik untuk membuka/menutup)
        with st.expander(f"{project.get('title', 'Untitled')} ({project.get('year', '')})", expanded=(i == 0)):
            # Membuat 2 kolom jika proyek memiliki gambar, jika tidak membuat 1 kolom (container)
            if project.get('has_image', False):
                col_left, col_right = st.columns([2, 1])
            else:
                col_left = st.container()
                col_right = None

            # Menggunakan kolom pertama untuk deskripsi
            with col_left:
                st.markdown(project.get('description', ''))

                # Jika ada URL proyek, gunakan itu; kalau tidak, hanya tampilkan tombol info
                proj_url = project.get('url', None)
                if proj_url:
                    # Tombol untuk membuka link di tab baru: gunakan markdown link (Streamlit akan membuka di tab baru)
                    if st.button("🔗 View Project", key=f"project_{i}"):
                        st.write(f"[Membuka project]({proj_url})")
                else:
                    if st.button("🔗 View Project", key=f"project_{i}"):
                        st.info(f"Link ke project {project.get('title', '')} akan dibuka!")

            # Mengecek apakah kolom kedua ada dan proyek memiliki gambar
            if col_right is not None and project.get('has_image', False):
                with col_right:
                    img_path = project.get('image_path', 'assets/project1_ss.png')
                    # Resolve path relative ke working directory jika bukan absolute
                    img_path = Path(img_path)
                    if not img_path.is_absolute():
                        img_path = Path.cwd() / img_path
                    if img_path.exists():
                        st.image(str(img_path), caption="Project Screenshot")
                    else:
                        st.info("📷 Screenshot tidak tersedia")

import streamlit as st
import re

def render_divider() -> None:
    """Render a horizontal divider line."""
    st.markdown("---")

# Optional: provide a simple divider if render_divider isn't defined elsewhere


def _is_valid_email(email: str) -> bool:
    """Very small email validity check (sufficient for simple form validation)."""
    if not email:
        return False
    # basic pattern: something@something.something
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email) is not None


# Fungsi untuk menampilkan halaman contact
def page_contact() -> None:
    # Menampilkan judul halaman dengan emoji
    st.title("📧 Get in Touch")

    # Menampilkan teks penjelasan
    st.write(
        "Jika Anda tertarik untuk berkolaborasi atau memiliki pertanyaan, "
        "silakan hubungi saya melalui form di bawah!"
    )

    # Menampilkan garis pemisah
    render_divider()

    # Membuat form untuk contact
    with st.form("contact_form"):
        # Membuat input text untuk nama lengkap
        nama = st.text_input("Nama Lengkap")

        # Membuat input text untuk email
        email = st.text_input("Email")

        # Membuat selectbox untuk subjek
        subject = st.selectbox(
            "Subjek:",
            ['Project Inquiry', 'Collaboration', 'General Question', 'Others']
        )

        # Membuat text area untuk pesan dengan tinggi 150 pixel
        message = st.text_area("Pesan:", height=150)

        # Membuat tombol submit untuk mengirim form
        submitted = st.form_submit_button("📤 Send Message")

        # Mengecek apakah form telah disubmit
        if submitted:
            # Validasi sederhana
            if not nama or not email or not message:
                st.error("❌ Mohon isi semua field!")
            elif not _is_valid_email(email):
                st.error("❌ Format email tidak valid. Contoh: nama@domain.com")
            else:
                # Menampilkan pesan sukses dengan nama user
                st.success(
                    f"✅ Terima kasih, {nama}! Pesan Anda telah dikirim. "
                    "Saya akan menghubungi Anda dalam 24 jam."
                )
                # (Opsional) tampilkan ringkasan
                st.markdown("**Rincian pesan:**")
                st.write(f"- Email: {email}")
                st.write(f"- Subjek: {subject}")
                st.write(f"- Pesan: {message}")

    # Menampilkan garis pemisah
    render_divider()

    # Menampilkan subheader untuk kontak lainnya
    st.subheader("🔗 Kontak Lainnya")

    # Membuat 3 kolom untuk menampilkan kontak lainnya
    col1, col2, col3 = st.columns(3)

    # Menampilkan kontak email di kolom pertama
    col1.markdown(
        """
        **Email**
        📧 [email@example.com](mailto:email@example.com)
        """
    )

    # Menampilkan kontak LinkedIn di kolom kedua
    col2.markdown(
        """
        **LinkedIn**
        💼 [linkedin.com/in/username](https://linkedin.com)
        """
    )

    # Menampilkan kontak GitHub di kolom ketiga
    col3.markdown(
        """
        **GitHub**
        🐙 [github.com/username](https://github.com)
        """
    )

