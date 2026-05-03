# Prompt Blueprint

Use this blueprint to convert rough image ideas into reliable GPT Image 2 prompts. Do not include every field by default; include only what helps the model preserve intent and avoid ambiguity.

## Minimal structure

```text
Generate an image of [subject and action].
Scene/environment: [where it is, what surrounds it, time/weather/background].
Composition/camera: [framing, angle, lens feel, crop, layout, panels/grid if relevant].
Lighting/color: [natural/studio/cinematic, shadows, color palette, contrast].
Style/medium: [photorealistic, 35mm film, CGI render, vector, UI mockup, ink drawing, etc.].
Important details: [locked counts, materials, clothing, packaging, product labels, visible text].
Text treatment: [exact text, language, typography placement, or no text].
Finish: [realistic texture, no over-sharpening, clean composition, high detail, etc.].
Avoid: [known failure modes that do not contradict the brief].
Aspect ratio: [3:1 through 1:3].
```

## Field guidance

### Subject

Make the subject unambiguous. Include count, identity constraints, scale, product shape, and locked details. For reference-image edits, say which details must remain unchanged.

### Scene and environment

Include enough environment to anchor realism: indoor/outdoor, location type, background elements, weather, time of day, surface materials, or context props. Avoid inventing a busy background when the user wants a clean product or UI image.

### Composition and camera

Use concrete composition language:

- close-up, medium shot, wide shot, top-down, low angle, three-quarter front angle, isometric, flat lay
- rule of thirds, centered hero, symmetrical, 2x2 grid, 9-panel storyboard, split-screen before/after
- shallow depth of field, motion blur in background, crisp product focus

### Lighting and color

Lighting is one of the highest-leverage prompt fields. Specify natural window light, overcast daylight, direct flash, soft diffused studio light, warm rim light, neon mixed lighting, high-contrast side light, or glossy commercial highlights.

Color direction should be purposeful: warm beige/gold luxury, monochrome black/white/red, pastel editorial, tropical saturated, dark-mode neon, etc.

### Text and typography

For text-heavy outputs, provide exact text and placement. Use instructions like:

- `visible text must read exactly: "..."`
- `use clean sans-serif typography`
- `no extra text, no misspelled text, no unrelated logos`
- `leave empty space for later copy` when text accuracy is not required

### Negative constraints

Use negatives sparingly. Target likely failures:

- no watermark
- no extra logos
- no unrelated text
- no plastic skin
- no oversharpening
- no overpolished stock-photo look
- no cluttered background
- no distorted hands or malformed product geometry

Do not include a negative constraint that conflicts with the user's request.

## Aspect ratio choices

- `3:1`: panoramic banner, wide hero, multi-panel row
- `16:9`: cinematic still, desktop mockup, wide ad, storyboard
- `3:2`: editorial photography, brand board
- `4:3`: natural photo, infographic, classic composition
- `1:1`: product hero, social square, icon/key visual
- `4:5`: social ad/poster/product card
- `3:4`: vertical portrait, flyer, product lifestyle
- `2:3`: poster, travel art, fashion editorial
- `9:16`: mobile story, app screen, tall poster, reel cover
- `1:3`: extreme vertical banner only when requested
