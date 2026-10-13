# Journal — 아스트라, 춤추는 리그 손질하기, 2026-10-13

One entry per step that changes something (a file you write, a command that builds). Number them.
Write lines 1–3 **before** the step and line 4 **after** it.

## Entry <n>

1. **Read:** which document, section or message this step rests on (path and heading, or the message quoted).
2. **Expect:** what the step will produce, concretely — an exit code, a file, a number, a line of output.
3. **Chose / turned down:** what you are about to do, and the alternative you considered and why not.
4. **Happened:** what the step actually produced. If it differs from line 2, begin the line with
   `WTF?:` and say in one sentence what you now think you misread — or that nothing told you. Say it
   the way it landed. Politeness is not graded here; a line that understates the surprise hides it.

## At the end

- **Where I guessed:** every value you wrote without a source (a number, a name), and what you would
  have needed to read to not guess.
- **What I could not find:** questions you had that no document or message answered.

## Entry 1 — 준비

1. **Read:** PROBLEM.md 도구 및 작업 폴더, JOURNAL.md.
2. **Expect:** 지정된 세 패키지가 node_modules에 설치되고 npm install이 0으로 끝난다.
3. **Chose / turned down:** 고정 버전 로컬 설치. 다른 레포나 기존 풀이를 읽지 않으며 부대 없이 직접 수행한다. 일지 생성 자체는 이 최초 항목을 담기 위한 부트스트랩이다.
4. **Happened:** npm install exit 0; 6 packages added, 0 vulnerabilities.

## Entry 2 — 단위별 비교 준비
1. **Read:** PROBLEM.md 단위별 비교, render --help의 --geometry/--folds; 입력 데모 648×480, 24fps.
2. **Expect:** 0–12초 데모의 1초 간격 비교 시트와 24fps 기준 리그 geometry/folds가 생성된다.
3. **Chose / turned down:** 기존 영상 비교 시트를 먼저 보고 같은 입력 빌드를 계측한다. 리포트의 경고만 보고 결함으로 단정하지 않는다.
4. **Happened:** render exit 0; 313프레임 생성. shins에서 216프레임에 삼각형 10·11이 접혔다. 나머지 11개 메시에서는 접힘을 보고하지 않았다.

## Entry 3 — 머리
1. **Read:** 입력 dance에는 head rotate만 있고 눈·입 트랙이 없다. overview의 얼굴과 실제 영상은 작아 표정 판정이 어렵다.
2. **Expect:** 0.25초 간격 원본 얼굴 시트와 0·4·8·12초 비교 프레임에서 표정 변화를 직접 확인한다.
3. **Chose / turned down:** 눈깜빡임 타이밍을 임의로 넣지 않고 원본을 확대해서 본다.
4. WTF?: 얼굴 확대 시트는 생겼지만 비교 프레임 추출은 ffmpeg가 `Unrecognized option 'vsync'`로 거부했다. 설치된 ffmpeg에서는 -fps_mode vfr로 바꾼다. 얼굴 시트에서 눈을 닫는 구간·입모양 변화가 보인다. fps 필터의 표본 시점은 정밀 타이밍 근거로 쓰지 않는다.

## Entry 4 — 머리·팔·몸·다리·옷 증거 채집
1. **Read:** Entry 3 ffmpeg 오류, geometry.json의 world transforms, 입력 run.txt의 shins 경고 및 frames.json.
2. **Expect:** 정확히 24fps 프레임 번호로 표기된 비교 프레임과 확대 시트가 생성되고, 발 높이·치마·팔 교체 및 정점 연결을 측정할 수 있다.
3. **Chose / turned down:** 각 단위는 시트를 순서대로 따로 읽는다. 좌우 비교 원본은 그대로 보존하고, 수치와 시각 결함을 구분한다. 이후 모든 실행을 기록하는 로컬 명령 래퍼를 만든다.
4. WTF?: 비교 프레임 33장과 단위별 시트는 생성됐으나 머리 추출은 313프레임 영상에서 54장을 썼다(끝에 시작 화면 반복). 원본 ffprobe는 313프레임, 13.041667초다. 이후 증거는 기존 비교 데모의 명시 프레임을 정본으로 삼고 영상 추출에 프레임 수 상한을 둔다. geometry의 per-frame 필드도 slots가 아니라 attachments였다.

## Entry 5 — 발견 기록 및 다리·옷 계측
1. **Read:** 단위별 비교 시트; AUTHORING §4.4·4.11; pose README의 What 0.1.0 does not do 및 alternates. shins 10·11은 오른쪽과 왼쪽 정강이를 가로지르는 연결이다.
2. **Expect:** 발견별 분류·시간·증거를 기록한다. 신발 바닥 높이와 치마 검정 실루엣을 직접 측정해 수리 기준을 만든다.
3. **Chose / turned down:** 폴드 수를 줄이려고 임의 삼각형을 지우지 않고, 두 다리 사이 투명 영역임을 텍스처에서 확인한다. 치마 물리 상수를 맹목적으로 키우는 대신 실제 영상의 옆 퍼짐을 측정한다.
4. WTF?: shins 두 연결 삼각형의 픽셀 알파는 모두 0이라 삭제해도 그림은 잃지 않는다. 신발 바닥 범위는 오른쪽 6.33–99.79, 왼쪽 -1.66–85.11이다. 치마 ROI를 눈으로 보니 들어올린 옆단을 윗경계가 잘랐다. 그대로 수리에 쓰면 흔들림을 과소 측정한다.

## Entry 6 — 옷 계측 수정
1. **Read:** skirt-mask-f192.png에서 윗경계 밖으로 나간 치마, f138의 비대칭 실루엣.
2. **Expect:** ROI를 hip y−40부터로 넓히면 옆단 전체가 포함된다. 270×480으로 디코드해 1080p 전체를 메모리에 둘 필요도 없앤다.
3. **Chose / turned down:** 같은 알고리즘의 관측 범위를 수정한다. 잘린 측정값을 더 큰 임의 배율로 보정하지 않는다.
4. **Happened:** ROI 확장 계측을 다시 수행했다. 영상은 270×480으로 디코드하며 모든 결과는 폴더 안에 있다. 수리에는 이 두 번째 측정만 사용한다.

## Entry 7 — 수리 스크립트 준비
1. **Read:** AUTHORING §4.4(상대 translate, scale), §4.5(키 시간), §4.11(가중치별 bind-space deform), pose README alternates(월드 각도 turn).
2. **Expect:** 부위별 독립 실행 스크립트와 입력 사본이 준비된다. 원본 inputs는 바꾸지 않는다.
3. **Chose / turned down:** 팔·접지·치마·눈을 각각 명령으로 수행한다. 눈은 기존 최소 scale 0.12, 팔은 기존 K0 ±5°를 유지한다. 접지는 root의 수직 보정만 하고 무릎 자세를 임의로 새로 만들지 않는다.
4. **Happened:** 부위별 스크립트와 after/rig.json·motion.json·map.json 사본 생성, init exit 0.

## Entry 8 — 팔 수리
1. **Read:** A1, f30·48·60 비교; pose README alternates의 drawn/turn 및 AUTHORING §4.4 attachment.
2. **Expect:** f19–60 오른손이 등 뒤로 돌아가며 왼팔 모션은 유지된다. K0의 ±5° 제한을 지킨다.
3. **Chose / turned down:** 기존 K0 오른팔 그림만 연장하고 원래 몸통·왼팔 선택은 유지해 혼합 이음새를 렌더에서 검사한다. 전체 K0를 씌워 왼팔 동작을 없애지 않는다.
4. **Happened:** 42프레임의 오른팔 attachment와 회전만 수정했다. exit 0. 화면 검사는 통합 렌더 뒤 수행한다.

## Entry 9 — 다리·몸 접지 수리
1. **Read:** L1·L2·B1; measurements-before.json의 투명 bridge와 신발 바닥, pose.json 발목 높이, AUTHORING §4.4 translatey.
2. **Expect:** 교차 삼각형 2개가 사라지고 점프 밖 최소 신발 바닥 높이가 f0의 46.95875로 유지된다. 원본 발목의 점프 높이는 남는다.
3. **Chose / turned down:** root 수직 이동으로 지지 높이를 보정한다. 두 발 IK나 깊이 방향 무릎 굽힘을 추정해 만들지는 않는다. 이 수리는 양발·수평 접지를 보장하지 않고 몸의 수직 흔들림 일부를 줄이는 절충이다.
4. **Happened:** 투명 삼각형 10·11 제거, root translatey 313키 추가, jump/contact-targets 기록. exit 0.

## Entry 10 — 옷 수리
1. **Read:** C1, 확장 ROI 실루엣 계측, AUTHORING §4.11 weighted deform는 influence당 bind-space 쌍이라는 문장.
2. **Expect:** 치마 허리선은 유지하면서 f96–261의 폭·옆 치우침·밑단 기울기가 커지고, 접힘 없는 메시가 유지된다.
3. **Chose / turned down:** 측정 실루엣의 변화분을 각 영향 뼈의 역행렬로 돌려 deform를 기록한다. 분할 mask·5프레임 평활·배율 제한은 편집 휴리스틱이며 실제 물리 측정으로 부르지 않는다. 물리 상수는 유지한다.
4. **Happened:** 313개의 bottomwear deform 키와 측정·편집 파라미터 파일 생성. exit 0. fold와 시각 효과는 빌드·렌더에서 판정한다.

## Entry 11 — 머리 수리
1. **Read:** H1과 원본 눈 감는 프레임, 입력 idle의 eyes scaley 최소 0.12 및 easings shut/open.
2. **Expect:** 관측된 다섯 눈 감기 구간이 dance에 표현된다. 입 그림은 변형하지 않는다.
3. **Chose / turned down:** 기존 눈 그룹과 easing을 재사용한다. 감고 뜨는 경계 보간은 편집값으로 기록하며 포즈 검출기가 눈꺼풀을 측정했다고 주장하지 않는다.
4. **Happened:** eyes scaley 키 추가 및 blink-timing.json 기록, exit 0.

## Entry 12 — 통합 빌드·렌더
1. **Read:** rigc build/render --help, AUTHORING §4.11, 수정된 after/rig.json·motion.json.
2. **Expect:** build 게이트 실패 0, after/render 313프레임, shins fold 0이며 치마에도 새 fold가 없어야 한다.
3. **Chose / turned down:** --copy-images로 독립 빌드를 만들고 --geometry --folds를 다시 읽는다. JSON 파일만 바꾸고 완료라 하지 않는다.
4. WTF?: build exit 1, `the triangles' outline is not one closed loop: the walk from vertex 0 closes after 64 of 126 boundary vertices`. 투명 삼각형만 지우면 두 섬이 되므로 하나의 mesh로 유효하지 않다. 렌더는 실행하지 않았다.

## Entry 13 — 다리 메시 분리 및 재빌드
1. **Read:** build 거부 메시지, AUTHORING §3.4 hull 및 §5.1: 외곽이 하나의 폐곡선이어야 하고 boundary vertices가 먼저 순서대로 와야 한다.
2. **Expect:** leg_r1·leg_l1 각각에 종속된 정강이를 두 mesh로 분리하면 두 외곽이 모두 유효해지고 fold 0이 된다.
3. **Chose / turned down:** 각 연결 성분의 경계 walk를 구하고 UV·weights·triangles를 함께 재번호화한다. 그림·좌표는 보존한다. 슬롯 수가 하나 늘어 meshSlots 예산도 12→13으로 명시하고 triangle 예산은 늘리지 않는다. 게이트 우회는 하지 않는다.
4. **Happened:** shins=142정점/218삼각형, shins_l=144정점/224삼각형로 분리한 뒤 build exit 0. build-report.json과 Spine/model/53페이지를 생성했다.

## Entry 14 — 수리 후 렌더
1. **Read:** Entry 13 build exit 0, render --help의 geometry·folds 출력.
2. **Expect:** 313프레임 렌더와 geometry/folds를 얻는다. 팔 이음새, 눈, 치마 변형을 화면으로 확인할 수 있다.
3. **Chose / turned down:** 이전과 같은 24fps·max480을 사용한다. 자동 viewport가 달라질 수 있으므로 전후 비교는 공통 좌표로 정렬한다.
4. **Happened:** render exit 0; 313프레임, 385×480. 13개 메시 모두 fold 0. 기존 shins의 216프레임 접힘이 사라졌다. 아직 자동 viewport 전후 차이를 정렬해야 한다.

## Entry 15 — 전후 영상·수치 검증
1. **Read:** 전후 frames.json·geometry.json·folds.json, after/contact-targets.json, 입력 데모 648×480·24fps.
2. **Expect:** 같은 월드 좌표/배율의 전후 비교 이미지와 왼쪽 원본|오른쪽 after 데모를 만들고 음악은 0초부터 붙인다. 지지 최소 바닥 오차는 0.01 단위 이하여야 한다.
3. **Chose / turned down:** before/after viewport 합집합으로 공통 화면을 만들고 결과를 직접 본다. 발 보정으로 몸통 바운스가 얼마나 줄었는지와 한쪽 발이 떠 있는 잔여 오차도 숨기지 않고 측정한다.
4. **Happened:** 313프레임 H.264/AAC 648×480, 24fps, 양 스트림 0초 시작, 13.041667초 확인. 지지 최소 바닥의 범위는 69.44468→0.000332 단위, 목표 최대 오차 0.000188. 반대 발 높이 차이는 최대 22.93355 남는다. f30에서 K0 원본 forearm의 가는 잔선이 몸 밖에 남아 추가 확인한다. 치마와 눈 변화는 f138·192에서 확인했다.

## Entry 16 — 팔의 실제 가림 확인
1. **Read:** compare-f030.png 및 K0_forearm_r.png. 원본 조각에 팔꿈치 아래 가는 잔선이 있고 혼합 세트에서 몸 밖으로 드러난다.
2. **Expect:** 등 뒤에서 완전히 가려져야 하는 forearm을 숨긴 렌더가 잔선을 없애고 상완 이음새는 유지한다.
3. **Chose / turned down:** --hide를 사용한 시험 렌더로 실제 가림을 먼저 확인한다. 픽셀을 다시 그리거나 팔 각도 제한을 넘겨 덮지 않는다.
4. WTF?: 숨기면 잔선은 사라지지만 팔꿈치의 둥근 소매까지 없어져 상완 끝이 뾰족하게 남는다. 시험안은 버린다. after 원본에는 hide를 적용하지 않았다.

## Entry 17 — 팔 가림 각도 조정·최종 렌더
1. **Read:** trial-hidden f30·60, K0_forearm_r.png의 잔선, K0 drawn/turn ±5°.
2. **Expect:** 팔꿈치를 보존한 채 아래팔을 허용 범위의 몸 안쪽 방향으로 옮기면 잔선 노출이 줄어든다. 다른 부위의 수치·fold는 유지된다.
3. **Chose / turned down:** f19–60 K0 아래팔을 drawn+5° 쪽으로 4프레임에 걸쳐 보정한다. 이는 가려진 손 위치에 대한 편집 선택이다. 조각 숨김과 각도 제한 확대는 버린다.
4. **Happened:** 최종 build/render 모두 exit 0, 313프레임에서 fold 0. f30·60을 직접 보니 팔꿈치는 남고 잔선은 몸 안에 가려졌다. ±5° 범위를 확대한 적 없다.

## Entry 18 — 최종 수치·데모 재생성
1. **Read:** 최종 렌더 f30·60, comparison-metrics, 실루엣 관측값. AUTHORING의 A39 deform winding 및 profile.
2. **Expect:** 최종 팔 각도가 K0 범위 내이고 치마의 정규화 폭 오차가 줄어든다. rig-play 프로파일도 실패 없이 통과해야 한다. 최종 데모가 이번 빌드 프레임으로 교체된다.
3. **Chose / turned down:** 최종 프레임으로 전후 증거·동영상을 재생성한다. 치마 폭 검사는 동일 실루엣 계측 기반의 보조 수치이며 독립된 품질 점수로 주장하지 않는다.
4. **Happened:** 치마 정규화 폭 MAE 0.113536→0.077282(31.93% 감소), K0 최대 |turn| 5.000177°(키 반올림 0.001° 이내), 눈 다섯 구간 scale 0.12 확인. rig-play는 30 measured/30 passed/0 failed/22 skipped이며 deform 313키·312보간 구간·32552삼각형을 측정하고 collapse 0이었다. 최종 데모 재생성도 exit 0.

## Entry 19 — 머리 증거 시트의 잘못된 추론 정정
1. **Read:** extract.py의 glob('head-*.png')가 head-reference.png까지 포함한다. 실제 head-053.png와 compare-f312.png는 모두 마지막 팔 든 자세다.
2. **Expect:** 숫자 파일만 모으면 정확히 53장(f0,6,…312)이 나온다.
3. **Chose / turned down:** Entry 4에서 영상/디코더 문제로 여긴 추론을 철회한다. 잘못된 정정도 지우지 않고 실제 원인과 함께 남긴다. 파일 선택 버그를 고친다.
4. **Happened:** 53개 숫자 파일만으로 head-exact.png를 다시 만들었다. 원본 마지막 프레임은 정상이며 입력 영상에 반복 프레임이 있다는 주장은 철회한다.

## Entry 20 — 보고·도구 피드백·기록 마무리
1. **Read:** findings, 최종 두 build reports, verification/comparison-metrics, 전후 이미지, journal과 transcript.
2. **Expect:** report.md·tools.md 및 재현 명령을 작성하고, 일지 항목/실패 수와 제출 파일을 기계적으로 재확인한다. usage는 정확한 세션 토큰 수가 없으므로 만들지 않는다.
3. **Chose / turned down:** 부분 개선과 새 그림 필요를 구분한다. 측정한 것만 수치로 쓰고, SKIP을 통과에 합치지 않는다. 문서에 실제 사용한 휴리스틱과 실패도 모두 남긴다.
4. **Happened:** 필수 파일·보고서 링크·일지 20항목/WTF 5항목·두 프로파일 실패 0을 다시 읽어 확인했다. 최종 영상 648×480/24fps/313프레임, 영상·음성 0초 시작도 재확인했다. usage.json은 만들지 않았다.

## At the end — 실제로 추정/선택한 값

- 눈 감기 진입/복귀 경계는 확대된 영상 표본 사이를 편집자가 보간했다. 눈꺼풀 landmark 원시 측정이 있으면 보간 선택을 대체할 수 있다. 최소 scale 0.12·easing은 입력 idle에서 왔다.
- 점프 창 f85–94·175–184·265–275는 화면 관찰로 지정했고, 상승량은 원본 발목값과 양 끝의 선형 지지 높이에서 계산했다. foot contact/발뒤꿈치·발끝 landmark가 있으면 양발 지지를 더 정확히 풀 수 있다.
- 첫 프레임의 낮은 신발 바닥 46.95875를 일정 바닥으로 선택했다. 물리적으로 보정된 카메라/바닥 평면은 입력에 없다.
- 치마 색 임계 68, 2/98% 분위수, ROI hip−40~+49(270×480 영상), 평활 5프레임, fade 프레임과 폭/전단 제한, 높이 제곱 falloff는 편집 휴리스틱이다. measurements-before.json·skirt-controls.json 및 mask 증거가 그 선택을 드러낸다. 독립된 실루엣 라벨과 천의 3D/깊이 데이터가 있으면 대체할 수 있다.
- f19–60의 K0 아래팔 가림 각도 drawn+5°와 4프레임 진입/이탈은 실제로 가려진 손 위치를 선택한 것이다. K0 turn 제한은 입력을 그대로 지켰다.

## At the end — 찾지 못한 것

- body-17에는 눈꺼풀, 손가락, 가려진 손의 깊이, 발바닥 접지 상태, 치마 외곽선이 없다.
- rigc render의 명시적인 고정 viewport 입력 옵션은 읽은 --help에 없었다. 제공된 viewport 메타데이터로 직접 공통 화면을 구성했다.
- 정강이의 독립 두 섬을 한 메시로 두는 것은 도구가 명시적으로 거부했다. 실패를 우회하지 않고 두 메시로 분리했다.
