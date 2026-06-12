# ATT Attack with Gradient Variance Reduction

## Objective

The goal of this assignment was to study transfer attacks for face verification systems and implement an improvement to the ATT (Adaptive Transfer Attack) framework.

The proposed improvement is Gradient Variance Reduction (GVR), which aims to stabilize gradients during iterative adversarial optimization and improve transferability across victim models.

---

## Understanding Transfer Attacks

A transfer attack generates adversarial examples using a source model and then evaluates whether those examples can successfully fool unseen victim models.

Good transferability is important because in real-world black-box scenarios the attacker usually does not have access to the victim model.

---

## Baseline Attacks Studied

The repository contained the following baseline attacks:

* PGD
* MI-FGSM
* TI-FGSM
* SI-NI-FGSM
* MI-ADMIX-DI-TI

Each attack improves transferability using different techniques such as momentum, translation invariance, scale invariance, input diversity, and admixing.

---

## Problem: Gradient Variance

During iterative optimization, gradients can fluctuate significantly from one iteration to another.

These unstable gradients may cause perturbations to overfit the source model and reduce their effectiveness against unseen victim models.

---

## Proposed Solution: Gradient Variance Reduction

To reduce gradient instability, multiple noisy copies of the current adversarial image are created.

Gradients are computed for each noisy sample.

The gradients are averaged before updating the adversarial image.

This produces a more stable optimization direction.

### Expected Benefits

* Reduced gradient noise
* Better optimization stability
* Improved transferability
* Reduced source-model overfitting

---

## Algorithm

For each iteration:

1. Generate K noisy copies of the adversarial image.
2. Compute gradients for each noisy sample.
3. Average all gradients.
4. Normalize the averaged gradient.
5. Update momentum.
6. Update adversarial image.
7. Apply epsilon clipping.

---

## Implementation

Modified file:

* core/transfer_attack_core.py

Changes made:

* Added ATT attack entry
* Added gradient variance reduction logic
* Updated attack dispatcher
* Generated ATT adversarial examples

---

## Results

The ATT implementation successfully generated adversarial images.

Output images were produced under:

generated_outputs/ArcFace/ATT/

The attack executed successfully without runtime errors.

---

## Conclusion

Gradient Variance Reduction was integrated into ATT
