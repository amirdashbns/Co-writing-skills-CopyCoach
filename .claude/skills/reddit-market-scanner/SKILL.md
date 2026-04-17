---
name: reddit-market-scanner
description: Scan Reddit to extract market intelligence — pain points, sentiment, beliefs, language patterns, AI/tech adoption levels, and content opportunities. Use when the user wants to understand their market, research audience problems, find content ideas, or gather real-world language for copywriting.
---

# Reddit Market Scanner

Scan Reddit communities to extract actionable market intelligence. This skill gathers real-world data about your audience: what they struggle with, how they talk about it, what they believe, and where opportunities exist.

## When to Use This Skill

- Understanding a new market or niche
- Refreshing market intelligence (run quarterly or when pivoting)
- Finding content ideas backed by real audience demand
- Gathering language patterns for copywriting
- Validating assumptions about audience pain points
- Understanding technology adoption levels in a market

## Before Scanning

1. **Read context profiles** to auto-detect targeting:
   - `/context/icp.json` — industries, job titles, platforms, jargon
   - `/context/business-profile.json` — niche focus, content pillars, category

2. **Derive subreddits and search terms** from context profiles. Match:
   - ICP industries → relevant industry subreddits
   - ICP job titles → professional community subreddits
   - Business niche → topic-specific subreddits
   - Content pillars → search terms

3. If context profiles are still template/placeholder, ask the user:
   - "What's your market/niche?"
   - "Who is your audience?"
   - "What topics matter most to you?"

## Scanning Process

### Phase 1: Targeting

Using the context profiles, identify:

- **3-5 primary subreddits** directly relevant to the ICP
- **2-3 adjacent subreddits** where the ICP also participates
- **5-10 search terms** combining niche keywords with intent phrases

**Search term construction:** Combine niche terms with these intent modifiers:
- Pain: `"struggling with"`, `"frustrated"`, `"doesn't work"`, `"hate"`, `"worst part"`
- Experience: `"my experience"`, `"I tried"`, `"what happened"`, `"honest review"`
- Workflow: `"my process"`, `"here's how"`, `"what I do"`, `"daily workflow"`
- Sentiment: `"overhyped"`, `"game changer"`, `"actually works"`, `"waste of time"`
- Questions: `"how do you"`, `"what's the best"`, `"anyone else"`, `"help with"`

**Example for a copywriting/marketing niche:**
```
site:reddit.com r/copywriting "struggling with" AI writing 2025 2026
site:reddit.com r/Entrepreneur AI content "my experience" 2025 2026
site:reddit.com r/digitalmarketing "what's working" content marketing 2026
```

### Phase 2: Discovery

Use **WebSearch** to find high-value threads. Run 8-12 searches targeting different categories:

1. **Pain points** — searches with frustration/struggle language
2. **What's working** — searches with success/results language
3. **What's failing** — searches with failure/disappointment language
4. **Personal stories** — searches with experience/journey language
5. **Beliefs & opinions** — searches with opinion/debate language
6. **Tool/tech adoption** — searches with tool names and workflow language
7. **Language patterns** — searches focused on how people describe problems
8. **Content gaps** — searches with question/help-seeking language

For each search, capture:
- Thread titles (these reveal market language)
- Key quotes from posts and top comments
- Upvote patterns (high upvotes = resonance)
- Common themes across multiple threads

### Phase 3: Deep Read

For the most valuable threads found in Phase 2, use **WebFetch** to pull full thread content. Prioritize:
- Threads with high engagement (many comments, high upvotes)
- Threads with detailed personal stories
- Threads with active debate (reveals beliefs and objections)
- "Ask" threads where the ICP is requesting help

**Note:** Reddit pages may time out on WebFetch. If this happens, rely on the WebSearch summaries and try the `.json` endpoint variant (append `.json` to the Reddit URL).

### Phase 4: Analysis

Organize all findings into these categories:

#### 4a. Pain Points
- What specific problems do they describe?
- How severe are the problems? (frequency of mention, emotional intensity)
- What have they tried that failed?
- What language do they use to describe these problems?

#### 4b. Market Sentiment
Map the emotional landscape:
- **Frustrated-but-stuck**: Know something should work but can't make it
- **Cautiously optimistic**: Found specific wins, always with caveats
- **Skeptical-and-vocal**: Actively push back against hype
- **Actively hostile**: Reject the premise entirely

Estimate the rough percentage of each sentiment category.

#### 4c. Current Beliefs
What assumptions does the market operate with? Capture:
- Beliefs stated as fact (often wrong or incomplete)
- Beliefs that create opportunities (if you can challenge them)
- Beliefs that create resistance (must be acknowledged, not fought)

#### 4d. Market Sophistication & Tech Adoption
Segment into tiers:
- **Tier 1 — Beginners**: What are they doing? What do they think is possible?
- **Tier 2 — Intermediate**: What techniques have they adopted? Where are they stuck?
- **Tier 3 — Advanced**: What systems have they built? What results do they get?
- **Tier 4 — Expert**: What are the most sophisticated approaches you find?

Estimate the rough distribution across tiers.

#### 4e. Common Language
Extract:
- Exact words and phrases used to describe problems
- Exact words and phrases used to describe desired outcomes
- Jargon and technical terms (and how correctly they're used)
- Emotional language (frustration words, aspiration words)
- Slang, shorthand, community-specific terminology

#### 4f. Content Opportunities
Identify:
- Questions asked repeatedly that never get good answers
- Debates that generate massive engagement
- Gaps between what people want and what's available
- Topics where misinformation or outdated advice dominates
- Angles that would resonate given the sentiment landscape

### Phase 5: Real Stories

Collect 5-10 detailed stories from real people sharing their experiences. For each story, capture:
- What they tried
- What happened (specific results, numbers if available)
- How they felt about it
- What they learned
- The source thread

These stories are gold for content creation — they become the foundation for relatable hooks, case studies, and "I see this all the time" posts.

## Output Format

Generate two outputs:

### Output 1: Detailed Markdown Report

Save to `/knowledge/research/reddit-scan-YYYY-MM-DD-[topic-slug].md`

Structure:
```markdown
# Reddit Market Intelligence: [Topic]

**Scan Date:** [Date]
**Subreddits Scanned:** [List]
**Focus:** [Description]

---

## EXECUTIVE SUMMARY
[3-5 paragraph synthesis of the most important findings]

## 1. PAIN POINTS
[Organized by severity, with direct quotes]

## 2. MARKET SENTIMENT
[Emotional landscape with estimated distribution]

## 3. CURRENT BELIEFS
[What the market assumes to be true]

## 4. MARKET SOPHISTICATION & TECH ADOPTION
[Tier breakdown with descriptions]

## 5. HOW THEY'RE ACTUALLY DOING [TOPIC] RIGHT NOW
[Specific behaviors, workflows, tools]

## 6. REAL STORIES FROM THE TRENCHES
[5-10 detailed stories with quotes]

## 7. COMMON LANGUAGE
[Words, phrases, questions, jargon — organized by category]

## 8. CONTENT OPPORTUNITIES
[Underserved questions, high-engagement debates, gaps]

## 9. KEY TAKEAWAYS FOR YOUR BUSINESS
[Actionable implications tied to business-profile.json]

---
*Sources: [X] Reddit threads across [Y] subreddits, scanned [Date]*
```

### Output 2: Structured JSON Summary

Save to `/context/market-intelligence.json`

```json
{
  "market_intelligence": {
    "version": "1.0",
    "last_updated": "YYYY-MM-DD",
    "scan_focus": "",
    "subreddits_scanned": [],

    "pain_points": {
      "primary": [
        {
          "pain_point": "",
          "severity": "HIGH/MEDIUM/LOW",
          "frequency": "",
          "sample_quotes": []
        }
      ],
      "secondary": []
    },

    "market_sentiment": {
      "overall": "",
      "distribution": {
        "frustrated_but_stuck": "",
        "cautiously_optimistic": "",
        "skeptical_and_vocal": "",
        "actively_hostile": ""
      },
      "hype_vs_reality_gap": ""
    },

    "current_beliefs": {
      "dominant_beliefs": [],
      "beliefs_creating_opportunities": [],
      "beliefs_creating_resistance": []
    },

    "market_sophistication": {
      "tier_1_beginners": {
        "percentage": "",
        "description": "",
        "behaviors": []
      },
      "tier_2_intermediate": {
        "percentage": "",
        "description": "",
        "behaviors": []
      },
      "tier_3_advanced": {
        "percentage": "",
        "description": "",
        "behaviors": []
      },
      "tier_4_expert": {
        "percentage": "",
        "description": "",
        "behaviors": []
      }
    },

    "common_language": {
      "problem_language": [],
      "aspiration_language": [],
      "technical_terms": [],
      "emotional_language": [],
      "community_slang": []
    },

    "content_opportunities": {
      "underserved_questions": [],
      "high_engagement_debates": [],
      "content_gaps": [],
      "recommended_angles": []
    },

    "key_stories": [
      {
        "title": "",
        "summary": "",
        "source_subreddit": "",
        "key_quote": ""
      }
    ]
  }
}
```

## After Scanning

1. Present the executive summary to the user
2. Highlight the 3 most actionable findings
3. Suggest specific content ideas based on the gaps found
4. Ask: "Want me to dive deeper into any of these areas?"

## Best Practices

- **Use recent timeframes**: Add "2025 2026" to searches to filter for current data
- **Prioritize comments over posts**: The most honest insights are in comment threads, not top-level posts (which can be self-promotional)
- **Capture exact language**: Don't paraphrase — the actual words people use are the most valuable output
- **Look for emotional intensity**: Strong emotions (frustration, excitement, anger) signal real pain points and desires
- **Cross-reference across subreddits**: A pain point mentioned in r/copywriting AND r/Entrepreneur AND r/Solopreneur is more significant than one mentioned in a single niche community
- **Note what's NOT discussed**: Gaps in conversation reveal opportunities as much as active discussions do
- **Don't over-filter**: Include minority opinions and contrarian views — they reveal the full belief landscape
- **Run multiple searches per category**: A single search won't capture the full picture. Aim for 8-12 searches minimum across different angles
