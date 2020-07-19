```python
nz = np.nonzero([0,0,1,2,4,1])
Z = np.eye(3)
print(Z)


np.random.seed(0)
Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
Zmin


Z = np.ones((5,5))
Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
print(Z)

Z = np.diag(np.arange(1,5), 1)

np.tile(np.array([[0,1],[0,1]]), (3,3))
Z = (Z-Z.mean())/np.std(Z)


Z = np.dot(np.ones((5,3)), np.ones((3,2)))
print(Z)

# Alternative solution, in Python 3.5 and above
Z = np.ones((5,3)) @ np.ones((3,2))
print(Z)

Z[(Z<8) & (Z>3)] *= -1

np.random.seed(0)
Z = np.random.randint(0,10,10)
2<<Z>>2

yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')

Z = np.arange('2016-07', '2016-08', dtype='datetime64[D]')

np.add(A,B,out=B)
np.divide(A,2,out=A)
np.negative(A,out=A)
np.multiply(A,B,out=A)

Z = np.linspace(0,1,11, endpoint = False)[1:]

Z = np.random.random(10)
Z.sort()



A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)

# Assuming identical shape of the arrays and a tolerance for the comparison of values
equal = np.allclose(A,B)
print(equal)

# Checking both the shape and the element values, no tolerance (values have to be exactly equal)
equal = np.array_equal(A,B)
print(equal)


Z = np.random.random((10,2))
X,Y = Z[:,0], Z[:,1]
R = np.sqrt(X**2+Y**2)
T = np.arctan2(Y,X)
print(R)
print(T)


np.argwhere(array == 1)

for index in np.ndindex(Z.shape):
    print(index, Z[index])


n = 10
p = 3
Z = np.zeros((n,n))
np.put(Z, np.random.choice(range(n*n), p, replace=False),1)
print(Z)

X = np.random.rand(5, 10)

# Recent versions of numpy
Y = X - X.mean(axis=1, keepdims=True)

# Older versions of numpy
Y = X - X.mean(axis=1).reshape(-1, 1)


Z = np.random.randint(0,10,(3,3))
print(Z)
print(Z[Z[:,1].argsort()])


Z = np.random.uniform(0,1,(3,3))
z = 0.5
m = Z.flat[np.abs(Z - z).argmin()]
print(m)

Z = np.random.randint(0,3,(3,10))
print((~Z.any(axis=0)).any())


# Author: Andreas Kouzelis
# NumPy >= 1.13
uZ = np.unique(Z, axis=0)
print(uZ)


np.add.accumulate([1,2,3]) #累加

np.multiply.accumulate([1,2,3,4])
np.multiply.at(x,[0,1,2],5)

>>> np.multiply.outer([1,2,3],[4,5,6])
array([[ 4,  5,  6],
       [ 8, 10, 12],
       [12, 15, 18]])

np.multiply.reduce([1,2,3,4])
24


Z = np.ones(10)
I = np.random.randint(0,len(Z),20)
Z += np.bincount(I, minlength=len(Z))
print(Z)

# Another solution
# Author: Bartosz Telenczuk
np.add.at(Z, I, 1)
print(Z)


C = np.bincount([1,1,2,3,4,4,6])
A = np.repeat(np.arange(len(C)), C)
print(A)

''https://blog.csdn.net/qq_37007384/article/details/88668729?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task''

max_5 = np.partition(Z, -5)[-5:]
Z[np.argpartition(-Z,5)[:5]]

uZ = np.unique(Z, axis=0)



X = np.random.randn(100) # random 1D array
N = 1000 # number of bootstrap samples
idx = np.random.randint(0, X.size, (N, X.size))
means = X[idx].mean(axis=1)
confint = np.percentile(means, [2.5, 97.5])
print(confint)


X = np.random.randn(3,3)
idx = np.random.randint(0, 3, (2,5))
idx
X[idx, idx]
```


5 Lasso三种求解方法：闭式解、LARS、CD （Least Angle Regression(LARS，最小角回归））
目前为止，已经介绍了Lasso的问题形式，以及与其相关的几个概念，但是都没有涉及到如何求解Lasso。Lasso的求解有很多方法，但是较为经典的则是利用LARS来求，当然另外一种经常使用的则是坐标下降法(Coordinate Descent, CD)。


6 ElasticNet解决Lasso存在的问题 & LARS-EN
前文说到，当d >> n的时候，Lasso最多只能选择出n个特征，其余特征的权值全为0，那么这不是我们想要的，因为很多情况下数据样本很少，但特征维度很多。

并且即便当d < n时，假设有几个特征高度相关，这种情况下，Lasso倾向于选择其中一个作为代表，而Ridge Regression会倾向于将权重均匀分配到这些相关特征上面。事实上，这种情况下，实验表明Ridge Regression的表现会比Lasso好很多。

所以，Lasso的使用场合还是比较适合于d < n，并且特征之间相关性很小的情况下。

那么为了综合Ridge Regression和Lasso的性质，又出现了ElasticNet，其优化目标为：

[公式]

即加入了L2和L1形式的正则化，由于L2正则化项的存在，即便在n << d的情况下，也可以选择多于n个特征。其求解过程也可以采用对LARS进行稍微修改得到，为什么呢？其实是因为，ElasticNet可以写成Lasso的形式。

一组人先在条件一(condition 1）完成，再在条件二（condition 2）完成
within-subject effect: paired t test  or    repeated measure ANOVA （condition>=3)
这里当然不能算有俩block，因为被试者不是被随机分配到人数相等的实验组里

“两组人在同一个条件下完成实验”这是个one way between-subject design。实验研究的是between-subject effect （组间差别）。就是你拿来给被试者分组的这个条件对实验结果有什么影响。比如说性别啊，受教育程度都是典型的组间因素。这里的分析方法是independent sample t-test 或者one way ANOVA.（分组>=3)。

如果实验条件有两个，或者两个层次呢，就会有两个组间差别(被试者分组条件+实验条件），用的方法也变为factorial ANOVA.其实还有一种情况你没有提到，就是Mixed design."两组人先在条件一完成，再在条件二完成” 这样的设计兼顾了组内和组间差别。统计方法是mixed ANOVA。


block越来越多，如果保持被试者数量不变的话，分配到每个block里的人数就越少。于是引入power analysis来计算在某种实验设计的前提下，要得到具有统计学意义（控制Type 2 error）的结果，需要的最小被试者人数(样本容量）是多少。


With a randomized block design, the experimenter divides subjects into subgroups called blocks, such that the variability within blocks is less than the variability between blocks. Then, subjects within each block are randomly assigned to treatment conditions. Compared to a completely randomized design, this design reduces variability within treatment conditions and potential confounding, producing a better estimate of treatment effects.

It is known that men and women are physiologically different and react differently to medication. This design ensures that each treatment condition has an equal proportion of men and women. As a result, differences between treatment conditions cannot be attributed to gender. This randomized block design removes gender as a potential source of variability and as a potential confounding variable.

nuisance factor: gender--> men and women are physiologically different and react differently to medication

http://www.cengage.com/resource_uploads/downloads/0495390879_94372.pdf



power analysis
http://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/BS704_Power/BS704_Power_print.html



Logistic  Regression Assumption:
1. The logistic regression assumes that there is minimal or no multi-collinearity among the independent variables.

2. The Logistic regression assumes that the independent variables are linearly related to the log of odds.

3. The logistic regression usually requires a large sample size to predict properly.

4. The Logistic regression which has two classes assumes that the dependent variable is binary and ordered logistic regression requires the dependent variable to be ordered, for example Too Little, About Right, Too Much.

5. The Logistic regression assumes the observations to be independent of each other.



non-parametric test:

这两种都是非参数检验non-parametric test，选择哪种主要看实验是否是独立的对象。如果是独立的对象（independent sample， or between-group），举个栗子，如果是两组，每组的对象都不同，则选用Mann Whitney U test 。

如果是同一组对象，例如测量同一组人不同时间的数据，则需要用wilcoxon signed-rank test

![non_parametric test](https://pic2.zhimg.com/v2-4b80dad4e155abc71c4b77d896860e81_b.jpg)

forward recurrence . rate of cost
http://www.columbia.edu/~ks20/stochastic-I/stochastic-I-RRT.pdf



bootstrap: 
However, in our real world, sometimes it’s hard to meet assumptions or theorem like above:
It’s hard to know the information about population, or it’s distribution.
The standard error of a estimate is hard to evaluate in general. Most of time, there is no a precise formula like standard error of sample mean. If now, we want to make a inference for the median of the smart phone pickups, what’s the standard error of sample median?


why bootstrap
Assume we want to estimate the standard error of our statistic to make an inference about population parameter, such as for constructing the corresponding confidence interval (just like what we have done before!). And:
1. We don’t know anything about population.
2. There is no precise formula for estimating the standard error of statistic.

The sample variance of these B statistic converges to the true variance of statistic M as B → ∞.

Using Empirical distribution function to approximate the distribution function of population, and applying Plug-in Principle to get an estimate for Var(M) — the Plug-in estimator.


Suppose we are interested in parameters of population. In statistic field , there is always a situation where parameters of interest is a function of the distribution function, these are called statistical functionals

It is called plug-in principle. Generally speaking, the plug-in principle is a method of estimation of statistical functionals from a population distribution by evaluating the same functionals, but with the empirical distribution which is based on the sample. This estimation is called a plug-in estimate for the population parameter of interest. For example, a median of a population distribution can be approximated by the median of the empirical distribution of a sample.

We don’t know the population P with CDF denoted as F, so bootstrap use Empirical distribution function(EDF) as estimate of F.
Using our existing sample data to form a EDF as a estimated population.
Applied the Plug-in Principle to make M=g(F) can be evaluate with EDF. Hence, M=g(F) becomes M_hat= g(F_hat), it’s the plugged-in estimator with EDF — F_hat.
Take simulation to approximate to the Var(M_hat).

Recall that to do the original version of simulation, we need to draw a sample data from population, obtain a statistic M=g(F) from it, and replicate the procedure B times, then get variance of these B statistic to approximate the true variance of statistic.
Therefore, to do simulation in step 4, we need to:
Draw a sample data from EDF.
Obtain a plug-in statistic M_hat= g(F_hat).
Replicate the two procedure B times.
Get the variance of these B statistic, to approximate the true variance of plug-in statistic.(It’s an easily confused part.)


We know EDF builds an CDF from existing sample data X1, …, Xn, and by definition it puts mass 1/n at each sample data point. Therefore, drawing an random sample from an EDF, can be seen as drawing n observations, with replacement, from our existing sample data X1, …, Xn. 

The variance of plug-in estimator M_hat=g(F_hat) is what the bootstrap simulation want to simulate.

 Therefore, drawing an random sample from an EDF, can be seen as drawing n observations, with replacement, from our existing sample data X1, …, Xn. So that’s why the bootstrap sample is sampled with replacement as shown before.

![error](https://miro.medium.com/max/1403/1*hwOJ8K1yQ-vnKTt-o5Bstg.png)


 From bootstrap variance estimation, we will get an estimate for Var(M_hat) — the plug-in estimate for Var(M). And the Law of Large Number tell us, if our simulation times B is large enough, the bootstrap variance estimation S², is a good approximate for Var(M_hat). Fortunately, we can get a larger B as we like with aid of a computer. So this simulation error can be small.

The Variance of M_hat, is the plug-in estimate for variance of M from true F. Is the Var(M_hat; F_hat) a good estimator for Var(M; F)? In other words, does a plug-in estimator approximate well to the estimator of interest ? That’s the key point what we really concern. In fact, the topic of asymptotic properties for plug-in estimators is classified in high level mathematical statistic. But let’s explain the main issues and ideas.

First, We know the empirical distribution will converges to true distribution function well if sample size is large, say F_hat → F.

Second, if F_hat → F, and if it’s corresponding statistical function g(.) is a smoothness conditions, then g(F_hat) → g(F). In our case, the statistical function g(.) is Variance, which satisfy the required continuity conditions. Therefore, that explains why the bootstrap variance is a good estimate of the true variance of the estimator M.

![bootstrap_error](https://miro.medium.com/max/1792/1*y42mIxqot08pZq8_ZoFiXw.png)



# multiple comparison
In statistics, the Bonferroni correction is one of several methods used to counteract the problem of multiple comparisons.
False discovery rate
Calculate p-values for each hypothesis test and order (smallest to largest, P(min)…….P(max))
For the ith ordered p-value check if the following is satisfied:
P(i) ≤ α × i/m



In statistics, family-wise error rate (FWER) is the probability of making one or more false discoveries, or type I errors when performing multiple hypotheses tests.

The FWER is the probability of making at least one type I error in the family,

Cauchy–Schwarz inequality:
https://en.wikipedia.org/wiki/Cauchy%E2%80%93Schwarz_inequality

Ridge: shrink the magnitude of coefficients fast
λ shows how much the cost of the βj parameter are inflated, controls the size of coefficients
and amount of regularization

LASSO: least absolute shrinkage and selection operator (model selection)

Compare mean and median, if mean = median, it's symmetric; if mean < median,
it's left skewed; if mean > median, it's right skewed ??? multi modal, one tail is long but the other is heavier


Check the distribution of CTR by country, if all of them are normal distributed, then
use chi-square test to check if these two countries have the same variance, then do
t-test with same variance/different variance.???



# Gaussian Process and Multivariate Gaussian
A multivariate normal distribution is a generalization of the one-dimensional
normal distribution to higher dimensions. A random vector is said to be k-variate
normally distributed if every linear combination of its k components has a
univariate normal distribution.


# AD metrics
Key metrics: revenue, MAU (month active advertiser), CPC/CPM (cost per click/ thousand
impression), CTR (click through rate), CVR (conversion rate), reach, ROAS (returns on ads spend)
• Funnel: impression – click – conversion – sale
• Cost type: by click, by impression, by conversion
• Second auction price bidding

# P Value
P value is the probability, computed assuming that null hypothesis is true, that the test statistic
would take a value as extreme or more extreme, in the direction of alternative hypothesis, than
that actually observed.

# Z score
Z score is the number of standard deviations from the mean a data point is (how many standard
deviation below or above the population mean).

Evaluation metrics: binary classification ( ROC curve, accuracy, recall, sensitivity,
specificity, confusion matrix), multi-classification (cross entropy - information gain
& gini impurity)

http://rasbt.github.io/mlxtend/user_guide/classifier/LogisticRegression/

https://blog.csdn.net/robert_chen1988/article/details/81253975

# sufficient statistic
In statistics, a statistic is sufficient with respect to a statistical model and its associated unknown parameter if "no other statistic that can be calculated from the same sample provides any additional information as to the value of the parameter".[1] In particular, a statistic is sufficient for a family of probability distributions if the sample from which it is calculated gives no additional information than does the statistic, as to which of those probability distributions is that of the population from which the sample was taken.

A sufficient statistic for a parameter is a statistic that captures all the information about theta in the sample. Any inference about theta depend on the sample only through the value of sufficent statistic
the conditional dist of sample X given T(X) independent of theta

# correlation coefficient
In statistics, Spearman's rank correlation coefficient or Spearman's ρ, named after Charles Spearman  is a nonparametric measure of rank correlation (statistical dependence between the rankings of two variables). It assesses how well the relationship between two variables can be described using a monotonic function.

The Spearman correlation between two variables is equal to the Pearson correlation between the rank values of those two variables; while Pearson's correlation assesses linear relationships, Spearman's correlation assesses monotonic relationships (whether linear or not). If there are no repeated data values, a perfect Spearman correlation of +1 or −1 occurs when each of the variables is a perfect monotone function of the other.

Spearman's coefficient is appropriate for both continuous and discrete ordinal variables.[1][2] Both Spearman's {\displaystyle \rho }\rho  and Kendall's {\displaystyle \tau }\tau  can be formulated as special cases of a more general correlation coefficient.

In statistics, the Kendall rank correlation coefficient, commonly referred to as Kendall's τ coefficient (after the Greek letter τ, tau), is a statistic used to measure the **ordinal association between two measured quantities**. A τ test is a non-parametric hypothesis test for statistical dependence based on the τ coefficient.

# sampling distribution
The sampling distribution of a statistic is the distribution of that statistic, considered as a random variable, when derived from a random sample of size {\displaystyle n}n. It may be considered as the distribution of the statistic for all possible samples from the same population of a given sample size. The sampling distribution depends on the underlying distribution of the population, the statistic being considered, the sampling procedure employed, and the sample size used. There is often considerable interest in whether the sampling distribution can be approximated by an asymptotic distribution, which corresponds to the limiting case either as the number of random samples of finite size, taken from an infinite population and used to produce the distribution, tends to infinity, or when just one equally-infinite-size "sample" is taken of that same population.



# ancova
ANCOVA by definition is a general linear model that includes both ANOVA (categorical) predictors and Regression (continuous) predictors. The simple linear regression model is:

