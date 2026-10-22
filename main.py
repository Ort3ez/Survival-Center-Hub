import folium
import streamlit as st
from streamlit_folium import st_folium
from folium import Popup 

if "sidebar_expanded" not in st.session_state:
    st.session_state.sidebar_expanded = False

st.set_page_config(
    page_title="Survival Center Map",
    page_icon=":map:",
    layout="wide",
    initial_sidebar_state="expanded" if st.session_state.sidebar_expanded else "collapsed"
)

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
        "website": "https://www.northamptonsurvival.org/",
        "image": "https://www.northamptonsurvival.org/images/logo.png"
    },
    "Amherst Survival Center": {
        "lat": 42.3732,
        "lng": -72.5199,
        "address": "138 Sunderland Rd, Amherst, MA 01002",
        "phone": "(413) 256-4006",
        "website": "https://www.amherstsurvival.org/",
        "image": "https://www.amherstsurvival.org/images/logo.png"
    },
}

NCLAT, NCLNG = 42.3323, -72.6412
mapfocus = [NCLAT, NCLNG]
current_zoom = 12

st.markdown("<h1 style='text-align: center;'>Survival Center Map</h1>", unsafe_allow_html=True)

m = folium.Map(location=mapfocus, zoom_start=current_zoom, width="100%", height="100%")

for centername, centerinfo in SCLocations.items():
    folium.Marker(
        location=[centerinfo["lat"], centerinfo["lng"]],
        # FIX: Using folium.Popup forces a clean string transfer to streamlit-folium
        popup=Popup(centername, parse_html=True), 
        tooltip=centername,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

map_data = st_folium(
    m, 
    height=650,  
    use_container_width=True
)

if map_data:
    
    clicked_target = map_data.get("last_object_clicked_popup")

    
    if clicked_target and not st.session_state.sidebar_expanded:
        st.session_state.sidebar_expanded = True
        st.rerun()


    if st.session_state.sidebar_expanded:
        with st.sidebar.expander("Survival Center Information", expanded=True):
            if clicked_target and clicked_target in SCLocations:
                info = SCLocations[clicked_target]
                st.write(f"### {clicked_target}")
                st.write(f"**Address:** {info['address']}")
                st.write(f"**Phone:** {info['phone']}")
                st.write(f"**Website:** [{info['website']}]({info['website']})")
                st.image(info['image'], width=200)
            else:
                st.write("Click a map marker to view structural layout profile details.")
        
        
