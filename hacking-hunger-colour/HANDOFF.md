# Hacking Hunger: colour review handoff

Written 12 Nov 2026 at the end of the session that produced the review. The user will ask you for your opinion of this work and of the reasoning behind it, so this document tries to make the case for each decision and also shows where the case is weak. Every number in it is recomputed by `analysis/check.py`, so you can check the claims instead of trusting them.

## 1. Where everything is

| What | Where |
|---|---|
| The design system that was reviewed | Artifact "Hacking Hunger", https://claude.ai/artifact/8c7A8fWTtYv3gjg6i1xBAZ (Design System type). Content is under `project/`: `README.md`, `tokens.json` (v13, 99 colour tokens), `fields-and-texture.md`, `scales.md`, and 20 cards under `components/` (each a `README.md` plus a `preview.html` with an embedded animated render). |
| The script the analysis is built on | Google Doc "Hacking Hunger – Script v2.1 (Checkpoint 1)", Drive file id `1efPztz6YTtnaaD18MCO-SQFi21OszYmVsVf-dEEg21Y`. Twelve segments, S01–S12, plus a 5 s cold open. |
| Project hub (molecule library, PDB ids, which scene uses which molecule) | Claude Doc "Hacking Hunger: project hub", https://claude.ai/artifact/EevMdMnxCfZsjGc1BE5PfV |
| The review the user has seen | https://claude.ai/artifact/8xGxDRrrb9qJ1eL7BmHiCJ. Version 1 is the first pass (palette only). Versions 2–4 are the story-led pass with the self-check corrections. The live version is the current recommendation. |
| Snapshot of the tokens reviewed | `analysis/tokens-v13.json` |
| Analysis code | `analysis/colour.py` (OKLCH, WCAG contrast, OKLab ΔE, Machado CVD simulation, mixing), `analysis/check.py` (every number cited here), `analysis/recolor.py` (the approximate before/after recolours). |
| The proposal as data | `proposed-colours.json` |

Not read: the "Storyboard, colour and lighting v3" PDF on Drive and the "Hacking Hunger · Style Bible v2" doc. The design system is the newer source of truth, but the storyboard may hold colour intent I did not see.

## 2. What the user asked, in order

1. "Take a look at the Hacking Hunger style system and do a color analysis… really spend time on what would be the best colors for everything and make a color change suggestion. If it doesn't need any change, then we don't change… just think about the best outcome."
2. "I also want you to make your analysis based on how it serves the story. Like maybe blue is not the best color for the drug… don't be too keen on protecting or keeping, but don't be too keen on cutting either. Just go for what is really, really best and serves ultimately the story the best."
3. This handoff: "make your case well… make sure your work is good."

The second ask changed the frame. The first pass judged the palette as a palette. The second judged every colour by what it does for the script's argument.

## 3. The recommendation in one paragraph

Keep the warm body: honey, rose and pink, shaded toward violet. Give the story's signal one colour that nothing in the body uses: teal. The film's thesis is "Semaglutide is not a foreign molecule. It is GLP-1, refined" (S04), and it closes on "It is biology, extended in time" (S12). So the drug should be the teal the film already gives GLP-1 in the gut (the L cell), made deeper. Lightness carries duration: native GLP-1 is a softer teal, the drug a deep teal, and the signal turns grey when it ends (GLP-1 clipped by DPP-4 in S03, the weight curve after injections stop in S12). To make a teal drug readable inside its receptor, the receptor moves from sage to lilac, and the G protein takes the sage. Insulin stays rose, glucose and hunger are amber, receptors are lilac, and machinery is quiet. Teal never appears where the script says GLP-1 acts indirectly (S09). Several smaller fixes follow from this, and four tokens for molecules the script dropped are retired.

## 4. How the work was done, and its limits

- Read the design system's README, fields, scales, all 20 card READMEs, and `tokens.json`. Extracted and looked at the frames embedded in 16 previews.
- Converted all 99 colour tokens to OKLCH. Measured WCAG contrast, OKLab ΔE ×100, and ΔE under protan, deutan and tritan simulation (Machado et al. 2009, severity 1.0). In this document "cvd" means the smallest of the three.
- Thresholds I used. The system's own rule: a molecule at least 1.7:1 on both molecular fields. My working bar for two colours that must be told apart: cvd ≥ 6. Below 4 I count as a failure when the two touch, and as acceptable when they never share a frame.
- Judged pairs only where they share a frame or where the script relies on their meaning. Many near-collisions in the palette don't matter because the two molecules never meet.
- The before/after images are pixel recolours of the previews, made by finding the nearest token for each pixel and shifting it by the token's change. Anti-aliased dots and thin lines are only partly remapped. They show the direction, not the result. **No frame has been rendered with the proposed values.** The real test is the pipeline (`pipeline/icons/molecule_depth.py`, `pipeline/organs/*.py`) rendering the S05 sheet.
- I did not change the design system. Nothing has been applied.

## 5. The decisions and the case for each

Format: the claim, why it serves the story, the evidence, what I rejected, how confident I am, and what would change my mind.

### 5.1 The drug is deep teal, not blue: `mol-semaglutide` `#6d7ea2` → `#217871`

**Story.** The script asks the viewer to accept that the drug *is* GLP-1, improved. The viewer meets GLP-1 in S02 as the only teal thing in a pink gut (the L cell, its granules, its plume, all locked). If the drug arrives in S04 in that same hue, deeper, the claim is visible before it is spoken. In slate blue, the drug reads as a new character, and S04's side-by-side of native GLP-1 and semaglutide compares two unrelated colours. The script's own visual note already wants a family: "native GLP-1 a lighter, greyer sibling of semaglutide's" colour (written when the drug was coral).

**Evidence.**
- Teal is the one region of the hue wheel the body doesn't occupy. Its nearest ground or shadow (the lavender cavity, the silhouette, the violet shadows) is about 110° away. Slate blue is 30–34° from the silhouette, the cavity and every shadow hue, because the system shades everything toward violet. On the figure (S01, S11, S12) the current drug is 5.0 ΔE from the silhouette (cvd 2.9), which is nearly invisible. Teal is 16.0 (cvd 10.1).
- Teal sits opposite the coral red of blood (166° from `wash-blood`; slate is 116°). The drug's key beats happen in blood: the bloodstream in S03, the depot draining into capillaries and docking on albumin in S04.
- The only stated reason for blue was factual: "it is a pale blue liquid when injected." Injectable semaglutide is a clear, colourless solution (Ozempic and Wegovy labels; worth a one-line check). A clear liquid can take any convention, and pale aqua is the more common one for clear liquid.

**Rejected.**
- A clearer blue (`#496ba8`) was my own first-pass proposal. It fixed contrast but not meaning, and it still sat in the violet neighbourhood.
- Moving the whole GLP-1 family to blue, L cell included, would re-render locked gut frames, keep the violet-shadow problem, and turn a blue L cell toward violet wherever it is shaded.
- Coral or crimson, the original drug colour, disappears among red cells and capillaries. The system already rejected it.

**Confidence:** high on teal as the family hue, medium on the exact value. At this lightness, sRGB holds only about 0.09 chroma for hue 188, so the drug cannot be the most saturated colour in the frame (albumin is 0.087, insulin 0.104, the drug 0.081). It stands out by hue and darkness instead.

**What would change my mind:** a pipeline render of S05 where the deep teal looks dull or murky next to the lilac. In that case try lightness around 55 with the most chroma the gamut allows before abandoning the hue.

### 5.2 The GLP-1 family: one hue, and depth stands for duration

| Member | Value | Role |
|---|---|---|
| `glp1-spent` (new) | `#909b9a` | GLP-1 after DPP-4 clips it (S03), and the weight curve after stopping (S12) |
| `plume-glp1` (keep) | `#96d1c3` | GLP-1 leaving the L cell (S02–S03) |
| `cell-l` (keep) | `#60ac9d` | The cell that makes GLP-1 |
| `camp` (new) | `#4c9ea1` | The signal inside the cell (S06, S07) |
| `mol-glp1` (new) | `#5d928a` | Native GLP-1 at molecular scale (S02–S05; the vagus route in S11) |
| `mol-semaglutide` | `#217871` | The drug |
| `mol-orforglipron` (new) | `#206079` | The next generation, leaning blue (S12) |

**Story.** Native GLP-1 lasts about two minutes and semaglutide about a week. Paler for fleeting and deeper for lasting makes "extended in time" a property of the colour. The grey "spent" state gives the film a visual rhyme: in S03 the signal dies and its colour drains to grey; in S12 the injections stop and the curve turns grey again.

**Evidence.** Native and drug are 1.49:1 apart, cvd 9.2, so they read as siblings that can still be told apart. DPP-4 against native GLP-1: cvd 15.0.

**Weak points.**
- Native GLP-1 inside the lilac receptor (structure 6X18) is only 1.20:1, cvd 7.0. It is acceptable, but less clear than the drug in the same pocket.
- Orforglipron against the drug: cvd 6.2. Fine unless S12 shows them side by side, in which case test it.

### 5.3 The receptor moves to lilac, and the G protein takes the sage

`mol-glp1r` `#84a06b` → `#a18fb9`; `mol-gprotein` `#a183ae` → `#788f62`.

**Story.** The cold open and S05, the benchmark scene, show one event: the drug is caught by the receptor's outer domain and then inserted into its core. The key has to read as a separate thing entering the lock.

**Evidence.**
- Teal inside sage measures well (1.81:1, cvd 15.0), but in the recoloured frame it reads as a darker patch of the receptor, because green and teal are neighbours. That was a judgement from looking at the image, not a number. Teal inside lilac: 1.79:1, ΔE 20.2, cvd 13.8. The hues are far apart.
- Lilac against the amber membrane is close to complementary, so the receptor reads as crossing it. On the membrane itself the receptor is 1.68:1 (sage today is 1.66). The system's 1.7 rule applies to the two fields, not to the membrane band.
- Mauve, the current G protein colour, sits next to lilac, so the G protein takes the sage. Receptor against G protein goes from 1.13:1 (cvd 6.6) to 1.21:1 (cvd 7.2), now separated by complementary hues. Lightness ladder: drug 52, G protein 62, receptor 68.
- Insulin's receptor is already a grey lilac (`#9d99ab`). With GLP-1R lilac, every lock in the film is lilac. S01 (rose insulin into its lilac receptor) and S05 (teal drug into its lilac receptor) become the same picture with a different key, which is the comparison the script draws between the old answer and the new.

**Rejected.**
- Keeping sage: analogous to teal, and the drug loses its outline as a separate object.
- Mauve-rose: native GLP-1 inside it only reaches cvd 4.5, and it collides with the insulin family.
- Ochre: merges with the amber membrane and the honey interior.

**Weak point:** alpha cells and glucagon are also lilac (`cell-alpha` `#bb9cca`, proposed `mol-glucagon` `#947aa8`, 6.1 ΔE from the receptor). So "lilac is the lock" holds only at molecular scale. They never share a frame (S08 is tissue scale, where receptors are not drawn), but a viewer could link them. I judged the cost acceptable. Your review might not.

**Confidence:** medium-high. This is the most consequential change after the drug, and the one most worth testing in a real render.

### 5.4 S06: three colours carry the scene, and machinery stays quiet

**Story.** S06's crucial line is that glucose pulls the trigger and cAMP only amplifies it. The scene needs exactly three readable roles:

- the trigger: glucose, ATP and calcium in deep amber `glucose` `#ba7e2d`
- the amplifier: cAMP in teal `#4c9ea1`
- the output: insulin granules in rose

The script asks for "pale yellow" cAMP, which would merge with the amber trigger and blur the scene's one distinction. cAMP in teal also carries the GLP-1 signal visibly from outside the cell to inside it.

**Evidence and corrections.** This is where the self-check found the most errors.

- My first cAMP value, the pale plume teal, is 1.15:1 on the honey interior: near invisible. The mid teal is 2.10:1.
- The meal's light amber `#F5C766` is 1.06:1 on honey. Inside cells glucose has to be the deep amber (2.30:1), and even then it differs from the honey ground in depth, not hue. Drawing glucose as small hexagon rings helps: glucose is a six-membered ring, and the hexagon is already the film's motif.
- Adenylyl cyclase today (steel `#789ba7`) matches the cAMP it produces (cvd 1.0), so it moves to slate `#66718f`: cvd 10.0 from cAMP, 7.4 from the sage Gαs it holds, 11.8 from the receptor.
- PKA `#907c6c` and EPAC2 `#766558` are two quiet warm stones, 8.0 apart. A grid search over lightness, chroma and hue found no mid-tone colour that clears cvd 7 against all six story colours of S06 (sage, teal, rose, amber, lilac, drug). Only deep browns did. So the enzymes can't each have their own hue, and the rule "machinery is quiet" comes from this constraint.
- PKA and EPAC2 sit about 3 from insulin's rose under CVD simulation. They don't touch it in the scene.

**Confidence:** high on the three roles. Low on the PKA and EPAC2 values, which are placeholders for the S06 sheet.

### 5.5 No teal where the effect is indirect (S09)

S09 says twice that the liver, muscle and fat effects are indirect ("Fat cells carry few GLP-1 receptors"). So the drug's colour should be absent from all three panels.

The FatCells card, locked today, shows adiponectin as leaf-green grains. Those are 4.1 cvd from the drug and close enough in hue to read as the drug acting on fat, which is exactly the claim the script rules out. Proposed: adiponectin blue, `mol-adiponectin` `#5774a9`, grains `#43629c`. That is 2.86:1 on the fat ground and clearly a different messenger. Blue is free once the drug leaves it; the viewer never saw blue as the drug.

**Confidence:** high on the principle, medium on blue as the answer.

### 5.6 The insulin family, the islet and the stomach

- Insulin keeps its brick rose. `mol-glut4` goes lighter, `#b16f89` → `#be859b`. Insulin and GLUT4 meet in S01 and S09, where they were too close (cvd 4.8). Now they are 10.5, and insulin is the deeper, active one.
- New: `mol-glucagon` `#947aa8` (alpha-cell family) and `mol-somatostatin` `#956186` (delta family). "As insulin rises, glucagon falls" becomes rose up and lilac down, which the islet card's beta and alpha cells already encode.
- S08: a brief teal pulse reaches only the beta and delta cells, because the script says GLP-1 receptor activation is there. In the low-glucose flip, no teal appears.
- S10: the amber meal tells the stomach story, as the Digestion card already does. A small teal light stays on in the brain, bridging to S11.

### 5.7 DPP-4 is graphite: `mol-dpp4` (new) `#585a66`

It is the one cold, heavy machine in a warm body, and the colour that remains as GLP-1's drains. It sits 4.2:1 on the blood ground. My first value (`#6f7082`) was close to the new cyclase slate, so DPP-4 went darker; the two are now 8.3 apart, and the villain doesn't look like a helper.

### 5.8 Albumin keeps its straw: `mol-albumin` `#b2995a`

The first pass moved albumin to gold, because it nearly matched the sage receptor beside it (contrast 1.05:1, cvd 2.0). With the receptor lilac that problem is gone (cvd 5.3; they float apart in the hero frame). Straw also sets the teal drug apart better than gold does (cvd 15.4 against 12.6) and is less loud, which suits a carrier. Plasma really is straw-coloured. This is a deliberate reversal, and an example of not changing what no longer needs it.

### 5.9 Outside the cell is truly rose: `extra-ground` `#efc3b0` → `#f3bfbd`, with tile `#ebb0ad` and line `#c58484`

The README calls the field "a quiet pink that continues the rose of the blood", but at hue 45 it is a peach. The proposed value matches `blood-ground` (0.4 ΔE), so pushing in from the vein to the molecules is seamless, and outside reads as blood. Teal on rose is the film's best pairing.

The separation between outside and inside improves for normal vision (ΔE 3.7 → 5.9). It barely changes under CVD simulation (2.2 → 2.6). For colour-blind viewers the pattern and the membrane still do that work.

### 5.10 Charts (S04 half-life, S12 outcomes)

Each series wears its subject's colour:

| Series | Value |
|---|---|
| drug | `#217871` |
| native GLP-1 | `#63a79f` |
| placebo | `#9a9098`, warm grey: the convention for a control arm |
| glucose | `#ba7e2d` |

Today's `chart-4` gives placebo the blue the film used for the drug, and `chart-2` gives the drug a rose. Both would mislead.

In S12 the drug line turns grey at the "stop" marker as the weight comes back. That grey (`glp1-spent`) is close to placebo grey (3.2 ΔE). I meant the two to converge, but the two lines must stay apart in space and be labelled. Challenge this if you think it reads as confusion rather than meaning.

### 5.11 Nausea is olive: `nausea` (new) `#a5aa73`

The script says the area postrema flickers "a queasy green-grey", which sits near the GLP-1 family. A sickly olive is 22.1 ΔE from the drug, so the side effect doesn't wear the drug's colour.

### 5.12 Retire the tokens the script dropped

`mol-exendin4`, `mol-pi3k-p110`, `mol-pi3k-p85`, `mol-rgs`, and their icons (3C59, 8DCP, 3C7K), plus 7LCJ, which the hub already retired. None is in script v2.1. Their colours constrained the palette for nothing; several of my first-pass fixes were spent on their collisions.

The hub lists 3C59 (exendin-4) for S07, but the narration never names exendin-4. Use 4ZGM (semaglutide on the receptor's outer domain) there.

### 5.13 To test, not decided

- A quieter membrane: heads `#d5ab6b` (from `#d9a143`), lines `#9a723e` (from `#865706`). The lipid heads are the most saturated thing in the molecular frame and pull the eye from the subject.
- Nuclei and cell walls one step lighter (`#6b4b80`, `#7f5e84`). In the recolour the gain was small. The bigger lever in the Islet and Lobule frames is the ink outline on every acinus.
- The drug's film over the fat cells at 15–20% rather than 25%: aqua over cream tints the cells slightly green.

### 5.14 What stays, and why

- The warm body and its violet shading, which is what lets one cool colour carry the story.
- Organ families (honey pancreas on a lavender cavity, pink gut), blood, vein, capillary and fat.
- The L cell, granules and plume, which become the anchor of the GLP-1 family.
- The islet coding (beta rose, alpha lilac), already the S08 story.
- Paper, ink and type colours.

The placeholder washes (brain, liver, muscle, nerve, adipose) were not reviewed. `wash-brain` is a grey, which the README rules out elsewhere.

## 6. The colour script in brief

| Scene | Colours |
|---|---|
| Open | Teal enters lilac: the key colour first. |
| S01 | Insulin rose, possibly as the only colour in a 1921 duotone (the system's own history-frame proposal), into its grey-lilac receptor. |
| S02 | First teal: the L cell. |
| S03 | Soft-teal GLP-1 in rose blood, graphite DPP-4, drain to grey. |
| S04 | Native and drug side by side, one hue at two depths. Teal pen band, aqua depot, the drug docking on straw albumin. |
| S05 | Teal into lilac, sage G protein. |
| S06 | Amber trigger, teal amplifier, rose output, quiet machinery. |
| S07 | Lilac receptors in vesicles, teal inside, a faint cAMP teal. |
| S08 | Rose up, lilac down, a teal pulse on beta and delta cells only. |
| S09 | No teal. Amber glucose through rose GLUT4, blue adiponectin. |
| S10 | Amber meal, a small lasting teal light in the brain. |
| S11 | Deep teal at the circumventricular organs and arcuate nucleus; pale native teal along the vagus (the script's "native GLP-1" route); fullness neurons teal; hunger and reward in amber, dimming; nausea olive. |
| S12 | Teal against a grey placebo, grey after stopping, a teal network over the lavender figure, orforglipron in the same lilac receptor. The last colour on screen is teal. |

## 7. The grammar (eight rules)

1. Teal is GLP-1's signal in every form. Pale is fleeting, deep is lasting.
2. Teal appears only where GLP-1 acts directly.
3. Grey is the signal gone.
4. Rose is insulin.
5. Amber is glucose, food and hunger.
6. Lilac is the lock. Alpha cells keep the family at tissue scale.
7. Machinery is quiet.
8. The body stays warm and shades toward violet; nothing in it is teal except the cell that makes GLP-1.

## 8. How my position moved (so you can judge it)

| Item | First pass | Story pass | After self-check |
|---|---|---|---|
| Drug | clearer blue `#496ba8` | teal `#217871` | same |
| Receptor | sage kept | lilac | same |
| G protein | deeper mauve | sage `#788f62` | same |
| Albumin | gold `#a48534` | gold | **back to straw** (gold only fixed the sage collision) |
| PI3K p110 | raspberry | retired | same |
| Exendin-4 | deeper taupe | retired | same |
| cAMP | not addressed | pale teal `#96d1c3` | **mid teal `#4c9ea1`** (pale vanished on honey) |
| Glucose in cells | not addressed | light amber | **deep amber `#ba7e2d`** (light vanished on honey) |
| Orforglipron | not addressed | `#5a92ab` | **`#206079`** (first value cvd 2.5 inside the receptor) |
| Adenylyl cyclase | kept | kept | **slate `#66718f`** (steel matched cAMP, cvd 1.0) |
| PKA / EPAC2 | not addressed | freed colours | **two stones** (first values collided with insulin and glucose) |
| DPP-4 | not addressed | `#6f7082` | **`#585a66`** (too close to the new slate) |
| Drug liquid | not addressed | `#afdfdd` | **`#9dd8d4`** |
| Charts | drug blue, placebo grey | drug teal | same |

The first pass also proposed outlines only for the molecules it changed. Section 5 now lists outlines for all.

## 9. Known weaknesses and open risks

1. **Nothing is rendered.** Every judgement about how a frame looks comes from approximate recolours. The S05, S06 and S03 sheets are the real test.
2. **Dark outlines.** The rule "outline = fill at 55%" turns the deeper fills into outlines darker than any outline in the system today (current range L 38–45): drug L 34.6, EPAC2 34.8, DPP-4 31.8, orforglipron 31.0. The README forbids near-black lines on molecules, and ink is L 26. If these read near-black at 4K, either lift those fills a little or floor outline lightness at about L 36.
3. **The drug isn't the most saturated colour.** The gamut limits teal at this lightness, and albumin and insulin are more chromatic. The drug stands out by hue and darkness. Check that this holds in the docking frame.
4. **Lilac means two things.** Receptor and alpha cell / glucagon (5.3).
5. **The liquid trades contrast for hue.** To normal vision it is as clear as the blue (9.3 ΔE from steel, 11.3 from cream fat), but under CVD simulation it is slightly worse (7.2 and 6.4 against 8.8 and 8.7). The gain is meaning and hue, not contrast.
6. **Glucose on honey reads by depth only** inside cells (5.4).
7. **Smaller margins that rely on two molecules never touching:** native GLP-1 in the receptor (cvd 7.0), G protein against albumin across the membrane (5.5), PKA and EPAC2 against insulin (about 3), placebo against spent grey (1.6).
8. **Teal near branding.** I did not check whether a teal semaglutide reads as a reference to any product's branding. The pen is generic, so it is probably fine, but someone should look.
9. **Cost.** Every icon with GLP-1R, the G protein, semaglutide or adenylyl cyclase regenerates (palette change in the pipeline). The locked Injection, Depot and FatCells clips re-render, because their colour constants live in `pen.py` and `adipose.py`. The README and about 8 card READMEs need their colour notes rewritten. Charts and S06 are not built yet, so they cost nothing.

## 10. What I'd ask a reviewer to push on

- Does "the drug is GLP-1's sibling" outweigh the drug having its own distinctive colour? A viewer might mistake the drug for the hormone in S04's side-by-side. My answer is that the lightness gap and the narration handle it, and that the script wants the kinship.
- Is the lilac receptor worth the churn, or would a receptor rendered with a stronger ink line around the drug do the same job in sage?
- Is "teal only where GLP-1 acts directly" too strict for the S12 network overlay?
- Are three teals (L cell, native GLP-1, cAMP) plus the drug too many for viewers to keep apart, or does a family not need its members kept apart?

## 11. Suggested next steps

1. Render the S05 sheet: three options from one seed (drug teal in sage, drug teal in lilac, current slate in sage) with the real pipeline. Decide 5.1 and 5.3 there.
2. Render S03's DPP-4 clip with the drain to grey, and S06 at the three-role level with placeholder machinery.
3. If the S05 sheet confirms the direction, update `tokens.json` (`proposed-colours.json` is the change list), the palette JSON in the repository, the README colour section, and the card READMEs. The Design System type's own instructions say how to publish file changes to that artifact.

## 12. Reproducing the numbers

```
cd analysis
python3 check.py
```

It prints every contrast, ΔE and CVD figure used above, grouped by section. `colour.py` holds the maths. It loads `tokens-v13.json`, the design system's colour tokens as of 12 Nov 2026, version 13.
