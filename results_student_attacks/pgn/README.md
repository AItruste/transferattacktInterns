# PGN Student Contribution

This folder contains a student-contributed face-verification adaptation of the PGN attack integrated into the shared transfer-attack pipeline.

## Contributor
- **Name:** Chidroopa Kanaparthy
- **College:** Maharaja Agrasen Institute of Technology (MAIT)
- **GitHub:** https://github.com/Chidroopakanaparthy

## Attack
- **Implementation name:** `PGN`
- **Type:** Penalizing Gradient Norm based transfer attack

## Reference paper
- **Title:** *Boosting Adversarial Transferability by Achieving Flat Local Maxima*
- **Authors:** Yao Ge, Yao Xiao, Weijie Huang, Xiaosen Wang, Yong Liu, Bo Han, Jiang Bian, Chunhua Shen
- **Venue:** NeurIPS 2023
- **Paper:** https://proceedings.neurips.cc/paper_files/paper/2023/hash/fbfe5f1d5474d9f4e0992852a3c7e171-Abstract-Conference.html

## Important note
This repository stores the student-integrated CNN face-verification adaptation. The core PGN idea is preserved through neighbor sampling and the two-gradient local-maxima style update, while the loss is adapted to the shared embedding-space verification objective.

## Verification status
- Integrated into the shared repository for further evaluation and comparison.
- Full result claims should be interpreted only after stable subset-scale reruns in the shared pipeline.
