# Notices

This repository is an exam, not a library. Its contents — the tasks, the
painting and its layers, the grader, and the runs — belong to the rig-c
organisation and are licensed under CC BY-NC 4.0 (`LICENSE`): free to use, share
and adapt with credit, not for commercial use. That is deliberately not the MIT
licence the rig-c tools carry — this is an exam's content, not code to build on. Naming a
project below identifies where something comes from; it does not imply that its
authors endorse this repository. Statements marked **[observed]** carry the
date and the place they were read; upstream terms can change.

## Runs

A run submitted to this repository (a journal, a transcript, the files handed
in) is published here under the same licence. Submit only what you are able to
publish that way.

## The tools the grader runs

- [`@rig-c/parts`](https://github.com/rig-c/parts),
  [`rig-c`](https://github.com/rig-c/core) and
  [`@rig-c/pose`](https://github.com/rig-c/pose), all MIT (their licence, not this
  repository's), installed from npm at the
  versions `package.json` pins. Their own notices cover what they depend on; in
  particular the skeleton data `rigc build` writes is in the Spine 4.3 format,
  and rig-c's `NOTICE.md` says what that does and does not involve.

## Task 06's dance

`tasks/06-pose/inputs/toca.pose.json` holds joint positions measured from a
public video of the *Toca Toca* dance challenge,
https://www.youtube.com/shorts/HSug-0AAp3k, credited by that URL. The dance and
the video are their creators'; no frame, still or sound of the video is in this
repository. `tasks/06-pose/inputs/NOTICE.md` says how the joints were measured.

## See-through

Each task's `inputs/layers/` holds two See-through decompositions of its
painting, made with the ComfyUI wrapper. No See-through code or weights are in
this repository. Project, paper, licences and weights:
[rig-c/parts `NOTICE.md` §1](https://github.com/rig-c/parts/blob/main/NOTICE.md).

## Checkpoint

The paintings were generated for this exam with `novaAnimeXL_ilV80.safetensors` —
[Nova Anime XL](https://civitai.com/models/376130) "IL v8.0" by Crody, an
Illustrious-base checkpoint — with no LoRA, and upscaled with
`4x-AnimeSharp.pth`; task 03's was posed with
`controlnet-openpose-sdxl-1.0.safetensors` from `pose_seated.json`, task 01's
with no pose control. The checkpoint is not redistributed.
*Painted with Nova Anime XL IL v8.0 by Crody (https://civitai.com/models/376130).*
**[observed 2026-10-11]** CivitAI's model API reported for model 376130
`allowCommercialUse: ["RentCivit", "Image", "Rent"]`, `allowNoCredit: true`,
`allowDerivatives: true` and `allowDifferentLicense: true`; version 1854228 is
named "IL v8.0" with base model "Illustrious".

Each task's `inputs/generation.json` records every setting. The prompts name
and describe no existing character.
