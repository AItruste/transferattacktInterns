

Existing transfer attacks often overfit to the surrogate model.

As a result, adversarial perturbations generated on one model
do not transfer effectively to unseen models.

Vision Transformers are particularly vulnerable to this issue
because some tokens dominate the gradient optimization process.


   DEFINITION OF ATT 
  ATT is a momentum-based iterative adversarial attack that improves transferability by identifying important image patches, reducing gradient variance, preserving useful feature gradients instead of removing them, and weakening overly dominant transformer attention gradients during backpropagation. This helps generate perturbations that generalize better to unseen models.
