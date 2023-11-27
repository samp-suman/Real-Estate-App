import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Real Estate System App - Gurgaon",
    page_icon="🏨",
)
PATH_Readme = Path("README.md")

st.image('house.png')

try:
    st.markdown(PATH_Readme.read_text())
except FileNotFoundError:
    st.error("README.md file not found.", icon="🔥")