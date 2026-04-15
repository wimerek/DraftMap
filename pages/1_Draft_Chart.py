"""
1_Draft_Chart.py — Main draft chart view.

Loads player data from the CSV and renders the DraftMap SVG chart via
st.components.v1.html(). The chart logic lives in draftmap-mockup-v2.html;
this page injects live CSV data and serves it inside a Streamlit iframe.

Chart design:
  - Positions as columns (X-axis)
  - Rounds as rows (Y-axis, R1 at top)
  - Dots colored by school, sized by round-tier
  - Three zoom states: Overview → Roles → Players
  - All controls (filter, zoom) are embedded in the HTML
"""

import json
import re
from pathlib import Path

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

from utils.data_loader import load_rankings

st.set_page_config(
    page_title="Draft Chart · DraftMap",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Hide Streamlit chrome for a cleaner embed ──────────────────────────────────
st.markdown(
    """
    <style>
    #MainMenu, footer, header { visibility: hidden; }
    .block-container { padding-top: 1rem; padding-bottom: 0rem; padding-left: 1rem !important; padding-right: 1rem !important; max-width: 100% !important; }
    [data-testid="stAppViewContainer"], .stApp { background-color: #F5EFE4; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Load data ──────────────────────────────────────────────────────────────────
df = load_rankings(2026)


def row_to_player(row: pd.Series) -> dict:
    """Convert a DataFrame row to the player object format expected by the chart JS."""

    def safe_str(val, default: str = "N/A") -> str:
        if pd.isna(val):
            return default
        v = str(val).strip()
        return v if v else default

    def safe_int(val, default: int = 0) -> int:
        try:
            return int(val)
        except (ValueError, TypeError):
            return default

    return {
        "name":   safe_str(row.get("name"), ""),
        "pos":    safe_str(row.get("pos"), ""),
        "rd":     safe_int(row.get("rd")),
        "rank":   safe_int(row.get("rank")),
        "height": safe_str(row.get("height")),
        "weight": safe_int(row.get("weight")),
        "role":   safe_str(row.get("role"), "Balanced"),
        "s1":     safe_str(row.get("s1")),
        "s2":     safe_str(row.get("s2")),
        "s3":     safe_str(row.get("s3")),
        "school": safe_str(row.get("school")),
    }


players_list = [row_to_player(row) for _, row in df.iterrows()]
players_json = json.dumps(players_list, indent=2)

# ── Load chart template and inject live data ───────────────────────────────────
APP_ROOT     = Path(__file__).parent.parent
template_path = APP_ROOT / "draftmap-mockup-v2.html"

if not template_path.exists():
    st.error(
        "Chart template not found. Expected: `draftmap-mockup-v2.html` in the app root."
    )
    st.stop()

template_html = template_path.read_text(encoding="utf-8")

# Replace the hard-coded players array with live CSV data.
# The mockup has:   const players = [ ... ];
# We inject:        const players = <json>;
chart_html, n_subs = re.subn(
    r"const players = \[.*?\];",
    f"const players = {players_json};",
    template_html,
    flags=re.DOTALL,
)

if n_subs == 0:
    st.error(
        "Data injection failed: could not find `const players = [...]` in the chart template. "
        "Check that `draftmap-mockup-v2.html` has not been modified."
    )
    st.stop()

# ── Render ─────────────────────────────────────────────────────────────────────
# Height of 1650px fits Overview mode fully; Players mode requires scrolling.
# scrolling=True adds a vertical scrollbar to the iframe when content overflows.
components.html(chart_html, height=900, scrolling=False)
