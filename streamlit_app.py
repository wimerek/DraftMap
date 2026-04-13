import streamlit as st

st.set_page_config(
    page_title="DraftMap",
    page_icon="🏈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container { padding-top: 2rem; }
    </style>
""", unsafe_allow_html=True)

st.title("DraftMap")
st.markdown("#### NFL Draft Analysis — Let the data tell the story.")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📊 Draft Chart")
    st.markdown("See the full draft class at a glance — depth by position, cliffs, and tier value by round.")
    if st.button("Open Draft Chart", use_container_width=True):
        st.switch_page("pages/1_Draft_Chart.py")

with col2:
    st.markdown("### 🔍 Position Breakdown")
    st.markdown("Top-down view by position with tiers and player names. Better than any pivot table.")
    if st.button("Open Position Breakdown", use_container_width=True, disabled=True):
        pass
    st.caption("Coming soon")

with col3:
    st.markdown("### ⚖️ Player Comparison")
    st.markdown("Compare athletic measurables side-by-side. Find the closest historical comps.")
    if st.button("Open Player Comparison", use_container_width=True, disabled=True):
        pass
    st.caption("Coming soon")

st.markdown("---")
st.caption("DraftMap · Built by Derek Wimer · Data: 2026 NFL Draft Projections")
