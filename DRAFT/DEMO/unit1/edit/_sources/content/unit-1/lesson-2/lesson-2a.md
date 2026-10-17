# 2A: Why we hold data back

## Training data and test data

When we fit a model we use some of the data to **train** it. We keep the rest, the **test set**, locked away until the end. The test score tells us how the model is likely to behave on new data.

```{code-block} python
:linenos:
import numpy as np

rng = np.random.default_rng(0)
indices = rng.permutation(100)
train_idx, test_idx = indices[:80], indices[80:]
print(len(train_idx), len(test_idx))
```

## Reflect

```{admonition} Reflect
:class: note
Think of a time you prepared for an exam by memorising past papers. How did that help, and where did it fall short? Post a short reflection in the unit discussion forum.
```
