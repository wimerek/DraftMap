"""
2_Player_List.py — Sortable, filterable player table with conditional formatting.

Phase 4 of DraftMap. Cell shading mirrors the positional grade thresholds
used in the player popup card (cardPositionalRangeData in the chart HTML).
  Bright amber shading = Great for that position
  Soft amber shading   = Good for that position
  No shading           = Average / no data
"""

import streamlit as st
import pandas as pd
from utils.data_loader import load_rankings, POSITION_ORDER

st.set_page_config(page_title="Player List · DraftMap", layout="wide")

# ── Nav ───────────────────────────────────────────────────────────────────────
st.page_link("pages/1_Draft_Chart.py", label="← Chart View", icon=None)

st.markdown("## Player List")
st.markdown(
    "Sort any column by clicking its header. "
    "Cell shading reflects positional measurable grades — "
    "<span style='background:rgba(212,160,23,0.65);color:#fff;"
    "padding:1px 7px;border-radius:3px;font-size:0.85em;font-weight:600'>"
    "bright amber</span> = Great &nbsp;·&nbsp; "
    "<span style='background:rgba(212,160,23,0.30);color:#fff;"
    "padding:1px 7px;border-radius:3px;font-size:0.85em;font-weight:600'>"
    "soft amber</span> = Good",
    unsafe_allow_html=True
)

# ── Load data ─────────────────────────────────────────────────────────────────

df = load_rankings(2026)

# ── Column definition (display order) ────────────────────────────────────────

DISPLAY_COLS = [
    "pos", "rd", "rank", "name", "school",
    "team_drafted", "rd_drafted", "pick_drafted",
    "height", "weight",
    "arm", "hand",
    "forty", "split10", "vertical", "broad", "cone3", "shuttle", "bench",
    "role", "s1", "s2", "s3",
]

# ── Positional thresholds ─────────────────────────────────────────────────────
# Source: cardPositionalRangeData in draftmap-mockup-v2.html
# Tuple format: (good_threshold, great_threshold, lower_is_better)
#   lower_is_better=True  → speed/agility metrics (lower = faster = better)
#   lower_is_better=False → size/power metrics (higher = better)

THRESHOLDS: dict[str, dict[str, tuple]] = {
    "CB": {
        "forty":   (4.50, 4.40, True),  "split10": (1.58, 1.54, True),
        "cone3":   (7.10, 6.90, True),  "shuttle": (4.40, 4.20, True),
        "vertical":(35,   38,   False), "broad":   (123,  125,  False),
        "arm":     (31,   32,   False), "hand":    (9.0,  9.5,  False),
        "weight":  (190,  198,  False), "bench":   (14,   17,   False),
    },
    "DT": {
        "forty":   (5.10, 4.90, True),  "split10": (1.80, 1.75, True),
        "cone3":   (8.00, 7.70, True),  "shuttle": (4.79, 4.69, True),
        "vertical":(29,   32,   False), "broad":   (105,  112,  False),
        "arm":     (32,   33,   False), "hand":    (9.5,  10,   False),
        "weight":  (298,  305,  False), "bench":   (24,   30,   False),
    },
    "EDGE": {
        "forty":   (4.70, 4.60, True),  "split10": (1.65, 1.60, True),
        "cone3":   (7.10, 7.00, True),  "shuttle": (4.40, 4.30, True),
        "vertical":(33,   36,   False), "broad":   (119,  122,  False),
        "arm":     (32,   33,   False), "hand":    (9.5,  10,   False),
        "weight":  (245,  255,  False), "bench":   (22,   26,   False),
    },
    "IOL": {
        "forty":   (5.20, 5.10, True),  "split10": (1.80, 1.75, True),
        "cone3":   (8.00, 7.70, True),  "shuttle": (4.79, 4.69, True),
        "vertical":(29,   32,   False), "broad":   (105,  111,  False),
        "arm":     (32,   33,   False), "hand":    (9.5,  10,   False),
        "weight":  (298,  305,  False), "bench":   (24,   30,   False),
    },
    "LB": {
        "forty":   (4.65, 4.55, True),  "split10": (1.62, 1.58, True),
        "cone3":   (7.20, 7.00, True),  "shuttle": (4.39, 4.29, True),
        "vertical":(33,   37,   False), "broad":   (119,  122,  False),
        "arm":     (31,   32,   False), "hand":    (9.0,  10,   False),
        "weight":  (230,  235,  False), "bench":   (18,   22,   False),
    },
    "OT": {
        "forty":   (5.20, 5.10, True),  "split10": (1.80, 1.76, True),
        "cone3":   (7.85, 7.75, True),  "shuttle": (4.79, 4.69, True),
        "vertical":(31,   33,   False), "broad":   (109,  113,  False),
        "arm":     (32.5, 33.5, False), "hand":    (9.5,  10,   False),
        "weight":  (298,  305,  False), "bench":   (26,   28,   False),
    },
    "QB": {
        "forty":   (4.70, 4.60, True),  "split10": (1.65, 1.55, True),
        "cone3":   (7.15, 7.00, True),  "shuttle": (4.35, 4.25, True),
        "vertical":(32,   35,   False), "broad":   (120,  124,  False),
        "arm":     (31,   32,   False), "hand":    (9.5,  10,   False),
        "weight":  (200,  215,  False), "bench":   (14,   17,   False),
    },
    "RB": {
        "forty":   (4.59, 4.49, True),  "split10": (1.59, 1.54, True),
        "cone3":   (7.10, 6.90, True),  "shuttle": (4.39, 4.29, True),
        "vertical":(33,   37,   False), "broad":   (121,  125,  False),
        "arm":     (30,   31,   False), "hand":    (9.0,  9.5,  False),
        "weight":  (205,  215,  False), "bench":   (20,   24,   False),
    },
    "S": {
        "forty":   (4.59, 4.49, True),  "split10": (1.59, 1.54, True),
        "cone3":   (7.10, 6.95, True),  "shuttle": (4.39, 4.29, True),
        "vertical":(34,   37,   False), "broad":   (123,  125,  False),
        "arm":     (31,   32,   False), "hand":    (9.0,  9.5,  False),
        "weight":  (195,  200,  False), "bench":   (15,   18,   False),
    },
    "TE": {
        "forty":   (4.65, 4.55, True),  "split10": (1.65, 1.60, True),
        "cone3":   (7.20, 7.10, True),  "shuttle": (4.40, 4.30, True),
        "vertical":(33,   36,   False), "broad":   (119,  122,  False),
        "arm":     (32,   33,   False), "hand":    (9.5,  10,   False),
        "weight":  (240,  250,  False), "bench":   (20,   24,   False),
    },
    "WR": {
        "forty":   (4.49, 4.44, True),  "split10": (1.58, 1.54, True),
        "cone3":   (7.00, 6.80, True),  "shuttle": (4.40, 4.20, True),
        "vertical":(35,   38,   False), "broad":   (123,  125,  False),
        "arm":     (31,   32,   False), "hand":    (9.5,  10,   False),
        "weight":  (185,  195,  False), "bench":   (14,   17,   False),
    },
}

# Height: NFL scout integer format (e.g. 6020 = 6'2") — always higher is better
HEIGHT_THRESHOLDS: dict[str, tuple] = {
    "CB":   (6000, 6020), "DT":   (6020, 6030), "EDGE": (6030, 6040),
    "IOL":  (6020, 6040), "LB":   (6000, 6010), "OT":   (6050, 6060),
    "QB":   (6010, 6030), "RB":   (5110, 6000), "S":    (6000, 6010),
    "TE":   (6040, 6050), "WR":   (6000, 6020),
}

GRADED_NUMERIC = {"arm", "hand", "forty", "split10", "vertical", "broad", "cone3", "shuttle", "bench", "weight"}

GRADE_BG = {
    "great": "background-color: rgba(212, 160, 23, 0.65); color: #ffffff;",
    "good":  "background-color: rgba(212, 160, 23, 0.30); color: #ffffff;",
    "":      "",
}


def _grade_numeric(val, pos: str, metric: str) -> str:
    """Return 'great', 'good', or '' for a numeric measurable."""
    if pd.isna(val) or val == 0:
        return ""
    thresh = THRESHOLDS.get(pos, {}).get(metric)
    if thresh is None:
        return ""
    good, great, lower = thresh
    if lower:
        return "great" if val <= great else ("good" if val <= good else "")
    else:
        return "great" if val >= great else ("good" if val >= good else "")


def _grade_height(height_str: str, pos: str) -> str:
    """Return 'great', 'good', or '' for a height string in NFL scout format."""
    try:
        val = int(str(height_str).strip())
    except (ValueError, TypeError):
        return ""
    thresh = HEIGHT_THRESHOLDS.get(pos)
    if thresh is None:
        return ""
    good, great = thresh
    return "great" if val >= great else ("good" if val >= good else "")


def _style_row(row: pd.Series) -> list[str]:
    """Return a list of CSS strings, one per column, for a player row."""
    pos = str(row.get("pos", ""))
    styles = []
    for col in row.index:
        if col in GRADED_NUMERIC:
            styles.append(GRADE_BG[_grade_numeric(row[col], pos, col)])
        elif col == "height":
            styles.append(GRADE_BG[_grade_height(row[col], pos)])
        else:
            styles.append("")
    return styles


# ── Filters ───────────────────────────────────────────────────────────────────

f1, f2, f3 = st.columns([2, 1, 2])

with f1:
    pos_filter = st.multiselect("Position", options=POSITION_ORDER, default=[], placeholder="All positions")
with f2:
    round_filter = st.multiselect("Round", options=[1, 2, 3, 4, 5, 6, 7], default=[], placeholder="All")
with f3:
    search = st.text_input("Search player", placeholder="Type a name…")

# ── Filter & sort ─────────────────────────────────────────────────────────────

view = df[DISPLAY_COLS].copy()
view = view.sort_values(["rd", "rank"], ascending=True).reset_index(drop=True)

if pos_filter:
    view = view[view["pos"].isin(pos_filter)]
if round_filter:
    view = view[view["rd"].isin(round_filter)]
if search.strip():
    view = view[view["name"].str.contains(search.strip(), case=False, na=False)]

st.write(f"**{len(view)} players**")

# ── Style & render ────────────────────────────────────────────────────────────

styled = view.style.apply(_style_row, axis=1)

st.dataframe(
    styled,
    use_container_width=True,
    hide_index=True,
    column_config={
        "pos":      st.column_config.TextColumn("Pos",     width="small"),
        "rd":       st.column_config.NumberColumn("Rd",    width="small",  format="%d"),
        "rank":     st.column_config.NumberColumn("Rank",  width="small",  format="%d"),
        "name":     st.column_config.TextColumn("Player",  width="medium"),
        "school":       st.column_config.TextColumn("School",       width="medium"),
        "team_drafted": st.column_config.TextColumn("Team",         width="small"),
        "rd_drafted":   st.column_config.NumberColumn("Rd Drafted", width="small",  format="%d"),
        "pick_drafted": st.column_config.NumberColumn("Pick",       width="small",  format="%d"),
        "height":   st.column_config.TextColumn("Height",  width="small"),
        "weight":   st.column_config.NumberColumn("Wt",    width="small",  format="%d"),
        "arm":      st.column_config.NumberColumn("Arm",   width="small",  format="%.2f"),
        "hand":     st.column_config.NumberColumn("Hand",  width="small",  format="%.2f"),
        "forty":    st.column_config.NumberColumn("40yd",  width="small",  format="%.2f"),
        "split10":  st.column_config.NumberColumn("10yd",  width="small",  format="%.2f"),
        "vertical": st.column_config.NumberColumn("Vert",  width="small",  format="%.1f"),
        "broad":    st.column_config.NumberColumn("Broad", width="small",  format="%.1f"),
        "cone3":    st.column_config.NumberColumn("3-Cone",width="small",  format="%.2f"),
        "shuttle":  st.column_config.NumberColumn("Shuttle",width="small", format="%.2f"),
        "bench":    st.column_config.NumberColumn("Bench", width="small",  format="%d"),
        "role":     st.column_config.TextColumn("Role",    width="medium"),
        "s1":       st.column_config.TextColumn("S1",      width="medium"),
        "s2":       st.column_config.TextColumn("S2",      width="medium"),
        "s3":       st.column_config.TextColumn("S3",      width="medium"),
    },
)
