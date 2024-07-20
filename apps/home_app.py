import os
import streamlit as st
from hydralit import HydraHeadApp

MENU_LAYOUT = [1,1,1,7,2]

class HomeApp(HydraHeadApp):


    def __init__(self, title = 'Pencarian Catalog Data GNSS dan Plotting pada Peta', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title


    #This one method that must be implemented in order to be used in a Hydralit application.
    #The application must also inherit from the hydrapp class in order to correctly work within Hydralit.
    def run(self):
        st.markdown("<h1 style='text-align:center;padding: 0px 0px;color:black;font-size:200%;'>Aplikasi Pencarian Catalog Data GNSS</h1>",unsafe_allow_html=True)
        st.markdown('<br><br>',unsafe_allow_html=True) 

        _,_,col_logo, col_text,_ = st.columns(MENU_LAYOUT)
        col_logo.image(os.path.join(".","resources","data.png"),width=80,)
        col_text.subheader("Selamat datang di Aplikasi pencarian data GNSS yang lebih mudah dan efisien dengan Aplikasi Pencarian Catalog Data GNSS")  
        
        _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
        # if col_text.button('Uber Pickups ➡️'):
        #     self.do_redirect('Uber Pickups')
        col_logo.image(os.path.join(".","resources","titik.png"),width=90,)
        col_text.subheader("Berdasarkan Titik") 
        col_text.info("Temukan data GNSS yang Anda butuhkan dengan cepat dan akurat berdasarkan titik koordinat spesifik. Cukup masukkan titik lokasi yang diinginkan, dan aplikasi kami akan memberikan informasi lengkap yang Anda butuhkan. Tidak perlu lagi membuang waktu dengan pencarian manual yang memakan waktu.")

        _,_,col_logo, col_text,col_btn = st.columns(MENU_LAYOUT)
        # if col_text.button('Uber Pickups ➡️'):
        #     self.do_redirect('Uber Pickups')
        col_logo.image(os.path.join(".","resources","region.png"),width=90,)
        col_text.subheader("Berdasarkan Region") 
        col_text.info("Butuh data untuk area yang lebih luas? Aplikasi kami juga memungkinkan pencarian berdasarkan region. Pilih area yang Anda inginkan, dan kami akan menyajikan data GNSS dari seluruh region tersebut. Solusi sempurna untuk analisis skala besar dan proyek yang membutuhkan cakupan area yang luas.")








