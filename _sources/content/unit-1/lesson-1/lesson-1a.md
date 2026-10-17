# 1A: Models, data and error

## A model is a rule with adjustable parts

Suppose you record the hours a student studies ($x$) and their test score ($y$). A very simple model proposes that the score rises steadily with study time:

$$
\hat{y} = w x + b
$$

Here $w$ (the slope) and $b$ (the intercept) are the **parameters**. Changing them changes the line. *Learning* means choosing parameters that make the line match the data well.

![Scatter plot of study hours against test score with a straight line fitted through the points](../unit-1-images/ml-fit-example.png)

## Measuring how wrong a model is

For each data point, the **error** is the gap between the true value and the model's prediction. Squaring the gaps and averaging them gives the **mean squared error** (MSE):

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} \left( y_i - \hat{y}_i \right)^2
$$

A smaller MSE means a better fit. Fitting the model means finding the $w$ and $b$ that make the MSE as small as possible.

```{admonition} Check your understanding
:class: tip
If you doubled every parameter in the model, would the MSE necessarily get better, worse or stay the same? Write down your prediction before moving on to 1B.
```

## Where next?

In **1B** you will fit this model with a few lines of Python and see the error for yourself.
