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
from collections import defaultdict
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

    def safe_float(val):
        """Return float or None (never NaN — json.dumps can't serialize NaN)."""
        try:
            v = float(val)
            return None if pd.isna(v) else round(v, 3)
        except (ValueError, TypeError):
            return None

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
        # Combine measurables — null when not recorded
        "arm":    safe_float(row.get("arm")),
        "hand":   safe_float(row.get("hand")),
        "forty":  safe_float(row.get("forty")),
        "split10": safe_float(row.get("split10")),
        "vertical": safe_float(row.get("vertical")),
        "broad":  safe_float(row.get("broad")),
        "cone3":  safe_float(row.get("cone3")),
        "shuttle": safe_float(row.get("shuttle")),
        "bench":  safe_float(row.get("bench")),
    }


players_list = [row_to_player(row) for _, row in df.iterrows()]

# Compute position rank (posRank) — rank within each position group, sorted by overall rank.
# Used for the card ID label (e.g. "WR-03").
_pos_counters: dict = defaultdict(int)
for _p in sorted(players_list, key=lambda x: (x["pos"], x["rank"])):
    _pos_counters[_p["pos"]] += 1
    _p["posRank"] = _pos_counters[_p["pos"]]

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
components.html(chart_html, height=1400, scrolling=False)
