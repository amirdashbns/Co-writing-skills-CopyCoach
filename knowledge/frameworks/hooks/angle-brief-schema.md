# Angle Brief Schema

Standard output for the **hook-angle skill** (Layer 1). Draft skills (email, carousel, LinkedIn, etc.) consume this object **without changing the angle**.

One locked angle. Full platform brief. Adapt cuts — not meaning.

---

## YAML template

```yaml
angle_brief:
  version: "1.0"
  created_for_topic: ""           # short label, e.g. "style-guide-lead-magnet"

  # Spine
  core_lesson_id: null            # from core-lessons.json, or null if N/A
  core_lesson_summary: ""
  belief_shift: ""                # what the reader should think differently after

  # Idea factory metadata
  idea_factory_category: ""       # controversial_opinion | myth_buster | pop_culture |
                                  # news_story | case_study | objection_flip | before_after_demo |
                                  # audience_language | tool_shock | personal_failure |
                                  # client_question | competitor_teardown | micro_moment |
                                  # data_point | pop_culture_mashup
  story_stem: ""                  # 1-3 sentences — the raw material

  # Hook engine
  proof_anchor: ""                # credibility — specific, vivid
  tangible_promise: ""            # concrete payoff — realistic
  curiosity_question: ""          # the "what/how/why" it opens
  hook_types: []                  # pattern_interrupt | problem_validation | curiosity_gap |
                                  # story_transformation | social_proof | contrarian

  # Hooks — long form is source of truth
  hooks:
    long_form: ""                 # full conversational hook; no word limit

    email_subject:
      - ""
      - ""
      - ""

    ig_slide_1: ""                # promise-forward title slide
    ig_slide_2: ""                # proof + bridge (second-chance hook)

    linkedin_opener: ""
    blog_title: ""
    substack_title: ""

    x_thread_hook: ""
    threads_bluesky_hook: ""

    reel_hook_spoken: ""          # first 3 seconds, verbal
    story_hook_text: ""           # IG story overlay — ultra short

  # Downstream hints (optional)
  offer_connection: ""            # what the CTA points to
  repurposing_notes: ""           # e.g. "Email = friend story; Carousel = 7 injections"
  suggested_format: ""            # email | carousel | linkedin | thread | multi

  # Selection metadata (when multiple angles generated)
  angle_label: ""                 # A | B | C
  strength_notes: ""              # why this angle might win
```

---

## Field rules

| Field | Rule |
|-------|------|
| `long_form` | Write first. Everything else derives from it. |
| `ig_slide_1` | Benefit + curiosity. Not proof-heavy. |
| `ig_slide_2` | Proof + "why keep swiping." Assume reader landed here on re-serve. |
| `email_subject` | 3–5 variants. Specific > clever. |
| `proof_anchor` | Must answer "who are you to say this?" |
| `tangible_promise` | Reader can picture the outcome. |
| `belief_shift` | One sentence. The paradigm move. |

---

## Handoff contract

**Draft skills MUST:**
- Use `story_stem`, `proof_anchor`, `belief_shift`, and `long_form` as locked spine
- Not change `ig_slide_1` / `ig_slide_2` meaning when writing carousels
- Not invent a new lesson — use `core_lesson_summary`

**Edit skills MAY:**
- Tighten wording per platform
- Cut email-isms from social surfaces
- Adjust punchiness (1–10 feedback)

**Edit skills MUST NOT:**
- Replace proof with vague authority
- Swap contrarian angle for safe/generic
- Remove tangible promise for hype

---

## Example (abbreviated)

```yaml
angle_brief:
  created_for_topic: "style-guide-prompt"
  core_lesson_id: 5
  core_lesson_summary: "Secondary rewards make writing fun to read"
  belief_shift: "Emails fail because they're boring, not because the info is wrong"
  idea_factory_category: "before_after_demo"
  story_stem: "Copywriter friend said AI writes slop. I ran his own email through Claude with my Style Guide prompt. He froze mid-Mai-Tai."
  proof_anchor: "His email. My prompt. Ten seconds. His reaction."
  tangible_promise: "One copy-paste prompt makes any email more fun to read"
  curiosity_question: "What did the prompt add that better adjectives never could?"
  hook_types: ["story_transformation", "contrarian", "pattern_interrupt"]
  hooks:
    long_form: "My copywriter friend bet me AI only writes slop..."
    email_subject:
      - "My copywriter friend said AI writes slop. Then I handed him his phone back."
      - "The clankers can't write for shit — my friend, five minutes before his existential crisis"
    ig_slide_1: "7 Injections That Make Boring Emails World-Class"
    ig_slide_2: "I studied what top copywriters actually put on the page. These 7 patterns showed up in almost every one."
    linkedin_opener: "A copywriter friend told me LLMs only write slop. I bet him his own email would prove him wrong."
    blog_title: "Why Your AI Emails Sound Boring (And the One Prompt That Fixes It)"
    x_thread_hook: "My copywriter friend said AI writes slop. So I ran HIS email through Claude. He stopped drinking his Mai Tai."
    reel_hook_spoken: "My friend said AI can't write. So I used his own email against him."
    story_hook_text: "AI writes slop? I bet him his own email."
  offer_connection: "Free Style Guide prompt → full voice system tease"
  repurposing_notes: "Email = full friend story; Carousel = 7 injections; Reel = phone handoff moment"
  suggested_format: "multi"
```
