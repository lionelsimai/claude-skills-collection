---
name: video-replica
description: "Recreate a reference video, better: study it frame by frame, rebuild it, and verify quality including sound. Use when the user asks to remake, replicate or recreate a video, or says 'make the same video, better'."
category: Content Creation
license: MIT
version: 1.0.0
---

# Video Replica — make the same video, better

Trigger: "make / redo / replicate this video / reel / ad like this one", any reference video link or upload where the user wants a replica, not just inspiration.

## The lesson this skill exists for

1 Nov 2026, reel DfKbx_ARsjq: v1 was built from the Instagram text summary and was wrong in every important way (woman holding products, seated laughing fall). The actual hook, only visible on a frame-by-frame watch, was: legs-only opening, giant products AIRBORNE, Matrix dodge, flat-on-back knockdown, giant cookie fills frame. the user: "weird and does not represent the hook."
26 Sep 2026: a generative extension was rejected for hallucinations/morphing; the accepted fix used only editorial transforms of clean footage.

**Rule zero: never generate a replica from a caption, summary, or media-understanding text alone.**

## Pipeline (no skipping)

1. **Get eyes on the actual video**
   - Best: the user uploads the video file. Extract frames every 0.5s + a contact sheet locally with ffmpeg.
   - Link only: Instagram connector for metadata, then a live browser watch, frame-sampled. State what could not be verified (audio, sub-second timing).
2. **Write the shot list before any generation** — per beat: timestamp, framing/crop, person + outfit, camera, action, product scale relative to body, text overlay (exact wording), sound. Mark each element: MUST MATCH / CAN CHANGE (product, location, person, brand).
   - Show the user the shot list when the hook is non-obvious or he has already rejected one version. A 30-second approval here saves a full render.
3. **Keyframes first for fidelity**
   - Text-to-video alone drifts. For a close replica: generate/approve the 2–3 hero frames as images first, then animate with image-to-video (Sogni `animate_photo`, sourceImageIndices) instead of pure T2V.
   - Pure T2V is fine only for loose "inspired by" work.
4. **Generate on Sogni via the proven direct HTTPS route** (see local-sogni-creative-agent skill + AGENTS.md notes): H3 structured prompt (integrated_multimodal_description / overall_soundscape / non_diegetic_music, expandPrompt: false), vertical 768×1344 for Reels, negative instructions in plain words ("she does NOT hold the product", "no seated laughing").
5. **Text in post, never in generation** — hook text, product labels and end cards via ffmpeg drawtext / HyperFrames. AI-rendered text is gibberish.
6. **QC against the reference, side by side**
   - Extract frames from the render at the same beats as the shot list. Score each beat match / partial / miss.
   - Deliver only if the hook beat matches. If the hook misses, say so and re-render — do not deliver a miss as done.
   - Verify file: ffprobe (dims, duration, codecs) + full ffmpeg decode.
7. **Feedback loop (this is the training)**
   - the user's corrections work best tied to a beat: "at 4s she should be flat, not seated."
   - Save every correction + which version was accepted/rejected, and why, in the project folder and memory. Accepted versions become golden examples; rejected ones become named anti-examples in this skill.

## What to ask the user for (training inputs, ranked)

1. The video file itself, not just a link
2. What must match exactly vs what to swap (hook action is usually must-match; location/product/person are swaps)
3. A yes/no on the shot list, then on keyframes — his two cheapest, highest-leverage approvals
4. Beat-specific corrections on drafts, not general quality words

## Files

- Project per replica under `.`: reference frames, shot-list.md, plan.json, raw render, final in `.`.

## When to use

Use this skill when the task matches its description above and you need a repeatable, checked workflow rather than an improvised answer.

## Guardrails and quality checks

- Apply the rules in this skill throughout. Never fabricate facts or numbers, keep external actions draft-only until a human approves them, and state anything you could not verify.
