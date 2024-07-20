import streamlit as st
import hydralit_components as hc
from hydralit import HydraApp
import apps
import apps.region
import apps.titik
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

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
    
    def image(src_as_string, **style):
        return img(src=src_as_string, style=styles(**style))

    def link(link, text, **style):
        return a(_href=link, _target="_blank", style=styles(**style))(text)

    def layout(*args):

        style = """
        <style>
        # MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """

        style_div = styles(
            left=0,
            bottom=0,
            margin=px(0, 0, 0, 0),
            width=percent(100),
            text_align="center",
            height="60px",
            opacity=0.6
        )

        style_hr = styles(
        )

        body = p()
        foot = div(style=style_div)(hr(style=style_hr), body)

        st.markdown(style, unsafe_allow_html=True)

        for arg in args:
            if isinstance(arg, str):
                body(arg)
            elif isinstance(arg, HtmlElement):
                body(arg)

        st.markdown(str(foot), unsafe_allow_html=True)

    def footer():
        myargs = [
            "<b>Made with</b>: Python 3.12 ",
            link("https://www.python.org/", image('https://i.imgur.com/ml09ccU.png',
                width=px(18), height=px(18), margin= "0em")),
            ", Streamlit ",
            link("https://streamlit.io/", image('https://docs.streamlit.io/logo.svg',
                width=px(24), height=px(25), margin= "0em")),
            ", Docker ",
            link("https://www.docker.com/", image('https://upload.wikimedia.org/wikipedia/en/thumb/f/f4/Docker_logo.svg/120px-Docker_logo.svg.png',
                width=px(45), height=px(18), margin= "0em")),
            " and PostgreSQL ",
            link("https://www.postgresql.org", image('https://www.postgresql.org/media/img/about/press/elephant.png',
                width=px(19), height=px(19), margin= "0em", align="top")),
            br(),
            "<b>Copyright © </b> 2024 MeteoITBDev. All Rights Reserved.",
        ]
        layout(*myargs)

if __name__ == "__main__":
    footer()
