from streamlit_lottie import st_lottie
import requests
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# fungsi lottie dengan error handling
def load_lottieurl(url: str):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# Custom CSS untuk styling yang lebih menarik
def load_css():
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Main container styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .header-container h1 {
        color: white !important;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 2.5rem;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .header-subtitle {
        color: rgba(255,255,255,0.9) !important;
        font-size: 1.2rem;
        font-weight: 300;
        margin-top: 1rem;
    }
    
    /* Feature cards */
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        border: 1px solid #e1e5e9;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        height: 100%;
        text-align: center;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    }
    
    .feature-title {
        color: #2c3e50;
        font-weight: 600;
        margin-bottom: 1rem;
        font-size: 1.1rem;
    }
    
    .feature-description {
        color: #6c757d;
        line-height: 1.6;
        font-size: 0.95rem;
    }
    
    /* Info sections */
    .info-section {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        border-left: 5px solid #667eea;
    }
    
    .info-section h3 {
        color: #2c3e50;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    .css-1d391kg .css-1v0mbdj {
        color: white;
        font-weight: 600;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-weight: 500;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Success/Info/Warning messages */
    .stSuccess, .stInfo, .stWarning {
        border-radius: 10px;
        border: none;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    /* Number input styling */
    .stNumberInput > div > div > input {
        border-radius: 8px;
        border: 2px solid #e1e5e9;
        transition: border-color 0.3s ease;
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        border-radius: 8px;
        border: 2px solid #e1e5e9;
        transition: border-color 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 15px;
        margin-top: 3rem;
        color: #6c757d;
        font-weight: 500;
    }
    
    /* About page specific styling */
    .about-hero {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }
    
    .about-section {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        margin-bottom: 2rem;
        border-left: 5px solid #4facfe;
    }
    
    .principle-item {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 4px solid #28a745;
    }
    
    .application-item {
        background: #fff3cd;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border-left: 4px solid #ffc107;
    }
    </style>
    """, unsafe_allow_html=True)

# Pengaturan halaman
st.set_page_config(
    page_title="Aplikasi Perhitungan Kadar Spektrofotometri UV-Vis",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
load_css()

# Fungsi untuk setiap halaman
def homepage():
    # Header dengan gradient background
    st.markdown("""
    <div class="header-container">
        <h1>🧪 Aplikasi Perhitungan Kadar Spektrofotometri UV-Vis</h1>
        <p class="header-subtitle">Platform Digital untuk Analisis Kuantitatif dan Evaluasi Akurasi Metode Spektrofotometri</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Hero section dengan animasi dan penjelasan
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        st.markdown("""
        <div class="info-section">
            <h3>🔬 Tentang Spektrofotometri UV-Vis</h3>
            <p style="text-align: justify; line-height: 1.8;">
                Spektrofotometri UV-Vis adalah teknik analisis instrumental yang mengukur absorbansi cahaya 
                oleh molekul pada rentang panjang gelombang ultraviolet (200-400 nm) dan cahaya tampak (400-800 nm). 
                Teknik ini berdasarkan pada Hukum Lambert-Beer yang menyatakan hubungan linier antara absorbansi 
                dengan konsentrasi larutan.
            </p>
            
            <h4 style="color: #667eea; margin-top: 1.5rem;">🔧 Komponen Utama Instrumen:</h4>
            <ul style="line-height: 1.8;">
                <li><strong>Sumber Cahaya:</strong> Lampu deuterium (UV) dan tungsten (Vis)</li>
                <li><strong>Monokromator:</strong> Memilih panjang gelombang spesifik</li>
                <li><strong>Kuvet:</strong> Wadah sampel dengan jalur optik tetap</li>
                <li><strong>Detektor:</strong> Mengkonversi sinyal cahaya menjadi data digital</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        try:
            st.image(
                "https://lsi.fleischhacker-asia.biz/wp-content/uploads/2022/05/Spektrofotometer-UV-VIS-Fungsi-Prinsip-Kerja-dan-Cara-Kerjanya.jpg", 
                caption="🖼️ Spektrofotometer UV-Vis (Sumber: PT. Laboratorium Solusi Indonesia)", 
                use_container_width=True
            )
        except:
            # Fallback jika gambar tidak bisa dimuat
            st.markdown("""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        padding: 3rem; border-radius: 15px; text-align: center; color: white;">
                <h3>🔬 Spektrofotometer UV-Vis</h3>
                <p>Instrumen untuk analisis absorbansi cahaya UV dan Visible</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Tambahan info box
        st.info("💡 **Prinsip Kerja:** Cahaya melewati sampel, sebagian diserap molekul, dan intensitas cahaya yang diteruskan diukur untuk menentukan konsentrasi.")
    
    # Section aplikasi dan manfaat
    st.markdown("""
    <div class="info-section">
        <h3>🌍 Aplikasi Spektrofotometri UV-Vis</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div class="application-item">
                <strong>🏥 Farmasi & Kesehatan</strong><br>
                Analisis obat, vitamin, dan senyawa bioaktif
            </div>
            <div class="application-item">
                <strong>🌊 Lingkungan</strong><br>
                Monitoring kualitas air dan deteksi polutan
            </div>
            <div class="application-item">
                <strong>🍎 Pangan</strong><br>
                Analisis kandungan nutrisi dan kontaminan
            </div>
            <div class="application-item">
                <strong>🧪 Industri Kimia</strong><br>
                Kontrol kualitas dan analisis bahan baku
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Fitur aplikasi dengan card design
    st.markdown("<h2 style='text-align: center; color: #2c3e50; margin: 3rem 0 2rem 0;'>⚙️ Fitur Unggulan Aplikasi</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    # Load animasi
    lottie_kadar = load_lottieurl("https://lottie.host/765b6ca4-5e8a-4baf-b1f8-703bc83b6e12/eKBFeaUGKE.json")
    lottie_rpd = load_lottieurl("https://lottie.host/3404aaaa-4440-49d3-8015-a91ad8a5d529/hgcgSw6HUz.json")
    lottie_rec = load_lottieurl("https://lottie.host/c23cbd35-6d04-490e-8a28-162d08f97c2e/dgvwoV7Ytb.json")

    with col1:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        if lottie_kadar:
            try:
                st_lottie(lottie_kadar, height=120, key="kadar")
            except:
                st.markdown("🔬", unsafe_allow_html=True)
        else:
            st.markdown("<div style='text-align: center; font-size: 4rem;'>📏</div>", unsafe_allow_html=True)
        st.markdown('<div class="feature-title">📏 Perhitungan C Terukur & Kadar</div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-description">Menghitung konsentrasi terukur dan kadar senyawa berdasarkan nilai absorbansi menggunakan persamaan regresi linier kurva standar</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        if lottie_rpd:
            try:
                st_lottie(lottie_rpd, height=120, key="rpd")
            except:
                st.markdown("🔄", unsafe_allow_html=True)
        else:
            st.markdown("<div style='text-align: center; font-size: 4rem;'>🔄</div>", unsafe_allow_html=True)
        st.markdown('<div class="feature-title">🔄 Perhitungan %RPD</div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-description">Evaluasi presisi dan kehandalan pengukuran duplikat dengan menghitung Relative Percent Difference untuk kontrol kualitas</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="feature-card">', unsafe_allow_html=True)
        if lottie_rec:
            try:
                st_lottie(lottie_rec, height=120, key="rec")
            except:
                st.markdown("🎯", unsafe_allow_html=True)
        else:
            st.markdown("<div style='text-align: center; font-size: 4rem;'>🎯</div>", unsafe_allow_html=True)
        st.markdown('<div class="feature-title">🎯 Perhitungan %Recovery</div>', unsafe_allow_html=True)
        st.markdown('<div class="feature-description">Mengukur akurasi metode analisis melalui perhitungan persentase perolehan kembali analit yang ditambahkan</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Keunggulan aplikasi
    st.markdown("""
    <div class="info-section" style="margin-top: 3rem;">
        <h3>✨ Keunggulan Aplikasi</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 1rem;">
            <div class="principle-item">
                <strong>🚀 User-Friendly Interface</strong><br>
                Antarmuka intuitif dengan panduan langkah demi langkah
            </div>
            <div class="principle-item">
                <strong>🎯 Akurasi Tinggi</strong><br>
                Perhitungan presisi hingga 7 digit desimal
            </div>
            <div class="principle-item">
                <strong>📊 Multiple Calculations</strong><br>
                Mendukung perhitungan batch hingga 50 sampel
            </div>
            <div class="principle-item">
                <strong>📱 Responsive Design</strong><br>
                Dapat diakses dari berbagai perangkat
            </div>
            <div class="principle-item">
                <strong>⚡ Real-time Results</strong><br>
                Hasil perhitungan langsung dan interpretasi otomatis
            </div>
            <div class="principle-item">
                <strong>🔍 Quality Control</strong><br>
                Evaluasi otomatis berdasarkan standar analitis
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="footer">
        <p>© 2025 🧪 Aplikasi Perhitungan Kadar Spektrofotometri UV-Vis | Kelompok 4 1F</p>
        <p style="font-size: 0.9rem; margin-top: 0.5rem;">Dikembangkan untuk mendukung analisis kuantitatif yang akurat dan efisien</p>
    </div>
    """, unsafe_allow_html=True)

# Halaman Tentang Aplikasi
def tentang():
    st.markdown("""
    <div class="about-hero">
        <h1>📖 Tentang Aplikasi</h1>
        <p style="font-size: 1.2rem; margin-top: 1rem;">Platform Digital untuk Analisis Spektrofotometri UV-Vis</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Overview aplikasi
    st.markdown("""
    <div class="about-section">
        <h3>🎯 Overview Aplikasi</h3>
        <p style="text-align: justify; line-height: 1.8; font-size: 1.1rem;">
            Aplikasi Perhitungan Kadar Spektrofotometri UV-Vis adalah platform digital yang dirancang khusus 
            untuk membantu analis laboratorium, mahasiswa, dan peneliti dalam melakukan perhitungan analisis 
            kuantitatif menggunakan metode spektrofotometri UV-Vis. Aplikasi ini mengintegrasikan berbagai 
            formula perhitungan yang essential dalam analisis spektrofotometri untuk menghasilkan data yang 
            akurat dan reliabel.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Tujuan dan manfaat
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="about-section">
            <h3>🎯 Tujuan Aplikasi</h3>
            <ul style="line-height: 2;">
                <li><strong>Mempermudah</strong> perhitungan konsentrasi terukur dari data absorbansi</li>
                <li><strong>Mengotomatisasi</strong> perhitungan kadar dengan berbagai metode</li>
                <li><strong>Mengevaluasi</strong> presisi melalui perhitungan %RPD</li>
                <li><strong>Mengukur</strong> akurasi metode melalui %Recovery</li>
                <li><strong>Menyediakan</strong> interpretasi hasil berdasarkan standar analitis</li>
                <li><strong>Mengurangi</strong> kesalahan perhitungan manual</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="about-section">
            <h3>💡 Manfaat Aplikasi</h3>
            <ul style="line-height: 2;">
                <li><strong>Efisiensi Waktu:</strong> Perhitungan otomatis dan cepat</li>
                <li><strong>Akurasi Tinggi:</strong> Minimalisir human error</li>
                <li><strong>Batch Processing:</strong> Hingga 50 sampel sekaligus</li>
                <li><strong>Quality Control:</strong> Evaluasi otomatis hasil</li>
                <li><strong>User-Friendly:</strong> Interface yang mudah dipahami</li>
                <li><strong>Accessibility:</strong> Dapat diakses kapan saja</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Fitur detail
    st.markdown("""
    <div class="about-section">
        <h3>🔧 Fitur Lengkap Aplikasi</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 1rem;">
            <div class="principle-item">
                <h4 style="color: #667eea; margin-bottom: 0.5rem;">📏 Perhitungan C Terukur</h4>
                <p>Menghitung konsentrasi terukur dari nilai absorbansi menggunakan persamaan linier:</p>
                <code style="background: #f8f9fa; padding: 0.3rem; border-radius: 4px;">C = (A - b) / m</code>
                <p style="margin-top: 0.5rem; font-size: 0.9rem;">Mendukung batch calculation hingga 50 sampel</p>
            </div>
            
            <div class="principle-item">
                <h4 style="color: #28a745; margin-bottom: 0.5rem;">📊 Perhitungan Kadar</h4>
                <p><strong>Tipe A:</strong> Tanpa bobot sampel (mg/L)</p>
                <code style="background: #f8f9fa; padding: 0.3rem; border-radius: 4px;">Kadar = (C - Blanko) × FP</code>
                <p><strong>Tipe B:</strong> Dengan bobot sampel (mg/kg)</p>
                <code style="background: #f8f9fa; padding: 0.3rem; border-radius: 4px;">Kadar = (C × V) / W</code>
            </div>
            
            <div class="principle-item">
                <h4 style="color: #ffc107; margin-bottom: 0.5rem;">🔄 Perhitungan %RPD</h4>
                <p>Relative Percent Difference untuk evaluasi presisi:</p>
                <code style="background: #f8f9fa; padding: 0.3rem; border-radius: 4px;">%RPD = |C1-C2| / ((C1+C2)/2) × 100%</code>
                <p style="margin-top: 0.5rem; font-size: 0.9rem;">Interpretasi otomatis: < 5% = konsisten</p>
            </div>
            
            <div class="principle-item">
                <h4 style="color: #dc3545; margin-bottom: 0.5rem;">🎯 Perhitungan %Recovery</h4>
                <p>Persentase perolehan kembali untuk evaluasi akurasi:</p>
                <code style="background: #f8f9fa; padding: 0.3rem; border-radius: 4px;">%REC = (C3-C1) / C2 × 100%</code>
                <p style="margin-top: 0.5rem; font-size: 0.9rem;">Range optimal: 80-120%</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Basis ilmiah
    st.markdown("""
    <div class="about-section">
        <h3>🧬 Basis Ilmiah</h3>
        <div class="principle-item" style="margin-bottom: 1rem;">
            <h4 style="color: #667eea;">📐 Hukum Lambert-Beer</h4>
            <p style="text-align: justify;">
                Aplikasi ini berdasarkan pada Hukum Lambert-Beer yang menyatakan hubungan linier antara 
                absorbansi (A) dengan konsentrasi (C): <strong>A = ε × b × C</strong>, dimana ε adalah 
                koefisien absorptivitas molar dan b adalah panjang jalur optik.
            </p>
        </div>
        
        <div class="principle-item" style="margin-bottom: 1rem;">
            <h4 style="color: #28a745;">📊 Validasi Metode Analitik</h4>
            <p style="text-align: justify;">
                Parameter %RPD dan %Recovery mengacu pada guidelines internasional seperti ICH, AOAC, dan EPA 
                untuk validasi metode analitik, memastikan hasil analisis yang reliable dan acceptable.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Target pengguna
    st.markdown("""
    <div class="about-section">
        <h3>👥 Target Pengguna</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
            <div class="application-item">
                <strong>🔬 Analis Laboratorium</strong><br>
                Quality control dan analisis rutin
            </div>
            <div class="application-item">
                <strong>🎓 Mahasiswa</strong><br>
                Pembelajaran dan praktikum analitik
            </div>
            <div class="application-item">
                <strong>👨‍🔬 Peneliti</strong><br>
                Riset dan pengembangan metode
            </div>
            <div class="application-item">
                <strong>🏭 Industri</strong><br>
                Kontrol kualitas produk
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Fungsi c terukur dengan styling yang diperbaiki
def c_terukur():
    st.markdown("""
    <div class="header-container">
        <h1>🔬 Perhitungan C Terukur</h1>
        <p class="header-subtitle">Menghitung konsentrasi terukur dari nilai absorbansi menggunakan persamaan regresi linier</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Animasi Lottie dengan error handling
    lottie_url = "https://lottie.host/5ee6c7e7-3c7b-473f-b75c-df412fe210cc/kF9j77AAsG.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            try:
                st_lottie(lottie_json, height=200, key="anim_c_terukur")
            except:
                st.markdown("<div style='text-align: center; font-size: 6rem;'>🔬</div>", unsafe_allow_html=True)

    # Info formula
    st.markdown("""
    <div class="info-section">
        <h3>📐 Formula Perhitungan</h3>
        <p style="text-align: center; font-size: 1.2rem; font-weight: 500;">
            <code style="background: #667eea; color: white; padding: 0.5rem 1rem; border-radius: 8px; font-size: 1.1rem;">
            C terukur = (A - b) / m
            </code>
        </p>
        <p style="text-align: center; margin-top: 1rem; color: #6c757d;">
            Dimana: A = Absorbansi, b = Intercept, m = Slope (gradien kurva standar)
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Pilih jumlah perhitungan
    n = st.number_input("Jumlah perhitungan sampel (maks. 50)", min_value=1, max_value=50, value=1, step=1)

    # Tempat menyimpan hasil
    results = []

    for i in range(1, n+1):
        st.markdown(f"""
        <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin: 1rem 0;">
            <h4 style="color: #667eea; margin-bottom: 1rem;">📊 Sampel #{i}</h4>
        </div>
        """, unsafe_allow_html=True)
        
        nama = st.text_input(f"Nama Sampel #{i}", value=f"Sample {i}", key=f"nama_{i}")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            absorban = st.number_input(f"Absorbansi (A)", format="%.4f",
                                       min_value=0.0, step=0.0001, key=f"a_{i}")
        with col2:
            intercept = st.number_input(f"Intercept (b)", format="%.4f",
                                        min_value=0.0, step=0.0001, key=f"b_{i}")
        with col3:
            slope = st.number_input(f"Slope (m)", format="%.4f",
                                    min_value=0.0001, step=0.0001, key=f"m_{i}")

        # Hitung segera, tapi tampilin nanti
        c_ukur = (absorban - intercept) / slope
        # Simpan nama + hasil rounded 4 desimal
        results.append((nama, round(c_ukur, 4)))

        st.markdown("---")

    # Tampilkan semua hasil
    if st.button("🧮 Hitung Semua C Terukur", key="btn_c_terukur"):
        st.markdown("## 📋 Hasil Perhitungan C Terukur")
        for nama, nilai in results:
            st.success(f"📊 Konsentrasi terukur pada '{nama}' = **{nilai:.4f} mg/L (ppm)**")

# Fungsi Kadar dengan styling yang diperbaiki
def kadar():
    st.markdown("""
    <div class="header-container">
        <h1>📏 Perhitungan Kadar</h1>
        <p class="header-subtitle">Menghitung kadar senyawa dengan dua metode: tanpa bobot sampel dan dengan bobot sampel</p>
    </div>
    """, unsafe_allow_html=True)

    # Animasi lottie dengan error handling
    lottie_url = "https://lottie.host/765b6ca4-5e8a-4baf-b1f8-703bc83b6e12/eKBFeaUGKE.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            try:
                st_lottie(lottie_json, height=200, key="anim_kadar")
            except:
                st.markdown("<div style='text-align: center; font-size: 6rem;'>📏</div>", unsafe_allow_html=True)

    # Pilih tipe perhitungan
    tipe = st.radio("Pilih jenis perhitungan:",
                    ("A. Tanpa Bobot Sample (ppm/mg·L⁻¹)",
                     "B. Dengan Bobot Sample (mg·kg⁻¹)"))

    # Info formula berdasarkan tipe
    if tipe.startswith("A"):
        st.markdown("""
        <div class="info-section">
            <h3>📐 Formula Tipe A (Tanpa Bobot Sample)</h3>
            <p style="text-align: center; font-size: 1.2rem; font-weight: 500;">
                <code style="background: #28a745; color: white; padding: 0.5rem 1rem; border-radius: 8px; font-size: 1.1rem;">
                Kadar = (C terukur - C blanko) × Faktor Pengenceran
                </code>
            </p>
            <p style="text-align: center; margin-top: 1rem; color: #6c757d;">
                Hasil dalam satuan: mg/L (ppm)
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="info-section">
            <h3>📐 Formula Tipe B (Dengan Bobot Sample)</h3>
            <p style="text-align: center; font-size: 1.2rem; font-weight: 500;">
                <code style="background: #dc3545; color: white; padding: 0.5rem 1rem; border-radius: 8px; font-size: 1.1rem;">
                Kadar = (C terukur × Volume labu takar) / Bobot sampel
                </code>
            </p>
            <p style="text-align: center; margin-top: 1rem; color: #6c757d;">
                Hasil dalam satuan: mg/kg
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Jumlah sampel (1–50)
    n = st.number_input("Jumlah sampel (maks. 50)", min_value=1, max_value=50, value=1, step=1)

    results = []

    for i in range(1, n+1):
        st.markdown(f"""
        <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin: 1rem 0;">
            <h4 style="color: #667eea; margin-bottom: 1rem;">📊 Sampel #{i}</h4>
        </div>
        """, unsafe_allow_html=True)
        
        nama = st.text_input(f"Nama Sampel #{i}", f"Sample {i}", key=f"k_nama_{i}")

        if tipe.startswith("A"):
            # A: tanpa bobot sample
            col1, col2, col3 = st.columns(3)
            with col1:
                c_ukur = st.number_input(
                    f"C terukur (mg/L)",
                    min_value=0.0, value=0.0, step=0.0000001,
                    format="%.7f",
                    key=f"kA_c_{i}"
                )
            with col2:
                blanko = st.number_input(
                    f"C terukur blanko (mg/L)",
                    min_value=0.0, value=0.0, step=0.0000001,
                    format="%.7f",
                    key=f"kA_b_{i}"
                )
            with col3:
                faktor = st.number_input(
                    f"Faktor Pengenceran",
                    min_value=0.0, value=0.0, step=0.0000001,
                    format="%.7f",
                    key=f"kA_f_{i}"
                )

            nilai = (c_ukur - blanko) * faktor
            satuan = "mg/L (ppm)"

        else:
            # B: dengan bobot sample
            col1, col2, col3 = st.columns(3)
            with col1:
                c_ukur = st.number_input(
                    f"C terukur (mg/L)",
                    min_value=0.0, value=0.0, step=0.0000001,
                    format="%.7f",
                    key=f"kB_c_{i}"
                )
            with col2:
                vol = st.number_input(
                    f"Volume labu takar (L)",
                    min_value=0.0, value=0.0, step=0.0000001,
                    format="%.7f",
                    key=f"kB_v_{i}"
                )
            with col3:
                bobot = st.number_input(
                    f"Bobot sample (kg)",
                    min_value=0.0, value=0.0, step=0.0000001,
                    format="%.7f",
                    key=f"kB_w_{i}"
                )

            nilai = (c_ukur * vol) / bobot if bobot != 0 else 0.0
            satuan = "mg/kg"

        # simpan tanpa membulatkan—kita bulatkan saat tampil
        results.append((nama, nilai, satuan))
        st.markdown("---")

    # tombol hitung
    if st.button("🧮 Hitung Kadar", key="btn_kadar"):
        st.markdown("## 📋 Hasil Perhitungan Kadar")
        for nama, nilai, satuan in results:
            st.success(f"📊 Kadar pada '{nama}' = **{nilai:.7f} {satuan}**")
            
# Fungsi RPD dengan styling yang diperbaiki
def rpd():
    st.markdown("""
    <div class="header-container">
        <h1>🔄 Perhitungan %RPD</h1>
        <p class="header-subtitle">Evaluasi presisi dan kehandalan pengukuran duplikat melalui Relative Percent Difference</p>
    </div>
    """, unsafe_allow_html=True)

    # Animasi lottie dengan error handling
    lottie_url = "https://lottie.host/3404aaaa-4440-49d3-8015-a91ad8a5d529/hgcgSw6HUz.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            try:
                st_lottie(lottie_json, height=200, key="anim_rpd")
            except:
                st.markdown("<div style='text-align: center; font-size: 6rem;'>🔄</div>", unsafe_allow_html=True)

    # Info formula
    st.markdown("""
    <div class="info-section">
        <h3>📐 Formula %RPD</h3>
        <p style="text-align: center; font-size: 1.2rem; font-weight: 500;">
            <code style="background: #ffc107; color: black; padding: 0.5rem 1rem; border-radius: 8px; font-size: 1.1rem;">
            %RPD = |C1 - C2| / ((C1 + C2)/2) × 100%
            </code>
        </p>
        <p style="text-align: center; margin-top: 1rem; color: #6c757d;">
            Dimana: C1 dan C2 adalah hasil pengukuran duplikat
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Pilihan jenis perhitungan
    tipe = st.radio("Pilih jenis perhitungan RPD:",
                    ("A. Single RPD", "B. Multiple RPD"))

    # Keterangan edukatif
    col1, col2 = st.columns(2)
    with col1:
        st.info("✅ **Nilai %RPD < 5%** menunjukkan bahwa hasil pengukuran sangat konsisten dan reprodusibel, sehingga dapat dianggap andal dan diterima secara analitis.")
    with col2:
        st.warning("⚠️ **Nilai %RPD ≥ 5%** mengindikasikan adanya perbedaan yang cukup besar antara dua hasil pengukuran, sehingga menunjukkan kurangnya konsistensi atau kemungkinan adanya kesalahan dalam prosedur analisis.")

    rpd_results = []

    if tipe.startswith("A"):
        # SINGLE RPD
        st.markdown("""
        <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin: 1rem 0;">
            <h4 style="color: #667eea; margin-bottom: 1rem;">📊 Input Data RPD</h4>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            c1 = st.number_input("Masukkan C1", min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key="rpd_c1")
        with col2:
            c2 = st.number_input("Masukkan C2", min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key="rpd_c2")

        if st.button("🧮 Hitung %RPD", key="btn_rpd_single"):
            num = abs(c1 - c2)
            den = (c1 + c2) / 2 if (c1 + c2) != 0 else 1
            rpd_val = num / den * 100

            st.markdown("## 📋 Hasil Perhitungan %RPD")
            st.success(f"📊 %RPD = **{rpd_val:.7f}%**")
            
            if rpd_val < 5:
                st.info("✅ **Kesimpulan:** Hasil pengukuran konsisten dan dapat diterima.")
            else:
                st.warning("⚠️ **Kesimpulan:** Hasil pengukuran tidak konsisten atau kurang andal.")

    else:
        # MULTIPLE RPD
        n = st.number_input("Jumlah perhitungan RPD (maks. 50)", min_value=1, max_value=50, value=1, step=1)
        
        for i in range(1, n + 1):
            st.markdown(f"""
            <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin: 1rem 0;">
                <h4 style="color: #667eea; margin-bottom: 1rem;">📊 Perhitungan RPD #{i}</h4>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                c1 = st.number_input(f"C1 untuk RPD #{i}", min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key=f"rpd_m_c1_{i}")
            with col2:
                c2 = st.number_input(f"C2 untuk RPD #{i}", min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key=f"rpd_m_c2_{i}")

            num = abs(c1 - c2)
            den = (c1 + c2) / 2 if (c1 + c2) != 0 else 1
            rpd_val = num / den * 100

            rpd_results.append((i, rpd_val))
            st.markdown("---")

        if st.button("🧮 Hitung Semua RPD", key="btn_rpd_multiple"):
            st.markdown("## 📋 Hasil Perhitungan %RPD")
            all_consistent = True

            for i, val in rpd_results:
                st.write(f"🔹 **%RPD #{i}** = **{val:.7f}%**")
                if val < 5:
                    st.info(f"✅ RPD #{i} menunjukkan hasil konsisten")
                else:
                    st.warning(f"⚠️ RPD #{i} menunjukkan hasil tidak konsisten")
                    all_consistent = False

            # Kesimpulan akhir
            st.markdown("---")
            if all_consistent:
                st.success("✅ **Kesimpulan Akhir:** Semua hasil perhitungan menunjukkan %RPD < 5%, sehingga dapat disimpulkan bahwa hasil analisis RPD konsisten dan dapat diterima.")
            else:
                st.error("❌ **Kesimpulan Akhir:** Terdapat hasil perhitungan dengan %RPD ≥ 5%, sehingga dapat disimpulkan bahwa analisis RPD tidak sepenuhnya konsisten.")

# Fungsi REC dengan styling yang diperbaiki
def rec():
    st.markdown("""
    <div class="header-container">
        <h1>🎯 Perhitungan %Recovery</h1>
        <p class="header-subtitle">Mengukur akurasi metode analisis melalui perhitungan persentase perolehan kembali analit</p>
    </div>
    """, unsafe_allow_html=True)

    # Animasi lottie dengan error handling
    lottie_url = "https://lottie.host/c23cbd35-6d04-490e-8a28-162d08f97c2e/dgvwoV7Ytb.json"
    lottie_json = load_lottieurl(lottie_url)
    if lottie_json:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            try:
                st_lottie(lottie_json, height=200, key="anim_rec")
            except:
                st.markdown("<div style='text-align: center; font-size: 6rem;'>🎯</div>", unsafe_allow_html=True)

    # Info formula
    st.markdown("""
    <div class="info-section">
        <h3>📐 Formula %Recovery</h3>
        <p style="text-align: center; font-size: 1.2rem; font-weight: 500;">
            <code style="background: #dc3545; color: white; padding: 0.5rem 1rem; border-radius: 8px; font-size: 1.1rem;">
            %REC = (C3 - C1) / C2 × 100%
            </code>
        </p>
        <p style="text-align: center; margin-top: 1rem; color: #6c757d;">
            C1 = Konsentrasi sampel, C2 = Konsentrasi spike, C3 = Konsentrasi sampel + spike
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Pilihan jenis perhitungan
    tipe = st.radio("Pilih jenis perhitungan Recovery:",
                    ("A. Single REC", "B. Multiple REC"))

    # Keterangan edukatif
    col1, col2 = st.columns(2)
    with col1:
        st.info("✅ **Nilai %Recovery 80-120%** menunjukkan bahwa metode analisis memiliki akurasi yang baik, di mana jumlah analit yang terukur mendekati jumlah yang sebenarnya. Ini menandakan bahwa tidak ada kehilangan signifikan atau interferensi yang berarti selama proses analisis.")
    with col2:
        st.warning("⚠️ **Nilai %Recovery di luar 80-120%** mengindikasikan adanya ketidaksesuaian antara jumlah analit yang seharusnya dan yang terukur, sehingga menandakan akurasi yang buruk.")

    rec_results = []

    if tipe.startswith("A"):
        # SINGLE REC
        st.markdown("""
        <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin: 1rem 0;">
            <h4 style="color: #667eea; margin-bottom: 1rem;">📊 Input Data Recovery</h4>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            c1 = st.number_input("C1 (Konsentrasi sampel)", min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key="rec_c1")
        with col2:
            c2 = st.number_input("C2 (Konsentrasi spike)", min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key="rec_c2")
        with col3:
            c3 = st.number_input("C3 (Konsentrasi sampel+spike)", min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key="rec_c3")

        if st.button("🧮 Hitung %REC", key="btn_rec_single"):
            den = c2 if c2 != 0 else 1
            rec_val = (c3 - c1) / den * 100

            st.markdown("## 📋 Hasil Perhitungan %Recovery")
            st.success(f"📊 %REC = **{rec_val:.7f}%**")

            if 80 <= rec_val <= 120:
                st.info("✅ **Kesimpulan:** Hasil menunjukkan akurasi yang baik.")
            else:
                st.warning("⚠️ **Kesimpulan:** Hasil menunjukkan akurasi yang buruk atau ada gangguan dalam analisis.")

    else:
        # MULTIPLE REC
        n = st.number_input("Jumlah perhitungan REC (maks. 50)", min_value=1, max_value=50, value=1, step=1)
        
        for i in range(1, n + 1):
            st.markdown(f"""
            <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); margin: 1rem 0;">
                <h4 style="color: #667eea; margin-bottom: 1rem;">📊 Perhitungan REC #{i}</h4>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                c1 = st.number_input(f"C1 untuk REC #{i}", min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key=f"rec_m_c1_{i}")
            with col2:
                c2 = st.number_input(f"C2 untuk REC #{i}", min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key=f"rec_m_c2_{i}")
            with col3:
                c3 = st.number_input(f"C3 untuk REC #{i}", min_value=0.0, value=0.0, step=0.0000001, format="%.7f", key=f"rec_m_c3_{i}")

            den = c2 if c2 != 0 else 1
            rec_val = (c3 - c1) / den * 100

            rec_results.append((i, rec_val))
            st.markdown("---")

        if st.button("🧮 Hitung Semua REC", key="btn_rec_multiple"):
            st.markdown("## 📋 Hasil Perhitungan %Recovery")
            all_accurate = True

            for i, val in rec_results:
                st.write(f"📊 **%REC #{i}** = **{val:.7f}%**")
                if 80 <= val <= 120:
                    st.info(f"✅ REC #{i} menunjukkan akurasi baik")
                else:
                    st.warning(f"⚠️ REC #{i} menunjukkan akurasi kurang baik")
                    all_accurate = False

            st.markdown("---")
            # Kesimpulan akhir
            if all_accurate:
                st.success("✅ **Kesimpulan Akhir:** Semua hasil %Recovery berada dalam rentang 80–120%, artinya metode analisis memiliki akurasi yang baik.")
            else:
                st.error("❌ **Kesimpulan Akhir:** Terdapat hasil %Recovery di luar rentang 80–120%, menunjukkan adanya ketidakakuratan dalam analisis.")

# --- Sidebar & Routing ---
st.sidebar.markdown("""
<div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 10px; margin-bottom: 1rem;">
    <h2 style="color: white; margin: 0;">🧪 Navigasi</h2>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio("Pilih Halaman:", ["🏠 Homepage", "📖 Tentang", "🔬 C Terukur", "📏 Kadar", "🔄 %RPD", "🎯 %REC"])

if page == "🏠 Homepage":
    homepage()
elif page == "📖 Tentang":
    tentang()
elif page == "🔬 C Terukur":
    c_terukur()
elif page == "📏 Kadar":
    kadar()
elif page == "🔄 %RPD":
    rpd()
elif page == "🎯 %REC":
    rec()
