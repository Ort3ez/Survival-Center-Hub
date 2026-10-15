import folium
import streamlit as st
from streamlit_folium import st_folium

st.set_page_config(page_title="Survival Center Map", page_icon=":map:", layout="wide")
st.markdown(
    """
    <style>
    
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
        max-width: 100%;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)


NCLAT,NCLNG = 42.3323, -72.6412

mapfocus = [NCLAT, NCLNG]
current_zoom = 12

st.markdown("<h1 style='text-align: center;'>Survival Center Map</h1>", unsafe_allow_html=True)


m = folium.Map(location=mapfocus, zoom_start=current_zoom, width="100%", height="100%")

folium.Marker(
    location=[NCLAT, NCLNG],
    popup= "Northampton Survival Center",
    tooltip = "Northampton Survival Center",
    icon=folium.Icon(color="blue", icon="info-sign")
).add_to(m)



st_folium(
    m, 
    height=850, 
    use_container_width=True
)

