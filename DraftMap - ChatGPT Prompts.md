# DraftMap — ChatGPT Prompts
*Ready-to-paste prompts for tasks that don't need Claude. Copy, paste, bring the output back.*

---

## Design Sandbox — Start & End Prompts

### START PROMPT (paste this first, then paste the full HTML file contents below it)

```
I'm building an NFL draft analysis web app called DraftMap. Below is a self-contained HTML file — it has all the CSS, layout, and rendering logic in one file. The player data is fake (sandbox only).

Here's what the app currently looks like:
- Light warm-cream background with a dark green accent color
- A scatter chart with player dots colored by draft round (green through purple)
- Three zoom states toggled by buttons: Overview (one row per position), Roles (rows split into 3 sub-bands), and Players (dots get name labels)
- Tier labels across the top: Great / Good / Solid / Role Player/Project
- Position rows for all 11 NFL positions, Defense first, then Offense

I want your help iterating on the visual design — colors, typography, spacing, overall feel. I'm NOT asking you to change any JavaScript logic. Only touch the CSS (inside the <style> tag) and the static HTML structure (header, buttons, etc.).

To preview any changes, I'll copy your updated CSS into the file and open it in a browser.

Here is the full file:

[PASTE THE FULL CONTENTS OF draftmap-sandbox.html HERE]
```

---

### END PROMPT (paste this when you're happy with a direction and ready to bring it back to Claude)

```
I'm done iterating on this design session. Please give me a clean handoff package:

1. The complete updated <style> block (everything between <style> and </style>), with no omissions — I need to be able to drop it directly into the real file.
2. A short summary (3–5 bullets) of every visual change you made vs. the original, with the specific hex values or CSS property names changed. Example: "Background changed from #F5EFE4 to #0d1526" or "Button border-radius changed from 16px to 8px."
3. Any changes you made outside the <style> block (HTML structure, button text, etc.) — list those separately.

Do not include any JavaScript changes. I'll apply this to the real file manually.
```

---

## How to Use This

Each prompt below is ready to copy into ChatGPT (free tier is fine). After ChatGPT responds, take the best output and bring it into a Claude session — Claude will know what to do with it. The goal is to arrive at every Claude session with the creative/research work already done, so Claude time is spent building, not brainstorming.

---

## 1. Color Palette Exploration

Use this if you want to explore color options before bringing the newlife.com screenshot to Claude.

```
I'm building a dark-themed NFL draft analysis web app called DraftMap. The current color scheme uses a dark navy background (#0d1526), gold accent (#D4A017), white primary text, and slate secondary text (#94a3b8). I want to consider a warmer, more premium feel — think clean neutrals, warm off-whites, maybe inspired by sports media brands.

Give me 3 alternative color palette options. For each one, provide:
- Background color (hex)
- Panel/card color (hex)
- Primary accent color (hex)
- Primary text color (hex)
- Secondary text color (hex)
- A one-sentence description of the vibe

Keep the existing round colors (R1–R7 dot colors) intact — those don't change.
```

**Bring back to Claude:** The 1-2 palettes you like most, with their hex codes. Claude will apply them to the mockup.

---

## 2. Landing Page Copy

Use this before Phase 1 to draft home page text. Paste the output into the Claude session when building streamlit_app.py.

```
I'm building a free public NFL draft analysis web app called DraftMap. The tagline is "NFL Draft at a glance. Find your sleeper."

The app is a scatterplot that shows all draft prospects plotted by position and projected round. The philosophy is data over opinion — instead of reading talking heads' rankings, users can visually see position depth, talent cliffs (where the drop-off is), and athletic measurables for themselves.

Write the following for the home page:
1. A headline (10 words max)
2. A subheadline (1–2 sentences explaining what the app does and why it's different)
3. A 3-sentence "About" paragraph
4. 3 short feature blurbs (one sentence each) for: Draft Map view, Position Breakdown view, and Player Comparison view

Tone: Direct, confident, data-nerd credibility. Not hype-y. Think ESPN Stats & Info, not ESPN First Take.
```

**Bring back to Claude:** The headline, subheadline, and feature blurbs you want to use. Claude will place them in the app.

---

## 3. Control Tooltip Text

Use this before or during Phase 1 to write the helper text that appears on hover or below each UI control.

```
I'm building a web app called DraftMap that visualizes NFL draft prospects on a scatter chart. It has the following controls:

1. Year selector — toggle between 2023, 2024, 2025 (historical actual draft results) and 2026 (pre-draft projections)
2. Position filter — toggle buttons for "All Positions", "Offense", "Defense"
3. Zoom level — toggle between "Overview" (one row per position), "Roles" (rows split into 3 role sub-bands), and "Players" (shows player name labels)
4. Pre-Draft / Actual toggle — for 2026, only Pre-Draft is available until after the draft

Write a one-sentence tooltip or helper description for each of these four controls. Keep them under 15 words each. Tone should be informative but casual — like a knowledgeable friend, not a user manual.
```

**Bring back to Claude:** The 4 tooltip strings. Claude will add them to the UI.

---

## 4. Position Breakdown Layout Options

Use this before Phase 2 to arrive at a layout direction before asking Claude to build it.

```
I'm designing a "Position Breakdown" view for an NFL draft web app. This view should show all draft prospects grouped by position (QB, RB, WR, TE, OT, IOL, EDGE, DT, LB, CB, S), with each group showing players sorted by their projected draft round/rank. There are roughly 20–40 players per position.

Each player card should show: name, projected round, height, weight, and 1–3 strengths (like "Route Running · Hands · YAC").

Tier groupings within each position: Great (R1 picks 1–15), Good (R1 picks 16+ through R2), Solid (R3), Role Player/Project (R4–R6).

Suggest 3 different layout approaches for this view with tradeoffs for each. Consider that this is a web app, not a mobile app, and users will compare across positions. Think about readability, density, and ease of scanning.
```

**Bring back to Claude:** The layout approach you want to build, described in plain English. Claude will implement it.

---

## 5. Admin UI Design Brainstorm

Use this before Phase 3 to think through what the admin page should look like before asking Claude to build it.

```
I'm building a password-protected admin page for a web app that manages NFL draft prospect data. I (the admin) need to be able to:

- Edit a player's projected round and rank
- Edit scouting notes (free text, up to a paragraph)
- Change an upside rating (High / Medium / Low)
- Toggle a "Hawk flag" (Yes/No — means I'm specifically watching this player)
- Add or update a player's 1–3 strengths from a fixed list per position

There are about 313 players total. The data is stored as a CSV in GitHub and changes should save back there.

Suggest 2–3 approaches for how to lay out the admin UI for this. Consider that I'm the only user, so simplicity beats aesthetics. I want to be able to find a player fast and edit them without a lot of clicks.
```

**Bring back to Claude:** The admin layout you prefer described in plain English.

---

## 6. SignalScout Code Explanation

Use this before Phase 4. Paste in the actual SignalScout comparison engine code and ask ChatGPT to document it.

```
I have a Python function (or set of functions) that implements an NFL prospect comparison engine. It uses weighted Euclidean distance across combine measurables (height, weight, arm length, 40 time, vertical, broad jump, 3-cone, shuttle) with Z-score normalization and a missing-data penalty.

Here is the code:

[PASTE YOUR SIGNALSCOUT CODE HERE]

Please write plain-English documentation for this code that explains:
1. What each function does in 2–3 sentences
2. What the inputs and outputs are for each function
3. What the missing-data penalty system does and why it matters
4. What the position-based weights are and how they affect results

Write this so a non-engineer could understand it clearly.
```

**Bring back to Claude:** The plain-English documentation. This lets Claude port the engine without you re-explaining it from scratch.

---

## 7. Year-over-Year Chart Type Options

Use this before Phase 5 to choose a chart approach before Claude builds it.

```
I'm building a "Year-over-Year Accuracy" view for an NFL draft analysis app. Each year (2023, 2024, 2025), I published pre-draft player rankings. After the draft, I can compare my projected round/rank to where players actually got picked.

I want to visualize how accurate my pre-draft projections were. Some ideas:
- Round delta (I said Round 2, they went Round 3)
- Tier hit rate (did I have them in the right tier: Great / Good / Solid / Role Player?)
- Position-level accuracy (was I better at projecting WRs than QBs?)

Suggest 3 different chart types or visualizations that would work well for this data. For each, describe what it shows, what the X and Y axes would be, and what insight it gives the user. This is a Plotly chart in a Streamlit app.
```

**Bring back to Claude:** The chart approach you like, with the axes and insight described. Claude will implement it.

---

## 8. Mock Draft Helper Feature Brainstorm

Use this before Phase 6 when it's time to define what the tool actually does.

```
I'm building a "Mock Draft Partner" tool for NFL draft fans who run mock draft simulators (tools like DraftWarsHQ, Fantrax, etc.). When a user is on the clock and needs to make a pick, I want to help them make a better decision using my pre-draft prospect rankings and data.

The tool should help with: understanding remaining positional depth, identifying late-round sleepers, and comparing two players side by side when debating a pick.

Brainstorm 5–8 specific features or interactions this tool could have. For each, describe: what the user inputs, what the tool shows, and what decision it helps them make. Keep it realistic for a solo developer building a free web app — no APIs, no live data, just static pre-draft ranking data.
```

**Bring back to Claude:** Your 3–4 favorite features from the list. Claude will design the page around those.

---

## 9. Reddit Launch Post

Use this during Phase 7 for the launch post on r/NFLDraft or r/DynastyFF.

```
I'm launching a free web app called DraftMap — an NFL draft analysis tool that shows all prospects plotted visually on a scatter chart by position and projected round. The philosophy is data over opinion: instead of reading talking heads, users can see position depth, talent cliffs (where the drop-off is), and player measurables for themselves.

Features include:
- Draft Map scatter chart (2026 pre-draft projections + 2023–2025 actual results for comparison)
- Three zoom levels: Overview, Roles (sub-positions), and Players (individual labels + strengths)
- Position filter (Offense / Defense / All)
- Player comparison via athletic measurables (like a comp finder)
- Position Breakdown view

Write a Reddit post for r/NFLDraft announcing the launch. Tone: humble, football-nerd, genuinely excited — not marketing-speak. Lead with what makes it useful. Keep it under 300 words. Include a call to feedback at the end.
```

**Bring back to Claude:** Only if there's any technical editing needed. Otherwise post directly.

---

## 10. Twitter/X Launch Thread

Use this alongside the Reddit post during Phase 7.

```
I'm launching a free web app called DraftMap for NFL draft fans. It's a visual scatter chart showing all draft prospects by position and projected round, with zoom levels that reveal role sub-bands and individual player labels. The philosophy: data tells the story, not talking heads.

Write a 5-tweet launch thread for Twitter/X. Tweet 1 should be the hook. Tweets 2–4 should each highlight one key feature or the "why" behind the design. Tweet 5 should be a call to action. Keep each tweet under 250 characters (room for a link). Tone: confident, football-smart, conversational.
```

**Bring back to Claude:** Only if there's any technical editing needed.

---

## General Tips for Using ChatGPT Efficiently

**Be specific about format.** Tell ChatGPT exactly what you want back: "Give me 3 options," "Keep it under 15 words," "Write this as a bullet list." Vague prompts get vague answers.

**Paste code for explanation, not generation.** ChatGPT is great at explaining existing code in plain English. It's unreliable at generating complex code that needs to fit into a larger project. Use it for the former; bring the latter to Claude.

**Iterate in ChatGPT, not Claude.** If the first response isn't quite right, say "make it shorter," "make the tone more casual," or "give me 2 more options." Each iteration in ChatGPT is free. Each iteration in Claude costs context.

**Bring finished output, not drafts.** Don't bring ChatGPT's first attempt to Claude — refine it first. Claude sessions go faster when the input is already close to right.
