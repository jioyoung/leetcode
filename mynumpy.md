
a.shape = 2,2
a = linspace(0, 2*pi, 21, endpoint = True)

mask = b >= 0
plot(a[mask], b[mask], 'ro')

plt.plot(x, sin(x), 
    x, sin(2 * x))


size(a)
a.size

a.fill(-4.8)
a
array([-4, -4, -4, -4])
但是与列表不同，数组中要求所有元素的 dtype 是一样的，如果传入参数的类型与数组类型不一样，需要按照已有的类型进行转换。


对于二维数组，可以传入两个数字来索引：

a[1, 3]
numpy切片在内存中使用的是引用机制。list不会这样
a = array([0,1,2,3,4])
b = a[2:4].copy()
b[0] = 10
a

mask = array([0,1,1,0,0,1,0,0],
            dtype=bool)

a[mask]
mask 必须是布尔数组。

a[3:, [0,2,5]]

a[(0,1,2,3,4), (1,2,3,4,5)]
mask = array([1,0,1,0,0,1],
            dtype=bool)
a[mask, 2]
与切片不同，花式索引返回的是原对象的一个复制而不是引用。

只给定行索引的时候，返回整行：

y = a[:3]
y

condition = array([0,1,1,0,1],
                 dtype=bool)
a[condition]

a.astype(float64)
astype 方法返回一个新数组：
astype也不会改变原来数组的值：
另外，astype 总是返回原来数组的一份复制，即使转换的类型是相同的：


asarray 不会修改原来数组的值：


array([ 1.5, -3. ], dtype=float32)
但当类型相同的时候，asarray 并不会产生新的对象，而是使用同一个引用：

b = asarray(a, dtype=float32)
sum(a, axis=-1) 
sum(a, axis=1)
sum(a) a.sum() a.sum(axis=0) a.sum(axis=-1)
a.prod()


全局最小：
a.min()

沿着某个轴的最小：
a.min(axis=0)
array([ 0.296,  0.06 ,  0.345,  0.02 ])

全局最大：
a.max()

沿着某个轴的最大：
a.max(axis=-1)

a.round(decimals=1)

ptp 方法
计算最大值和最小值之差：
a.ptp(axis=1)
a.ptp()

将数值限制在某个范围：
array([[1, 2, 3],
       [4, 5, 6]])
a.clip(3,5)
a.std(axis=1)
a.var(axis=1, ddof = 1)

a.mean()
a.mean(axis=-1)
average(a, axis = 0, weights=[1,2])

a.argmin(axis=0)
a.argmin()

sort(weights)
array([ 20.8,  53.4,  61.8,  93.2])
sort 返回的结果是从小到大排列的。

argsort 返回从小到大的排列在数组中的索引位置：
weights[ordered_indices]

data = array([20.8,  93.2,  53.4,  61.8])
data.argsort()


但是 sort方法会改变数组的值：
data.sort()
对于多维数组，sort方法默认沿着最后一维开始排序：
对于二维数组，默认相当于对每一行进行排序：

searchsorted 接受两个参数，其中，第一个必需是已排序的数组。
返回这两个值对应的插入位置：
low_idx, high_idx = searchsorted(data, bounds)
利用插入位置，将数组中所有在这两个值之间的值提取出来：



将形状修改为2乘3：
a.shape = 2,3
array([[0, 1, 2],
       [3, 4, 5]])
与之对应的方法是 reshape ，但它不会修改原来数组的值，而是返回一个新的数组：
a.reshape(3,2)


转置只是交换了轴的位置。
另一方面，转置返回的是对原数组的另一种view，所以改变转置会改变原来数组的值。


atleast_xd 函数
保证数组至少有 x 维：
a = array([1,2,3])
b = atleast_2d(a)
b.shape (1L, 3L)


除此之外，还可以使用 ravel 方法，ravel 使用高效的表示方式：
a = array([[0,1],
           [2,3]])
b = a.ravel()
b
array([0, 1, 2, 3])
修改 b 会改变 a ：


Flatten 数组
flatten 方法的作用是将多维数组转化为1维数组：

In [32]:
a = array([[0,1],
           [2,3]])
b = a.flatten()
b
Out[32]:
array([0, 1, 2, 3])
返回的是数组的复制，因此，改变 b 并不会影响 a 的值：

In [33]:
b[0] = 10
print b
print a


还可以使用数组自带的 flat 属性：
a.flat
a.flat 相当于返回了所有元组组成的一个迭代器：
b = a.flat
b[0]
但此时修改 b 的值会影响 a ：

z = concatenate((x,y), axis=1)
vstack((x,y))
hstack((x,y))
dstack((x,y))
z = concatenate((x,y))


除此之外，还可以使用 ravel 方法，ravel 使用高效的表示方式：
a = array([[0,1],
           [2,3]])
b = a.ravel()
b
array([0, 1, 2, 3])
修改 b 会改变 a 

a.diagonal(offset=1)

a.any(axis=None)
a.all()

a.argmax(axis=None)
a.argmin(axis=None)

a.nonzero()

想要找出 nan 值需要使用 isnan：
np.isnan(b)

nan 与任何数进行比较都是 False：
b == np.nan


np.isinf(1.0)

hypot 返回对应点 (x,y) 到原点的距离。
x = np.array([1,2,3])
y = np.array([4,5,6])
np.hypot(x,y)