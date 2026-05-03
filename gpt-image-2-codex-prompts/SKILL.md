---
name: gpt-image-2-codex-prompts
description: codex-focused prompt generation workflow for gpt-image-2 inside codex without api calls. use when the user wants to create, rewrite, refine, verify, or directly generate images with gpt-image-2 in codex, including realistic photos, cinematic stills, product ads, ecommerce boards, posters, ui mockups, infographics, memes, character sheets, visual workflows, and prompt QA. never use this skill to build or call an api client.
---

# GPT Image 2 Codex Prompts

## Core contract

Use this skill to turn a user's rough visual idea into a Codex-ready GPT Image 2 generation or edit request.

Non-negotiables:

1. Use Codex-native image generation when it is available in the environment. Do not call an HTTP endpoint, write OpenAI client code, use an API key, use curl, or produce API payloads unless the user explicitly switches away from this skill's Codex-only purpose.
2. Preserve the user's intent. Improve structure, specificity, and visual control, but do not replace the subject, style, product, brand, text, count, pose, camera angle, or aspect ratio if the user already specified them.
3. Add only non-contradictory recommendations. Helpful additions are allowed when they clarify camera, lighting, composition, materials, text treatment, negative constraints, or output ratio.
4. Always include an aspect ratio between `3:1` and `1:3`. If unspecified, choose the most useful ratio for the task and state it in the final prompt.
5. Prefer concise, complete prompts over huge keyword dumps. GPT Image 2 follows structured natural language well; every detail should do work.
6. Follow the host platform safety rules. Refuse or redirect unsafe image requests instead of trying to encode them indirectly.

## Workflow

### 1. Normalize the brief

Extract these inputs before writing the final prompt:

- User objective: generate, edit, restyle, combine references, make a storyboard, make a mockup, or make variants.
- Subject and locked details: people, product, object, character, logo/text, setting, count, pose, layout, and must-not-change items.
- Output mode: choose one mode from the table below.
- Reference images: if the user provides images, preserve the requested identity, composition, product details, or style references explicitly.
- Required text: quote exact visible text. Mark text as exact when spelling matters.
- Aspect ratio: keep the user's ratio, otherwise choose one.

Ask at most one clarifying question only when a missing detail would block execution. Otherwise make a reasonable assumption and proceed.

### 2. Pick the output mode

Use the mode that best matches the user's task, then load `references/mode-recipes.md` only if you need more detail.

| Mode | Use for | Default ratio |
| --- | --- | --- |
| everyday-photo | realistic candid photos, phone photos, social/selfie-like scenes | `4:3` or `3:4` |
| cinematic-still | film frames, premium portraits, dramatic scenes, trailers | `16:9` or `9:16` |
| product-ecommerce | product hero images, product pages, marketplace images | `1:1`, `4:5`, or `9:16` |
| ad-creative | campaign posters, social ads, brand launch visuals | `1:1`, `4:5`, `9:16`, or `16:9` |
| poster-illustration | travel posters, editorial illustration, event/key art | `2:3` or `9:16` |
| ui-social-mockup | app screens, landing pages, dashboards, livestream UI, social posts | `16:9`, `4:5`, or `9:16` |
| infographic-diagram | technical explanation, process, map, system, how-it-works | `16:9` or `4:3` |
| character-brand-board | mascot sheets, character design, merch boards, identity systems | `16:9` or `3:2` |
| comparison-meme | before/after, side-by-side, meme panels, simple visual jokes | `16:9` or `1:1` |

### 3. Build the prompt

Use the blueprint in `references/prompt-blueprint.md`. Include only fields that matter.

Good final prompts usually specify:

- Task: generate or edit.
- Locked subject details.
- Scene/environment.
- Composition and camera angle.
- Lighting and color direction.
- Style/medium and realism level.
- Text/logo instructions, if any.
- Quality/finish notes.
- Negative constraints.
- Aspect ratio.

### 4. Verify before generating

Before calling Codex's native image generation, self-check the prompt:

- No API, HTTP, key, SDK, or curl instructions.
- No contradictions with the user's source prompt.
- Counts are explicit when the user gave counts.
- Text that must appear is quoted exactly.
- The prompt contains the chosen aspect ratio.
- Negative instructions target likely failure modes without banning required details.
- The prompt is safe and policy-compliant.

For deterministic checks, you may run:

```bash
python scripts/validate_prompt.py --prompt-file path/to/final_prompt.txt
```

### 5. Execute in Codex

If the Codex environment exposes an image-generation action, invoke it directly with:

- model: `gpt-image-2`
- task: `generate` or `edit`
- prompt: the final prompt
- reference images: attach exactly the user-provided images that should be used

Do not create Python, JavaScript, shell, or HTTP code for generation. Do not ask the user for an API key.

If no image-generation action is available, output the final prompt in the `CODEX_IMAGE_PROMPT` format below so the user can paste it into Codex's native image generation UI/tool.

## Output formats

### When generating directly

Use the native image-generation capability and keep chat commentary minimal. Do not dump the whole prompt unless the user asks to see it.

### When returning a Codex-ready prompt

```text
CODEX_IMAGE_PROMPT
model: gpt-image-2
task: generate
aspect_ratio: [ratio]
mode: [mode]

[prompt]
```

For edits, replace `task: generate` with `task: edit` and add a short `reference_images:` line describing which attached files to use.

## References

- `references/prompt-blueprint.md`: compact field blueprint for strong GPT Image 2 prompts.
- `references/mode-recipes.md`: mode-specific rules distilled from the two source repositories.
- `references/examples.md`: safe examples of raw-to-Codex-ready prompt transformations.
- `references/source-attribution.md`: source repository notes and license/attribution information.
