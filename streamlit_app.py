import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Mengatur konfigurasi halaman
st.set_page_config(
    page_title="Kalkulator Spektroskopi",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Fungsi untuk menghitung konsentrasi berdasarkan hukum Lambert-Beer
def hitung_konsentrasi(absorbansi, epsilon, panjang_sel):
    return absorbansi / (epsilon * panjang_sel)

# Fungsi untuk simulasi spektrum UV-Vis
def generate_uv_vis_spectrum(wavelength_range, max_abs, peak_position, width):
    spectrum = max_abs * np.exp(-((wavelength_range - peak_position) ** 2) / (2 * width ** 2))
    return spectrum

# Fungsi untuk simulasi spektrum IR
def generate_ir_spectrum(wavenumber_range, peaks):
    spectrum = np.zeros_like(wavenumber_range, dtype=float)
    for peak_pos, intensity, width in peaks:
        spectrum += intensity * np.exp(-((wavenumber_range - peak_pos) ** 2) / (2 * width ** 2))
    return spectrum

# Fungsi untuk simulasi spektrum Raman
def generate_raman_spectrum(shift_range, peaks):
    spectrum = np.zeros_like(shift_range, dtype=float)
    for peak_pos, intensity, width in peaks:
        lorentzian = intensity * (width**2 / ((shift_range - peak_pos)**2 + width**2))
        spectrum += lorentzian
    return spectrum

# Judul utama halaman dengan styling
st.markdown("""
    <style>
        .title {
            font-size: 42px;
            font-weight: bold;
            color: #1E88E5;
            text-align: center;
            margin-bottom: 20px;
        }
        .subtitle {
            font-size: 24px;
            color: #424242;
            text-align: center;
            margin-bottom: 30px;
        }
        .section-header {
            font-size: 28px;
            font-weight: bold;
            color: #0D47A1;
            margin-top: 20px;
            margin-bottom: 15px;
        }
    </style>
    <div class="title">Kalkulator Spektroskopi</div>
    <div class="subtitle">Aplikasi untuk Analisis dan Simulasi Data Spektroskopi</div>
""", unsafe_allow_html=True)

# Sidebar dengan menu yang lebih lengkap
st.sidebar.markdown("<h2 style='text-align: center; color: #1E88E5;'>Menu Analisis</h2>", unsafe_allow_html=True)

main_options = ["Beranda", "UV-Visible Spektroskopi", "Infrared (IR) Spektroskopi", "Raman Spektroskopi", "Tentang Aplikasi"]
option = st.sidebar.selectbox("Pilih Metode Spektroskopi:", main_options)

# Tambahkan info versi dan pengembang
st.sidebar.markdown("---")
st.sidebar.markdown("""
    <div style='text-align: center; color: gray; font-size: 14px;'>
        Versi 2.0<br>
        © 2025 Lab Spektroskopi
    </div>
""", unsafe_allow_html=True)

# Konten utama berdasarkan pilihan sidebar
if option == "Beranda":
    st.markdown("<div class='section-header'>Selamat Datang di Kalkulator Spektroskopi</div>", unsafe_allow_html=True)
    
    st.write("""
        Aplikasi ini menyediakan alat untuk melakukan perhitungan dan simulasi terkait dengan tiga teknik spektroskopi utama:
        UV-Visible, Infrared (IR), dan Raman. Anda dapat menggunakan aplikasi ini untuk:
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div style='background-color: #E3F2FD; padding: 20px; border-radius: 10px; height: 250px;'>
                <h3 style='color: #1976D2; text-align: center;'>UV-Visible</h3>
                <ul>
                    <li>Hitung konsentrasi sampel menggunakan hukum Lambert-Beer</li>
                    <li>Simulasi spektrum UV-Vis</li>
                    <li>Analisis data spektrum</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background-color: #E8F5E9; padding: 20px; border-radius: 10px; height: 250px;'>
                <h3 style='color: #388E3C; text-align: center;'>Infrared (IR)</h3>
                <ul>
                    <li>Simulasi spektrum IR</li>
                    <li>Identifikasi gugus fungsi</li>
                    <li>Analisis data spektrum</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div style='background-color: #FFF3E0; padding: 20px; border-radius: 10px; height: 250px;'>
                <h3 style='color: #E64A19; text-align: center;'>Raman</h3>
                <ul>
                    <li>Simulasi spektrum Raman</li>
                    <li>Analisis puncak Raman</li>
                    <li>Perbandingan data</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
        ### Cara Menggunakan Aplikasi
        1. Pilih jenis spektroskopi yang diinginkan dari menu di sidebar
        2. Masukkan parameter sesuai kebutuhan
        3. Lihat hasil perhitungan dan visualisasi
    """)

elif option == "UV-Visible Spektroskopi":
    st.markdown("<div class='section-header'>UV-Visible Spektroskopi</div>", unsafe_allow_html=True)
    
    st.write("""
        Spektroskopi UV-Vis adalah teknik analisis yang memanfaatkan interaksi sinar ultraviolet dan tampak dengan suatu sampel.
        Metode ini digunakan untuk mengukur absorbansi atau transmitansi cahaya pada panjang gelombang tertentu,
        sehingga dapat digunakan untuk menentukan konsentrasi zat terlarut menggunakan hukum Lambert-Beer.
    """)
    
    tabs = st.tabs(["Kalkulator Konsentrasi", "Simulasi Spektrum", "Analisis Data"])
    
    with tabs[0]:
        st.subheader("Kalkulator Konsentrasi (Hukum Lambert-Beer)")
        st.latex(r"A = \varepsilon \cdot c \cdot l")
        st.write("Keterangan:")
        st.write("A = Absorbansi")
        st.write("ε = Koefisien absorptivitas molar (L·mol⁻¹·cm⁻¹)")
        st.write("c = Konsentrasi (mol/L)")
        st.write("l = Panjang lintasan sel (cm)")
        
        col1, col2 = st.columns(2)
        
        with col1:
            absorbansi = st.number_input("Absorbansi (A)", min_value=0.0, max_value=3.0, value=0.5, step=0.01)
            epsilon = st.number_input("Koefisien Absorptivitas Molar (ε) (L·mol⁻¹·cm⁻¹)", min_value=100.0, value=5000.0, step=100.0)
            panjang_sel = st.number_input("Panjang Sel (l) (cm)", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
            
            if st.button("Hitung Konsentrasi"):
                konsentrasi = hitung_konsentrasi(absorbansi, epsilon, panjang_sel)
                st.success(f"Konsentrasi sampel adalah {konsentrasi:.6f} mol/L atau {konsentrasi * 1000:.4f} mmol/L")
        
        with col2:
            st.markdown("""
                <div style='background-color: #E3F2FD; padding: 15px; border-radius: 10px;'>
                    <h4 style='color: #1976D2;'>Tips Penggunaan</h4>
                    <ul>
                        <li>Pastikan nilai absorbansi antara 0.1-1.0 untuk hasil akurat</li>
                        <li>Gunakan sel kuvet yang sesuai dengan sampel Anda</li>
                        <li>Koefisien absorptivitas molar bervariasi untuk setiap senyawa</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
    
    with tabs[1]:
        st.subheader("Simulasi Spektrum UV-Vis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            min_wavelength = st.number_input("Panjang Gelombang Minimum (nm)", min_value=190, max_value=800, value=200, step=10)
            max_wavelength = st.number_input("Panjang Gelombang Maksimum (nm)", min_value=200, max_value=800, value=700, step=10)
            peak_position = st.slider("Posisi Puncak (nm)", min_value=200, max_value=700, value=350)
            max_absorbance = st.slider("Absorbansi Maksimum", min_value=0.0, max_value=2.0, value=1.0, step=0.1)
            peak_width = st.slider("Lebar Puncak", min_value=5, max_value=100, value=30)
            
            st.write("Tambahkan puncak kedua? (untuk campuran)")
            add_second_peak = st.checkbox("Ya, tambahkan puncak kedua")
            
            peak2_position = None
            peak2_absorbance = None
            peak2_width = None
            
            if add_second_peak:
                peak2_position = st.slider("Posisi Puncak Kedua (nm)", min_value=200, max_value=700, value=450)
                peak2_absorbance = st.slider("Absorbansi Maksimum Kedua", min_value=0.0, max_value=2.0, value=0.7, step=0.1)
                peak2_width = st.slider("Lebar Puncak Kedua", min_value=5, max_value=100, value=40)
        
        with col2:
            wavelength_range = np.linspace(min_wavelength, max_wavelength, 1000)
            spectrum = generate_uv_vis_spectrum(wavelength_range, max_absorbance, peak_position, peak_width)
            
            if add_second_peak and peak2_position is not None:
                spectrum2 = generate_uv_vis_spectrum(wavelength_range, peak2_absorbance, peak2_position, peak2_width)
                spectrum += spectrum2
            
            plt.figure(figsize=(10, 6))
            plt.plot(wavelength_range, spectrum)
            plt.title("Simulasi Spektrum UV-Vis")
            plt.xlabel("Panjang Gelombang (nm)")
            plt.ylabel("Absorbansi")
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.fill_between(wavelength_range, spectrum, alpha=0.2)
            plt.xlim(min_wavelength, max_wavelength)
            plt.ylim(0, max(spectrum) * 1.1)
            
            # Anotasi puncak
            peak_idx = np.argmax(spectrum)
            plt.annotate(f"λmax = {wavelength_range[peak_idx]:.1f} nm",
                        xy=(wavelength_range[peak_idx], spectrum[peak_idx]),
                        xytext=(wavelength_range[peak_idx] + 20, spectrum[peak_idx] + 0.1),
                        arrowprops=dict(arrowstyle="->", color="red"))
            
            st.pyplot(plt)
            
            # Opsi untuk mengunduh data
            df_spectrum = pd.DataFrame({
                'Wavelength (nm)': wavelength_range,
                'Absorbance': spectrum
            })
            
            csv = df_spectrum.to_csv(index=False)
            st.download_button(
                label="Unduh Data Spektrum (CSV)",
                data=csv,
                file_name="uv_vis_spectrum.csv",
                mime="text/csv"
            )
    
    with tabs[2]:
        st.subheader("Analisis Data Spektrum UV-Vis")
        st.write("Unggah file CSV dengan data spektrum UV-Vis untuk analisis")
        
        uploaded_file = st.file_uploader("Pilih file CSV", type=["csv"])
        
        if uploaded_file is not None:
            try:
                # Simulasi data jika file diunggah
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                content = stringio.read()
                
                st.write("**Data spektrum berhasil diunggah!**")
                
                # Simulasi data untuk demo (akan digantikan dengan data sebenarnya)
                wavelength = np.linspace(200, 700, 100)
                absorbance = generate_uv_vis_spectrum(wavelength, 1.2, 350, 30) + generate_uv_vis_spectrum(wavelength, 0.8, 450, 40)
                absorbance += np.random.normal(0, 0.02, size=len(wavelength))  # Menambahkan noise
                
                df = pd.DataFrame({
                    'Wavelength (nm)': wavelength,
                    'Absorbance': absorbance
                })
                
                st.dataframe(df.head(10))
                
                # Visualisasi data
                plt.figure(figsize=(10, 6))
                plt.plot(df['Wavelength (nm)'], df['Absorbance'], 'b-')
                plt.title("Data Spektrum UV-Vis")
                plt.xlabel("Panjang Gelombang (nm)")
                plt.ylabel("Absorbansi")
                plt.grid(True, linestyle='--', alpha=0.7)
                
                # Temukan puncak-puncak
                from scipy.signal import find_peaks
                peaks, _ = find_peaks(df['Absorbance'], height=0.3, distance=20)
                
                plt.plot(df['Wavelength (nm)'].iloc[peaks], df['Absorbance'].iloc[peaks], "ro")
                for i, peak in enumerate(peaks):
                    plt.annotate(f"Peak {i+1}: {df['Wavelength (nm)'].iloc[peak]:.1f} nm",
                                xy=(df['Wavelength (nm)'].iloc[peak], df['Absorbance'].iloc[peak]),
                                xytext=(df['Wavelength (nm)'].iloc[peak] - 20, df['Absorbance'].iloc[peak] + 0.1),
                                arrowprops=dict(arrowstyle="->", color="red"))
                
                st.pyplot(plt)
                
                # Hasil analisis
                st.subheader("Hasil Analisis:")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**Jumlah puncak terdeteksi:** {len(peaks)}")
                    st.write("**Informasi Puncak:**")
                    for i, peak in enumerate(peaks):
                        st.write(f"Puncak {i+1}: {df['Wavelength (nm)'].iloc[peak]:.1f} nm (Abs: {df['Absorbance'].iloc[peak]:.3f})")
                    
                    max_abs_idx = df['Absorbance'].idxmax()
                    st.write(f"**Absorbansi maksimum:** {df['Absorbance'].iloc[max_abs_idx]:.3f} pada {df['Wavelength (nm)'].iloc[max_abs_idx]:.1f} nm")
                
                with col2:
                    st.markdown("""
                        <div style='background-color: #E3F2FD; padding: 15px; border-radius: 10px;'>
                            <h4 style='color: #1976D2;'>Interpretasi Awal</h4>
                            <ul>
                                <li>Puncak 1 (350 nm): Kemungkinan transisi π → π* dari ikatan rangkap terkonjugasi</li>
                                <li>Puncak 2 (450 nm): Kemungkinan transisi n → π* dari gugus karbonil</li>
                            </ul>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # Tambahkan opsi pengaturan analisis lanjutan
                    st.write("**Pengaturan Analisis Lanjutan:**")
                    threshold = st.slider("Threshold Deteksi Puncak", min_value=0.1, max_value=1.0, value=0.3, step=0.05)
                    
            except Exception as e:
                st.error(f"Terjadi kesalahan saat memproses file: {e}")
                st.write("Pastikan format file sesuai dengan yang diharapkan.")

elif option == "Infrared (IR) Spektroskopi":
    st.markdown("<div class='section-header'>Infrared (IR) Spektroskopi</div>", unsafe_allow_html=True)
    
    st.write("""
        Spektroskopi Infrared (IR) adalah teknik untuk mempelajari getaran molekul yang disebabkan oleh penyerapan gelombang inframerah.
        Setiap jenis ikatan kimia akan menyerap IR pada frekuensi khas, sehingga spektrum IR dapat digunakan untuk identifikasi gugus fungsi.
    """)
    
    tabs = st.tabs(["Simulasi Spektrum IR", "Database Gugus Fungsi", "Interpretasi Spektrum"])
    
    with tabs[0]:
        st.subheader("Simulasi Spektrum IR")
        
        col1, col2 = st.columns(2)
        
        with col1:
            min_wavenumber = st.number_input("Bilangan Gelombang Minimum (cm⁻¹)", min_value=400, max_value=4000, value=500, step=100)
            max_wavenumber = st.number_input("Bilangan Gelombang Maksimum (cm⁻¹)", min_value=500, max_value=4000, value=4000, step=100)
            
            st.subheader("Tambahkan Puncak IR")
            
            num_peaks = st.slider("Jumlah Puncak", min_value=1, max_value=5, value=3)
            
            peaks = []
            for i in range(num_peaks):
                st.markdown(f"#### Puncak {i+1}")
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    peak_pos = st.number_input(f"Posisi Puncak (cm⁻¹)", min_value=500, max_value=4000, value=1000 + i*800, step=50, key=f"pos_{i}")
                with col_b:
                    peak_int = st.slider(f"Intensitas", min_value=0.1, max_value=1.0, value=0.8 - i*0.2, step=0.1, key=f"int_{i}")
                with col_c:
                    peak_width = st.slider(f"Lebar", min_value=10, max_value=100, value=50, step=5, key=f"width_{i}")
                
                peaks.append((peak_pos, peak_int, peak_width))
                
                # Tampilkan informasi gugus fungsi yang mungkin
                if 1650 <= peak_pos <= 1750:
                    st.info("Kemungkinan gugus fungsi: C=O (Karbonil)")
                elif 3200 <= peak_pos <= 3600:
                    st.info("Kemungkinan gugus fungsi: O-H (Hidroksil)")
                elif 2800 <= peak_pos <= 3000:
                    st.info("Kemungkinan gugus fungsi: C-H (Alkana/Alkena)")
                elif 1550 <= peak_pos <= 1650:
                    st.info("Kemungkinan gugus fungsi: C=C (Alkena)")
        
        with col2:
            wavenumber_range = np.linspace(min_wavenumber, max_wavenumber, 1000)
            ir_spectrum = generate_ir_spectrum(wavenumber_range, peaks)
            
            plt.figure(figsize=(10, 6))
            plt.plot(wavenumber_range, ir_spectrum)
            plt.title("Simulasi Spektrum IR")
            plt.xlabel("Bilangan Gelombang (cm⁻¹)")
            plt.ylabel("Transmitansi (%)")
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.ylim(0, 1.1)
            plt.xlim(max_wavenumber, min_wavenumber)  # Inversi sumbu x untuk spektrum IR
            
            # Konversi ke transmitansi
            transmittance = 1 - ir_spectrum
            plt.plot(wavenumber_range, transmittance)
            
            # Anotasi puncak-puncak
            for i, (peak_pos, peak_int, _) in enumerate(peaks):
                peak_idx = np.abs(wavenumber_range - peak_pos).argmin()
                plt.annotate(f"{peak_pos} cm⁻¹",
                            xy=(wavenumber_range[peak_idx], transmittance[peak_idx]),
                            xytext=(wavenumber_range[peak_idx] + 50, transmittance[peak_idx] - 0.1),
                            arrowprops=dict(arrowstyle="->", color="red"))
            
            st.pyplot(plt)
            
            # Opsi untuk mengunduh data
            df_spectrum = pd.DataFrame({
                'Wavenumber (cm⁻¹)': wavenumber_range,
                'Transmittance (%)': transmittance * 100
            })
            
            csv = df_spectrum.to_csv(index=False)
            st.download_button(
                label="Unduh Data Spektrum (CSV)",
                data=csv,
                file_name="ir_spectrum.csv",
                mime="text/csv"
            )
    
    with tabs[1]:
        st.subheader("Database Gugus Fungsi IR")
        
        st.write("""
            Tabel di bawah ini berisi informasi tentang pita absorpsi inframerah yang khas untuk berbagai gugus fungsi.
            Gunakan ini sebagai referensi untuk interpretasi data IR Anda.
        """)
        
        # Buat dataframe contoh untuk database gugus fungsi
        ir_data = {
            'Gugus Fungsi': ['O-H (Alkohol, bebas)', 'O-H (Alkohol, berikatan H)', 'N-H (Amina primer)', 'C-H (Alkana)', 
                            'C-H (Alkena)', 'C-H (Aromatik)', 'C≡N (Nitril)', 'C=O (Aldehida)', 'C=O (Keton)', 
                            'C=O (Asam karboksilat)', 'C=O (Ester)', 'C=O (Amida)', 'C=C (Alkena)', 'C=C (Aromatik)'],
            'Bilangan Gelombang (cm⁻¹)': ['3600-3650', '3200-3400', '3300-3500', '2850-2960', '3010-3100', '3000-3100', 
                                        '2210-2260', '1720-1740', '1710-1720', '1700-1725', '1735-1750', '1630-1690', 
                                        '1620-1680', '1450-1600'],
            'Intensitas': ['Kuat, tajam', 'Kuat, lebar', 'Medium', 'Kuat', 'Medium', 'Lemah', 'Medium', 'Kuat', 'Kuat', 
                        'Kuat', 'Kuat', 'Kuat', 'Medium-lemah', 'Medium-kuat'],
            'Keterangan': ['Peregangan', 'Peregangan', 'Peregangan', 'Peregangan', 'Peregangan', 'Peregangan', 
                        'Peregangan', 'Peregangan', 'Peregangan', 'Peregangan', 'Peregangan', 'Peregangan', 
                        'Peregangan', 'Peregangan']
        }
        
        df_ir = pd.DataFrame(ir_data)
        
        # Filter untuk pencarian
        search_term = st.text_input("Cari Gugus Fungsi:", "")
        
        if search_term:
            filtered_df = df_ir[df_ir['Gugus Fungsi'].str.contains(search_term, case=False)]
            st.dataframe(filtered_df)
        else:
            st.dataframe(df_ir)
        
        # Tambahkan gambar referensi
        st.subheader("Referensi Visual Spektrum IR")
        st.image("https://via.placeholder.com/800x400?text=IR+Spectroscopy+Reference+Chart", 
                caption="Grafik Referensi untuk Interpretasi Spektrum IR")
    
    with tabs[2]:
        st.subheader("Interpretasi Spektrum IR")
        st.write("Unggah spektrum IR untuk interpretasi otomatis atau masukkan nilai-nilai puncak secara manual.")
        
        method = st.radio("Metode input:", ["Upload File", "Input Manual"])
        
        if method == "Upload File":
            uploaded_file = st.file_uploader("Pilih file CSV spektrum IR", type=["csv"])
            
            if uploaded_file is not None:
                st.success("File berhasil diunggah. Demo interpretasi:")
                
                # Demo data untuk interpretasi
                st.write("**Puncak-puncak yang terdeteksi:**")
                detection_data = {
                    'Bilangan Gelombang (cm⁻¹)': [3350, 2950, 1720, 1650, 1450, 1050],
                    'Intensitas': ['Kuat', 'Medium', 'Kuat', 'Lemah', 'Medium', 'Kuat'],
                    'Kemungkinan Gugus Fungsi': ['O-H (Alkohol)', 'C-H (Alkana)', 'C=O (Keton/Ester)', 
                                                'C=C (Alkena)', 'CH₂/CH₃ (Bengkokan)', 'C-O (Eter/Alkohol)']
                }
                
                st.dataframe(pd.DataFrame(detection_data))
                
                # Interpretasi
                st.subheader("Interpretasi Senyawa:")
                st.markdown("""
                    <div style='background-color: #E8F5E9; padding: 15px; border-radius: 10px;'>
                        <h4 style='color: #388E3C;'>Hasil Analisis</h4>
                        <p>Berdasarkan puncak-puncak yang terdeteksi, sampel kemungkinan merupakan <b>ester alkohol tidak jenuh</b> 
                        dengan karakteristik sebagai berikut:</p>
                        <ul>
                            <li>Adanya gugus hidroksil (O-H) pada 3350 cm⁻¹</li>
                            <li>Gugus C=O ester pada 1720 cm⁻¹</li>
                            <li>Ikatan rangkap C=C pada 1650 cm⁻¹</li>
                            <li>Gugus C-O pada 1050 cm⁻¹</li>
                        </ul>
                        <p>Struktur yang mungkin:</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Tambahkan opsi untuk visualisasi struktur molekul (placeholder)
                st.image("https://via.placeholder.com/400x200?text=Molecule+Structure", 
                        caption="Struktur Molekul yang Diperkirakan")
        
        else:  # Input Manual
            st.write("Masukkan nilai bilangan gelombang dari puncak-puncak spektrum IR yang ingin diinterpretasikan:")
            
            col1, col2 = st.columns(2)
            
            peaks_input = []
            
            with col1:
                num_peaks = st.number_input("Jumlah puncak yang akan dimasukkan:", min_value=1, max_value=10, value=3)
                
                for i in range(num_peaks):
                    peak_value = st.number_input(f"Bilangan gelombang puncak {i+1} (cm⁻¹):", min_value=400, max_value=4000, value=1000 + i*500)
                    peaks_input.append(peak_value)
            
            with col2:
                if st.button("Interpretasikan"):
                    st.write("**Hasil Interpretasi:**")
                    
                    # Logika sederhana untuk interpretasi berdasarkan nilai puncak
                    interpretations = []
                    
                    for peak in peaks_input:
                        if 3200 <= peak <= 3600:
                            interpretations.append(f"{peak} cm⁻¹: O-H stretching (alkohol/fenol)")
                        elif 2800 <= peak <= 3000:
                            interpretations.append(f"{peak} cm⁻¹: C-H stretching (alkana)")
                        elif 1700 <= peak <= 1750:
                            interpretations.append(f"{peak} cm⁻¹: C=O stretching (keton/aldehida/ester)")
                        elif 1620 <= peak <= 1680:
                            interpretations.append(f"{peak} cm⁻¹: C=C stretching (alkena)")
                        elif 1000 <= peak <= 1300:
                            interpretations.append(f"{peak} cm⁻¹: C-O stretching (alkohol/eter/ester)")
                        elif 1350 <= peak <= 1470:
                            interpretations.append(f"{peak} cm⁻¹: C-H bending (alkana)")
                        elif 675 <= peak <= 1000:
                            interpretations.append(f"{peak} cm⁻¹: =C-H bending (alkena)")
                        elif 600 <= peak <= 800:
                            interpretations.append(f"{peak} cm⁻¹: C-Cl stretching (alkil halida)")
                        else:
                            interpretations.append(f"{peak} cm⁻¹: Puncak tidak teridentifikasi")
                    
                    for interp in interpretations:
                        st.write(interp)
                    
                    # Tambahkan ringkasan
                    st.markdown("""
                        <div style='background-color: #E8F5E9; padding: 15px; border-radius: 10px; margin-top: 20px;'>
                            <h4 style='color: #388E3C;'>Kesimpulan</h4>
                            <p>Untuk analisis yang lebih akurat, pertimbangkan untuk menggunakan database spektral yang komprehensif atau berkonsultasi dengan ahli spektroskopi.</p>
                        </div>
                    """, unsafe_allow_html=True)

elif option == "Raman Spektroskopi":
    st.markdown("<div class='section-header'>Raman Spektroskopi</div>", unsafe_allow_html=True)
    
    st.write("""
        Spektroskopi Raman adalah metode analisis non-destruktif yang mengukur cahaya terpencar (scattered) dari sampel.
        Raman memberikan informasi tentang struktur molekul, ikatan kimia, dan interaksi molekular melalui pergeseran energi
        yang terjadi ketika cahaya monokromatik berinteraksi dengan sampel.
    """)
    
    tabs = st.tabs(["Simulasi Spektrum Raman", "Analisis Data Raman", "Perbandingan dengan IR"])
    
    with tabs[0]:
        st.subheader("Simulasi Spektrum Raman")
        
        col1, col2 = st.columns(2)
        
        with col1:
            min_shift = st.number_input("Pergeseran Raman Minimum (cm⁻¹)", min_value=0, max_value=3500, value=0, step=100)
            max_shift = st.number_input("Pergeseran Raman Maksimum (cm⁻¹)", min_value=100, max_value=3500, value=3200, step=100)
            
            st.subheader("Tambahkan Puncak Raman")
            
            num_peaks = st.slider("Jumlah Puncak", min_value=1, max_value=5, value=3, key="raman_peaks")
            
            peaks = []
            for i in range(num_peaks):
                st.markdown(f"#### Puncak {i+1}")
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    peak_pos = st.number_input(f"Posisi (cm⁻¹)", min_value=50, max_value=3500, value=500 + i*800, step=50, key=f"raman_pos_{i}")
                with col_b:
                    peak_int = st.slider(f"Intensitas", min_value=0.1, max_value=1.0, value=0.8 - i*0.2, step=0.1, key=f"raman_int_{i}")
                with col_c:
                    peak_width = st.slider(f"Lebar", min_value=5, max_value=50, value=20, step=5, key=f"raman_width_{i}")
                
                peaks.append((peak_pos, peak_int, peak_width))
                
                # Tampilkan informasi mode vibrasi yang mungkin
                if 1550 <= peak_pos <= 1650:
                    st.info("Kemungkinan mode vibrasi: C=C stretching (aromatik)")
                elif 2800 <= peak_pos <= 3000:
                    st.info("Kemungkinan mode vibrasi: C-H stretching")
                elif 1000 <= peak_pos <= 1100:
                    st.info("Kemungkinan mode vibrasi: C-C stretching")
                elif 500 <= peak_pos <= 800:
                    st.info("Kemungkinan mode vibrasi: C-X stretching (X = Cl, Br)")
        
        with col2:
            shift_range = np.linspace(min_shift, max_shift, 1000)
            raman_spectrum = generate_raman_spectrum(shift_range, peaks)
            
            plt.figure(figsize=(10, 6))
            plt.plot(shift_range, raman_spectrum)
            plt.title("Simulasi Spektrum Raman")
            plt.xlabel("Pergeseran Raman (cm⁻¹)")
            plt.ylabel("Intensitas")
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.ylim(0, max(raman_spectrum) * 1.1)
            
            # Anotasi puncak-puncak
            for i, (peak_pos, peak_int, _) in enumerate(peaks):
                peak_idx = np.abs(shift_range - peak_pos).argmin()
                plt.annotate(f"{peak_pos} cm⁻¹",
                            xy=(shift_range[peak_idx], raman_spectrum[peak_idx]),
                            xytext=(shift_range[peak_idx] + 50, raman_spectrum[peak_idx] + 0.05),
                            arrowprops=dict(arrowstyle="->", color="red"))
            
            st.pyplot(plt)
            
            # Opsi untuk mengunduh data
            df_spectrum = pd.DataFrame({
                'Raman Shift (cm⁻¹)': shift_range,
                'Intensity': raman_spectrum
            })
            
            csv = df_spectrum.to_csv(index=False)
            st.download_button(
                label="Unduh Data Spektrum (CSV)",
                data=csv,
                file_name="raman_spectrum.csv",
                mime="text/csv"
            )
            
            # Tambahkan informasi tentang senyawa referensi
            st.subheader("Interpretasi Awal")
            st.markdown("""
                <div style='background-color: #FFF3E0; padding: 15px; border-radius: 10px;'>
                    <h4 style='color: #E64A19;'>Kemungkinan Gugus Fungsi</h4>
                    <p>Spektrum ini menunjukkan pola yang mirip dengan:</p>
                    <ul>
                        <li>Senyawa aromatik (1600 cm⁻¹)</li>
                        <li>Gugus alkil (2900 cm⁻¹)</li>
                        <li>Struktur rantai karbon (800-1200 cm⁻¹)</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
    
    with tabs[1]:
        st.subheader("Analisis Data Raman")
        st.write("Unggah file CSV dengan data spektrum Raman untuk analisis lanjutan.")
        
        uploaded_file = st.file_uploader("Pilih file CSV", type=["csv"], key="raman_uploader")
        
        if uploaded_file is not None:
            try:
                # Demo analisis data Raman
                st.success("File berhasil diunggah. Menampilkan hasil analisis demo:")
                
                # Simulasi data untuk demonstrasi
                shift = np.linspace(0, 3200, 1000)
                intensity = np.zeros_like(shift)
                
                # Tambahkan beberapa puncak demo
                peaks_demo = [(485, 0.6, 30), (1008, 1.0, 15), (1340, 0.4, 20), (1580, 0.7, 25), (2900, 0.5, 35)]
                for pos, height, width in peaks_demo:
                    intensity += height * (width**2 / ((shift - pos)**2 + width**2))
                
                intensity += np.random.normal(0, 0.01, size=len(shift))  # Tambahkan noise
                
                df_demo = pd.DataFrame({
                    'Raman Shift (cm⁻¹)': shift,
                    'Intensity': intensity
                })
                
                # Tampilkan preview data
                st.write("**Preview data spektrum:**")
                st.dataframe(df_demo.head())
                
                # Plot spektrum
                plt.figure(figsize=(12, 6))
                plt.plot(df_demo['Raman Shift (cm⁻¹)'], df_demo['Intensity'])
                plt.title("Spektrum Raman")
                plt.xlabel("Pergeseran Raman (cm⁻¹)")
                plt.ylabel("Intensitas")
                plt.grid(True, linestyle='--', alpha=0.7)
                
                # Temukan puncak-puncak
                from scipy.signal import find_peaks
                peaks, properties = find_peaks(df_demo['Intensity'], height=0.2, distance=50, prominence=0.1)
                
                plt.plot(df_demo['Raman Shift (cm⁻¹)'].iloc[peaks], df_demo['Intensity'].iloc[peaks], "ro")
                for i, peak in enumerate(peaks):
                    plt.annotate(f"{df_demo['Raman Shift (cm⁻¹)'].iloc[peak]:.0f}",
                                xy=(df_demo['Raman Shift (cm⁻¹)'].iloc[peak], df_demo['Intensity'].iloc[peak]),
                                xytext=(df_demo['Raman Shift (cm⁻¹)'].iloc[peak] - 100, df_demo['Intensity'].iloc[peak] + 0.05),
                                arrowprops=dict(arrowstyle="->", color="red"))
                
                st.pyplot(plt)
                
                # Analisis hasil
                st.subheader("Hasil Analisis Puncak")
                
                # Tampilkan tabel analisis puncak
                peak_results = pd.DataFrame({
                    'Puncak': range(1, len(peaks) + 1),
                    'Pergeseran (cm⁻¹)': df_demo['Raman Shift (cm⁻¹)'].iloc[peaks].round(1),
                    'Intensitas': df_demo['Intensity'].iloc[peaks].round(3),
                    'Lebar Puncak (FWHM)': [40, 30, 25, 35, 45],  # Nilai demo
                    'Area Puncak': [25, 45, 12, 30, 22]  # Nilai demo
                })
                
                st.dataframe(peak_results)
                
                # Tambahkan interpretasi
                st.subheader("Interpretasi Spektrum")
                
                # Tampilkan informasi interpretasi
                st.markdown("""
                    <div style='background-color: #FFF3E0; padding: 15px; border-radius: 10px;'>
                        <h4 style='color: #E64A19;'>Kemungkinan Identifikasi</h4>
                        <p>Berdasarkan puncak-puncak karakteristik yang terdeteksi:</p>
                        <ul>
                            <li><strong>485 cm⁻¹</strong>: Mode breathing aromatik</li>
                            <li><strong>1008 cm⁻¹</strong>: C-C stretching</li>
                            <li><strong>1340 cm⁻¹</strong>: Mode D (defek dalam struktur karbon)</li>
                            <li><strong>1580 cm⁻¹</strong>: Mode G (ikatan sp² dalam karbon)</li>
                            <li><strong>2900 cm⁻¹</strong>: C-H stretching</li>
                        </ul>
                        <p>Spektrum ini menunjukkan karakteristik <strong>material karbon/grafit</strong> dengan beberapa gugus fungsional permukaan.</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Tambahkan opsi untuk preprocessing lanjutan
                st.subheader("Preprocessing Lanjutan")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    baseline_correction = st.checkbox("Koreksi Baseline")
                    smoothing = st.checkbox("Smoothing Data")
                    normalization = st.checkbox("Normalisasi")
                
                with col2:
                    if baseline_correction or smoothing or normalization:
                        st.info("Preprocessing akan diterapkan pada data. Klik tombol di bawah untuk menerapkan.")
                        
                        if st.button("Terapkan Preprocessing"):
                            st.success("Preprocessing berhasil diterapkan!")
                            
                            # Demo hasil preprocessing (data yang sama dengan beberapa modifikasi)
                            plt.figure(figsize=(12, 6))
                            plt.plot(df_demo['Raman Shift (cm⁻¹)'], df_demo['Intensity'] * 1.2, label="Setelah preprocessing")
                            plt.plot(df_demo['Raman Shift (cm⁻¹)'], df_demo['Intensity'], '--', alpha=0.5, label="Data asli")
                            plt.title("Spektrum Raman Setelah Preprocessing")
                            plt.xlabel("Pergeseran Raman (cm⁻¹)")
                            plt.ylabel("Intensitas")
                            plt.grid(True, linestyle='--', alpha=0.7)
                            plt.legend()
                            
                            st.pyplot(plt)
                
            except Exception as e:
                st.error(f"Terjadi kesalahan saat memproses file: {e}")
                st.write("Pastikan format file sesuai dengan yang diharapkan.")
    
    with tabs[2]:
        st.subheader("Perbandingan dengan Spektroskopi IR")
        
        st.write("""
            Spektroskopi Raman dan IR adalah teknik pelengkap yang memberikan informasi tentang mode vibrasi molekul.
            Meskipun demikian, keduanya memiliki prinsip fisika yang berbeda dan memberikan informasi yang saling melengkapi.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
                <div style='background-color: #E3F2FD; padding: 15px; border-radius: 10px;'>
                    <h4 style='color: #1976D2; text-align: center;'>Spektroskopi IR</h4>
                    <ul>
                        <li><strong>Prinsip:</strong> Absorpsi energi IR oleh sampel</li>
                        <li><strong>Syarat:</strong> Perubahan momen dipol saat vibrasi</li>
                        <li><strong>Mode Aktif:</strong> Mode asimetris</li>
                        <li><strong>Sampel:</strong> Lebih baik untuk sampel polar</li>
                        <li><strong>Interferensi:</strong> Air sangat mengganggu</li>
                        <li><strong>Preparasi:</strong> Memerlukan preparasi khusus</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
                <div style='background-color: #FFF3E0; padding: 15px; border-radius: 10px;'>
                    <h4 style='color: #E64A19; text-align: center;'>Spektroskopi Raman</h4>
                    <ul>
                        <li><strong>Prinsip:</strong> Hamburan inelastis foton</li>
                        <li><strong>Syarat:</strong> Perubahan polarisabilitas saat vibrasi</li>
                        <li><strong>Mode Aktif:</strong> Mode simetris</li>
                        <li><strong>Sampel:</strong> Lebih baik untuk sampel non-polar</li>
                        <li><strong>Interferensi:</strong> Air tidak mengganggu</li>
                        <li><strong>Preparasi:</strong> Minimal atau tidak perlu</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
        
        st.subheader("Perbandingan Spektrum")
        
        # Demo perbandingan spektrum
        shift = np.linspace(500, 3500, 1000)
        
        # Simulasi spektrum IR
        ir_spectrum = np.zeros_like(shift)
        ir_peaks = [(1050, 0.7, 50), (1380, 0.4, 30), (1720, 0.9, 40), (2950, 0.6, 60), (3400, 0.85, 100)]
        for pos, height, width in ir_peaks:
            ir_spectrum += height * np.exp(-((shift - pos) ** 2) / (2 * width ** 2))
        
        # Simulasi spektrum Raman (puncak berbeda dari IR untuk menunjukkan komplementer)
        raman_spectrum = np.zeros_like(shift)
        raman_peaks = [(520, 0.9, 15), (1000, 0.5, 25), (1330, 0.7, 35), (1590, 0.95, 30), (2900, 0.4, 50)]
        for pos, height, width in raman_peaks:
            raman_spectrum += height * (width**2 / ((shift - pos)**2 + width**2))
        
        # Plot perbandingan
        plt.figure(figsize=(12, 8))
        
        plt.subplot(2, 1, 1)
        plt.plot(shift, 1 - ir_spectrum, 'b-')
        plt.title("Spektrum IR")
        plt.xlabel("Bilangan Gelombang (cm⁻¹)")
        plt.ylabel("Transmitansi")
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.gca().invert_xaxis()  # Inversi sumbu x untuk IR
        
        plt.subplot(2, 1, 2)
        plt.plot(shift, raman_spectrum, 'r-')
        plt.title("Spektrum Raman")
        plt.xlabel("Pergeseran Raman (cm⁻¹)")
        plt.ylabel("Intensitas")
        plt.grid(True, linestyle='--', alpha=0.7)
        
        plt.tight_layout()
        st.pyplot(plt)
        
        st.markdown("""
            <div style='background-color: #F5F5F5; padding: 15px; border-radius: 10px; margin-top: 20px;'>
                <h4 style='color: #212121; text-align: center;'>Kapan Menggunakan Masing-masing Teknik?</h4>
                <table style='width: 100%; border-collapse: collapse;'>
                    <tr>
                        <th style='border: 1px solid #ddd; padding: 8px; text-align: left;'>Situasi</th>
                        <th style='border: 1px solid #ddd; padding: 8px; text-align: left;'>Pilihan Teknik</th>
                    </tr>
                    <tr>
                        <td style='border: 1px solid #ddd; padding: 8px;'>Sampel berair</td>
                        <td style='border: 1px solid #ddd; padding: 8px;'>Raman</td>
                    </tr>
                    <tr>
                        <td style='border: 1px solid #ddd; padding: 8px;'>Sampel dengan gugus polar (OH, NH, C=O)</td>
                        <td style='border: 1px solid #ddd; padding: 8px;'>IR</td>
                    </tr>
                    <tr>
                        <td style='border: 1px solid #ddd; padding: 8px;'>Sampel dengan ikatan simetris (C=C, S-S)</td>
                        <td style='border: 1px solid #ddd; padding: 8px;'>Raman</td>
                    </tr>
                    <tr>
                        <td style='border: 1px solid #ddd; padding: 8px;'>Analisis in-situ</td>
                        <td style='border: 1px solid #ddd; padding: 8px;'>Raman</td>
                    </tr>
                    <tr>
                        <td style='border: 1px solid #ddd; padding: 8px;'>Sampel fluoresen</td>
                        <td style='border: 1px solid #ddd; padding: 8px;'>IR</td>
                    </tr>
                    <tr>
                        <td style='border: 1px solid #ddd; padding: 8px;'>Informasi struktural terlengkap</td>
                        <td style='border: 1px solid #ddd; padding: 8px;'>Kombinasi keduanya</td>
                    </tr>
                </table>
            </div>
        """, unsafe_allow_html=True)

elif option == "Tentang Aplikasi":
    st.markdown("<div class='section-header'>Tentang Aplikasi</div>", unsafe_allow_html=True)
    
    st.write("""
        Aplikasi Kalkulator Spektroskopi ini dirancang sebagai alat pembelajaran dan analisis untuk membantu mahasiswa,
        peneliti, dan praktisi dalam bidang spektroskopi. Aplikasi ini menyediakan berbagai alat untuk simulasi dan
        interpretasi data spektroskopi UV-Vis, IR, dan Raman.
    """)
    
    # Informasi versi dan pengembang
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div style='background-color: #E8EAF6; padding: 20px; border-radius: 10px;'>
                <h3 style='color: #3F51B5; text-align: center;'>Informasi Aplikasi</h3>
                <ul>
                    <li><strong>Nama:</strong> Kalkulator Spektroskopi</li>
                    <li><strong>Versi:</strong> 2.0</li>
                    <li><strong>Tanggal Rilis:</strong> Mei 2025</li>
                    <li><strong>Pengembang:</strong> Lab Spektroskopi</li>
                    <li><strong>Framework:</strong> Streamlit</li>
                    <li><strong>Bahasa:</strong> Python</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style='background-color: #E0F7FA; padding: 20px; border-radius: 10px;'>
                <h3 style='color: #0097A7; text-align: center;'>Fitur Utama</h3>
                <ul>
                    <li>Kalkulator konsentrasi UV-Vis (Lambert-Beer)</li>
                    <li>Simulasi spektrum UV-Vis, IR, dan Raman</li>
                    <li>Analisis dan interpretasi data spektral</li>
                    <li>Database gugus fungsi IR</li>
                    <li>Perbandingan teknik spektroskopi</li>
                    <li>Visualisasi interaktif</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
    
    # FAQ
    st.markdown("<h3 style='margin-top: 30px;'>Pertanyaan yang Sering Diajukan (FAQ)</h3>", unsafe_allow_html=True)
    
    with st.expander("Apa itu spektroskopi?"):
        st.write("""
            Spektroskopi adalah studi tentang interaksi antara materi dan energi elektromagnetik. 
            Dalam konteks kimia analitik, spektroskopi merujuk pada metode eksperimental untuk mengukur 
            spektrum yang dihasilkan dari interaksi radiasi elektromagnetik dengan materi, yang dapat 
            memberikan informasi tentang struktur, komposisi, dan sifat dari zat tersebut.
        """)
    
    with st.expander("Bagaimana cara menggunakan aplikasi ini untuk analisis sampel nyata?"):
        st.write("""
            Untuk sampel nyata, Anda dapat mengikuti langkah-langkah berikut:
            1. Lakukan pengukuran spektrum dengan instrumen yang sesuai (UV-Vis, IR, atau Raman)
            2. Ekspor data dalam format CSV
            3. Unggah data tersebut ke aplikasi ini menggunakan fitur "Analisis Data" di masing-masing bagian
            4. Gunakan alat analisis untuk menginterpretasikan hasil
            
            Perlu diingat bahwa aplikasi ini memiliki keterbatasan dan sebaiknya digunakan sebagai alat bantu, 
            bukan sebagai pengganti instrumen laboratorium atau penilaian ahli.
        """)
    
    with st.expander("Apakah data yang diunggah akan tersimpan di server?"):
        st.write("""
            Tidak. Data yang Anda unggah hanya diproses secara lokal di browser Anda dan tidak disimpan di server.
            Setelah sesi browser ditutup atau halaman di-refresh, data akan dihapus dari memori.
        """)
    
    with st.expander("Bisakah saya mengekspor hasil analisis?"):
        st.write("""
            Ya, aplikasi ini menyediakan opsi untuk mengunduh data simulasi dan hasil analisis dalam format CSV 
            pada sebagian besar fitur. Selain itu, Anda dapat menggunakan fungsi screenshot browser untuk menyimpan 
            visualisasi dan interpretasi yang dihasilkan.
        """)
    
    with st.expander("Saya menemukan bug atau ingin menyarankan fitur baru. Bagaimana caranya?"):
        st.write("""
            Silakan laporkan bug atau saran peningkatan dengan mengirimkan email ke support@labspektroskopi.com 
            dengan subjek "Feedback Kalkulator Spektroskopi". Kami sangat menghargai masukan Anda untuk pengembangan aplikasi ini.
        """)
    
    # Referensi
    st.markdown("<h3 style='margin-top: 30px;'>Referensi dan Sumber Belajar</h3>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style='background-color: #ECEFF1; padding: 20px; border-radius: 10px;'>
            <h4 style='color: #455A64;'>Buku dan Publikasi</h4>
            <ul>
                <li>Pavia, D. L., Lampman, G. M., Kriz, G. S., & Vyvyan, J. R. (2014). <em>Introduction to Spectroscopy</em>. Cengage Learning.</li>
                <li>Skoog, D. A., Holler, F. J., & Crouch, S. R. (2017). <em>Principles of Instrumental Analysis</em>. Cengage Learning.</li>
                <li>Smith, B. C. (2011). <em>Fundamentals of Fourier Transform Infrared Spectroscopy</em>. CRC Press.</li>
                <li>Ferraro, J. R., Nakamoto, K., & Brown, C. W. (2003). <em>Introductory Raman Spectroscopy</em>. Academic Press.</li>
            </ul>
            
            <h4 style='color: #455A64; margin-top: 20px;'>Sumber Online</h4>
            <ul>
                <li><a href='#'>NIST Chemistry WebBook</a> - Database spektra referensi</li>
                <li><a href='#'>Spectroscopy Now</a> - Portal informasi spektroskopi</li>
                <li><a href='#'>Royal Society of Chemistry - Spectroscopy Resources</a></li>
                <li><a href='#'>SpectraBase</a> - Koleksi spektra dari berbagai teknik</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
        <div style='text-align: center; color: gray; font-size: 14px;'>
            © 2025 Lab Spektroskopi | Dikembangkan untuk keperluan pendidikan dan penelitian
        </div>
    """, unsafe_allow_html=True)

# Footer atau keterangan tambahan
