# 도구가 아쉬웠던 점 — rig-c 2.51.1 · @rig-c/pose 0.6.0 · @rig-c/parts 1.17.0

## 포즈 파일 스펙 문자열이 리더와 다르다 (@rig-c/pose)
- **하려던 것:** 주어진 `inputs/reference/pose.json`으로 `rig-pose retarget`을 다시 돌려 K4 세트의 교체 시점을 바꾸기.
- **도구가 준 것:** `FAIL  POSE_SPEC: inputs/reference/pose.json "spec" is the string "rig-c-pose-frames/0"; this reader reads "rig-pose-sequence/1"` · `FAIL  POSE_SPACE: … "space" is {"units":"painting-px",…}; it must be exactly {"units":"picture-px",…}` · `FAIL  POSE_KEYS: … a key this reader does not know: "fps"`. 출하된 `dance/`는 같은 파일로 만들어져 있었다.
- **있었으면 했던 것:** 옛 스펙 이름을 읽어 주거나(「`rig-c-pose-frames/0`도 같은 형식으로 읽는다」), README 「The pose」 절에 옛 이름과의 관계 한 줄. 또는 `rig-pose convert`에 이 변환.
- **비용:** 약 5분(세 메시지 읽고 변환 사본 작성). 해냈다.

## `frames` 창은 허용각을 넘지 못한다 (@rig-c/pose)
- **하려던 것:** K4가 각도만으로는 f27에 켜지는데 손은 f23부터 귀에 있으니, map의 `"frames": [[23, 37]]`로 앞당기기.
- **도구가 준 것:** README 「A stopgap window: `frames`」 — *"it shows only inside those windows, and on them it is chosen over any set within tolerance that has no window"*. 실행 결과 `SWITCH set "K4_hand_up" … frames 27–33` 그대로. 왜 창의 앞 네 프레임이 안 켜졌는지 말해 주는 줄은 없다.
- **있었으면 했던 것:** 문장 하나 — 「창은 허용각 안에서만 고른다; 창 안이라도 `--switch-tolerance` 밖이면 켜지지 않는다」 — 와 run 출력에 `FRAMES set "K4" window 23–37: frames 23–26 outside tolerance (33.1°)` 같은 줄. 혹은 창 안이면 무조건 켜는 옵션.
- **비용:** 약 10분(리타깃 한 번 더 + 트랙 전수 비교로 「아무것도 안 바뀜」 확인). 결국 attachment 키를 손으로 옮겨서 해냈다.

## retarget에 `--images`가 없다 (@rig-c/pose)
- **하려던 것:** 물리 값을 바꾼 `rig.json` 사본(`run/after/rig/`)으로 리타깃.
- **도구가 준 것:** `FAIL  RIG_GATE_BASE: … with no motion spec is red under rigc build --profile spine before any animation` + `FAIL  RIGC: rigc compile error: image "hair_back.png" is not on disk at run/after/rig/images/hair_back.png`. `rigc build`엔 `--images <dir>`가 있는데 `rig-pose --help`엔 없다.
- **있었으면 했던 것:** 같은 플래그, 또는 README 「Requirements」에 「rig.json의 `images`는 rig 파일 기준이다 — 사본을 쓰면 그 필드를 고쳐라」.
- **비용:** 약 3분. `images` 필드를 상대경로로 고쳐 해냈다.

## 물리 값에 척도가 없다 (rig-c)
- **하려던 것:** 치마 세 사슬의 흔들림을 영상만큼으로 키우기.
- **도구가 준 것:** AUTHORING §4.6 — 필드 목록과 경계(`damping` [0,1], `strength: 0`·음수는 A23, 클록 주석). 「inertia 0.15 → 0.5가 54유닛 사슬에서 몇 도가 되나」를 가늠할 문장이나 표는 없다.
- **있었으면 했던 것:** 한 줄 측정표 — 「길이 L의 한 마디, 엉덩이 ±10° 흔들림에서 inertia/strength 조합별 끝마디 진폭」 — 또는 `rigc render --geometry` 결과를 받아 「뼈 A − 뼈 B 각 범위」를 찍어 주는 `inspect`/`bonedist` 한 줄.
- **비용:** 빌드·렌더·측정 두 바퀴 약 8분(1차는 130.7°로 네 배 과함). 해냈다.

## 12 fps 렌더의 폴더 이름 (rig-c)
- **하려던 것:** 측정용으로 `--fps 12` 렌더 후 `geometry.json` 읽기.
- **도구가 준 것:** `--fps 24`는 `render/dance@24fps/`, `--fps 12`는 `render/dance/` — 기본값일 때만 접미사가 빠진다. `render --help`의 `--out` 설명에는 「directory to write the frame series into」뿐.
- **있었으면 했던 것:** 「<animation>@<fps>fps, 기본 12 fps는 접미사 없음」 한 줄, 또는 항상 접미사.
- **비용:** 1분(파일 없음 오류 한 번). 해냈다.

## run.txt에 rigc 버전이 없다 (@rig-c/pose · rig-c)
- **하려던 것:** 주어진 빌드를 같은 입력으로 다시 빌드해 바이트 동일을 확인한 뒤 고치기 시작.
- **도구가 준 것:** `skeleton.json` 1,363곳 차이(메시 가중치의 뼈 순서) + run.txt의 게이트 줄 `51 assertions: 19 measured…` vs 내 빌드 `52 assertions: 21 measured…`. 어느 rigc로 만들었는지 run.txt·report.json 어디에도 없다. 2.51.1 changelog의 #1407(뼈 순서 정렬)로 추적했다.
- **있었으면 했던 것:** retarget 첫 줄과 `report.json`에 `rigc <version>` 한 줄(rigc의 `build --report`엔 들어 있는지 확인 못 함).
- **비용:** 약 6분. 해냈다(원인 특정).

## 발 접지는 도구 몫 (@rig-c/pose)
- **하려던 것:** 영상에선 발이 바닥에 있는데 리그 발이 바닥선 아래위로 ±50유닛 오가는 것 고치기.
- **도구가 준 것:** README 「What 0.1.0 does not do — Plant feet beyond what the pose gives」. 이 문장이 전부이고, 리포트에 발 높이 줄은 없다.
- **있었으면 했던 것:** `--plant-feet <bone,bone>` 같은 옵션(낮은 발을 `ground`에 고정, 두 발목이 동시에 오르는 프레임은 예외) — 입력(포즈 발목 y, 리그 발 y)이 도구 안에 다 있다. 최소한 `FEET` 리포트 줄(낮은 발 y의 범위).
- **비용:** 스크립트 작성·역치 수정 포함 약 12분. 해냈다(`run/after/post_motion.py`).

(@rig-c/parts 1.17.0은 이번에 호출할 일이 없었다 — 참고용으로만 두어 항목 없음.)
