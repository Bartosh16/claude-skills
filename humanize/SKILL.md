---
name: humanize
description: Humanizes English AI-generated text - audits it against 20 categories of AI writing signals (slop vocabulary, rule of three, weasel attribution, importance puffery, copula avoidance, metronome rhythm, em dash overuse, chatbot artifacts) and rewrites it so it reads like a person wrote it. ALWAYS use this skill when the user says "humanize this", "make this sound human", "this sounds like ChatGPT", "remove the AI slop", "de-AI this", "fix the AI writing", "this reads like a robot", "too corporate", "sounds generated", "clean up the GPT-isms", "will this trip an AI detector" - or pastes English text and asks whether it sounds AI-written, how obvious it is, or how to fix it. Also use proactively when the user pastes English text and asks for a "polish" or "improvement" pass. FOR ENGLISH TEXT ONLY - if the text is Polish, use the /humanizacja skill instead.
---

# Humanizing AI-generated English

The job: take generated text and rewrite it so it reads like a person with an opinion, experience, and a voice wrote it. Not like a language model compiled it.

**This skill is for ENGLISH text.** For Polish, use `/humanizacja`. The structural layer transfers between the two. The vocabulary, the punctuation rules, and the inflection handling do not: in Polish the em dash is an actual punctuation error, the period goes outside the closing quote, and curly quotes are the correct form rather than a tell.

When the rewrite is done, verify it with `/humanizacja-check` (works for both languages). It measures whether the changes actually landed instead of trusting your own read on whether the text "sounds better."

Two steps:
1. **Audit** - find every AI signal in the text (with quotes and categories).
2. **Rewrite** - rebuild the text, keeping meaning and roughly the length, with the signals gone.

Add nothing of your own. Do not invent facts, numbers, or names. Your job is to **cut and rebuild**, not to expand.

## Workflow

### Step 1: audit

Scan the whole text against the 20 categories below ("Catalog of AI signals"). For each hit, note:

- the category (e.g. "Weasel attribution", "Rule of three", "Copula avoidance"),
- the exact quote,
- one line on why it reads as AI,
- the fix, stated briefly.

Report format:

```
## AI signal audit

### 1. [Category]
- "quote from text" - [why it reads as AI] - [fix]

### 2. [Category]
- "quote from text" - [why it reads as AI] - [fix]
```

If a category is clean, skip it. Do not write "Category N: nothing to fix." Just leave it out.

**Match word stems, not exact forms.** English inflection is light but real: "delve" also appears as "delving", "delves", "delved"; "leverage" as "leveraging", "leveraged". Scan for the stem.

### Step 2: rewrite

After the report, write this header:

```
## Humanized text
```

Then give the full rebuilt text. Keep:

- the same topic, facts, and meaning,
- roughly the same length (within 20%),
- the heading structure if there was one (but fix Title Case to sentence case),
- the lists if there were any (but fix the formatting patterns in category 6).

Replace:

- AI cadence with human rhythm,
- passive and subjectless constructions with an actor doing something,
- filler vocabulary with specifics,
- hedged claims with direct ones.

After the rewritten text, add a short note (1 to 3 sentences) on what the main stylistic problem was and what you changed most.

## Catalog of AI signals

These 20 categories are a checklist. Walk through each one during the audit.

**Structure beats vocabulary.** The structural categories (rhythm, missing agent, rule of three, weasel attribution, importance puffery, copula avoidance, synonym cycling) are durable. Models reproduce them regardless of version. Word lists expire roughly every year as model vocabulary shifts: GPT-4 leaned on "delve", "boasts", "crucial"; GPT-4o on "align with", "enhance", "highlighting"; GPT-5 on "showcasing", "emphasizing". Deleting a flagged word does not make text human. It makes it thinner. Fix the pattern, not the wordlist. Vocabulary last reviewed: 2026-07.

### 1. Metronome rhythm, and its opposite

**The metronome.** AI writes sentences of similar length, evenly, like a click track. People write music: a short sentence. A medium one. And then a longer, three-clause sentence that carries the reader through the rest of the paragraph.

**Signal:** three or more consecutive sentences of similar length. Paragraphs of uniform size.

**Fix:** drop in a two-word sentence. Or fuse two sentences into one longer one. Vary paragraph length.

> **BAD:** "Deep learning is an advanced form of machine learning. It uses networks of algorithms inspired by the brain. A deep neural network has nested neural nodes. Each question leads to a set of related questions."
>
> **GOOD:** "Deep learning imitates the structure of the human brain. The network nests its nodes, and one question spawns the next. And the next. Until the system can pick a cat out of a photo or translate a sentence from Swahili."

**The other pole: staccato drama.** The metronome is one AI pattern. The machine gun is the other. Strings of punch sentences ("Seriously. That's it. That's the whole thing."), connected thoughts chopped into separate fragments, and manufactured drama ("No preference. No aesthetic. No nostalgia.") are the same template running the other direction. If two thoughts belong together, put them in one sentence. A punch line works when there is one per section, not three per paragraph.

### 2. Missing agent (passive voice, subjectless fragments)

AI hides behind "it was decided", "changes were implemented", "it is believed", "one should". Every sentence needs someone doing something: a person, a company, a tool, a document.

**Signal:** passive constructions, "it is [verb]ed that", headless fragments that drop the subject entirely.

**Fix:** name the actor. If the actor is obvious, use it anyway.

> **BAD:** "A decision was made to implement the system." → **GOOD:** "The board decided to implement the system."
> **BAD:** "It is recommended that this approach be used." → **GOOD:** "Use this approach." / "The vendor recommends this approach."
> **BAD:** "No configuration file needed." → **GOOD:** "You don't need a configuration file."

### 3. Hedging and soft commitment

AI qualifies everything into mush: "it's worth noting", "may help", "can potentially", "one might consider", "it could be argued that". Nobody is offended, nothing is claimed, no one is told to do anything.

**Signal:** stacked qualifiers, "worth" constructions, modal pileups ("could potentially possibly").

**Fix:** state the benefit, the consequence, or the instruction.

| Hedged (AI) | Direct (human) |
|---|---|
| It's worth considering | Consider / Do this, because... |
| May help improve | Improves / Cuts / Reduces |
| It's important to remember | Remember |
| It is recommended | Do this / [Who] recommends |
| One should | You need to / [Who] should |
| Can be beneficial | [The specific benefit] |
| It could be argued that | [State the claim, or cut it] |

### 4. AI vocabulary and stock phrases

**Words that mark generated text:**

| AI word | What to do |
|---|---|
| delve (into) | look at, dig into, examine |
| leverage (verb) | use |
| robust | say what it actually withstands |
| crucial, pivotal, vital, key | state the fact, let the reader judge weight |
| tapestry, landscape, realm | name the actual thing (industry, market, field) |
| showcase | show, or say what is visible |
| testament (to) | evidence, proof, or cut it |
| underscore, highlight, emphasize | cut the clause (see category 16) |
| foster, cultivate | build, create, encourage |
| navigate (abstract) | handle, deal with, work through |
| streamline | say what got shorter, and by how much |
| seamless, effortless | describe what stopped breaking |
| cutting-edge, groundbreaking, game-changing | describe what is new and why it beats the old thing |
| transformative, revolutionary | show the before and after |
| myriad, plethora | a number, or "many" |
| intricate, nuanced | explain the actual complication |
| vibrant, bustling, nestled | cut it, this is travel-brochure filler |
| significantly | give the scale (by 30%, twice as fast) |
| holistic, comprehensive | complete, full, or cut |
| deliver value | give a benefit, produce results |
| unlock, empower, elevate | say what the reader can now do |

**Phrases to cut outright:**

- "In today's fast-paced world..."
- "In the ever-evolving landscape of..."
- "In this article, we'll explore..."
- "It's worth noting that..."
- "At the end of the day..."
- "When it comes to..."
- "In order to" (just "to")
- "It's important to note that..."
- "Whether you're a beginner or an expert..."
- "The bottom line is..."

Cut them and start at the point. The reader does not need a warm-up lap.

**Constructions to break:**

| AI construction | What to do |
|---|---|
| "Not just X, but Y" | State Y directly |
| "It's not X. It's Y." | State Y in one sentence with a reason |
| "More than just a..." | Say what it is |
| "X isn't about Y. It's about Z." | "X is about Z, because..." |
| "Think of it as X" (when X adds nothing) | Cut the analogy, describe the thing |

### 5. Nominalizations and gerund openers

**Nominalizations:** AI turns verbs into nouns and then needs a weak verb to carry them. "The implementation of the system was carried out" instead of "we implemented the system." "Provides an improvement in" instead of "improves."

> **BAD:** "The utilization of this framework results in a reduction of processing time."
> **GOOD:** "This framework cuts processing time."

**Gerund openers:** "Understanding X is crucial...", "Implementing Y requires...", "Ensuring Z means..." Sentence after sentence starting with an -ing noun is a model tic. Rebuild with a subject and a verb.

> **BAD:** "Understanding organizational culture is crucial in the merger process."
> **GOOD:** "Miss the culture of the company you're buying and you'll wreck the merger."

**Participial openers:** "Having established X, we can now...", "Building on this foundation..." Cut them and start with the actual sentence.

### 6. Punctuation and formatting (English standard)

#### Em dashes

The em dash (—, U+2014) is not a grammatical error in English. It is, however, the single strongest formatting tell of generated text, because models reach for it as a rhythm crutch in place of commas, colons, and full stops.

**Rule:** zero em dashes in short text. One or two in a long piece, and only where the alternative is genuinely worse. Replace the rest with a comma, a colon, a full stop, or parentheses.

> **BAD:** "The decision came from the institutions—not from the people—and it showed."
> **GOOD:** "The decision came from the institutions, not from the people, and it showed."

En dashes (–, U+2013) stay in number and date ranges (2019–2024). They do not belong between clauses.

#### Quotation marks

Use **straight quotes** (`"` U+0022 and `'` U+0027) in plain text, markdown, and anything headed for the web. Curly quotes (`"` `"` `'` `'`) are not wrong in typeset prose, but in a draft they usually mean the text passed through a model, and combined with other signals they strengthen the case. Convert them.

#### Punctuation order

American English puts the period and comma **inside** the closing quote. British English puts them outside unless they belong to the quoted material.

| | US | UK |
|---|---|---|
| Period | `"like this."` | `"like this".` |
| Comma | `"like this,"` | `"like this",` |
| Colon, semicolon | `"like this":` | `"like this":` |

Pick one convention and hold it across the whole text. Mixed conventions inside one document are their own signal, usually of a hybrid human/AI draft.

#### Everything else

- **Headings:** sentence case. Title Case On Every Major Word is a model default, not a style choice.
- **Bold:** mechanical mid-sentence bolding ("combines **OKRs** with **KPIs**") reads as generated. Bold only where a skimming reader should stop. A few per document, not a few per paragraph.
- **Inline-header lists:** "**Header:** explanation..." repeated down every bullet is a template. Short points get a plain list. Long ones get prose.
- **Heading echo:** a heading followed by a one-line paragraph restating the heading, then the real content. Cut the echo.
- **Horizontal rules:** never `---` between sections. The heading is the separator.
- **Generic upbeat endings:** "In conclusion", "Ultimately", "The future looks bright", "Exciting times ahead". Cut them. The text ends on its last concrete point.
- **Hyphenation:** hyphenate compound modifiers before a noun ("a high-quality report"), not after the verb ("the report is high quality"). Models over-hyphenate in the predicative position.
- **Oxford comma:** either always or never. Inconsistency is a hybrid-draft tell.

#### Automated check after humanizing

Run this after the rewrite:

```python
import re

em_dash    = text.count(chr(0x2014))                       # — should be 0-2
curly      = sum(text.count(c) for c in "“”‘’")

slop = ["delve", "leverage", "robust", "tapestry", "seamless", "showcase",
        "testament", "underscore", "pivotal", "vibrant", "myriad",
        "cutting-edge", "game-chang", "navigat", "streamlin", "holistic"]
hits = {w: len(re.findall(w, text, re.I)) for w in slop}
hits = {w: n for w, n in hits.items() if n}

# metronome check: stdev of sentence word counts
sents = [s for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
lens  = [len(s.split()) for s in sents]
mean  = sum(lens) / len(lens)
stdev = (sum((n - mean) ** 2 for n in lens) / len(lens)) ** 0.5

assert em_dash <= 2,  f"Em dashes: {em_dash} (cut to 0-2)"
assert curly == 0,    f"Curly quotes: {curly} (convert to straight)"
assert not hits,      f"Slop vocabulary still present: {hits}"
assert stdev >= 5,    f"Sentence length stdev {stdev:.1f} - metronome rhythm, vary it"
```

If an assertion fails, fix it and rerun.

### 7. Emoji

If the text is studded with emoji (in every bullet, in headings), cut nearly all of them. Keep one to three in the whole piece, and only if the genre calls for it (social posts). In articles, reports, and email: none.

### 8. Vagueness without specifics

- If you don't have the specific, **cut the sentence**. A shorter text beats one padded with generalities.
- If the specific is available, use it: a name, a company, a date, a number, a place.
- Cut tautology. If two paragraphs say the same thing in different words, keep one.
- **False ranges:** "from X to Y" where X and Y sit on no real scale ("from strategy to emotion", "from startups to enterprises and everything in between"). This is fake completeness. Replace with a concrete list, or cut.

> **BAD:** "Many people believe AI is changing the market."
> **GOOD:** "McKinsey's 2024 report estimates AI will automate 30% of marketing tasks by 2030." (if you have the source) / [cut the sentence, if you don't].

### 9. Credential openers

AI loves "As a seasoned marketing professional with over a decade of experience...". Cut it. If the author is an expert, the text should show it.

> **BAD:** "As an SEO expert with 10 years of experience, I can tell you that..."
> **GOOD:** "I've watched this happen at four companies in the last three years."

### 10. Internal consistency

If the text is a hybrid (part human, part generated), unify:

- one dash convention,
- one quote style,
- one punctuation-order convention (US or UK),
- one heading case,
- one list-punctuation rule,
- one spelling standard (US or UK: "organize" or "organise", not both).

### 11. Corporate and LinkedIn jargon

Different from category 4. Those are model tics. These are business-speak the model absorbed from its training data and reproduces because it reads "professional."

**Cut or replace:**

| Jargon | Plain English |
|---|---|
| leverage (as a verb) | use |
| synergize, synergy | work together |
| circle back, touch base | follow up, talk again |
| double down on | commit to, do more of |
| move the needle | change the result |
| low-hanging fruit | the easy wins (or name them) |
| at the end of the day | ultimately, or cut |
| take it to the next level | say what improves |
| best-in-class, world-class | say what it beats and by how much |
| actionable insights | findings you can use (or name them) |
| deep dive | look closely, examine |
| bandwidth (as time) | time, capacity |
| align on | agree on |
| unpack (an idea) | explain, break down |
| operationalize | put into practice |
| ideate | come up with ideas |
| utilize | use |

**Terms that stay** (real technical vocabulary, not decoration): API, SaaS, LLM, RAG, MCP, CTR, ROI, B2B, churn rate, conversion rate, embedding, token, prompt, anchor text, canonical. Introduce an unfamiliar one on first use, then use it freely.

**The test:** would you say this out loud to a colleague standing in front of you? If not, rewrite it.

### 12. Negation-based promises

"No fluff", "no gimmicks", "no strings attached", "no pressure". Models overuse the negative frame, which says what is absent instead of what is there.

**Limit:** once per sentence at most, once per 200 words at most.

**Fix:** replace with the positive specific.

| Negative (AI) | Concrete (human) |
|---|---|
| No hidden fees | Every cost is on the first page |
| No pressure | You decide on your own schedule |
| No commitment | Audit first, then decide |
| No effort required | It runs on its own |
| No risk | 30-day refund, no questions |

### 13. Anaphoric triples

The rhythm of three with the same word starting each member: "No X. No Y. No Z." or "Zero X, zero Y, zero Z." It sounds persuasive and reads instantly as a template.

**Signal:** three or more members sharing an opening word, split by commas or full stops. Especially with "no", "zero", "just", or "every".

**Fix:**

1. **Keep one member and develop it.** "No gimmicks, no upsells, no pressure" becomes "No upsells. I'd rather you buy once and stay than buy twice and leave."
2. **Turn it into a full sentence with a specific.**
3. **Keep two members instead of three.** Two reads as a choice, three as a template.
4. **Cut the whole thing** if the context already made the point.

**Limit:** one anaphoric triple per document, and only as a deliberate rhetorical move.

### 14. Rule of three

The most universal AI pattern, confirmed across every published ruleset (Wikipedia's "Signs of AI writing", no-ai-slop, and the rest). Models package everything in threes to fake completeness: three adjectives ("fast, simple, and effective"), three nouns ("innovation, inspiration, and industry insights"), three parallel sentences in a row. Category 13 catches the anaphoric variant. This one catches every triad.

**Signal:** three items listed together, especially when the third adds nothing to the first two. More than one triad in a document means it's a template.

**Fix:**

1. **Keep two.** Two reads as a choice, three as a formula.
2. **Keep one and make it concrete.** "Fast, simple, and effective" becomes "It cuts the process from three days to two hours."
3. **Break it into a real list** if there genuinely are more items and each carries weight.

> **BAD:** "The tool is fast, intuitive, and reliable."
> **GOOD:** "The tool renders a page in two seconds and hasn't gone down once in six months."

### 15. Weasel attribution

AI attributes claims to entities you cannot check: "studies show", "experts agree", "it is widely believed", "observers note", "many argue", "industry reports suggest", "some critics say". This manufactures authority out of nothing.

**Signal:** a claim with a phantom subject. Which study? Which expert? Reported by whom?

**Fix:** name the source (author, institution, year), or cut the claim. There is no third option.

> **BAD:** "Experts agree that automation plays a crucial role in content marketing."
> **GOOD:** "HubSpot's 2025 report: 67% of marketers automate at least one stage of content production." / [cut it, if you have no source].

### 16. Importance puffery and pseudo-depth

AI asserts significance instead of showing it. Three variants of the same problem:

**a) Puffery:** "plays a crucial role", "stands as a testament to", "marks a pivotal moment", "reflects a broader trend", "is of fundamental importance". State the fact. The reader decides whether it matters.

> **BAD:** "The AI rollout marks a pivotal moment in the company's history."
> **GOOD:** "After the AI rollout, article production dropped from six hours to forty minutes."

**b) Participial analysis tails:** trailing clauses like "..., highlighting the team's commitment", "..., underscoring the importance of flexibility", "..., reflecting a global shift". These imitate analysis and carry no content. Category 5 catches -ing constructions at the start of a sentence. This one catches them bolted to the end. Stop the sentence after the fact. If the conclusion deserves saying, give it its own sentence with something concrete in it.

> **BAD:** "The company redesigned its onboarding, underscoring its commitment to employee growth."
> **GOOD:** "The company redesigned its onboarding. New hires now join projects in a week instead of a month."

**c) Aphorism kickers:** a pseudo-profound closing line at the end of a section: "Because symmetry is the language of trust." "After all, content is really just conversation." It sounds like wisdom and means nothing. End on a specific, not a fortune cookie.

### 17. Copula avoidance

Models replace the simplest verbs with elaborate substitutes: "serves as", "functions as", "stands as", "boasts", "features", "offers", "represents", "constitutes". Measured effect: use of "is" and "are" in academic writing dropped more than 10% after 2023, because models prefer these constructions.

**Signal:** "serves as", "functions as", "boasts", "features", "represents" where "is" or "has" would do.

**Fix:** go back to the simple verb.

| Elaborate (AI) | Plain (human) |
|---|---|
| Serves as a central hub | Is the hub |
| Functions as a reference point | Is the reference point |
| Boasts four meeting rooms | Has four meeting rooms |
| Features an export option | Exports / Has an export option |
| Represents a significant shift | Is a big change / [show the change] |
| Constitutes the basis for | Is the basis for |

### 18. Synonym cycling

Models rotate synonyms to avoid repetition (a side effect of repetition penalties in the architecture): "the protagonist... the main character... the central figure... the hero." A human repeats the clear term and nobody notices. Readers notice the carousel.

**Signal:** one concept named three or more different ways for no reason.

**Fix:** pick one word per concept and stick to it. Use a synonym only when it carries a different shade of meaning.

### 19. Chatbot artifacts and sycophancy

Text that reads like a chat response rather than a finished piece.

**a) Collaborative residue:** "I hope this helps!", "Let me know if you'd like me to expand on any section", "Feel free to adjust as needed", "Here's a draft for you". Cut it. Also cut placeholder brackets ([insert company name here]) and section stubs the model left behind.

**b) Knowledge-cutoff disclaimers and speculative gap-filling:** "As of my last update...", "While specific figures aren't publicly available...", and its worse cousin, guessing to fill a hole ("He maintains a low profile and keeps personal details private"). If the source doesn't exist, cut the claim.

**c) Sycophancy:** "Great question!", "That's an excellent point", "Absolutely!", "You're right to focus on this". In prose it appears as flattery aimed at the reader ("As a smart marketer, you already know..."). Cut it.

### 20. Throat-clearing and rhetorical setups

The model builds a stage before saying anything.

**a) Throat-clearing openers:** "Here's the thing.", "Let me be clear.", "The uncomfortable truth is...", "Let's be honest." Cut and go to the point.

**b) Fake-insight setups:** "What nobody tells you is...", "The part everyone misses:", "Here's what most people get wrong." This flatters the writer as an insider. If the insight is real, just state it.

**c) Rhetorical setups:** "What if I told you...", "Think about it:", "Plot twist:", "But here's the kicker." Cut them.

**d) The dramatic colon:** phrase, colon, revelation. "The detail: a separate agent grades it." Write the ordinary sentence: "A separate agent grades it."

**e) Signposting:** announcing the work instead of doing it. "Let's dive into how caching works" becomes a sentence about how caching works.

**f) Conversational fake-candor openers:** "Honestly? It depends." "Look, I get it." A performed shrug before an ordinary point.

## Diagnostic: quick test

After the rewrite, check:

1. Read it aloud. Wherever you stumble, rewrite.
2. Is there anything here a model could not generate? A specific observation, a real number, an anecdote?
3. After the first paragraph, do you know who is writing? Or could this be anyone?
4. Are all the signals gone? (Walk the 20 categories.)
5. Does this answer a real question a real person has, or does it "communicate" into a void?
6. Does it read like someone talking to an audience, or like a paper being read off a card? (See "Conversational mode".)

## Rules for the rewrite

1. **Add nothing.** Your job is to cut, not to expand. If the model padded, cut the padding and the text gets shorter. That's fine.
2. **Invent nothing.** No numbers, names, dates, or places. If the model invented them, cut them or flag them in the report for verification.
3. **Hold the register.** If the text is formal (a report, a legal document), don't drop in slang. Humanizing is not casualizing. People write formally and still write with a pulse.
4. **Shorter is usually better.** Models expand. Writers cut.
5. **Write conversationally.** The default output mode is talking to an audience, not filing an essay. Details below.

## Conversational mode (default output style)

The rewritten text should read like someone talking to a specific audience, as if the author were on stage or on camera. Not a paper read from a card.

Techniques:

- **Address the reader.** Second person, and questions aimed at them: "Know the feeling?", "How many times has that happened to you?"
- **Rhetorical questions as hinges.** Instead of a dry transition, ask: "The result?", "So what do you get?" One or two per section, not one per paragraph.
- **Anticipate objections.** "I know what you're thinking." "Sounds obvious? Not quite." Answer the reader's pushback before they voice it.
- **Beats and asides.** A short punch sentence after a long stretch: "Seriously." "That's it." **Hard limit: one or two per document.** These constructions are themselves a recognized AI pattern now (staccato drama, category 1). Overused, they stop being a pause and become the template.
- **Spoken syntax, not written syntax.** Constructions that come out of a mouth: "OK so", "look", "here's what happened". Dose according to register.

Limits:

- Register still rules (rule 3 above). In a report or a formal document, conversational means direct address and live rhythm, nothing more.
- Direct address and rhetorical questions are seasoning, not the meal. In every paragraph, the text reads like a webinar script. Which is a template again.
- **No dramatic colons** (category 20d) and **no aphorism kickers** (category 16c). Conversational means talking to people normally, not delivering maxims like a motivational speaker.
- Test: read it aloud. If you wouldn't say the sentence to a live human, rewrite it.

## Final output format

```
## AI signal audit

### 1. [Category]
- "quote" - [problem] - [fix]
- "quote" - [problem] - [fix]

### 2. [Category]
- "quote" - [problem] - [fix]

[...remaining categories...]

## Humanized text

[The full rebuilt text.]

## Editor's note

[1-3 sentences: what the main problem was, what you changed most.]
```

## Sources

The structural patterns here come from Wikipedia's "Signs of AI writing" (maintained by WikiProject AI Cleanup), which is the only ruleset built on a confirmed sample rather than impressions, plus the pattern sets in petergyang/no-ai-slop and blader/humanizer.

For Polish-language text, use the `/humanizacja` skill instead. The structural layer transfers between languages. The vocabulary, the punctuation rules, and the inflection handling do not.
