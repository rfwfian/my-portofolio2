# Mengimpor library Streamlit untuk membuat aplikasi web interaktif
import streamlit as st

# Mengimpor Pandas untuk manipulasi dan analisis data
import pandas as pd

# Mengimpor NumPy untuk komputasi numerik
import numpy as np

# Mengimpor Plotly Express untuk visualisasi data interaktif
import plotly.express as px

# Mengimpor datetime untuk menangani data tanggal dan waktu
from datetime import datetime

# Mengimpor Path untuk menangani file paths dengan benar
from pathlib import Path

# Mengimpor regex untuk validasi email
import re
from typing import Optional, Callable, Dict

# Mengatur konfigurasi halaman Streamlit
st.set_page_config(
    # Judul halaman yang ditampilkan di tab browser
    page_title="Portfolio Data Analyst",

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

# Dekorator untuk meng-cache data skills
@st.cache_data
# Fungsi untuk mengembalikan data skills/keahlian
def get_skills_data():
    # Mengembalikan DataFrame berisi daftar skill dan tingkat keahlian
    return pd.DataFrame({
        # Kolom nama skill
        'Skill': ['Python', 'SQL', 'Tableau', 'PowerBI', 'Excel', 'Statistics'],

        # Kolom profisiensi dengan nilai 0-100
        'Level' : [4, 4, 2, 5, 5, 2]
    })

# Dekorator untuk meng-cache data proyek
@st.cache_data
# Fungsi untuk mengembalikan data proyek dengan kemampuan filter
def get_projects_data():
    return pd.DataFrame([
        {
            'title': '📊 Employee Attrition and Satisfaction Analyst',
            'category': 'Dashboard',
            'year': 2023,
            'description': '''**Deskripsi:**
Melakukan analisis mendalam terhadap penyebab karyawan resign.

**Tools:** Python, Pandas, Power BI

**Key Insights:**
- Total sales meningkat 45% YoY
- Kategori Electronics adalah top performer
- Waktu terbaik untuk promo adalah Q4''',
            'url': 'https://docs.google.com/presentation/d/1dvpe_zUuRGbdzRQSM0WQTIjHNSfwU-EMPWOpGxxfpxE/edit',
            'has_image': False
        },
        {
            'title': '📈 Evaluasi Kinerja Bisnis Bee Cycle',
            'category': 'Visualization',
            'year': 2025,
            'description': '''**Deskripsi:**
Melakukan Analisa Mengenai Penjualan Sepeda.

**Tools:** SQL, Tableau, Python

**Key Metrics:**
- 5 customer segments identified
- Average CLV per segment
- Churn risk prediction''',
            'url': 'https://docs.google.com/presentation/d/1ULKgM7Ev7aDrTG__epGIPZYKWR2BMFyEWddOE1JTEIg/edit',
            'has_image': False
        }
    ])

# Fungsi untuk menampilkan garis pemisah
def render_divider():
    # Menampilkan garis horizontal sebagai pemisah
    st.markdown("---")

# Fungsi untuk menampilkan navigasi di sidebar
def render_sidebar_nav():
    # Menampilkan judul navigasi di sidebar
    st.sidebar.markdown("# 📍 Navigasi")

    # Membuat tombol radio untuk memilih halaman
    page = st.sidebar.radio(
        # Label untuk radio button
        "Pilih halaman:",
        # Opsi halaman yang tersedia
        ["🏠 Beranda", "👤 Tentang Saya", "📁 Proyek", "📊 Dashboard", "📧 Contact", "📝Reflection Questions"]
    )

    return page

def render_project_filter(page):
    selected_category, selected_years = None, None

    if page == "📁 Proyek":
        st.sidebar.divider()
        st.sidebar.subheader("🔍 Filter Proyek")

        # Membuat 2 kolom untuk filter
        selected_category = st.sidebar.multiselect(
            "Kategori",
            ['Dashboard', 'Visualization','EDA']
            # default=['Dashboard']
        )
    
        st.sidebar.subheader("📅 Tahun Proyek")
        # available_years = 
        selected_years = [
            year for year in [2022, 2023, 2024, 2025]
            if st.sidebar.checkbox(str(year), True)
        ]

    # Menampilkan pemisah di sidebar
    # st.sidebar.markdown("---")

    # Menampilkan tautan media sosial di sidebar
    st.sidebar.divider()
    st.sidebar.markdown(
    """
    <style>
    .social a {
        text-decoration: none;
        font-size: 16px;
        display: flex;
        align-items: center;
        margin-bottom: 8px;
        color: inherit;
    }
    .social img {
        width: 18px;
        margin-right: 8px;
    }
    </style>
    <H4 class="social-title">🔗 Media Sosial</H4>
    
    <p></p>

    <div class="social">
        <a href="https://www.linkedin.com/in/rfwfian/" target="_blank">
            💼 LinkedIn
        </a>
        <a href="https://github.com/rfwfian" target="_blank">
            <img src="https://cdn.simpleicons.org/github/000000"/> GitHub
        </a>
        <a href="https://instagram.com/rfwfian" target="_blank">
            <img src="https://cdn.simpleicons.org/instagram/E4405F"/> Instagram
        </a>
        <a href="https://my-portofolio2-fian.streamlit.app/" target="_blank">
            <img src="https://cdn.simpleicons.org/streamlit/FF4B4B"/> Streamlit
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

    # Menampilkan pemisah lagi di sidebar
    st.sidebar.markdown("---")

    # Menampilkan caption/teks kecil di sidebar
    st.sidebar.caption("© 2025 Portofolio Saya")

    # Mengembalikan halaman yang dipilih user
    return selected_category, selected_years

# Fungsi untuk menampilkan foto profil
def render_profile_image():
    # Mencoba untuk menampilkan foto profil
    try:
        # Menampilkan gambar dari file
        st.image(
            # Path ke file gambar profil
            "assets/profile_fian.png",
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

def page_beranda():
    # intro
    col1, col2 = st.columns([2, 1])

    with col1:
        st.title("🌟 Selamat Datang!")

        st.markdown(
            """
            Halo, nama saya **Rahadian Firstya Wisesa (Fian)**. Seorang **Data Analyst**
            yang berfokus pada mengolah data menjadi insight yang bernilai dan dapat ditindaklanjuti.

            Dalam portfolio ini, saya menampilkan proyek data yang telah saya kerjakan,
            yaitu *Employee Attrition and Satisfaction Analysis*.
            """
        )

        st.write("")

        col_btn1, col_btn2 = st.columns(2)

        with col_btn1:
            if st.button("📥 Download CV"):
                st.success("CV berhasil diunduh!")

        with col_btn2:
            if st.button("💬 Hubungi Saya"):
                st.info("Silakan scroll ke halaman Contact!")

    with col2:
        render_profile_image()

    # Bagian: Learning Progress
    st.divider()
    st.subheader("🧠 Learning Progress Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📅 Learning Duration")
        st.write("5 months of consistent data learning")
        st.progress(0.5)
        st.caption("From fundamentals to applied analytics")

    with col2:
        st.markdown("### 📝 Assignments Completed")
        st.write("26 practical assignments")
        st.progress(0.8)
        st.caption("Hands-on exercises & mini projects")

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("### 🎓 Courses Finished")
        st.write("4 structured courses")
        st.progress(0.6)
        st.caption("Data Analyst & Microsoft Excel Expert")

    with col4:
        st.markdown("### 🛠️ Technologies Explored")
        st.write("5 core tools")
        st.progress(0.7)
        st.caption("Python, Pandas, SQL, Streamlit, Visualization")

#TENTANG SAYA
def page_tentang_saya():
    st.title("👤 Tentang Saya")

    st.subheader("Latar Belakang")
    st.write(
        """
        Saya adalah seorang Data Analyst pemula yang memiliki ketertarikan besar dalam
        mengolah data menjadi insight yang bermanfaat.

        Saat ini, saya aktif mengembangkan kemampuan teknis dan pemahaman bisnis melalui
        pembelajaran mandiri serta proyek latihan.

        Fokus keterampilan yang sedang saya dalami meliputi:
        - **Data Exploration & Cleaning** (Pandas & NumPy)
        - **Data Visualization** (Tableau, Power BI, Streamlit)
        - **Statistical Analysis** (A/B Testing, Hypothesis Testing)
        - **Business Intelligence** (Dashboard & KPI Monitoring)
        """
    )

    # Technical Skills
    st.subheader("🛠️ Technical Skills Matrix")

    skills_data = get_skills_data()

    def skill_bar(level):
        return "🟩" * level + "⬜" * (5 - level)

    def skill_label(level):
        labels = {
            1: "Beginner",
            2: "Beginner+",
            3: "Intermediate",
            4: "Intermediate+",
            5: "Advanced"
        }
        return labels.get(level, "Unknown")

    for _, row in skills_data.iterrows():
        st.markdown(
            f"""
            **{row['Skill']}**  
            {skill_bar(row.get('Level', 0))}  
            _{skill_label(row.get('Level', 0))}_
            """
        )

    # Sertifikasi
    st.subheader("📚 Sertifikasi")

    col1, col2, col3 = st.columns(3)

    col1.markdown(
        """
        **Excel Expert Bootcamp Certification**  
        ✅ Certified, 2025
        """
    )

    col2.markdown(
        """
        **BNSP Data Analys Certification**  
        ✅ ⏳ On Progress
        """
    )

    col3.markdown(
        """
        **Micorosft Excel Expert Certification**  
        ✅ ⏳ On Progress
        """
    )

    #DATA
    def get_projects_data():
        return pd.DataFrame({
        "title": ["A", "B"],
        "category": ["Dashboard", "EDA"],
        "year": [2024, 2023]
        })
def page_proyek(projects_df, selected_category, selected_years):
    st.title("📂 Proyek")
    st.caption("Kumpulan proyek data yang pernah saya kerjakan")

    if not selected_category or not selected_years:
        st.info("Silakan pilih filter di sidebar")
        return

    filtered_projects = projects_df[
        (projects_df['category'].isin(selected_category)) &
        (projects_df['year'].isin(selected_years))
    ]
    
    if filtered_projects.empty:
        st.info("📭 Tidak ada proyek yang sesuai dengan filter Anda")
        return
        
    for _, project in filtered_projects.iterrows():
        st.markdown("---")

        col_left, col_right = st.columns([3, 1])

        #left
        with col_left:
            st.subheader(project["title"])
            st.write(project["description"])
            if "tools" in project:
                st.markdown(f"**Tools:** {project['tools']}")
            
            if "insights" in project:
                st.markdown("**Key Insights:**")
                for insight in project["insights"]:
                    st.markdown(f"- {insight}")
        st.link_button("🔗 Lihat Detail Proyek", project["url"])

        #right
        with col_right:
            st.markdown("**📌 Info Proyek**")
            st.markdown(f"- 🏷️ {project.get('category', '-')}")
            st.markdown(f"- 📅 {project.get('year', '-')}")

def page_dashboard():
    # Menampilkan judul halaman dengan emoji
    st.title("📊 Employee Attrition and Satisfaction Analysis Dashboard")

    # Menampilkan subheader
    st.subheader("Ringkasan Performa Data")

    # Mendapatkan data dashboard
    dashboard_data = generate_dashboard_data()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Employee", "1,470")
    col2.metric("Total Active Employee", "1,233")
    col3.metric("Total Attrition", "237")

    # Menampilkan garis pemisah
    render_divider()
    
    #PIE
    pie_col1, pie_col2 = st.columns(2)

    #pie chart 1
    with pie_col1:
        st.subheader("Attrition by Marital Status")

        marital_data ={
            "Marital Status": ["Married", "Single", "Divorced"],
            "Total": [673, 470, 327]
        }

        fig_marital = px.pie(
            marital_data,
            names="Marital Status",
            values="Total",
            title="Attrition Distribution by Marital Status",
            hole=0.4
        )

        fig_marital.update_traces(
            textinfo="label+percent",
            pull=[0.05, 0, 0]
        )

        st.plotly_chart(fig_marital, use_container_width=True)

    #pie chart 2
    with pie_col2:
        st.subheader("Attrition by Gender")
    
        gender_data = {
            "Gender": ["Male", "Female"],
            "Total": [882, 588]
        }

        fig_gender = px.pie(
        gender_data,
        names="Gender",
        values="Total",
        title="Attrition Distribution by Gender",
        hole=0.4
        )

        fig_gender.update_traces(
        textinfo="label+percent",
        pull=[0.05, 0]
        )
        st.plotly_chart(fig_gender, use_container_width=True)

    #bar chart
    st.subheader("Attrition by Job Satisfaction")

    # data job
    job_satisfaction_data = {
        "Job Satisfaction Level": ["1", "2", "3", "4"],
        "Total Employees": [66, 46, 73, 52]
    }

    #create bar chart
    fig_job_sat = px.bar(
        job_satisfaction_data,
        x="Job Satisfaction Level",
        y="Total Employees",
        title="Employee Count by Job Satisfaction Level",
        text="Total Employees"
    )

    #atur sumbu Y
    fig_job_sat.update_layout(
        yaxis=dict(
            tickmode="array",
            tickvals=[0, 20, 40, 60, 80],
            range=[0, 80]
        ),
        xaxis_title="Job Satisfaction",
        yaxis_title="Number of Employees"
    )
    st.plotly_chart(fig_job_sat, use_container_width=True)

def _is_valid_email(email: str) -> bool:
    """Validasi email sederhana untuk form."""
    if not email:
        return False
    # Pattern dasar: something@something.something
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
                # Tampilkan ringkasan
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
        📧 [rfwfian@gmail.com](mailto:rfwfian@gmail.com)
        """
    )

    # Menampilkan kontak LinkedIn di kolom kedua
    col2.markdown(
        """
        **LinkedIn**  
        💼 [linkedin.com/in/rfwfian](https://www.linkedin.com/in/rfwfian/)
        """
    )

    # Menampilkan kontak GitHub di kolom ketiga
    col3.markdown(
        """
        **WhatsApp**  
        📞 [wa.me/6282264551708](https://api.whatsapp.com/send/?phone=6282264551708&text&type=phone_number&app_absent=0)
        """
    )

def page_Reflection_Questions():

    st.markdown("""
    <div style="padding:25px; border-radius:12px; background-color:#f8f9fa;">
    <h3>1. Mengapa penting mendeploy project ke Streamlit dibandingkan hanya notebook ?</h3>

    <p>
    Mendeploy project ke <b>Streamlit</b> mengubah hasil analisis dari sekadar dokumen teknis
    menjadi <b>produk yang dapat digunakan langsung</b>.
    </p>

    <h4>Keterbatasan Jupyter Notebook</h4>
    <ul>
    <li>Sulit diakses oleh orang non-teknis</li>
    <li>Tidak intuitif tanpa pengetahuan Python</li>
    <li>Bersifat statis</li>
    </ul>

    <h4>Value Utama Streamlit</h4>

    <b>Aksesibilitas</b>
    <p>Aplikasi bisa dibuka melalui browser tanpa instalasi tambahan.</p>

    <b>Interaktivitas</b>
    <p>Pengguna dapat mengeksplorasi data secara real-time.</p>

    <b>Kemudahan bagi Stakeholder Non-Teknis</b>
    <p>Insight disajikan dalam bentuk dashboard yang siap dipakai.</p>

    <hr>
    <b>Kesimpulan:</b> Deployment ke Streamlit mengubah <i>data analysis</i> menjadi
    <b>data product</b>.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="padding:25px; border-radius:12px; background-color:#f8f9fa;">

    <h3>2. Mengapa interaktivitas menjadi bagian penting dari dashboard atau ML app?</h3>

    <p>
    Interaktivitas bukan sekadar fitur tambahan, tetapi <b>elemen inti</b> yang membuat
    dashboard atau ML app benar-benar berguna.
    </p>

    <p>
    Tanpa interaktivitas, dashboard hanya menampilkan insight dari satu sudut pandang,
    padahal setiap pengguna memiliki kebutuhan dan pertanyaan yang berbeda.
    </p>

    <h4>Alasan Mengapa Interaktivitas Sangat Penting</h4>

    <b>Mendukung eksplorasi mandiri (self-service analytics)</b>
    <p>
    Dengan slider, selectbox, atau filter, pengguna dapat menjawab pertanyaan mereka sendiri
    tanpa harus meminta ulang ke data analyst. Hal ini menghemat waktu dan mempercepat
    pengambilan keputusan.
    </p>

    <b>Membantu memahami dampak perubahan</b>
    <p>
    Dalam dashboard bisnis atau ML app, interaktivitas memungkinkan user melihat bagaimana
    perubahan input memengaruhi output, misalnya perubahan tahun, kategori, atau parameter
    model.
    </p>

    <b>Meningkatkan engagement dan trust</b>
    <p>
    Ketika pengguna dapat mencoba berbagai skenario sendiri, dashboard tidak terasa sebagai
    “black box”, melainkan transparan dan dapat diuji.
    </p>

    <b>Menjembatani gap teknis dan bisnis</b>
    <p>
    Interaktivitas membantu menerjemahkan kompleksitas teknis menjadi pengalaman visual yang
    mudah dipahami oleh stakeholder non-teknis.
    </p>

    <hr>
    <b>Kesimpulan:</b> Interaktivitas menjadikan dashboard dan ML app
    <b>lebih actionable, transparan, dan relevan secara bisnis</b>.
    </div>
    """, unsafe_allow_html=True)

def main():
    # Render sidebar navigation
    page = render_sidebar_nav()
    selected_category, selected_years = render_project_filter(page)

    projects_df = get_projects_data()

    # Build mapping dari sidebar labels ke page functions
    if page == "🏠 Beranda":
        page_beranda()
    elif page == "👤 Tentang Saya":
        page_tentang_saya()
    elif page == "📁 Proyek":
        page_proyek(projects_df, selected_category, selected_years)
    elif page == "📊 Dashboard":
        page_dashboard()
    elif page == "📧 Contact":
        page_contact()
    elif page == "📝Reflection Questions":
        page_Reflection_Questions()

if __name__ == "__main__":
    main()


