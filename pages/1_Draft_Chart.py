"""
1_Draft_Chart.py — Main draft chart view.

Positions as columns (X), Rounds as rows (Y).
Three zoom states: Overview, Roles, Players.
"""

import streamlit as st
import pandas as pd
from utils.data_loader import load_rankings, filter_by_side, POSITION_ORDER, ROUND_COLORS
from utils.chart_helpers import apply_dark_theme

st.set_page_config(page_title="Draft Chart · DraftMap", layout="wide")

st.title("Draft Chart")
st.caption("Positions as columns · Rounds as rows · Dots = players · Gaps = talent cliffs")

# ── Controls ──────────────────────────────────────────────────────────────────
col_side, col_zoom, col_spacer = st.columns([2, 2, 6])

with col_side:
    side = st.radio("Side of Ball", ["All", "Defense", "Offense"], horizontal=True)

with col_zoom:
    zoom = st.radio("View", ["Overview", "Roles", "Players"], horizontal=True)

# ── Data ──────────────────────────────────────────────────────────────────────
df = load_rankings(2026)
df = filter_by_side(df, side.lower())

# ── Chart (placeholder — full Plotly build in Phase 1 session) ───────────────
st.info("Draft Chart coming in Phase 1. Data loaded successfully.")
st.dataframe(df.head(20), use_container_width=True)
