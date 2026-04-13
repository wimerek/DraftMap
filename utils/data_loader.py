"""
data_loader.py — Shared data loading functions for DraftMap.

All pages import from here. If we swap from CSV to Supabase later,
only this file needs to change.
"""

import pandas as pd
import streamlit as st
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

POSITION_ORDER = ["EDGE", "DT", "LB", "CB", "S", "RB", "WR", "TE", "OT", "IOL", "QB"]
DEFENSE = ["EDGE", "DT", "LB", "CB", "S"]
OFFENSE = ["RB", "WR", "TE", "OT", "IOL", "QB"]

ROUND_COLORS = {
    1: "#34d399",
    2: "#a3e635",
    3: "#facc15",
    4: "#fb923c",
    5: "#f87171",
    6: "#c084fc",
    7: "#94a3b8",
}


@st.cache_data(ttl=300)
def load_rankings(year: int = 2026) -> pd.DataFrame:
    """Load player rankings for a given draft year."""
    path = DATA_DIR / f"rankings_{year}.csv"
    if not path.exists():
        raise FileNotFoundError(f"Rankings file not found: {path}")
    df = pd.read_csv(path)
    # Normalize position column (handle DT/DL alias from historical data)
    df["pos"] = df["pos"].str.strip().str.upper()
    df["pos"] = df["pos"].replace({"DL": "DT"})
    return df


@st.cache_data(ttl=3600)
def load_draft_results(year: int) -> pd.DataFrame:
    """Load historical draft results for a given year."""
    path = DATA_DIR / f"draft_results_{year}.csv"
    if not path.exists():
        raise FileNotFoundError(f"Draft results not found: {path}")
    df = pd.read_csv(path)
    df["Pos"] = df["Pos"].str.strip().str.upper()
    df["Pos"] = df["Pos"].replace({"DT": "DT", "DL": "DT"})
    return df


def filter_by_side(df: pd.DataFrame, side: str) -> pd.DataFrame:
    """Filter rankings dataframe by 'offense', 'defense', or 'all'."""
    if side == "offense":
        return df[df["pos"].isin(OFFENSE)]
    elif side == "defense":
        return df[df["pos"].isin(DEFENSE)]
    return df


def get_available_years() -> list[int]:
    """Return sorted list of years with rankings data available."""
    files = DATA_DIR.glob("rankings_*.csv")
    years = []
    for f in files:
        try:
            year = int(f.stem.split("_")[1])
            years.append(year)
        except (ValueError, IndexError):
            pass
    return sorted(years, reverse=True)
