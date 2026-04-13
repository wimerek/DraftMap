# DraftMap — Claude Efficiency Guide
*How to get the most out of Claude without burning usage limits*

---

## The Core Problem

Claude has two limits that affect this project:
1. **Rate limit** — number of messages per time window (varies by plan)
2. **Context limit** — each conversation has a max token budget; as a conversation grows longer, every new message costs more, and response quality eventually degrades

The biggest efficiency killer is **long, sprawling conversations** where you're iterating, debugging, and exploring all in the same session. Every back-and-forth adds to the context cost.

---

## The Golden Rules

**1. One session = one sub-task.**
Start a new chat for each sub-task from the project plan. Don't carry a session into the next task just because you have momentum. End clean, start fresh.

**2. Start new chats often — it costs you almost nothing.**
The memory system loads your key project context automatically at the start of every conversation. You don't lose continuity by starting fresh. You gain a cheaper context window.

**3. Front-load every session.**
The first message should be specific and complete. Don't warm up. Don't say "hey I want to work on the mockup" — say exactly what you want done, with all the information Claude needs to do it. The first message is cheap. The tenth is expensive.

**4. Do creative/exploratory work in ChatGPT, bring finished output to Claude.**
Don't brainstorm colors, copy, or layout options with Claude. Use the sandbox + ChatGPT loop, arrive with decisions already made, and let Claude execute.

**5. Never ask Claude to read the full mockup file unless you have to.**
The mockup is 3,380 lines. Reading it whole costs significant tokens. When possible, tell Claude which specific section to look at, or paste only the relevant block yourself.

---

## When to Start a New Chat

Start a fresh conversation when:
- You've completed a sub-task (even a small one)
- A session has gone past ~15–20 exchanges
- You're switching from design work to code work (or vice versa)
- You're hitting rate limits — don't push through, just start fresh next session
- Claude's responses start getting longer, more hedged, or less precise (sign of context bloat)

Do NOT start a new chat when:
- You're mid-debug and Claude is actively holding error context
- You just pasted a large file and haven't gotten the output yet

---

## Session Start Templates

Copy and adapt these at the start of each new chat. The goal: give Claude everything it needs in message 1, with zero warmup.

---

### Apply CSS Changes from ChatGPT (color/design update)

```
I'm working on DraftMap, my NFL draft analysis app. Refer to project memory for context.

I have a CSS update to apply to the mockup file at:
C:\Users\wimer\OneDrive\Faith\Claude\Projects\NFL Draft Database and View Site\draftmap-mockup.html

Here are the specific changes from my design session (paste ChatGPT's summary):
[PASTE THE CHANGE SUMMARY FROM CHATGPT'S END PROMPT RESPONSE]

Please apply these changes to draftmap-mockup.html. Only touch what's listed — don't rewrite anything else.
```

---

### Mockup Review / UI Fix

```
I'm working on DraftMap — refer to project memory for full context.

Mockup file: C:\Users\wimer\OneDrive\Faith\Claude\Projects\NFL Draft Database and View Site\draftmap-mockup.html

I have [X] specific UI issues to fix:
1. [Describe issue clearly — what you see, what you want instead]
2. [etc.]

Please read the file and fix only these issues. Don't refactor anything outside the scope of these fixes.
```

---

### Phase 1 — App Scaffold (first coding session)

```
Starting Phase 1 of DraftMap. Refer to project memory for full spec and architecture decisions.

Goal for this session: Set up the GitHub repo structure and write data_loader.py.

Data file location: C:\Users\wimer\OneDrive\Faith\Claude\Projects\NFL Draft Database and View Site\data\rankings_2026.csv

Before writing any code, confirm your plan in 3–4 sentences: what files you're creating, what data_loader.py will do, and what assumptions you're making. I'll confirm, then you build.
```

---

### Phase 1 — Draft Chart Page (second coding session)

```
Continuing Phase 1 of DraftMap. Refer to project memory for full spec.

App scaffold is already set up. Today's goal: build 1_Draft_Chart.py — the Plotly scatter chart page.

The visual reference is the approved mockup at:
C:\Users\wimer\OneDrive\Faith\Claude\Projects\NFL Draft Database and View Site\draftmap-mockup.html

Before writing code, confirm your plan: what the page renders, how the zoom toggle works in Streamlit, and how position filter affects the chart. I'll confirm, then you build.
```

---

### Debugging Session

```
I'm debugging an issue in DraftMap. Refer to project memory for context.

File with the issue: [specific file path]
What I'm seeing: [exact error message or behavior]
What I expect: [what should happen]

Here's the relevant code section:
[PASTE ONLY THE RELEVANT 20–50 LINES, not the whole file]

Please diagnose and fix.
```

---

### Picking Up a Paused Phase

```
I'm resuming work on DraftMap Phase [X]. Refer to project memory for full context and spec.

Last session we completed: [brief description of what was built]
Remaining sub-tasks for this phase: [list from the project plan]

Today's goal: [one specific sub-task]

What do you need from me to start?
```

---

## Where We Are Right Now

**Current state (as of this conversation):**
- Pre-Phase 1 mockup is nearly done — one item remaining: colors
- Design sandbox (`draftmap-sandbox.html`) is ready for ChatGPT iteration
- ChatGPT prompts doc has the start/end prompts for the sandbox session
- Project Plan and this guide are in the workspace folder

**Immediate next steps (in order):**
1. Open `draftmap-sandbox.html` in Chrome — confirm it looks right
2. Take it to ChatGPT using the START prompt in `DraftMap - ChatGPT Prompts.md`
3. Iterate on colors/design in ChatGPT until you're happy
4. Use the END prompt to get the CSS handoff
5. Start a **new Claude chat** with the "Apply CSS Changes" template above
6. Claude applies the changes to `draftmap-mockup.html` in one shot
7. Review the real mockup — if approved, Phase 1 begins

---

## What Burns Usage Fast (Avoid These)

| Habit | Why It's Costly | Better Approach |
|---|---|---|
| "Can you also..." at the end of a long session | Adds to already-large context | Note it, start fresh next session |
| Asking Claude to read the full mockup every session | 3,380 lines = lots of tokens | Paste only the relevant CSS block |
| Iterating colors/copy with Claude | Exploration burns context | Do it in ChatGPT, bring decisions |
| Vague first messages | Requires clarifying Q&A | Use the session templates above |
| Staying in one chat all day | Context grows, quality drops | One task per chat |

---

## The Handoff Rule

At the end of every session, before you close the chat, ask:

> "Summarize what was built or changed this session in 3 bullets, and state the exact next sub-task from the project plan."

Save that summary as a note in Obsidian. That note becomes the input to the next session's start template. You never lose context between sessions.

---

## Obsidian Tip

Keep a running note called `DraftMap - Session Log.md` with entries like:

```
## 2026-04-10
- Applied warm color palette from ChatGPT sandbox session
- Fixed tier label alignment
- Next: mockup approval → start Phase 1

## [next date]
- Built GitHub repo structure, data_loader.py
- Next: 1_Draft_Chart.py
```

This gives you a fast briefing you can paste into the "Picking Up a Paused Phase" template without having to remember where you were.
