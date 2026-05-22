Repo orientation for coding agents

Purpose
- This repository is a standalone vanilla transfer-attack exercise for interns.
- It is not the FaceSM repo and should not be treated as a paper-reproduction branch.
- The goal is to add a new transfer attack and compare it against the existing vanilla baselines.

What is already implemented
- Baseline attacks in core/transfer_attack_core.py:
  - PGD
  - MI_FGSM
  - TI_FGSM
  - SI_NI_FGSM
  - MI_ADMIX_DI_TI
- Supported attacker models:
  - Facenet512
  - ArcFace
  - GhostFaceNet
  - VGG-Face
- Victim pool used for evaluation:
  - FaceNet
  - FaceNet512
  - ArcFace
  - GhostFaceNet
  - VGG-Face
  - IR152
- IR152 resources should be taken from the shared Drive folder, not from this repo.

Important exclusions
- Do not add FaceSM logic here.
- Do not add old RAP code from another branch.
- Do not add API-specific code paths.
- Keep this repo focused on vanilla baselines plus a newly implemented attack.

Key files
- README.md
  - High-level description of the assignment repo.
- docs/trackA_assignment.md
  - Main assignment instructions for interns.
- docs/subset_input_pairs.csv
  - Small subset that interns should use first.
- results_baseline/subset_attack_summary.csv
  - Current baseline leaderboard on the subset.
- results_baseline/subset_attack_summary_by_goal.csv
  - Baseline comparison split into impersonation and dodging.
- results_baseline/subset_attacker_victim_summary.csv
  - Baseline attacker-victim breakdown.
- results_baseline/subset_attack_eval_long.csv
  - Long-format evaluated baseline table.
- results_baseline/subset_raw_similarities_long.csv
  - Raw similarity values used to derive the subset baseline summaries.
- scripts/build_subset_baselines.py
  - Rebuilds subset baseline CSVs from the raw long similarity file.
- experiments/run_vanilla_subset_generation.py
  - Minimal baseline generator for adversarial examples on the subset.
- core/transfer_attack_core.py
  - Main baseline attack implementations and shared utilities.
- core/verification_thresholds.json
  - Dataset-specific thresholds for the victim models.
.

Current strongest vanilla baselines on the provided subset
- SI_NI_FGSM
- MI_FGSM

Evaluation rules
- Skip self-transfer pairs.
- If attacker is FaceNet512, also skip FaceNet as victim.
- Use the thresholds in core/verification_thresholds.json.

What a good contribution looks like
- Clean implementation of a newer attack from recent literature.
- Reproducible subset experiment.
- Clear comparison against the current baselines.
- Honest reporting of strengths, failures, and limitations.
