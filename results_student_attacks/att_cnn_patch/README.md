# ATT_CNN_PATCH Student Contribution

This folder contains a verified student-contributed CNN-side ATT-inspired patch-masking variant evaluated on the same subset baseline setup used in this repository.

## Contributor
- **Name:** Pratyush Kumar
- **College:** KCC Institute of Technology and Management, A.K.T.U.

## Attack
- **Implementation name:** `ATT_CNN_PATCH`
- **Type:** ATT-inspired CNN gradient-shaping and stochastic patch-masking transfer attack

## Reference note
- **Inspiration source:** *Boosting the Transferability of Adversarial Attack on Vision Transformer with Adaptive Token Tuning* (NeurIPS 2024)

## Important note
This implementation should be treated as a CNN-side adaptation inspired by ATT, not as an official reproduction of the original ViT token-level ATT implementation. It is also separate from the existing `ATT_CNN` contribution: this variant uses gradient-variance-based modulation across iterations together with stochastic patch masking.

## Verified result on the provided subset
- **Overall breach rate:** `23.54%`
- **Mean impact:** `0.1476`
- **Dodging breach rate:** `28.75%`
- **Impersonation breach rate:** `18.33%`

## Comparison against current baseline
This verified result is above `TI_FGSM` and `PGD`, but below `MI_ADMIX_DI_TI`, `MI_FGSM`, and `SI_NI_FGSM` on the provided subset.
