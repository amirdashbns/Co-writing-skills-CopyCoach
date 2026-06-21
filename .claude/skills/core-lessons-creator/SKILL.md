---
name: core-lessons-creator
description: Extract a set of "core lessons" — the counter-industry-norm ideas that position you as unique and bust the myths keeping prospects from buying. Use when the user wants to define their core lessons, content angles, unique POV, or signature paradigm shifts.
---

# Core Lessons Creator

Build a library of **core lessons**: the recurring big ideas you teach over and over to (1) establish your unique position in the market and (2) bust the myths holding your prospects back from buying. These become the *fuel* for content — each piece of paradigm-shift content delivers ONE core lesson as its "aha" moment.

## When to Use This Skill

- Setting up a new writing system (alongside voice-dna and ICP)
- Onboarding a new client or a new market
- Refreshing your POV when you reposition
- When content feels like it's missing a unique angle or point of view

## What a Core Lesson Is (and Isn't)

A core lesson is a **stance**, not a topic and not a tactic. Each one does one (usually both) of two jobs:

1. **Establish your unique position** — how you go against the grain (e.g. "Most AI copywriting advice misses the point").
2. **Bust a myth** — a wrong belief keeping the prospect stuck or from buying (e.g. "AI can be MORE creative than you, not less").

It is NOT a "how-to," a content pillar (topic), or a voice trait. It's a *belief you want to inject into your audience's head*.

## Before the Interview

Read for raw material and alignment:
- `/context/icp.json` — especially `beliefs_to_shift` and `objections` (each maps to a potential core lesson)
- `/context/business-profile.json` — offers and positioning (lessons should ladder to an offer)
- `/context/voice-dna.json` — `values_and_beliefs` (often contains latent core lessons)
- `/context/market-intelligence.json` — real audience beliefs and pain points (if present)
- Any guide, book, or long-form content the user has written (richest source)

## Interview Process

Lead with the two core questions (from the user's own framework). Ask one at a time, push for specificity.

### The Two Anchor Questions
1. **"What are your unique approaches to the problems your market faces? How do you go against the grain?"** (→ positioning lessons)
2. **"What myths or wrong beliefs do you need to eliminate from your prospect's mind that are holding them back from buying?"** (→ myth-bust lessons)

### Idea-Prompt Follow-ups (to surface 10+ lessons)
- What does everyone in your industry teach that you think is flat-out wrong?
- What "best practice" do you ignore on purpose? Why?
- What do prospects believe about themselves that isn't true? ("I'm not creative," "I'm not ready," etc.)
- What do they believe about your solution category that's outdated or false?
- When someone says "I could just [cheaper/DIY alternative]," why are they wrong?
- What's the #1 objection you hear, and what's the belief underneath it?
- What do you wish your market understood before they ever talk to you?
- What's a stance you hold that would make some people in your industry mad?

### For Each Lesson, Capture
- **lesson** — the stance, in one punchy line
- **function** — `positioning`, `myth-bust`, or `both`
- **industry_norm_it_counters** — the conventional wisdom it goes against
- **the_myth_or_why_norm_is_wrong** — why the norm is incomplete or false
- **the_aha** — the mindset shift / "aha" moment for the audience
- **deeper_truth** — the underlying principle, distilled
- **audience_belief_it_shifts** — map to an entry in `icp.json` `beliefs_to_shift` / `objections` where possible
- **ladders_to_offer** — which offer/transformation this lesson sets up
- **one_liners** — 2-4 punchy, voice-matched expressions (these become hooks)

Aim for **8-12 core lessons.** Fewer than 8 and the content gets repetitive; more than ~15 and they start to overlap.

## Output

1. Present the lessons as a summary for approval, grouped by function (positioning / myth-bust / both).
2. Generate the complete JSON following the structure in `/context/core-lessons.json`:

```json
{
  "core_lessons": {
    "version": "1.0",
    "last_updated": "YYYY-MM-DD",
    "what_this_is": "",
    "how_each_lesson_works": "",
    "how_to_use": "",
    "lessons": [
      {
        "id": 1,
        "lesson": "",
        "function": "positioning | myth-bust | both",
        "industry_norm_it_counters": "",
        "the_myth_or_why_norm_is_wrong": "",
        "the_aha": "",
        "deeper_truth": "",
        "audience_belief_it_shifts": "",
        "ladders_to_offer": "",
        "one_liners": []
      }
    ]
  }
}
```

3. Save to `/context/core-lessons.json`.
4. Write the one-liners in the user's voice (read `voice-dna.json` first) — these are content hooks, so they must sound like the user.

## Best Practices

- **Push for stances, not platitudes.** "Quality matters" is not a core lesson. "'Good enough' is the most expensive content you can publish" is.
- **Each lesson should make someone slightly uncomfortable.** If nobody could disagree, it's not a stance.
- **Tie every lesson to an offer.** A core lesson that doesn't ladder toward a sale is just a hot take.
- **Map to the ICP.** The strongest myth-bust lessons are direct answers to `icp.json` `beliefs_to_shift` and `objections`.
- **Mine existing long-form first.** If the user has written a guide, book, sales page, or signature talk, the lessons are usually already in there — extract before you interview.

## Validation Test

For each lesson, ask: "Could you write 10 different emails or posts that all teach this one lesson from different angles?" If yes, it's a real core lesson. If you can only think of one way to say it, it's a topic, not a lesson.
