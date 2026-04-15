"""
data_loader.py — Shared data loading functions for DraftMap.

Primary source: Airtable (if [airtable] secrets are configured).
Fallback:       data/rankings_YYYY.csv

If Airtable credentials exist in st.secrets, all pages read live from
Airtable. The CSV is kept as a local fallback / dev option.
To swap to Supabase later, only this file needs to change.
"""

import requests
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


def _fetch_airtable_records() -> list[dict]:
    """Fetch all raw records from Airtable, handling pagination."""
    cfg = st.secrets["airtable"]
    headers = {"Authorization": f"Bearer {cfg['token']}"}
    url = f"https://api.airtable.com/v0/{cfg['base_id']}/{cfg['table_id']}"

    records = []
    offset = None

    while True:
        params: dict = {"pageSize": 100}
        if offset:
            params["offset"] = offset

        resp = requests.get(url, headers=headers, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()

        records.extend(data.get("records", []))
        offset = data.get("offset")
        if not offset:
            break

    return records


def _records_to_df(records: list[dict]) -> pd.DataFrame:
    """Convert raw Airtable records to a normalised DataFrame."""
    rows = []
    for r in records:
        f = r.get("fields", {})
        rows.append({
            "name":   str(f.get("name",   "")),
            "pos":    str(f.get("pos",    "")),
            "rd":     f.get("rd",     0),
            "rank":   f.get("rank",   0),
            "height": str(f.get("height", "N/A")),
            "weight": f.get("weight", 0),
            "role":   str(f.get("role",   "Balanced")),
            "s1":     str(f.get("s1",     "N/A")),
            "s2":     str(f.get("s2",     "N/A")),
            "s3":     str(f.get("s3",     "N/A")),
            "school": str(f.get("school", "")),
        })

    df = pd.DataFrame(rows)

    # Normalise types
    df["pos"]    = df["pos"].str.strip().str.upper().replace({"DL": "DT"})
    df["rd"]     = pd.to_numeric(df["rd"],     errors="coerce").fillna(0).astype(int)
    df["rank"]   = pd.to_numeric(df["rank"],   errors="coerce").fillna(0).astype(int)
    df["weight"] = pd.to_numeric(df["weight"], errors="coerce").fillna(0).astype(int)

    # Any role that doesn't match a known band label falls through to Balanced
    # in the chart JS — no remapping needed here.

    return df


@st.cache_data(ttl=300)
def load_rankings(year: int = 2026) -> pd.DataFrame:
    """
    Load player rankings for a given draft year.

    Tries Airtable first if [airtable] secrets are present.
    Falls back to the local CSV if Airtable is unavailable or unconfigured.
    Cache TTL: 5 minutes, so Airtable edits propagate to the live chart
    within 5 minutes without a manual redeploy.
    """
    if "airtable" in st.secrets:
        try:
            records = _fetch_airtable_records()
            return _records_to_df(records)
        except Exception:
            # Silent fallback — don't surface errors to public chart viewers
            pass

    # ── CSV fallback ──────────────────────────────────────────────────────
    path = DATA_DIR / f"rankings_{year}.csv"
    if not path.exists():
        raise FileNotFoundError(f"Rankings file not found: {path}")
    df = pd.read_csv(path)
    df["pos"] = df["pos"].str.strip().str.upper().replace({"DL": "DT"})
    return df


@st.cache_data(ttl=3600)
def load_draft_results(year: int) -> pd.DataFrame:
    """Load historical draft results for a given year."""
    path = DATA_DIR / f"draft_results_{year}.csv"
    if not path.exists():
        raise FileNotFoundError(f"Draft results not found: {path}")
    df = pd.read_csv(path)
    df["Pos"] = df["Pos"].str.strip().str.upper().replace({"DT": "DT", "DL": "DT"})
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
