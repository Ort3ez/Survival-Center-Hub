
import folium
import streamlit as st
from streamlit_folium import st_folium
from folium import Popup
from locations import get_locations
#from locations import get_buslocations

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



NCLAT, NCLNG = 42.3323, -72.6412
mapfocus = [NCLAT, NCLNG]
current_zoom = 12

st.markdown("<h1 style='text-align: center;'>Survival Center Map</h1>", unsafe_allow_html=True)

m = folium.Map(location=mapfocus, zoom_start=current_zoom, width="100%", height="100%")

for centername, centerinfo in get_locations().items():
    folium.Marker(
        location=[centerinfo["lat"], centerinfo["lng"]],
        
        popup=Popup(centername, parse_html=True), 
        tooltip=centername,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

#for mobilename, mobileinfo in get_buslocations().items():
    #folium.Marker(
       # location=[mobileinfo["lat"], mobileinfo["lng"]],
        
       # popup2=Popup(mobileinfo, parse_html=True), 
       # tooltip2=mobilename,
        #icon2=folium.Icon(color="blue", icon="info-sign")
    #).add_to(m)

map_data = st_folium(
    m, 
    height=650,  
    use_container_width=True
)

if map_data:
    
    clicked_target = map_data.get("last_object_clicked_popup")
    #clicked_target2 = map_data.get("last_object_clicked_popup2")

    
    #if clicked_target or clicked_target2 and not st.session_state.sidebar_expanded:
    if clicked_target or clicked_target and not st.session_state.sidebar_expanded:
        st.session_state.sidebar_expanded = True
        st.rerun()


    if st.session_state.sidebar_expanded:
        with st.sidebar.expander("Survival Center Information", expanded=True):
            # locations = {**get_locations(), **get_buslocations()}
            locations = get_locations()
            if clicked_target and clicked_target in locations:
                info = locations[clicked_target]
                st.write(f"### {clicked_target}")
                st.write(f"**Address:** {info['address']}")
                st.write(f"**Phone:** {info['phone']}")
                st.write(f"**Website:** [{info['website']}]({info['website']})")
                st.image(info['image'], width=200)

            """
            if 'website' in info and info['website']:
                st.write(f"**Website:** [{info['website']}]({info['website']})")
                
            if 'schedule' in info and info['schedule']:
                st.write(f"**Schedule:** {info['schedule']}")
                
            if 'image' in info and info['image']:
                st.image(info['image'], width=200)"""