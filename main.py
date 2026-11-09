import folium
import streamlit as st
from streamlit_folium import st_folium
from folium import Popup
from locations import get_locations, get_buslocations

##################
if "selected_location" not in st.session_state:
    st.session_state.selected_location = None
#######################
st.set_page_config(
    page_title="Survival Center Map",
    layout="wide",
    initial_sidebar_state="expanded"
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
    #MainMenu
    footer 
    header 
    </style>
    """,
    unsafe_allow_html=True
)

NCLAT, NCLNG = 42.3323, -72.6412
mapfocus = [NCLAT, NCLNG]
current_zoom = 12

st.markdown("<h1 style='text-align: center;'>Survival Center Map</h1>", unsafe_allow_html=True)

all_locations = {**get_locations(), **get_buslocations()}

m = folium.Map(location=mapfocus, zoom_start=current_zoom, width="100%", height="100%")

for centername, centerinfo in all_locations.items():
    icon_color = "blue" if centername in get_locations() else "green"
    folium.Marker(
        location=[centerinfo["lat"], centerinfo["lng"]],
        popup=Popup(centername, parse_html=True), 
        tooltip=centername,
        icon=folium.Icon(color=icon_color, icon="info-sign")
    ).add_to(m)

map_data = st_folium(
    m, 
    height=650,  
    use_container_width=True
)

##########################
if map_data:
    clicked_target = map_data.get("last_object_clicked_popup")
    if clicked_target and clicked_target in all_locations:
        if st.session_state.selected_location != clicked_target:
            st.session_state.selected_location = clicked_target
            st.rerun()
#########################################
with st.sidebar:
    with st.expander("Survival Center Information", expanded=True):
        selected_loc = st.session_state.get("selected_location")
        if selected_loc and selected_loc in all_locations:
            info = all_locations[selected_loc]
            st.write(f"### {selected_loc}")
            
            if 'address' in info and info['address']:
                st.write(f"**Address:** {info['address']}")
            if 'phone' in info and info['phone']:
                st.write(f"**Phone:** {info['phone']}")
            if 'website' in info and info['website']:
                st.write(f"**Website:** [{info['website']}]({info['website']})")
            if 'schedule' in info and info['schedule']:
                st.write(f"**Schedule:** {info['schedule']}")
            if 'image' in info and info['image']:
                st.image(info['image'], width=200)
        else:
            st.info("Click on a marker on the map to view details here.")

