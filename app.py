# Streamlit version: shows the same one-term-per-page viewer inside a Streamlit app.
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Golden Eagle AI Terms", page_icon="🦅", layout="wide")
st.markdown("<style>.block-container{padding:0.5rem 1rem 0 1rem;max-width:100%} header{visibility:hidden}</style>", unsafe_allow_html=True)

html = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
components.html(html, height=900, scrolling=False)
st.caption("Tip: click inside the viewer once, then use ← → to move between terms, Q for quiz mode, P to present.")
