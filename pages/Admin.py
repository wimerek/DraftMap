"""
Admin.py — Password-protected admin panel.

Edit player rankings, notes, upside, hawk flag.
Writes changes back to GitHub via API commit.

Access: Streamlit secrets required.
  [passwords]
  derek = "your-password-here"
"""

import streamlit as st
import pandas as pd
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

# ── Admin UI (Phase 3) ────────────────────────────────────────────────────────
st.title("DraftMap Admin")
st.success("Authenticated.")

st.info("Full admin editor coming in Phase 3.")

# Preview data
df = load_rankings(2026)
st.subheader(f"rankings_2026.csv — {len(df)} players")
st.dataframe(df, use_container_width=True)
