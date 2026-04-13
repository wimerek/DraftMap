"""
chart_helpers.py — Shared chart/viz utilities for DraftMap.

Plotly-based helpers used across pages.
"""

import plotly.graph_objects as go

ROUND_COLORS = {
    1: "#34d399",
    2: "#a3e635",
    3: "#facc15",
    4: "#fb923c",
    5: "#f87171",
    6: "#c084fc",
    7: "#94a3b8",
}

TIER_LABELS = [
    {"label": "Great",              "rounds": [1],    "picks_max": 15, "color": "#d97706"},
    {"label": "Good",               "rounds": [1, 2], "picks_min": 16, "color": "#059669"},
    {"label": "Solid",              "rounds": [3, 4],                  "color": "#2563eb"},
    {"label": "Role Player/Project","rounds": [5, 6, 7],               "color": "#7c3aed"},
]

BG_COLOR = "#0d1526"
GRID_COLOR = "#1e2d3d"
TEXT_COLOR = "#e2e8f0"


def apply_dark_theme(fig: go.Figure) -> go.Figure:
    """Apply the DraftMap dark navy theme to any Plotly figure."""
    fig.update_layout(
        paper_bgcolor=BG_COLOR,
        plot_bgcolor=BG_COLOR,
        font=dict(color=TEXT_COLOR, family="Inter, sans-serif"),
        margin=dict(l=60, r=120, t=60, b=40),
    )
    return fig
