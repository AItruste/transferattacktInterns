# MIG Student Contribution

This folder contains a verified student-contributed attack adaptation evaluated on the same subset baseline setup used in this repository.

## Contributor
- **Name:** Lakshita Sharma
- **College:** Bhagwan Parshuram Institute of Technology
- **GitHub:** https://github.com/slakshita04
- **Email:** slakshita04@gmail.com

## Attack
- **Implementation name:** `MIG`
- **Type:** Momentum integrated-gradient based transfer attack

## Reference paper
- **Title:** *Transferable Adversarial Attack for Both Vision Transformers and Convolutional Networks via Momentum Integrated Gradients*
- **Authors:** Wenshuo Ma, Yidong Li, Xiaofeng Jia, Wei Xu
- **Venue:** ICCV 2023
- **Paper:** https://openaccess.thecvf.com/content/ICCV2023/html/Ma_Transferable_Adversarial_Attack_for_Both_Vision_Transformers_and_Convolutional_Networks_ICCV_2023_paper.html
- **Reference implementation:** https://github.com/Trustworthy-AI-Group/TransferAttack

## Important note
The implementation in this repository adapts MIG to the face-verification setting by replacing the classification-logit objective with the embedding cosine-similarity attack loss used by the shared pipeline. The baseline image is represented as black in the repository's normalized `[-1, 1]` input space.

## Verified result on the provided subset
- **Overall breach rate:** `33.54%`
- **Mean impact:** `0.1946`
- **Dodging breach rate:** `43.75%`
- **Impersonation breach rate:** `23.33%`

## Comparison against current baseline
Compared with the current official vanilla baseline in this repo, `MIG` outperformed all five vanilla attacks on the shared subset and ranked below the strongest verified student-contributed attacks such as `DPA_HMA`, `BSR`, and `LI_BOOST_MI` under the same evaluation setup.
