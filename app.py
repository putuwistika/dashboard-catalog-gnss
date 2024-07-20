import streamlit as st
import hydralit_components as hc
from hydralit import HydraApp
import apps
import apps.region
import apps.titik

#make it look nice from the start
st.set_page_config(page_title='Pencarian Catalog Data GNSS dan Plotting pada Peta',page_icon="💾",layout='wide',initial_sidebar_state='auto',)

if __name__ == '__main__':
    app = HydraApp(
        title='Pencarian Catalog Data GNSS dan Plotting pada Peta',
        favicon="🐙",
        hide_streamlit_markers=True,
        use_navbar=True, 
        navbar_sticky=True,
        navbar_animation=True,
        navbar_theme=True
    )
    app.add_app("Home", icon="🏠", app=apps.HomeApp(title='Home'),is_home=True)
    app.add_app("Berdasarkan Titik", icon="📍", app=apps.TitikApp(title="Berdasarkan Titik"))
    app.add_app("Berdasarkan Region", icon="⏲", app=apps.RegionApp(title="Berdasarkan Region"))
    complex_nav = {
    'Home': ['Home'],
    'Berdasarkan Region': ['Berdasarkan Region'],
    'Berdasarkan Titik': ['Berdasarkan Titik'],
    }
    app.run(complex_nav)
