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


SCLocations = {
    "Northampton Survival Center": {
        "lat": 42.3323,
        "lng": -72.6412,
        "address": "265 Prospect St, Northampton, MA 01060",
        "phone": "(413) 584-2662",
        "website": "https://www.northamptonsurvival.org/"
    },
    "Amherst Survival Center": {
        "lat": 42.3732,
        "lng": -72.5199,
        "address": "138 Sunderland Rd, Amherst, MA 01002",
        "phone": "(413) 256-4006",
        "website": "https://www.amherstsurvival.org/"
    },
}

NCLAT,NCLNG = 42.3323, -72.6412

mapfocus = [NCLAT, NCLNG]
current_zoom = 12

st.markdown("<h1 style='text-align: center;'>Survival Center Map</h1>", unsafe_allow_html=True)


m = folium.Map(location=mapfocus, zoom_start=current_zoom, width="100%", height="100%")

for centername, centerinfo in SCLocations.items():
    folium.Marker(
        location= [centerinfo["lat"], centerinfo["lng"]],
        popup= centername,
        tooltip = centername,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)



mapstuff= st_folium(
    m, 
    height=850,  
    use_container_width=True
)

