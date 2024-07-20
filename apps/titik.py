import streamlit as st
from pathlib import Path
import base64
import utils
from hydralit import HydraHeadApp
from itables.streamlit import interactive_table

# Thanks to streamlitopedia for the following code snippet
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

class TitikApp(HydraHeadApp):

    def __init__(self, title='', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        
    def run(self):
        self._cs_sidebar()
        self._cs_body()

    # sidebar
    def _cs_sidebar(self):
        with st.sidebar:
            # Kontainer styling
            st.markdown(
                """
                <style>
                    div[data-testid="stVerticalBlock"] div:has(div.select-bar) {
                        position: sticky;
                        top: 0;
                        background-color: white;
                        z-index: 999;
                    }
                    .select-bar {
                        border-bottom: 0 solid black;
                    }
                </style>
                """,
                unsafe_allow_html=True
            )
            st.sidebar.markdown(
                "<div style='padding-top: 0px; margin-top: -60px; margin-left: 40px;'>"
                f"<img src='{utils.replace_image('resources/titik.png', 'logo')}' alt='Logo' width='200'>",
                unsafe_allow_html=True,
            )
            # Pilih tanggal
            tanggal = st.date_input("Pilih Tanggal")
            lat = st.number_input("Latitude", format="%.2f")
            lon = st.number_input("Longitude", format="%.2f")
            st.markdown("<div class='select-bar'></div>", unsafe_allow_html=True)

            # Tombol submit
            submit = st.button("Submit")

            if submit:
                # Validasi input
                if not tanggal:
                    st.error("Silakan pilih tanggal terlebih dahulu.")
                else:
                    # Format tanggal ke string sesuai format SQL
                    tanggal_str = tanggal.strftime('%Y-%m-%d')
                    year = tanggal.year

                    # Tentukan tabel berdasarkan tahun
                    if 2019 <= year <= 2024:
                        table = f"catalog_{year}"
                    else:
                        st.error("Data untuk tahun ini tidak tersedia.")
                        return

                    # Query data berdasarkan pilihan user
                    query = f"SELECT * FROM {table} WHERE formatted_date = '{tanggal_str}'"
                    query += f" AND (CLAT BETWEEN '{lat-5}' AND '{lat+5}') AND (CLON BETWEEN '{lon-5}' AND '{lon+5}')"
                    
                    # Load data
                    df = utils.load_data(query)
                    
                    # Simpan data ke session state
                    st.session_state['data'] = df

    def _cs_body(self):
        if 'data' in st.session_state:
            df = st.session_state['data']
            
            if df.empty:
                st.error("Tidak ada data yang ditemukan.")
            else:
                # Tampilkan data
                interactive_table(df, buttons=["copyHtml5", "csvHtml5", "excelHtml5"])
        else:
            st.info("Silakan isi parameter di sidebar dan klik Submit untuk menampilkan data.")


