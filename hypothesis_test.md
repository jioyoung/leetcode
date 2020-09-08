# Type I error
When we reject the null hypothesis when the null hypothesis is true.

# Type II error
When we fail to reject the null hypothesis when the null hypothesis is false.
The “reality”, or truth, about the null hypothesis is unknown and therefore we do not know if we have made the correct decision or if we committed an error. We can, however, define the likelihood of these events.

# Alpha $\alpha$
The probability of committing a Type I error. Also known as the significance level.

# Beta $\beta$
The probability of committing a Type II error.

# Power
Power is the probability the null hypothesis is rejected given that it is false (ie. 1- $\beta$)

$\alpha$ and $\beta$ are probabilities of committing an error so we want these values to be low. However, we cannot decrease both. As $alpha$ decreases, $\beta$ increases.

## Note! 
Type I error is also thought of as the event that we reject the null hypothesis GIVEN the null is true. In other words, Type I error is a conditional event and $\alpha$ is a conditional probability. The same idea applies to Type II error and $\beta$.

# Test statistic
The sample statistic one uses to either reject $H_0$ (and conclude $H_a$ ) or fail to reject $H_0$.

There are two methods to determine if we have enough evidence: the __rejection region__ method and the __p-value__ method.

# Critical values
The values that separate the rejection and non-rejection regions.
# Rejection region
The set of values for the test statistic that leads to rejection of $H_0$

# P-value
The p-value (or probability value) is the probability that the test statistic equals the observed value or a more extreme value under the assumption that the null hypothesis is true.

Recall that the P-value is a probability of obtaining a value of the test statistic or a more extreme value of the test statistic assuming that the null hypothesis is true.

# Left-tailed 
If $H_a$ is left-tailed, then the p-value is the probability the sample data produces a value equal to or less than the observed test statistic.
# Right-tailed
If $H_a$ is right-tailed, then the p-value is the probability the sample data produces a value equal to or greater than the observed test statistic.

# Two-tailed
If $H_a$ is two-tailed, then the p-value is two times the probability the sample data produces a value equal to or greater than the absolute value of the observed test statistic.

This makes for a confusion in terminology. $\alpha$ is the preset level of significance whereas the p-value is the observed level of significance. The p-value, in fact, is a summary statistic which translates the observed test statistic's value to a probability which is easy to interpret.

Both approaches will ensure the same conclusion and either one will work. However, using the p-value approach has the following advantages:

Using the rejection region approach, you need to check the table or software for the critical value every time you use a different $\alpha$ value.
In addition to just using it to reject or not reject $H_0$ by comparing p-value to $\alpha$ value, the p-value also gives us some idea of the strength of the evidence against $H_0$.


Z score: 1.96: 97.5%; 1.65: 95%; 1.28: 90%

The primary purpose of a **confidence interval** is to estimate some unknown parameter. A secondary use of confidence intervals is to support decisions in hypothesis testing, especially when the test is two-tailed. The essence of this method is to compare the hypothesized value to the confidence interval. If the hypothesized value falls within the interval, we fail to reject the null hypothesis. If the hypothesized value falls outside the interval, we reject the null hypothesis.