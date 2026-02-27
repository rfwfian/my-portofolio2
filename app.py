# Mengimpor library Streamlit untuk membuat aplikasi web interaktif
import streamlit as st

# Mengimpor Pandas untuk manipulasi dan analisis data
import pandas as pd

# Mengimpor NumPy untuk komputasi numerik
import numpy as np

# Mengimpor Plotly Express untuk visualisasi data interaktif
import plotly.express as px
import plotly.graph_objects as go

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
        ["🏠 Beranda", "👤 Tentang Saya", "📁 Proyek", "📊 Dashboard", "📊 E-Commerce Dashboard", "📊 Data Science", "📧 Contact", "📝Reflection Questions"]
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
    st.sidebar.caption("© 2026 Portofolio Saya")

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
            Halo,  saya **Rahadian Firstya Wisesa (Fian)**. Seorang **Data Analyst**
            yang berfokus pada mengubah data menjadi insight yang bermakna dan dapat ditindaklanjuti.

            Saya percaya bahwa data bukan hanya angka, tetapi cerita yang dapat membantu bisnis mengambil keputusan yang lebih tepat dan strategis.

            Melalui portofolio ini, saya menampilkan berbagai proyek analisis data, mulai dari eksplorasi data, visualisasi dashboard interaktif, hingga studi kasus bisnis.
            
            Silakan jelajahi setiap proyek.
            
            """
        )

        st.write("")

        col_btn1, col_btn2 = st.columns(2)

        with col_btn1:
            if st.button("📥 Download CV"):
                st.success("CV berhasil diunduh!")

        # with col_btn2:
        #     st.markdown(
        #         """
        #         <a href="https://wa.me/6282264551708" target="_blank">
        #             <button style="
        #                 background-color:#25D366;
        #                 color:white;
        #                 padding:10px 20px;
        #                 border:none;
        #                 border-radius:8px;
        #                 font-size:16px;
        #                 cursor:pointer;">
        #                 💬 Hubungi Saya
        #             </button>
        #         </a>
        #         """,
        #         unsafe_allow_html=True
        #     )

        with col_btn2:
            st.markdown("""
                <style>
                .wa-button {
                    background-color: #f0f2f6;
                    color: #333;
                    padding: 10px 20px;
                    border: 1px solid #d3d3d3;
                    border-radius: 8px;
                    font-size: 16px;
                    cursor: pointer;
                    transition: all 0.3s ease;
                }
        
                .wa-button:hover {
                    background-color: #25D366;
                    color: white;
                    border: 1px solid #25D366;
                }
                </style>
        
                <a href="https://wa.me/6282264551708" target="_blank">
                    <button class="wa-button">
                        💬 Hubungi Saya
                    </button>
                </a>
            """, unsafe_allow_html=True)

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
    st.subheader("📚 Sertifikasi & Bootcamp")

    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="card">
        <b>MySkill</b><br>
        Microsoft Excel Basic to Advanced<br>
        Juli 2025 - Agustus 2025</br>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        **dibimbing**  
        Data Analyst / Data Science  
        Agustus 2025 - Februari 2026
        """)
    
    with col3:
        st.markdown("""
        **KarirNex**  
        Pelatihan Sertifikasi Microsoft Excel Specialist  
        Desember 2025 - Desember 2025
        """)
    
    with col4:
        st.markdown("""
        **DQLab**  
        BNSP Data Analyst with SQL & Python in Google Platform  
        Desember 2025 - Februari 2026
        """)

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

def page_dashboardEComm():
    st.set_page_config(layout="wide")

    # =========================
    # HEADER
    # =========================
    header_col1, header_col2 = st.columns([5,1])

    with header_col1:
        st.markdown(
            "<h1 style='text-align:center;'>E-Commerce Analytics Overview</h1>",
            unsafe_allow_html=True
        )

    with header_col2:
        st.selectbox("Month Name", ["All", "Jan", "Feb", "Mar"])

    st.markdown("---")

    # =========================
    # MAIN LAYOUT
    # =========================
    left_col, right_col = st.columns([4,1])

    # =========================
    # LEFT SIDE (Charts)
    # =========================
    with left_col:

        # ROW 1
        top_left, top_right = st.columns(2)

        # 🎯 GAUGE
        with top_left:
            st.subheader("Checkout Conversion Performance")

            fig_gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=71.4,
                number={
                    'suffix': "%",
                    'valueformat': ".1f"
               },
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "#2E6BD9"},
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'value': 75
                    }
                }
            ))
            
            #add parameter
            fig_gauge.add_annotation(
                # posisi horizontal
                x=0.83,  
                # posisi vertikal
                y=0.75,  
                text="75.00%",
                showarrow=False,
                font=dict(size=14, color="black")
            )
            st.plotly_chart(fig_gauge, use_container_width=True)

        # 📊 USER ACTION TABLE
        with top_right:
            st.subheader("User Action Performance")

            action_data = pd.DataFrame({
                "Action": ["read_reviews", "search", "product_view", "add_to_cart", "checkout", "click_wishlist_page", "purchase", "first_app_open", "add_review", "add_to_wishlist", "product_review", "add_to_wishist"],
                "Count of Action": [343, 320, 292, 280, 202, 202, 201, 121, 69, 33, 22, 5]
            })

            st.dataframe(action_data, use_container_width=True)

        # ROW 2
        bottom_left, bottom_right = st.columns(2)

        # 📊 CATEGORY PERFORMANCE
        with bottom_left:
            st.subheader("Category Performance")

            cat_data = pd.DataFrame({
                "Category": ["Tablets", "Mobile & Acc", "Digital Devices",
                             "Women's Fashion", "Laptop & Desktop",
                             "TV & Appliances", "Accessories"],
                "Revenue": [225000, 127000, 122000, 103000, 90000, 85000, 77000]
            })

            cat_sorted = cat_data.sort_values("Revenue")

            fig_cat = px.bar(
                cat_sorted,
                x="Revenue",
                y="Category",
                orientation="h",
                text=cat_sorted["Revenue"].apply(lambda x: f"{x/1000:.0f}K"),
                color_discrete_sequence=["#2E6BD9"]
            )

            fig_cat.update_traces(textposition="outside") #samping

            fig_cat.update_layout(
                xaxis_title="Total Revenue",
                yaxis_title="Category"
            )

            st.plotly_chart(fig_cat, use_container_width=True)

        # 📊 SUB CATEGORY PERFORMANCE
        with bottom_right:
            st.subheader("Sub Category Performance")

            subcat_data = pd.DataFrame({
                "SubCategory": ["Watches", "Tops", "Mobile", "Cases",
                                "iPad", "Laptop", "Ethnic Wear"],
                "Count": [36, 27, 25, 23, 21, 21, 18]
            })

            sub_sorted = subcat_data.sort_values("Count")

            fig_sub = px.bar(
                sub_sorted,
                x="Count",
                y="SubCategory",
                orientation="h",
                text="Count",
                color_discrete_sequence=["#2E6BD9"]
            )

            fig_sub.update_traces(textposition="outside")

            fig_sub.update_layout(
                xaxis_title="Count of SubCategory",
                yaxis_title="SubCategory"
            )

            st.plotly_chart(fig_sub, use_container_width=True)

        # =========================
        # RIGHT SIDE (KPI CARDS)
        # =========================
        st.markdown("""
        <style>
        .kpi-column {
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 100%;
        }
        </style>
        """, unsafe_allow_html=True)
        
        with right_col:
            st.markdown('<div class="kpi-column">', unsafe_allow_html=True)
        
            st.metric("Total Users", "401")
            st.metric("Total Sessions", "2064")
            st.metric("Total Revenue", "2M")
            st.metric("Total Transactions", "201")
            st.metric("Sum of Quantity", "596")
        
            st.markdown('</div>', unsafe_allow_html=True)

def page_dataScience():
    # intro
    col1, col2 = st.columns([2, 1])

    with col1:
        st.title("🧠 Portofolio Data Science")

        st.markdown(
            """
            Pada halaman ini, saya menampilkan proyek data science yang telah saya kerjakan,
            yaitu *Customer Churn Prediction Using Machine Learning*.
            """
        )

        st.write("")

        col_btn1, col_btn2 = st.columns(2)

        with col_btn1:
            st.link_button(
                "🔵 Lihat Detail Proyek Pada Google Colab",
                "https://colab.research.google.com/drive/1nCAYJYnvvTfq3VK_GKIdV3gRVORVjjLQ?usp=sharing"
            )
        
        with col_btn2:
            st.link_button(
                "🧑‍💻 Lihat Detail Proyek Pada Google Drive",
                "https://drive.google.com/drive/folders/1bPigA-AI1PplNa0_ZwGsF7Qd3Gy9kWU9?usp=drive_link"
            )

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
    elif page == "📊 E-Commerce Dashboard":
        page_dashboardEComm()
    elif page == "📊 Data Science":
        page_dataScience()
    elif page == "📧 Contact":
        page_contact()
    elif page == "📝Reflection Questions":
        page_Reflection_Questions()

if __name__ == "__main__":
    main()















































