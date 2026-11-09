import folium
import streamlit as st
from streamlit_folium import st_folium
from locations import get_locations

st.set_page_config(page_title="Survival Center Map", page_icon=":map:", layout="wide")

st.markdown(
    """
    <style>
    .block-container {padding: 0rem; max-width: 100%;}
    #MainMenu, footer, header {visibility: hidden;}

    /* floating info panel on the right (needs Streamlit 1.39+ for key-based classes) */
    .st-key-info_panel {
        position: fixed;
        top: 80px;
        right: 20px;
        width: 320px;
        max-height: 80vh;
        overflow-y: auto;
        z-index: 1000;
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.3);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

@st.cache_data
def load_locations():
    return get_locations()

locations = load_locations()

if "selected" not in st.session_state:
    st.session_state.selected = None
if "last_seen" not in st.session_state:
    st.session_state.last_seen = None

st.markdown("<h1 style='text-align: center;'>Survival Center Map</h1>", unsafe_allow_html=True)

m = folium.Map(location=[42.3323, -72.6412], zoom_start=12)
for name, info in locations.items():
    folium.Marker(
        location=[info["lat"], info["lng"]],
        tooltip=name,
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(m)

map_data = st_folium(
    m,
    height=650,
    use_container_width=True,
    key="map",
    returned_objects=["last_object_clicked_tooltip"],
)

# Only react when the click actually changes, so closing the panel sticks
clicked = (map_data or {}).get("last_object_clicked_tooltip")
if clicked != st.session_state.last_seen:
    st.session_state.last_seen = clicked
    if clicked in locations:
        st.session_state.selected = clicked

# Panel only exists after a click
if st.session_state.selected:
    name = st.session_state.selected
    info = locations[name]
    with st.container(key="info_panel"):
        if st.button("✕ Close"):
            st.session_state.selected = None
            st.rerun()
        st.write(f"### {name}")
        st.write(f"**Address:** {info['address']}")
        st.write(f"**Phone:** {info['phone']}")
        st.write(f"**Website:** [{info['website']}]({info['website']})")
        if info.get("image"):
            st.image(info["image"], width=200)