import streamlit as st
from pathlib import Path
import base64
import utils
import folium
from streamlit_folium import folium_static
from hydralit import HydraHeadApp
from itables.streamlit import interactive_table

# Fungsi untuk mengubah gambar menjadi bytes
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


class RegionApp(HydraHeadApp):

    def __init__(self, title='', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        
    def run(self):
        self._cs_sidebar()
        self._cs_body()

    # Sidebar
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
                f"<img src='{utils.replace_image('resources/region.png', 'logo')}' alt='Logo' width='200'></div>",
                unsafe_allow_html=True,
            )
            # Pilih rentang tanggal
            start_date = st.date_input("Pilih Start Date")
            end_date = st.date_input("Pilih End Date")
            slon = st.number_input("Start Longitude", format="%.2f")
            elon = st.number_input("End Longitude", format="%.2f")
            slat = st.number_input("Start Latitude", format="%.2f")
            elat = st.number_input("End Latitude", format="%.2f")
            st.markdown("<div class='select-bar'></div>", unsafe_allow_html=True)

            # Tombol submit
            submit = st.button("Submit")

            if submit:
                # Validasi input
                if not start_date or not end_date:
                    st.error("Silakan pilih start date dan end date.")
                elif start_date > end_date:
                    st.error("Start date tidak boleh lebih besar dari end date.")
                else:
                    # Simpan nilai ke session state
                    st.session_state['start_date'] = start_date
                    st.session_state['end_date'] = end_date
                    st.session_state['slon'] = slon
                    st.session_state['elon'] = elon
                    st.session_state['slat'] = slat
                    st.session_state['elat'] = elat

                    # Format tanggal ke string sesuai format SQL
                    start_date_str = start_date.strftime('%Y-%m-%d')
                    end_date_str = end_date.strftime('%Y-%m-%d')
                    year = start_date.year

                    # Tentukan tabel berdasarkan tahun
                    if 2019 <= year <= 2024:
                        table = f"catalog_{year}"
                    else:
                        st.error("Data untuk tahun ini tidak tersedia.")
                        return

                    # Query data berdasarkan pilihan user
                    query = f"SELECT * FROM {table} WHERE formatted_date BETWEEN '{start_date_str}' AND '{end_date_str}'"
                    query += f" AND (SLAT BETWEEN '{slat}' AND '{elat}') AND (SLON BETWEEN '{slon}' AND '{elon}')"
                    
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
                # st.dataframe(df)
                interactive_table(df, buttons=["copyHtml5", "csvHtml5", "excelHtml5"])
                map_center = [(st.session_state['slat'] + st.session_state['elat']) / 2, (st.session_state['slon'] + st.session_state['elon']) / 2]
                m = folium.Map(location=map_center, zoom_start=6, width='100%')
                for index, row in df.iterrows():
                    popup_text = f"({row['clat']}, {row['clon']}), {row['basefile']}"
                    folium.Marker([row['clat'], row['clon']], popup=popup_text).add_to(m)
                folium_static(m, width=1000, height=600)
        else:
            st.info("Silakan isi parameter di sidebar dan klik Submit untuk menampilkan data.")
