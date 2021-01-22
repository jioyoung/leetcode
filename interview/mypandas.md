# change col names

# rename two of the columns by using the 'rename' method
ufo.rename(columns={'Colors Reported':'Colors_Reported', 'Shape Reported':'Shape_Reported'}, inplace=True)
ufo.columns

# replace all of the column names by overwriting the 'columns' attribute
ufo_cols = ['city', 'colors reported', 'shape reported', 'state', 'time']
ufo.columns = ufo_cols
ufo.columns

# remove col

# remove multiple columns at once
ufo.drop(['City', 'State'], axis=1, inplace=True)
ufo.head()

# remove multiple rows at once (axis=0 refers to rows)
ufo.drop([0, 1], axis=0, inplace=True)
ufo.head()

# sort by col values
df.sort_values(['a', 'b'], ascending=[True, False])

# sort the 'title' Series in ascending order (returns a Series)
movies.title.sort_values().head()


# sort in descending order instead
movies.title.sort_values(ascending=False).head()

# sort the DataFrame first by 'content_rating', then by 'duration'
movies.sort_values(['content_rating', 'duration']).head()

# filter
movies[movies.duration >= 200]

# select the 'genre' Series from the filtered DataFrame
movies[movies.duration >= 200].genre

# or equivalently, use the 'loc' method
movies.loc[movies.duration >= 200, 'genre']
df2 = df[~(df.A > 0) | ~(df.B > 0)]


# CORRECT: use the '&' operator to specify that both conditions are required
movies[(movies.duration >=200) & (movies.genre == 'Drama')]

# INCORRECT: using the '|' operator would have shown movies that are either long or dramas (or both)
movies[(movies.duration >=200) | (movies.genre == 'Drama')].head()


# use the '|' operator to specify that a row can match any of the three criteria
movies[(movies.genre == 'Crime') | (movies.genre == 'Drama') | (movies.genre == 'Action')].head(10)

# or equivalently, use the 'isin' method
movies[movies.genre.isin(['Crime', 'Drama', 'Action'])].head(10)

# specify which columns to include by name
ufo = pd.read_csv('http://bit.ly/uforeports', usecols=['City', 'State'])

# or equivalently, specify columns by position
ufo = pd.read_csv('http://bit.ly/uforeports', usecols=[0, 4])
ufo.columns

# specify how many rows to read
ufo = pd.read_csv('http://bit.ly/uforeports', nrows=3)
ufo

# various methods are available to iterate through a DataFrame
for index, row in ufo.iterrows():
    print(index, row.City, row.State)


# only include numeric columns in the DataFrame
import numpy as np
drinks.select_dtypes(include=[np.number]).dtypes

# pass a list of data types to only describe certain types
drinks.describe(include=['object', 'float64'])
drinks.describe(include='all')


# calculate the mean of each numeric column
drinks.mean()

# or equivalently, specify the axis explicitly
drinks.mean(axis=0)


# calculate the mean of each row
drinks.mean(axis=1).head()



# string method 'contains' checks for a substring and returns a boolean Series
orders.item_name.str.contains('Chicken').head()

# use the boolean Series to filter the DataFrame
orders[orders.item_name.str.contains('Chicken')].head()


# string methods can be chained together
orders.choice_description.str.replace('[', '').str.replace(']', '').head()

# change the data type of an existing Series
drinks['beer_servings'] = drinks.beer_servings.astype(float)
drinks.dtypes
# alternatively, change the data type of a Series while reading in a file
drinks = pd.read_csv('http://bit.ly/drinksbycountry', dtype={'beer_servings':float})
drinks.dtypes

# multiple aggregation functions can be applied simultaneously
drinks.groupby('continent').beer_servings.agg(['count', 'mean', 'min', 'max'])

# allow plots to appear in the notebook
%matplotlib inline
# side-by-side bar plot of the DataFrame directly above
drinks.groupby('continent').mean().plot(kind='bar')


# compute a cross-tabulation of two Series
pd.crosstab(movies.genre, movies.content_rating)

# count how many times each value in the Series occurs
movies.genre.value_counts()

# display the unique values in the Series
movies.genre.unique()
movies.genre.nunique()

# count the number of missing values in each Series
ufo.isnull().sum()
notnull()


# use the 'isnull' Series method to filter the DataFrame rows
ufo[ufo.City.isnull()].head()


# if 'any' values are missing in a row, then drop that row
ufo.dropna(how='any')
# if 'all' values are missing in a row, then drop that row (none are dropped in this case)
ufo.dropna(how='all')

# if 'any' values are missing in a row (considering only 'City' and 'Shape Reported'), then drop that row
ufo.dropna(subset=['City', 'Shape Reported'], how='any')
# if 'all' values are missing in a row (considering only 'City' and 'Shape Reported'), then drop that row
ufo.dropna(subset=['City', 'Shape Reported'], how='all')

# explicitly include missing values
ufo['Shape Reported'].value_counts(dropna=False)

# fill in missing values with a specified value
ufo['Shape Reported'].fillna(value='VARIOUS', inplace=True)

# set an existing column as the index
drinks.set_index('country', inplace=True)
drinks.head()
# index name is optional
drinks.index.name = None
drinks.head()
# restore the index name, and move the index back to a column
drinks.index.name = 'country'
drinks.reset_index(inplace=True)
drinks.head()
# you can interact with any DataFrame using its index and columns
drinks.describe().loc['25%', 'beer_servings']

# elements in a Series can be selected by index (using bracket notation)
drinks.continent.value_counts()['Africa']

# any Series can be sorted by its values
drinks.continent.value_counts().sort_values()


# any Series can also be sorted by its index
drinks.continent.value_counts().sort_index()

# create a Series containing the population of two countries
people = pd.Series([3000000, 85000], index=['Albania', 'Andorra'], name='population')
people

# calculate the total annual beer servings for each country
(drinks.beer_servings * people).head()

# concatenate the 'drinks' DataFrame with the 'population' Series (aligns by the index)
pd.concat([drinks, people], axis=1).head()
pd.reset_index(drop=True, inplace=True)

# row 0, all columns
ufo.loc[0, :]
# rows 0 and 1 and 2, all columns
ufo.loc[[0, 1, 2], :]
# rows 0 through 2 (inclusive), all columns
ufo.loc[0:2, :]
# this implies "all columns", but explicitly stating "all columns" is better
ufo.loc[0:2]
# rows 0 through 2 (inclusive), column 'City'
ufo.loc[0:2, 'City']

# rows 0 through 2 (inclusive), columns 'City' and 'State'
ufo.loc[0:2, ['City', 'State']]
# rows 0 through 2 (inclusive), columns 'City' through 'State' (inclusive)
ufo.loc[0:2, 'City':'State']
# rows in which the 'City' is 'Oakland', column 'State'
ufo.loc[ufo.City=='Oakland', 'State']


# rows in positions 0 and 1, columns in positions 0 and 3
ufo.iloc[[0, 1], [0, 3]]

# rows in positions 0 through 2 (exclusive), columns in positions 0 through 4 (exclusive)
ufo.iloc[0:2, 0:4]


# fill missing values using "backward fill" strategy (doesn't affect the DataFrame since inplace=False)
ufo.fillna(method='bfill').tail()


# repeat this process for the 'country' Series
drinks['country'] = drinks.country.astype('category')
drinks.memory_usage(deep=True)


# strings are now encoded (0 means 'Africa', 1 means 'Asia', 2 means 'Europe', etc.)
drinks.continent.cat.codes.head()

# memory usage increased because we created 193 categories
drinks.country.cat.categories


# define a logical ordering for the categories
df['quality'] = df.quality.astype('category', categories=['good', 'very good', 'excellent'], ordered=True)
df.quality

# comparison operators work with ordered categories
df.loc[df.quality > 'good', :]


# use the 'random_state' parameter for reproducibility
ufo.sample(n=3, random_state=42)
# sample 75% of the DataFrame's rows without replacement
train = ufo.sample(frac=0.75, random_state=99)

# store the remaining 25% of the rows in another DataFrame
test = ufo.loc[~ufo.index.isin(train.index), :]

# create the 'Sex_male' dummy variable using the 'map' method
train['Sex_male'] = train.Sex.map({'female':0, 'male':1})
train.head()

# drop the first dummy variable ('female') using the 'iloc' method
pd.get_dummies(train.Sex).iloc[:, 1:].head()

# add a prefix to identify the source of the dummy variables
pd.get_dummies(train.Sex, prefix='Sex').iloc[:, 1:].head()

# save the DataFrame of dummy variables and concatenate them to the original DataFrame
embarked_dummies = pd.get_dummies(train.Embarked, prefix='Embarked').iloc[:, 1:]
train = pd.concat([train, embarked_dummies], axis=1)

# use the 'drop_first' parameter (new in pandas 0.18) to drop the first dummy variable for each feature
pd.get_dummies(train, columns=['Sex', 'Embarked'], drop_first=True).head()

# hour could be accessed using string slicing, but this approach breaks too easily
ufo.Time.str.slice(-5, -3).astype(int).head()


# convert 'Time' to datetime format
ufo['Time'] = pd.to_datetime(ufo.Time)
ufo.head()

# convenient Series attributes are now available
ufo.Time.dt.hour.head()
ufo.Time.dt.weekday_name.head()
ufo.Time.dt.dayofyear.head()

# compare a datetime Series with a timestamp
ufo.loc[ufo.Time >= ts, :].head()

# timedelta objects also have attributes you can access
(ufo.Time.max() - ufo.Time.min()).days


# count the duplicate items (True becomes 1, False becomes 0)
users.zip_code.duplicated().sum()

# count the duplicate rows
users.duplicated().sum()

# examine the duplicate rows (including all duplicates)
users.loc[users.duplicated(keep=False), :]

1. keep='first' (default): Mark duplicates as True except for the first occurrence.
2. keep='last': Mark duplicates as True except for the last occurrence.
3. keep=False: Mark all duplicates as True.


# drop the duplicate rows (inplace=False by default)
users.drop_duplicates(keep='first').shape

# replace the 'NOT RATED' values with 'NaN' (does not cause a SettingWithCopyWarning)
movies.loc[movies.content_rating=='NOT RATED', 'content_rating'] = np.nan


Solution: Any time you are attempting to create a DataFrame copy, use the copy method.
# explicitly create a copy of 'movies'
top_movies = movies.loc[movies.star_rating >= 9, :].copy()

# create a new Series using the Series constructor
s = pd.Series(['round', 'square'], index=['c', 'b'], name='shape')

# concatenate the DataFrame and the Series (use axis=1 to concatenate columns)
pd.concat([df, s], axis=1)


Goal: Map the existing values of a Series to a different set of values
Method: map (Series method)
train['Sex_num'] = train.Sex.map({'female':0, 'male':1})


Goal: Apply a function to each element in a Series
Method: apply (Series method)
Note: map can be substituted for apply in many cases, but apply is more flexible and thus is recommended
# calculate the length of each string in the 'Name' Series
train['Name_length'] = train.Name.apply(len)
train.loc[0:4, ['Name', 'Name_length']]

# round up each element in the 'Fare' Series to the next integer
import numpy as np
train['Fare_ceil'] = train.Fare.apply(np.ceil)

# alternatively, use a lambda function
train.Name.str.split(',').apply(lambda x: x[0]).head()

# define a function that returns an element from a list based on position
def get_element(my_list, position):
    return my_list[position]
train.Name.str.split(',').apply(get_element, position=0).head()

train.Name.str.split(',').head()

# apply the 'max' function along axis 0 to calculate the maximum value in each column
drinks.loc[:, 'beer_servings':'wine_servings'].apply(max, axis=0)

# use 'np.argmax' to calculate which column has the maximum value for each row
drinks.loc[:, 'beer_servings':'wine_servings'].apply(np.argmax, axis=1).head()


# overwrite the existing DataFrame columns
drinks.loc[:, 'beer_servings':'wine_servings'] = drinks.loc[:, 'beer_servings':'wine_servings'].applymap(float)



# What if the columns you want to join on don't have the same name?
movies.columns = ['m_id', 'title']

ratings.columns
Index(['user_id', 'movie_id', 'rating', 'timestamp'], dtype='object')
pd.merge(movies, ratings, left_on='m_id', right_on='movie_id').head()

movies = movies.set_index('m_id')
movies.head()
pd.merge(movies, ratings, left_index=True, right_on='movie_id').head()


pd.merge(A, B, how='inner')

inner: use intersection of keys from both frames, similar to a SQL inner join; preserve the order of the left keys
outer: use union of keys from both frames, similar to a SQL full outer join; sort keys lexicographically
left: use only keys from left frame, similar to a SQL left outer join; preserve key order
right: use only keys from right frame, similar to a SQL right outer join; preserve key order


df.groupby(['A'])['B','C'].apply(lambda x: x.nlargest(2, columns=['B'])
df.groupby(['A']).apply(lambda x: x.nlargest(2, 'B')[['B','C']]
df.groupby('State')['Population'].apply(lambda grp: grp.nlargest(2).sum())
g = df.groupby(['id']).apply(lambda x: x.nlargest(topk,['value'])).reset_index(drop=True)
df = df.set_index(['mainid','pidy']).groupby('pidx')['score'].nlargest(2).reset_index()
1st and second
select a1.equipment, highest_date, max(b.date) as second_highest_date
from
(
select equipment, max(date) as highest_date
from YOUR_TABLE as a
group by equipment
) a1
join YOUR_TABLE as b
on b.equipment = a1.equipment and b.date != a1.highest_date
group by a1.equipment, a1.highest_date


select pm.*
from (select pm.*,
             row_number() over (partition by project_id order by completed_date desc) as seqnum
      from project_milestone pm
      where pm.completed_date is not null
     ) pm
where seqnum = 2;

SELECT MAX( col )
  FROM table
 WHERE col < ( SELECT MAX( col )
                 FROM table )



SELECT t.id, t.rate, t.year, COUNT(l.rate) AS rank
FROM t
LEFT JOIN t AS l ON t.id = l.id AND t.rate < l.rate
GROUP BY t.id, t.rate, t.year
HAVING COUNT(l.rate) < 5
ORDER BY t.id, t.rate DESC, t.year

HAVING COUNT(DISTINCT l.rate) < 5 to get 8 rows:

get 5 rows:
ON t.id = l.id AND (t.rate < l.rate OR (t.rate = l.rate AND t.pri_key > l.pri_key))

%%timeit
d.groupby(
 'x'
 ).head(
 K
 ).reset_index(drop=True)

# top N per category
SELECT rs.Field1,rs.Field2 
    FROM (
        SELECT Field1,Field2, Rank() 
          over (Partition BY Section
                ORDER BY RankCriteria DESC ) AS Rank
        FROM table
        ) rs WHERE Rank <= 10

row_number() 是没有重复值的排序(即使两天记录相等也是不重复的)，可以利用它来实现分页
dense_rank() 是连续排序，两个第二名仍然跟着第三名
rank()       是跳跃拍学，两个第二名下来就是第四名


SELECT rs.Field1,rs.Field2 
FROM (
    SELECT Field1,Field2, ROW_NUMBER() 
      OVER (Partition BY Section
            ORDER BY RankCriteria DESC ) AS Rank
    FROM table
    ) rs WHERE Rank <= 10


select top 10 * from table where section=1
union
select top 10 * from table where section=2
union
select top 10 * from table where section=3


g = gapminder_2007.groupby(["continent"]).apply(lambda x: x.sort_values(["lifeExp"], ascending = False)).reset_index(drop=True)
# select top N rows within each continent
g.groupby('continent').head(1)

# 异方差的处理

## # Breusch-Pagan White: heteroskedasticity
It’s similar to the Breusch-Pagan test, but the White test allows the independent variable to have a nonlinear and interactive effect on the error variance.

1．使用“OLS + 稳健标准误” 
robust standard error 重新计算T统计量
2. 加权最小二乘法(WLS): 给予方差较小的观测值较大的权重，然后进行加权最小二乘法估计
3. 可行加权最小二乘法(FWLS)

a. 线性回归的参数估计是每一个观测值对应的预测变量和响应变量的某种方程的线性组
合。如果观测值对应的变动越大，则它在此线性组合中的权重也越大。所以参数估计基本
上都被少数几个高变动的观测决定了。这样建出来的模型一方面损失了原始数据中的信
息，一方面不稳定，因为模型是由高变动的观测决定的，做外部预测的时候结果也会变动
极大，预测值非常不准确。
b. 对方差的估计是有偏的。这个是很自然的错误，因为OLS假设方差恒定，估出来的方
差是一个数，而真实方差是变动的。所以方差估计不会跟真实值一样。
c. 参数估计是无偏但是低效的。
怎么检测同方差性假设是否成立？
画出残差与预测值的对比图（residuals vs predicted values）或者画出残差与时间的对比图（residuals
vs time）或者画出残差与预测变量的对比图（residuals
vs predictors）。如果残差随着预测值或者时间或者预测变量的增加而单调递增的话，那就说明同方差性被违背。

怎么解决违背同方差性时产生的问题呢？

a. 使用加权最小二乘法对变动比较小的观测值强行赋予较大的权重，增加它们在参数估计中所占的比重
b. 对那些高度扭曲（highly skewed）的数据，可以考虑使用log变换。
c. 我博士期间做的项目研究了如何对异方差数据进行分段，使得切分出的每一段都服从同方差性性质。然后对每一段再具体建模分析。





# autocorrelation
## 时间序列model
序列相关也称自相关，是指误差项之间不是完全相互独立的，而是存在相关性。序列相关分为两种，一种得正序列相关，一种是负序列相关。正序列相关中，正的误差项之后有较大概率仍是一个正的误差项，在负序列相关中，正的误差项之后有较大概率是一个负的误差项。

系数的标准误缩小，从而夸大了T统计量，使得第一类错误的可能性上升，即在原假设成立时错误的拒绝它，这会使得我们错误的把不显著的结果当成显著的。但系数本身的估计仍是可靠的。

a. 会低估参数的方差。这是因为我们知道参数的估计值可以看成是误差项的加权平均，独立误差的方差会比非独立的误差的方差小。

b. t统计量会变大，因为作为分母的方差项变小了。

c. 所以对应的t检测，即预测变量的系数等于0的检测就很容易被拒绝。于是推断出预测变量是统计意义上显著的。然而实际情况可能是这个预测变量并不显著，并不应该被用来解释响应变量。

d. 参数的估计虽然是无偏（unbiased）的但是是低效（inefficient）的因为参数估计的方差不是最小的。



a. 画残差的时间序列图（residual time series plot， residual
vs row number）或者自相关图（plot of residual autocorrelations ACF）。自相关图阐述了一个变量与其自身在不同时间点的观测的互相关关系。比如考虑滞后n天的自相关就是研究股票今天的价格和n天前的价格之间的相关关系。如果ACF图中的某些滞后对应的自相关超过了95%的置信区间，那么独立性假设就被违反了。

b. Durbin-Watson检验。这个检验只用于检查股票的滞后1天的自相关强度。其统计量大致等于2(1-a)，其中a是滞后1天的样本自相关强度。如果残差是独立的，那么统计量应该约等于2，所以如果对于一个50样本量的数据来说，此统计量超过1.4~2.6的范围，则认为独立性假设被违反了。

a. 有不是太明显的正的自相关，即Durbin-Watson统计量虽然不在1.4~2.6范围内，但是比1.4小的不多的情况下（比如1.3），那么我们可以对现有模型进行一些小幅度的调整。比如在使用线性回归之前，先对数据使用诸如ARIMA(p,d,q)模型进行拟合，对这个时间序列的残差再使用线性回归，然后再更新DW统计量。你可以考虑对所有的p<=5,d<=3,q<=5的组合都这么算一遍，找出使得更新了的DW统计量落在1.4~2.6的范围之间的(p,d,q)的组合。

b. 如果有明显的负的自相关，即DW统计量>2.6。说明我们可能对响应变量做了过度的差分处理（overdifferenced）。我们知道，过度的差分甚至于可以让本来毫不相关的数据变得有关联。这就迫使我们停下来想一想是不是有必要对变量做那么高阶的差分。

c. 如果有明显的季节性相关，比方对说包含每月观测值的数据可能以滞后12为间隔表现出相关性。那么一种办法是先以12为间隔进行差分，然后在对差分以后的数据使用线性回归。另一种办法是引入示性变量来显示当前的观测的月份。这个时候再调用线性回归就能自动在每年的一月份上加上一个调整参数，二月份上加上一个不同的调整参数，然后三月，四月，以此类推。这样就在一定程度上减轻了因为月份相同所带来的季节性相关性。

d. 如果有非常明显的正的自相关，即DW统计量<1.0，那你就应该很认真的在心里打起退堂鼓了，直接调用线性回归很可能就错大发了。这个时候你应该好好的再审视一下你的数据或者你的预处理的步骤，比方说你就应该再想想对变量该不该做差分，做几阶差分，或者该不该做log变换之类的问题。调整你的预处理策略再看看更新的DW统计量会不会变好。

处理：1)使用 Hansen-white标准误，对原来的标准误进行调整；2)进一步修正模型，将数据的时间序列性质纳入到模型中。

# Linearity
一种常用的判断线性性的方法是把残差（residual）作为y轴，拟合值（fitted value）作为x轴画一个残差图（residual
plot）。如果残差图的点以大致恒定的方差（constant variance）大致成对称的分布在x轴附近

a. 对响应变量或者预测变量或者对于两者同时使用合适的非线性变换（nonlinear transformation）。比如说，如果某个变量的值全部都是正的，可以考虑log变换（log
transformation），如果变量大于等于0，则可以考虑log+1变换（log+1
transformation）。举一个具体点的例子，在调查价格和需求的关系（price-demand）时，经常会发现预测变量的百分比变化会导致响应变量发生相应的百分比变化而且两个变化之间竟然是成近似正比的关系，这时对解释变量和预测变量同时使用log变化再对变化后的变量搞一个线性回归就很合理了。

b. 可以考虑造一些新的预测变量加入到数据中。使得新加入的变量与已有的预测变量x有某种非线性关系。比方说，加入x^2或者x^3或者甚至于更高阶的。但这个办法常常会引入过拟合（overfitting， 后面文章具体讲）的问题。

c. 还有种可能就是你在收集数据（data collection）的时候漏掉了很重要的预测变量。这些变量可能与响应变量有很大的关系，或者跟其他的预测变量的交互能够很好的解释响应变量。举一个简单的例子吧，金融机构里搞时间序列模型，经常会有这种情况，数据实际上是应该分成一段一段的，每一段上有一个明显的线性关系，但是把每一段全部合在一起看，并不存在一个简单的线性关系。那么很容易想象，如果我们能对数据进行正确的分段并且加入一个示性变量来表示观测值属于哪一段，那么最终得到的模型就是分段线性回归模型，此时的数据模拟与预测就是准确的了。当然，正如前面所说，随着新变量的加入，modeler需要时时关注过拟合的程度，找到一个好的平衡点。

# Normality
要求误差项来自正态分布。实际上这个假设并不是太重要，很多统计学的书籍和文章都不把它列作必须要检测的假设之一。原因是就算违背了正态性假设，通过OLS得到的参数估计也是无偏且有效的。只是因为p值（p-value）的计算涉及到误差的分布，所以不满足正态分布可能导致p值计算的不准确。然而当数据的样本量非常大时（>200），根据中心极限定理（central
limit theorem CLT）我们知道误差的分布可以近似看做正态分布而且不会有太大的问题，随着样本量不断增大，p值计算也会越来越精确，正态分布假设也就越来越不重要了。当然如果处理的是小数据的话，那么还是应该仔细考察一下正态分布是否满足。

怎么检测正态性满不满足？

a. 画正态分位数图（normal quantile plot）。这个图把我们所考察的变量的每一个分位数与正态分布的相应分位数进行对比。如果变量服从正态分布则，正态分位数图上的点应该大致呈一条对角线。如果偏离对角线越多，越说明变量不满足正态性。

b. 一些传统的统计测试，比如Kolmogorov-Smirnov 测试, the
Shapiro-Wilk 测试, the Jarque-Bera 测试, 以及Anderson-Darling
测试等等。大多数软件有直接现成的包可以调用，这里就不深入讲它们怎么实现的了，不然大家就会觉得比较无聊了。

怎么解决正态性不满足的问题？

a. 可以试试把各种变量做一下log 看看情况会不会变好

b. 可以想办法把数据进行分段，使得每一段上正态性得到满足。

# 合理的outlier
对合理的outlier，传统的处理方式是 OLS估计+Robust standard error（参考NW estimator），该方法的能重新估算相对准确的t value，方便其判断变量significant。 更好的方法是用robust regression，经典的如huber M estimator. 具体百度原论文咯！
 least absolute deviation


# Multilineality
Detecting Multicollinearity Using Variance Inflation Factors
## Reducing Structural Multicollinearity
The neat thing here is that we can reduce the multicollinearity in our data by doing what is known as "centering the predictors." Centering a predictor merely entails subtracting the mean of the predictor values in the data set from each predictor value. 

## Reducing Data-based Multicollinearity
As the example in the previous section illustrated, one way of reducing data-based multicollinearity is to remove one or more of the violating predictors from the regression model. Another way is to collect additional data under different experimental or observational conditions. We'll investigate this alternative method in this section.

# uncorrelated predictor
The estimated slope coefficients b1 and b2 are the same regardless of the model used.
The standard errors se(b1) and se(b2) don't change much at all from model to model.
The sum of squares SSR(x1) is the same as the sequential sum of squares SSR(x1|x2). The sum of squares SSR(x2) is the same as the sequential sum of squares SSR(x2|x1).

# SVM

SVM stands for support vector machine, it is a supervised machine learning algorithm which can be used for both Regression and Classification. If you have n features in your training data set, SVM tries to plot it
Follow Steve Nouri for more AI and Data science posts: https://lnkd.in/gZu463X
in n-dimensional space with the value of each feature being the value of a particular coordinate. SVM uses hyperplanes to separate out different classes based on the provided kernel function.

# decision tree

A decision tree is a supervised machine learning algorithm mainly used for Regression and Classification. It breaks down a data set into smaller and smaller subsets while at the same time an associated decision tree is incrementally developed. The final result is a tree with decision nodes and leaf nodes. A decision tree can handle both categorical and numerical data.
Q49.

## entropy
A decision tree is built top-down from a root node and involve partitioning of data into homogenious subsets. ID3 uses enteropy to check the homogeneity of a sample. If the sample is completely homogenious then entropy is zero and if the sample is an equally divided it has entropy of one.

## Information Gain
The Information Gain is based on the decrease in entropy after a dataset is split on an attribute. Constructing a decision tree is all about finding attributes that return the highest information gain.

# What is pruning in Decision Tree?
Pruning is a technique in machine learning and search algorithms that reduces the size of decision trees by removing sections of the tree that provide little power to classify instances. So, when we remove sub-nodes of a decision node, this process is called pruning or opposite process of splitting.

# What Are the Drawbacks of the Linear Model?
Some drawbacks of the linear model are:
• The assumption of linearity of the errors.
• It can’t be used for count outcomes or binary outcomes
• There are overfitting problems that it can’t solve

# K-means
within group sum of squares vs k
• The Graph is generally known as Elbow Curve.
• Red circled a point in above graph i.e. Number of Cluster =6 is the point after which you don’t see any decrement in WSS.
• This point is known as the bending point and taken as K in K – Means.

假设要将数据分到 [公式] 个 簇，选取的中心分别为 [公式] 。我们的代价函数就是要将每个特征与被分配到的簇的中心之间的距离和最小化（ 直观来说就是凑得近的分一起 ）。

[公式]

可以看出 代价函数 一方面取决于 [公式] 的分配，一方面取决于 簇 中心的位置。

k-means
https://zhuanlan.zhihu.com/p/39739841
下面我们先来看下 k-means 的算法，然后来解释它是如何优化 代价函数 的。

随机选择 [公式] 个 簇 的中心 [公式]
重复下面步骤直到收敛：
1. 对于每个 [公式] ，计算 [公式] （ [公式] 距离第 [公式] 个簇的中心最近，则 [公式] ）
2. 更新 [公式] （ 新 [公式] 为所有满足 [公式] 的 [公式] 的中心 ）
对于步骤 [公式] 来说，我们固定了 [公式] ，并为每个 [公式] 选取了距离最近的 簇，这使得 代价函数 减小。对于步骤 [公式] ，我们固定了 [公式] ，并将 [公式] 移动到了各个分类的中心，这也使得 代价函数 减小。因此随着不断循环这个过程，我们将得到一个最优解（ 也可能是局部最优 ）。

相关问题
k-means 算法挺好理解的，最后我们来说说簇中心的初始化与 [公式] 的选择问题。对于簇中心的初始化，一般直接随机选 [公式] 个数据为中心，选比如说 100 次并计算 代价函数 的值，选择其中最小的那一次的结果。
对于 [公式] 的选择，一方面可以运用 肘部法则，原理是 代价函数 一开始会随着 [公式] 的增大下降的很快，但过了某个值之后下降变缓，我们选择这个点的 [公式] 值。另一方面我们可以根据自己的业务需求来选择 [公式] （ 业务就是需要分为 [公式] 个类的情况 ）。


# What is Ensemble Learning?
Ensemble Learning is basically combining a diverse set of learners(Individual models) together to improvise on the stability and predictive power of the model.


# Boosting
Boosting is an iterative technique which adjusts the weight of an observation based on the last classification. If an observation was classified incorrectly, it tries to increase the weight of this observation and vice versa. Boosting in general decreases the bias error and builds strong predictive models. However, they may over fit on the training data.

# Bagging
Bagging tries to implement similar learners on small sample populations and then takes a mean of all the predictions. In generalised bagging, you can use different learners on different population. As you expect this helps us to reduce the variance error.


# How Do You Work Towards a Random Forest?
The underlying principle of this technique is that several weak learners combined to provide a keen learner. The steps involved are
• Build several decision trees on bootstrapped training samples of data
• On each tree, each time a split is considered, a random sample of mm predictors is chosen as split candidates, out of all pp predictors
• Rule of thumb: At each split m=p√m=p
• Predictions: At the majority rule

# CV on time series
In case of time series data, you should use techniques like forward=chaining — Where you will be model on past data then look at forward-facing data.
fold 1: training[1], test[2]
fold 1: training[1 2], test[3]
fold 1: training[1 2 3], test[4]
fold 1: training[1 2 3 4], test[5]

# box-cox
A Box-Cox transformation is a way to transform non-normal dependent variables into a normal shape. Normality is an important assumption for many statistical techniques, if your data isn’t normal, applying a Box-Cox means that you are able to run a broader number of tests. The Box-Cox transformation is named after statisticians George Box and Sir David Roxbee Cox who collaborated on a 1964 paper and developed the technique.

# numpy large data
1. Load the whole data in the Numpy array. Numpy array has a property to create a mapping of the complete data set, it doesn’t load complete data set in memory.
2. You can pass an index to Numpy array to get required data.


# How Are Weights Initialized in a Network?
There are two methods here: we can either initialize the weights to zero or assign them randomly.
Initializing all weights to 0: This makes your model similar to a linear model. All the neurons and every layer perform the same operation, giving the same output and making the deep net useless.
Initializing all weights randomly: Here, the weights are assigned randomly by initializing them very close to 0. It gives better accuracy to the model since every neuron performs different computations. This is the most commonly used method.

#  What Is the Cost Function?
Also referred to as “loss” or “error,” cost function is a measure to evaluate how good your model’s performance is. It’s used to compute the error of the output layer during backpropagation. We push that error backwards through the neural network and use that during the different training functions.
# What Are Hyperparameters?
With neural networks, you’re usually working with hyperparameters once the data is formatted correctly. A hyperparameter is a parameter whose value is set before the learning process begins. It determines how a network is trained and the structure of the network (such as the number of hidden units, the learning rate, epochs, etc.).

# What Is the Difference Between Epoch, Batch, and Iteration in Deep Learning?
• Epoch – Represents one iteration over the entire dataset (everything put into the training model).
• Batch – Refers to when we cannot pass the entire dataset into the neural network at once, so we divide the dataset into several batches.
Follow Steve Nouri for more AI and Data science posts: https://lnkd.in/gZu463X
• Iteration – if we have 10,000 images as data and a batch size of 200. then an epoch should run 50 iterations (10,000 divided by 50).


# What is the role of the Activation Function?
The Activation function is used to introduce non-linearity into the neural network helping it to learn more complex function. Without which the neural network would be only able to learn linear function which is a linear combination of its input data. An activation function is a function in an artificial neuron that delivers an output based on inputs.

# What are the variants of Back Propagation?
• Stochastic Gradient Descent: We use only a single training example for calculation of gradient and update parameters.
• Batch Gradient Descent: We calculate the gradient for the whole dataset and perform the update at each iteration.
• Mini-batch Gradient Descent: It’s one of the most popular optimization algorithms. It’s a variant of Stochastic Gradient Descent and here instead of single training example, mini-batch of samples is used.

# RNN
RNNs are a type of artificial neural networks designed to recognise the pattern from the sequence of data such as Time series, stock market and government agencies etc. To understand recurrent nets, first, you have to understand the basics of feedforward nets.
Both these networks RNN and feed-forward named after the way they channel information through a series of mathematical orations performed at the nodes of the network. One feeds information through straight(never touching the same node twice), while the other cycles it through a loop, and the latter are called recurrent.


Recurrent networks, on the other hand, take as their input, not just the current input example they see, but also the what they have perceived previously in time.
The decision a recurrent neural network reached at time t-1 affects the decision that it will reach one moment later at time t. So recurrent networks have two sources of input, the present and the recent past, which combine to determine how they respond to new data, much as we do in life.
The error they generate will return via backpropagation and be used to adjust their weights until error can’t go any lower. Remember, the purpose of recurrent nets is to accurately classify sequential input. We rely on the backpropagation of error and gradient descent to do so.


# How Does an LSTM Network Work?
Long-Short-Term Memory (LSTM) is a special kind of recurrent neural network capable of learning long-term dependencies, remembering information for long periods as its default behaviour. There are three steps in an LSTM network:
• Step 1: The network decides what to forget and what to remember.
• Step 2: It selectively updates cell state values.
• Step 3: The network decides what part of the current state makes it to the output.

# Explain the steps in making a decision tree.
 1. Take the entire data set as input 
 2. Calculate entropy of the target variable, as well as the predictor attributes 
 3. Calculate your information gain of all attributes (we gain information on sorting different objects from each other) 
 1. Choose the attribute with the highest information gain as the root node 
 2. Repeat the same procedure on every branch until the decision node of each branch is finalized 

1. Take the entire data set as input. 
2. 2. Look for a split that maximizes the separation of the classes. A split is any test that divides the data into two sets. 
3. 3. Apply the split to the input data (divide step). 
4. 4. Re-apply steps one and two to the divided data. 
5. 5. Stop when you meet any stopping criteria. 
6. 6. This step is called pruning. Clean up the tree if you went too far doing splits.


# random forest
A random forest is built up of a number of decision trees. If you split the data into different packages and make a decision tree in each of the different groups of data, the random forest brings all those trees together. Steps to build a random forest model: 1. Randomly select 'k' features from a total of'm' features where k << m 2. Among the 'k' features, calculate the node D using the best split point 3. Split the node into daughter nodes using the best split 4. Repeat steps two and three until leaf nodes are finalized 5. Build forest by repeating steps one to four for 'n' times to create 'n' number of trees


# How can you avoid the overfitting your model? 
Overfitting refers to a model that is only set for a very small amount of data and ignores the bigger picture. There are three main methods to avoid overfitting: 
1. Keep the model simple—take fewer variables into account, thereby removing some of the noise in the training data 
2. Use cross-validation techniques, such as k folds cross-validation 
3. Use regularization techniques,

# You are given a data set consisting of variables with more than 30 percent missing values. How will you deal with them? 
The following are ways to handle missing data values: If the data set is large, we can just simply remove the rows with missing data values. It is the quickest way; we use the rest of the data to predict the values. 

For smaller data sets, we can substitute missing values with the mean or average of the rest of the data using pandas data frame in python. There are different ways to do so, such as df.mean(), df.fillna(mean).

# What are dimensionality reduction and its benefits? 
Dimensionality reduction refers to the process of converting a data set with vast dimensions into data with fewer dimensions (fields) to convey similar information concisely. This reduction helps in compressing data and reducing storage space. It also reduces computation time as fewer dimensions lead to less computing. It removes redundant features; for example, there's no point in storing a value in two different units (meters and inches).

# How can outlier values be treated?
 You can drop outliers only if it is a garbage value. Example: height of an adult = abc ft. This cannot be true, as the height cannot be a string value. In this case, outliers can be removed. If the outliers have extreme values, they can be removed. For example, if all the data points are clustered between zero to 10, but one point lies at 100, then we can remove this point. If you cannot drop outliers, you can try the following: 
 • Try a different model. Data detected as outliers by linear models can be fit by nonlinear models. Therefore, be sure you are choosing the correct model. 
 • Try normalizing the data. This way, the extreme data points are pulled to a similar range.
• You can use algorithms that are less affected by outliers; an example would be random forests.

# Logistic regression 
is also known as the logit model. It is a technique used to forecast the binary outcome from a linear combination of predictor variables.

# Root cause analysis 
was initially developed to analyze industrial accidents but is now widely used in other areas. It is a problem-solving technique used for isolating the root causes of faults or problems. A factor is called a root cause if its deduction from the problem-fault-sequence averts the final undesirable event from recurring.

# bagging
Bagging is the aggregation of machine learning models trained on bootstrap samples (Bootstrap AGGregatING).

Assumptions:
average out biases
reduce variance

Bagging works because some underlying learning algorithms are unstable: slightly different inputs leads to very different outputs. If you can take advantage of this instability by running multiple instances, it can be shown that the reduced instability leads to lower error. If you want to understand why, the original bagging paper( http://www.springerlink.com/) has a section called "why bagging works"
Boosting works because of the focus on better defining the "decision edge". By re-weighting examples near the margin (the positive and negative examples) you get a reduced error (see http://citeseerx.ist.psu.edu/vie...)
Use the outputs of your models as inputs to a meta-model. 

## bootstrap
These are almost independent and identically distributed (iid) samples – in that there is low correlation between the samples and they are drawn from the same distribution. The process of bootstrapping is used to create these samples. This involves drawing samples with replacement from a dataset keeping in mind that if these samples are large enough, they will be representative of the dataset they are drawn from, under the assumption that the dataset they are being drawn from is also large enough to be representative of the population. Having a high number of observations in our dataset also means that the bootstrap samples are more likely to have low correlation between samples.

Bagging provides a good representation of the true population and so is most often used with models that have high variance (such as tree based models).

## boosting

Boosting algorithms is to try predictors sequentially, where each subsequent model attempts to fix the errors of its predecessor.

# GBDT
The difference lies in what it does with the underfitted values of its predecessor. Contrary to AdaBoost, which tweaks the instance weights at every interaction, this method tries to fit the new predictor to the residual errors made by the previous predictor.

The predictions made by this new model are combined with the predictions of the previous.

A new model is created using the errors calculated as target variable. Our objective is to find the best split to minimise the error.

# XGBoost
Extreme Gradient Boosting is an advanced implementation of the Gradient Boosting. This algorithm has high predictive power and is ten times faster than any other gradient boosting techniques. Moreover, includes a variety of regularisation which reduces overfitting and improves overall performance.
Advantages
Implements regularisation helping reduce overfit (GB does not have);
Implements parallel processing being much faster than GB;
Allows users to define custom optimisation objectives and evaluation criteria adding a whole new dimension to the model;
XGBoost has an in-built routine to handle missing values;
XGBoost makes splits up to the max_depth specified and then starts pruning the tree backwards and removes splits beyond which there is no positive gain;
XGBoost allows a user to run a cross-validation at each iteration of the boosting process and thus it is easy to get the exact optimum number of boosting iterations in a single run.
column subsampling

# linear regression assumpt
Linear Function: The mean of the response, E(Yi), at each set of values of the predictors, (x1i,x2i,...), is a Linear function of the predictors.
Independent: The errors, ϵi, are Independent.
Normally Distributed: The errors, ϵi, at each set of values of the predictors, (x1i,x2i,...), are Normally distributed.
Equal variances (denoted α2): The errors, ϵi, at each set of values of the predictors, (x1i,x2i,...), have Equal variances (denoted α2).

An equivalent way to think of the first (linearity) condition is that the mean of the error, ϵi, at each set of values of the predictors, (x1i,x2i,…), is zero

然宝:
Transforming the y values should be considered when non-normality and/or unequal variances are the problems with the model.

然宝:
Transforming the y values corrects problems with the error terms (and may help the non-linearity).
Transforming the x values primarily corrects the non-linearity

# polynomial regression
The fitted model is more reliable when it is built on a larger sample size n.
Do not extrapolate beyond the limits of your observed values, particularly when the polynomial function has a pronounced curve such that an extraploation produces meaningless results beyond the scope of the model.
Consider how large the size of the predictor(s) will be when incorporating higher degree terms as this may cause numerical overflow for the statistical software being used.
Do not go strictly by low p-values to incorporate a higher degree term, but rather just use these to support your model only if the resulting residual plots looks reasonable. This is an example of a situation where you need to determine "practical significance" versus "statistical significance".
In general, as is standard practice throughout regression modeling, your models should adhere to the hierarchy principle, which says that if your model includes Xh and Xh is shown to be a statistically significant predictor of Y, then your model should also include each Xj for all j<h, whether or not the coefficients for these lower-order terms are significant.

1. (Given a Dataset) Analyze this dataset and give me a model that can predict this response variable.
Problem Determination -> Data Cleaning -> Feature Engineering -> Modeling
Benchmark Models
Linear Regression (Ridge or Lasso) for regression
Logistic Regression for Classification
Advanced Models
Random Forest, Boosting Trees, and so on
Scikit-Learn, XGBoost, LightGBM, CatBoost
Determine if the problem is classification or regression
Plot and visualize the data.
Start by fitting a simple model (multivariate regression, logistic regression), do some feature engineering accordingly, and then try some complicated models. Always split the dataset into train, validation, test dataset and use cross validation to check their performance.
Favor simple models that run quickly and you can easily explain.
Mention cross validation as a means to evaluate the model.


# What are some ways I can make my model more robust to outliers?
We can have regularization such as L1 or L2 to reduce variance (increase bias).
Changes to the algorithm:
Use tree-based methods instead of regression methods as they are more resistant to outliers. For statistical tests, use non parametric tests instead of parametric ones.
Use robust error metrics such as MAE or Huber Loss instead of MSE.
Changes to the data:
Winsorizing the data
Transforming the data (e.g. log)
Remove them only if you’re certain they’re anomalies and not worth predicting

# What are some differences you would expect in a model that minimizes squared error, versus a model that minimizes absolute error? In which cases would each error metric be appropriate?
MSE is more strict to having outliers. MAE is more robust in that sense, but is harder to fit the model for because it cannot be numerically optimized. So when there are less variability in the model and the model is computationally easy to fit, we should use MAE, and if that’s not the case, we should use MSE.
MSE: easier to compute the gradient, MAE: linear programming needed to compute the gradient
MAE more robust to outliers. If the consequences of large errors are great, use MSE
MSE corresponds to maximizing likelihood of Gaussian random variables

# What error metric would you use to evaluate how good a binary classifier is? What if the classes are imbalanced? What if there are more than 2 groups?
Accuracy: proportion of instances you predict correctly.
Pros: intuitive, easy to explain
Cons: works poorly when the class labels are imbalanced and the signal from the data is weak
ROC curve and AUC: plot false-positive-rate (fpr) on the x axis and true-positive-rate (tpr) on the y axis for different threshold. Given a random positive instance and a random negative instance, the AUC is the probability that you can identify who's who.
Pros: Works well when testing the ability of distinguishing the two classes.
Cons: can’t interpret predictions as probabilities (because AUC is determined by rankings), so can’t explain the uncertainty of the model, and it doesn't work for multi-class case.
logloss/deviance/cross entropy:
Pros: error metric based on probabilities
Cons: very sensitive to false positives, negatives
When there are more than 2 groups, we can have k binary classifications and add them up for logloss. Some metrics like AUC is only applicable in the binary case.


# What are various ways to predict a binary response variable? Can you compare two of them and tell me when one would be more appropriate? What’s the difference between these? (SVM, Logistic Regression, Naive Bayes, Decision Tree, etc.)
Things to look at: N, P, linearly separable, features independent, likely to overfit, speed, performance, memory usage and so on.
Logistic Regression
features roughly linear, problem roughly linearly separable
robust to noise, use l1,l2 regularization for model selection, avoid overfitting
the output come as probabilities
efficient and the computation can be distributed
can be used as a baseline for other algorithms
(-) can hardly handle categorical features
SVM
with a nonlinear kernel, can deal with problems that are not linearly separable
(-) slow to train, for most industry scale applications, not really efficient
Naive Bayes
computationally efficient when P is large by alleviating the curse of dimensionality
works surprisingly well for some cases even if the condition doesn’t hold
with word frequencies as features, the independence assumption can be seen reasonable. So the algorithm can be used in text categorization
(-) conditional independence of every other feature should be met
Tree Ensembles
good for large N and large P, can deal with categorical features very well
non parametric, so no need to worry about outliers
GBT’s work better but the parameters are harder to tune
RF works out of the box, but usually performs worse than GBT
Deep Learning
works well for some classification tasks (e.g. image)
used to squeeze something out of the problem