import streamlit as st

# Mengatur konfigurasi halaman
st.set_page_config(
    page_title="Kalkulator",
    layout="wide"
)

# Judul utama halaman
st.title("Kalkulator")

# Sidebar dengan tiga pilihan menu
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
    "Pilih Opsi:",
    ["a", "B", "C"]
)

# Konten utama berdasarkan pilihan sidebar
if option == "a":
    st.header("Opsi a")
    st.write(
        "Spektroskopi UV-Vis adalah teknik analisis yang memanfaatkan interaksi sinar ultraviolet dan tampak dengan suatu sampel. "
        "Metode ini digunakan untuk mengukur absorbansi atau transmitansi cahaya pada panjang gelombang tertentu, "
        "sehingga dapat digunakan untuk menentukan konsentrasi zat terlarut."
    )
elif option == "B":
    st.header("Opsi B")
    st.write(
        "Spektroskopi Infrared (IR) adalah teknik untuk mempelajari getaran molekul yang disebabkan oleh penyerap gelombang inframerah. "
        "Setiap jenis ikatan kimia akan menyerap IR pada frekuensi khas, sehingga spektrum IR dapat digunakan untuk identifikasi gugus fungsi."
    )
else:
    st.header("Opsi C")
    st.write(
        "Spektroskopi Raman adalah metode analisis non-destruktif yang mengukur cahaya terpencar (scattered) dari sampel. "
        "Raman memberikan informasi tentang struktur molekul, ikatan kimia, dan interaksi molekular."
    )

# Footer atau keterangan tambahan
st.markdown("---")
st.markdown(
    "<small>Dibuat dengan Streamlit untuk tugas aplikasi spektroskopi.</small>",
    unsafe_allow_html=True
)
