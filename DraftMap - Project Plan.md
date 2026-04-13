# DraftMap — Project Plan
*Last updated: 2026-04-10*

---

## How to Use This Document

This is the master reference for building DraftMap. Every phase is broken into sub-tasks with a designated **AI tool** to minimize Claude usage limits and keep work moving. The rule is simple: Claude handles anything that requires deep project context, complex code, or debugging. Everything else goes to ChatGPT or another free tool first.

---

## AI Tool Routing Guide

| Task Type | Use This |
|---|---|
| HTML mockup iterations | **Claude** — requires full spec context |
| Complex Python / Streamlit code | **Claude** |
| Debugging errors | **Claude** |
| Data pipeline / CSV parsing code | **Claude** |
| Architecture & design decisions | **Claude** |
| Simple CSS tweaks (colors, spacing) after design is set | ChatGPT |
| Writing UI copy, labels, tooltips, marketing text | ChatGPT |
| Logo concept brainstorming / image generation | ChatGPT (DALL-E) |
| Color palette exploration (suggest hex values) | ChatGPT |
| Basic boilerplate code (bring to Claude for integration) | ChatGPT |
| Explaining what a block of code does | ChatGPT |
| Research (community forums, SEO strategy, domain ideas) | ChatGPT / Google |
| Writing README or documentation | ChatGPT |
| Drafting Reddit / Twitter posts for launch | ChatGPT |

**Practical rule:** If you could answer the question with a Google search or a quick creative prompt, it doesn't need Claude. If the task requires knowing what's in the spec, what data looks like, or why a bug is happening — that's Claude.

---

## Current Status

**Phase:** Pre-Phase 1 — Visual Mockup
**Status:** One item remaining before mockup approval
**Mockup file:** `C:\Users\wimer\OneDrive\Faith\Claude\Projects\NFL Draft Database and View Site\draftmap-mockup.html`

### What's Done
- Full interactive HTML mockup with 227 real players embedded
- Three zoom states working: Overview → Roles → Players
- Position filter (Offense / Defense / All)
- Defense-first position order, QB last
- Tier labels (Great / Good / Solid / Role Player/Project) with pill boxes, background fills, and dashed boundary lines
- Alternating row backgrounds, 4px left accent strips (teal = defense, yellow-green = offense), 2px bottom borders
- Role sub-bands with Balanced band teal tint; band labels at right edge
- 3-line player labels: Name / Round+Pick+Height+Weight / Strengths
- Floating Player Legend (top-right, gold border, Players zoom only)
- X-position math fixed (rank order within full position+round)
- Height format fixed

### One Item Remaining
- **Color scheme:** Derek likes the palette from newlife.com (warm whites, clean neutrals). Need a screenshot to apply it. This is the gate before mockup approval.

---

## Phase Plan

---

### Pre-Phase 1 — Visual Mockup
*Goal: A fully approved static HTML mockup that locks the visual design before any Streamlit code is written.*

| Sub-task | AI Tool | Status |
|---|---|---|
| Chart layout, zoom states, position order | Claude | ✅ Done |
| Tier labels, row backgrounds, band differentiators | Claude | ✅ Done |
| Player labels, legend, label stagger | Claude | ✅ Done |
| **Color scheme from newlife.com reference** | **Claude** | ⏳ Blocked — need screenshot |
| Additional UI polish (anything discovered after colors) | Claude | Pending |
| **Mockup approval gate — Derek signs off** | — | Pending |

**What to bring to Claude:** The newlife.com screenshot + any remaining UI issues found after seeing the color update applied.

**What to do in ChatGPT before that session:** If you want to explore color options before committing, paste a description of the dark navy + gold scheme and ask ChatGPT to suggest warm-neutral alternatives with hex values. Bring the ones you like into Claude for application.

---

### Phase 0 — Naming & Domain
*Goal: Register draftmap.io after the build is further along.*

| Sub-task | AI Tool | Status |
|---|---|---|
| Name decided: DraftMap | — | ✅ Done |
| Domain: draftmap.io (draftmap.com taken) | — | ✅ Decided |
| Register domain on Namecheap | Derek (manual) | Not started — defer until closer to launch |

---

### Phase 1 — App Scaffold + Draft Chart
*Goal: Working Streamlit app with the Draft Chart as page 1. Deployed to Streamlit Community Cloud. Matches the approved mockup.*

| Sub-task | AI Tool | Status |
|---|---|---|
| Set up GitHub repo structure (folders, initial files) | Claude | Not started |
| Write data_loader.py (read CSVs from GitHub) | Claude | Not started |
| Write chart_helpers.py (Plotly scatter chart) | Claude | Not started |
| Build streamlit_app.py (home / landing page) | Claude | Not started |
| Build 1_Draft_Chart.py page | Claude | Not started |
| Wire up year selector, position filter, zoom toggle | Claude | Not started |
| Deploy to Streamlit Community Cloud | Derek (manual, ~10 min) | Not started |
| Write landing page copy and header text | ChatGPT | Not started |
| Write tooltip text for controls (what does each button do?) | ChatGPT | Not started |

**Before starting Phase 1:** Use ChatGPT to draft the home page headline, subhead, and short description of what DraftMap is. Bring that text into the Claude session ready to paste in — saves Claude tokens on copywriting.

---

### Phase 2 — Position Breakdown View
*Goal: A clean position-by-position depth chart view. Replaces the Excel pivot tables. Shows players by position, tier groupings, and names.*

| Sub-task | AI Tool | Status |
|---|---|---|
| Design the layout (wireframe it on paper or in ChatGPT) | ChatGPT | Not started |
| Build 2_Position_Breakdown.py | Claude | Not started |
| Position depth logic (group by position, sort by rank) | Claude | Not started |
| Tier grouping visual treatment | Claude | Not started |
| Write UI labels and section headers | ChatGPT | Not started |

**ChatGPT prompt to try first:** "I'm building a position breakdown view for an NFL draft analysis app. It should show players grouped by position (QB, RB, WR, etc.) with tier groupings (Great / Good / Solid / Role Player). Suggest 2-3 layout options with their tradeoffs." Bring the best idea to Claude to build.

---

### Phase 3 — Admin / Player Data Editor
*Goal: Password-protected admin page inside the same Streamlit app. Derek can edit rankings, notes, upside ratings, hawk flags, and save back to GitHub.*

| Sub-task | AI Tool | Status |
|---|---|---|
| Design admin UI (which fields, what layout) | ChatGPT | Not started |
| Build Admin.py with st.secrets password check | Claude | Not started |
| Editable data table (st.data_editor) | Claude | Not started |
| GitHub write-back on save | Claude | Not started |
| Multi-user credential support | Claude | Not started |

**Note:** This is one of the more complex phases. Don't let ChatGPT write the GitHub write-back code — it'll get the details wrong without project context. Bring that entirely to Claude.

---

### Phase 4 — Measurables / Player Comparison
*Goal: Port the SignalScout engine into DraftMap as a view. Weighted Euclidean distance, Z-score normalization, position-based weights, missing-data penalty.*

| Sub-task | AI Tool | Status |
|---|---|---|
| Locate SignalScout GitHub repo + data structure | Derek (manual) | Not started |
| Understand existing engine code | ChatGPT (paste the code, ask for explanation) | Not started |
| Port engine into utils/compare_engine.py | Claude | Not started |
| Build 3_Player_Comparison.py page | Claude | Not started |
| Wire in combine_measurables.csv | Claude | Not started |
| Tune position weights for 2026 data | Derek + Claude | Not started |

**ChatGPT shortcut:** Paste the SignalScout player_comparison.py into ChatGPT and ask it to write plain-English documentation explaining exactly what each function does. Bring that doc into the Claude session so you don't spend tokens re-explaining the engine.

---

### Phase 5 — Year-over-Year Accuracy
*Goal: Visualize how Derek's pre-draft rankings compared to actual draft results across 2023–2025.*

| Sub-task | AI Tool | Status |
|---|---|---|
| Define the accuracy metric (round delta? exact pick? tier hit rate?) | Derek + Claude | Not started |
| Decide on chart type for accuracy display | ChatGPT (brainstorm options) | Not started |
| Parse historical draft results CSVs | Claude | Not started |
| Join pre-draft rankings to actual picks | Claude | Not started |
| Build 4_Year_Over_Year.py page | Claude | Not started |
| Write interpretive copy ("How to read this chart") | ChatGPT | Not started |

---

### Phase 6 — Mock Draft Partner Tool
*Goal: Round-by-round decision support for users running NFL draft simulators. Position value comparison, late-round sleepers, remaining depth.*

| Sub-task | AI Tool | Status |
|---|---|---|
| Define the core use case and user flow | Derek + Claude (dialogue first) | Not started |
| Brainstorm feature set and filters | ChatGPT | Not started |
| Build 5_Mock_Draft_Helper.py | Claude | Not started |
| Write "How to use this tool" explainer | ChatGPT | Not started |

---

### Phase 7 — Public Launch
*Goal: Custom domain live, community distribution, optional SEO landing page.*

| Sub-task | AI Tool | Status |
|---|---|---|
| Register draftmap.io on Namecheap | Derek (manual) | Not started |
| Point custom domain to Streamlit URL | Derek + Claude (for DNS config help) | Not started |
| Write Reddit post for r/NFLDraft and r/DynastyFF | ChatGPT | Not started |
| Write Twitter/X launch thread | ChatGPT | Not started |
| Optional: GitHub Pages SEO landing page | Claude | Not started |
| Submit app to mock draft simulator communities | Derek (manual outreach) | Not started |

---

## Session Protocol

To avoid burning Claude context unnecessarily, follow this rhythm for every Claude session:

1. **Before the session:** Do any ChatGPT prep work listed for that sub-task. Arrive with copy, wireframes, or code explanations already in hand.
2. **Start the session:** State the specific sub-task you want to accomplish (not the whole phase). Reference this doc.
3. **During the session:** Stay focused on one sub-task. Don't let sessions sprawl into adjacent tasks — those go on the list for next time.
4. **End the session:** Before context runs out, ask Claude to summarize what was built and what the next sub-task is. Save that as a note so the next session starts fast.

---

## Key Decisions Already Locked

- **Stack:** Python / Streamlit / Plotly / GitHub CSVs → Supabase later
- **Hosting:** Streamlit Community Cloud (free)
- **Position labels:** QB, RB, WR, TE, OT, IOL, EDGE, DT, LB, CB, S
- **Round colors:** R1=#34d399, R2=#a3e635, R3=#facc15, R4=#fb923c, R5=#f87171, R6=#c084fc, R7=#94a3b8
- **Weaknesses removed:** Strengths only (up to 3 per player)
- **Blank role = Balanced band** by default
- **Position order:** Defense first (EDGE, DT, LB, CB, S), then Offense (RB, WR, TE, OT, IOL, QB)
- **Click-to-modal:** Deferred to a later phase
- **Domain:** draftmap.io — register after build is further along
