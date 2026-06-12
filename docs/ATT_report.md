Understanding Transfer Attacks

Transfer attacks are a way to create examples that can trick other models. This is done by using one model to create these examples and then seeing if they can fool models that we do not know about.

It is important to have transferability because in real life attackers usually do not have access to the model they are trying to trick.

Baseline Attacks Studied

The repository had the basic attacks:

* PGD

* MI-FGSM

* TI-FGSM

* SI-NI-FGSM

* MI-ADMIX-DI-TI

Each of these attacks uses different techniques like momentum, translation and scale to improve transferability.

Problem: Gradient Variance

When we try to optimize something the gradients can change a lot from one step to another.

These changing gradients can cause the fake examples to work on the model we used to create them and not on other models.

Proposed Solution: Gradient Variance Reduction

To make the gradients more stable we create copies of the fake image with some noise added.

We calculate the gradients for each of these images.

Then we average all the gradients before updating the image.

This gives us a stable direction to follow.

Expected Benefits

* Less noise in the gradients

* stable optimization

* Better transferability

* Less overfitting to the source model

Algorithm

For each step:

1. Create noisy copies of the fake image.

2. Calculate the gradients for each image.

3. Average all the gradients.

4. Normalize the averaged gradient.

5. Update the momentum.

6. Update the image.

7. Apply epsilon clipping.

Implementation

We changed the following file:

core/transfer_attack_core.py

We made the following changes:

* Added an attack called ATT

* Added the logic to reduce variance

* Updated the attack dispatcher

* Generated examples using the ATT attack

Results

The ATT attack worked successfully and created fake images.

These images were saved in:

generated_outputs/ArcFace/ATT/

The attack ran without any errors.

We added Gradient Variance Reduction, to the ATT attack. It worked well.
Input:
    Source image x
    Target embedding y
    Number of noisy samples K

Initialize:
    adv = x
    momentum = 0

For each iteration:

    avg_grad = 0

    Repeat K times:
        noisy_adv = adv + random_noise
        Compute gradient g on noisy_adv
        avg_grad += g

    avg_grad = avg_grad / K

    Normalize avg_grad

    momentum = momentum + avg_grad

    adv = adv + alpha * sign(momentum)

    Clip adv within epsilon-ball

Return adv
