---
name: ai-avatar-critique
description: "Ruthlessly critique an AI video avatar before it ships, with a verdict, scored dimensions and a timestamped fix list. Use when the user says 'critique this avatar', 'review my avatar video', 'avatar QC', or asks why an avatar looks fake."
category: Content Creation
license: MIT
version: 1.0.0
---

# AI Avatar Critique — world-class self-critique for AI video avatars

## Purpose

- Judge an AI avatar video the way a hostile expert, a scrolling viewer and the person whose face it is would judge it, all in one pass.

- Never let a video ship on technical checks alone. A clean ffprobe, the right duration and a loudness pass say nothing about whether the avatar looks alive, sounds like the person or holds attention.

- Produce one verdict, a scored critique, a timestamped fix list ranked by severity, and a re-score after fixes. No vague praise and no unranked notes.

## When to use it

- Use it on every avatar video before delivery or posting, whether it came from HeyGen, Sogni, HyperFrames, Synthesia, D-ID, Hedra, a talking-head pipeline or a real-person edit with an AI voice.

- Use it on a competitor or reference avatar when the user asks what makes it work or fail.

- Use it again after every fix round. A critique without a re-score is unfinished work.

## Verdict first, always

- Lead with one verdict in the first line. SHIP means it can go out as is. FIX means named fixes would make it shippable. KILL means do not post it and do not patch it, rebuild it.

- Follow the verdict with the total score out of 100, the weakest dimension, and the single worst moment with its timestamp.

- Give depth after the verdict, not before it. the user wants the call first, then the evidence.

## Hard fails — any one of these is an automatic KILL

- The face is not the same person throughout, or it does not match the approved reference look. Identity drift, a look swap or a different person in any shot fails the whole video.

- Lip movement does not match the speech, the mouth stays still while speaking, or audio and video are visibly out of sync.

- There is no sound, no coherent voiceover, or no music or sound bed. Silent avatar videos never ship.

- The voice was sped up, tempo fitted or time stretched to fit a window. Re-record or re-synthesise a shorter take instead.

- The voice is the wrong person, the wrong gender for what was asked, or a voice the user has rejected before. Check the catalogue entry, never assume from the name.

- The transcript differs from the approved script in meaning, names, numbers or the call to action.

- True peak is above minus 1.5 dB, the noise floor swings audibly between cuts, or a homemade synth noise bed is audible.

- Hands, teeth, eyes or props morph, duplicate or break in a way a normal viewer would notice at full speed.

- Text rendered inside the generation is gibberish, a name or price is wrong, or a claim in the script is untrue or unapproved.

## Run the critique in five passes

- Pass 1, cold watch. Watch the full video once at natural speed, full screen, with sound on, without pausing. Write what a scrolling viewer would feel in the first 3 seconds and whether you would keep watching.

- Pass 2, silent watch. Watch again muted. Judge face, eyes, blinks, head motion, hands and scene coherence without the voice covering flaws.

- Pass 3, eyes-closed listen. Listen without picture. Judge voice identity, prosody, pacing, breath, room tone, music bed taste and mix.

- Pass 4, frame pass. Run the helper in `bin/avatar-critique` to extract frames, a contact sheet, loudness, silence and stream data. Inspect the sheet for identity drift, teeth and eye artifacts, flicker and background drift.

- Pass 5, measured pass. Run the open-source measurements that fit the video, from `references/open-source-stack.md`. Record the actual numbers, not adjectives, and compare them with the thresholds in `references/rubric.md`.

## Score the 10 dimensions

- Score every dimension from 0 to 10 and weight it as set out in `references/rubric.md`. Score what is on screen, not the effort or the tool.

- Identity fidelity and consistency, weight 20. The face matches the reference and stays the same person in every frame.

- Lip sync and audio-video sync, weight 15. Mouth shapes match phonemes and timing, with no lag or lead a viewer can feel.

- Voice clone fidelity and delivery, weight 15. It sounds like the person, at a human pace, with stress and pauses in the right places.

- Audio quality and mix, weight 10. Clean voice, stable noise floor, a proven music bed ducked under speech, loudness and peak inside limits.

- Facial performance, weight 10. Natural blinks, gaze that lands, brow and expression that match the words, no frozen or rubber face.

- Head, body and hand realism, weight 10. Motion is smooth and purposeful, never lifeless, looping, jerky or morphing.

- Visual and temporal quality, weight 8. Sharp, stable, no flicker, warping, smeared teeth or skin, and consistent lighting and grade.

- Scene, props and background coherence, weight 5. Nothing appears, vanishes, changes size or changes identity between cuts.

- Script, hook and persuasion, weight 4. The first 3 seconds earn attention, one idea lands at a time, and the close and call to action are clear.

- Platform fitness, weight 3. Correct aspect and safe zones, captions that are accurate and readable, a strong first frame and no dead air at the start or end.

## Name flaws like a director, not a fan

- Tie every flaw to a timestamp or a time range, the dimension it hits, and what the viewer sees or hears. Write "at 0:07 the teeth smear when he says founders" rather than "mouth looks off".

- Separate three kinds of finding. Measured means a tool produced a number. Observed means you saw or heard it in a pass. Inferred means you are guessing at the cause, and you must label it as a guess.

- Rank fixes by viewer impact, not by how easy they are. Identity, sync and voice fixes outrank grade, captions and polish.

- For each fix, say the cheapest action that would actually fix it. Re-render one segment, re-record one line, swap the bed, cut the shot, or rebuild. Do not prescribe a full rebuild for a one-line flaw.

- Include at least one adversarial read. State the harshest fair thing a critic, a competitor or a commenter would say, and whether it is true.

## The self-critique loop

- After fixes, run all five passes again on the new file and re-score with the same rubric. Show a delta table of old score, new score and what changed per dimension.

- Never carry a score forward from an older cut. A changed file is a new video until it is re-watched, re-listened to and re-measured.

- Stop the loop only at SHIP, at KILL with a rebuild plan, or when the user says stop, done or that he has handled it. Then close it and do not relitigate it.

- Keep a golden set. Save accepted avatar videos and rejected ones by name in the project folder, with the score sheet for each, so later critiques compare against real examples and not taste alone.

- Record every repeated flaw in this skill or in the project notes. A flaw that appears twice becomes a named check in the next critique.

## the user-specific gates

- Apply his standing video rules in full. Every video has sound, voice segments are verified inside their scene at natural speed, the music bed itself is listened to, and a proven bed beats a novel one.

- Use DESIGN.md for any visual or caption treatment. Master brand is ink #1a2530 and gold #a5854a, Georgia and Helvetica.

- Check the avatar against his known HeyGen setup when it is a the user avatar. His avatar is named the user, his cloned voice is LIONEL VOICE, and an avatar ID he supplies overrides any default look. If an ID he gave does not resolve, stop and report it rather than substituting another avatar.

- Do not default to voices he has rejected, and never use a male voice when he asked for a female voice.

- Present the critique the way he reads. Verdict first, brief headers, short bullets, recommended fix first, no big chunks of prose.

## Tools in this skill

- Run `. <video.mp4>` before the frame and measured passes. It writes a critique folder with stream data, loudness, silence spans, sampled frames, a contact sheet and a score sheet scaffold.

- Read `references/rubric.md` for weights, thresholds and score bands. A dimension score must cite the evidence or the measurement that earned it.

- Read `references/open-source-stack.md` before claiming a measurement. It lists the open-source tools that back each dimension, what each one proves and what it cannot prove.

- Read `references/report-template.md` for the exact delivery shape. Fill every section, including the ones that passed, so a pass is on the record.

## Guardrails and quality checks

- Apply the rules in this skill throughout. Never fabricate facts or numbers, keep external actions draft-only until a human approves them, and state anything you could not verify.
