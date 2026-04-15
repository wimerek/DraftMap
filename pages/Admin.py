"""
Admin.py — Password-protected admin panel for DraftMap.

Player data is managed directly in Airtable (single source of truth).
This page provides a quick link into the base plus a live data preview
so you can confirm what the chart is currently reading.

Access: Streamlit secrets required.
  [passwords]
  derek = "your-password-here"
"""

import streamlit as st
from utils.data_loader import load_rankings

st.set_page_config(page_title="Admin · DraftMap", layout="wide")

# ── Auth ──────────────────────────────────────────────────────────────────────
def check_password() -> bool:
    """Simple password gate using st.secrets."""
    if "authenticated" in st.session_state and st.session_state.authenticated:
        return True

    st.title("DraftMap Admin")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        valid_passwords = list(st.secrets.get("passwords", {}).values())
        if password in valid_passwords:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Incorrect password.")
    return False


if not check_password():
    st.stop()

# ── Admin UI ──────────────────────────────────────────────────────────────────
st.title("DraftMap Admin")

st.markdown(
    "Player data lives in **Airtable** — your single source of truth. "
    "Edit players there directly. Changes appear in the live chart within 5 minutes."
)

st.link_button(
    "Open Airtable → Edit Players",
    "https://airtable.com/apphHlEBLATe8hrII/tblwqv6lrfmREuVt4",
    type="primary",
)

st.divider()

# ── Live data preview ─────────────────────────────────────────────────────────
st.subheader("Live Data Preview")
st.caption("What the chart is currently reading from Airtable. Cache refreshes every 5 minutes.")

if st.button("Force Refresh Now"):
    load_rankings.clear()
    st.rerun()

df = load_rankings(2026)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Players", len(df))
col2.metric("Rounds", df["rd"].nunique())
col3.metric("Positions", df["pos"].nunique())
col4.metric("Schools", df["school"].nunique())

st.dataframe(
    df.sort_values(["rd", "rank"]).reset_index(drop=True),
    use_container_width=True,
    hide_index=True,
)
