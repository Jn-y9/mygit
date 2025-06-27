# 尼日利亚歌曲聚类分析

本项目旨在对尼日利亚歌曲数据进行聚类分析，识别不同类型歌曲的特征模式。我们将使用K-Means聚类算法，并分析不同特征对聚类结果的影响。

## 数据预处理

首先，我们对数据进行了预处理，包括填补缺失值和数据归一化。

### 缺失值处理

- 对数值型特征使用中位数填补缺失值。
- 对分类特征使用众数填补缺失值。

### 数据描述

处理后的数据包含以下字段：

- `length`: 歌曲长度
- `popularity`: 歌曲流行度
- `danceability`: 舞蹈性
- `acousticness`: 声学性
- `energy`: 能量
- `instrumentalness`: 器乐性
- `liveness`: 现场感
- `loudness`: 响度
- `speechiness`: 语音性
- `tempo`: 节奏
- `time_signature`: 拍号

## 数据分析

### 特征分布

我们对各个特征进行了分布分析，生成了直方图和核密度估计图。

[特征分布]
![Figure_1](https://github.com/user-attachments/assets/94744901-d82a-4afc-9bd9-1e156523ecc0)

从图中可以看出，大多数特征如`length`、`popularity`、`danceability`等呈现出正态分布或近似正态分布，而`energy`、`instrumentalness`等特征则表现出较大的偏态分布。

### 特征相关性

通过热图展示了特征之间的相关性矩阵。

[特征相关性]
![Figure_2](https://github.com/user-attachments/assets/bc1f353a-f1e6-4a60-b80e-3c3f83c3556b)

从图中可以看出，`energy`和`loudness`之间存在较强的正相关性（0.73），而`acousticness`和`energy`之间存在较强的负相关性（-0.29）。这些相关性信息可以帮助我们理解特征之间的关系，并在后续分析中进行特征选择。

### 轮廓系数

通过轮廓系数图选择最佳的聚类数（K值）。

[轮廓系数图]
![Figure_3](https://github.com/user-attachments/assets/958dcfaa-c8ce-4c63-8ecd-bfdffebabbea)

从图中可以看出，当K值为7时，轮廓系数达到最大值0.14，因此我们选择K=7作为最佳聚类数。

### 聚类结果分布

展示了不同聚类的分布情况。

[聚类结果分布]
![Figure_4](https://github.com/user-attachments/assets/beb540c0-8f06-4d24-8833-0ee6cbbb765f)

从图中可以看出，聚类结果分布较为均匀，其中第3类聚类的数量最多，接近250个样本。

### 聚类结果与特征的关系

展示了每个特征在不同聚类中的箱线图。

[聚类结果与特征的关系]
![Figure_5](https://github.com/user-attachments/assets/8a8247f4-c599-4b31-ae24-7781834d4693)

从图中可以看出，不同聚类在各个特征上的分布存在显著差异。例如，第3类聚类在`danceability`和`energy`上表现出较高的值，而第4类聚类在`acousticness`上表现出较高的值。

### K-Means 初始值敏感性分析

分析了K-Means算法对初始值的敏感性。

[K-Means 初始值敏感性分析]
![Figure_6](https://github.com/user-attachments/assets/5f81215f-7283-4b5a-b6e8-b1946fd8c7ba)

从图中可以看出，K-Means算法对初始值有一定的敏感性，特别是在随机初始值6时，惯性值显著增加。这表明初始值的选择可能会影响聚类结果的稳定性。

### 数据归一化对 K-Means 的影响

比较了数据归一化前后的轮廓系数，分析了归一化对聚类结果的影响。

- 归一化前的轮廓系数：0.125
- 归一化后的轮廓系数：0.130

从轮廓系数的比较可以看出，归一化后聚类效果略有提升，说明归一化对K-Means聚类结果有一定的影响。

## 特征分析

### 每个聚类的特征均值

计算了每个聚类的特征均值，展示了不同聚类的特征模式。

[每个聚类的特征均值]
![image](https://github.com/user-attachments/assets/54b0c0d2-bc38-448d-9687-267c57e5dccf)

从图中可以看出，不同聚类在各个特征上的均值存在显著差异。例如，第3类聚类在`danceability`和`energy`上表现出较高的均值，而第4类聚类在`acousticness`上表现出较高的均值。

### 归一化后的每个聚类的特征均值

展示了归一化后每个聚类的特征均值。

[归一化后的每个聚类的特征均值]
![image](https://github.com/user-attachments/assets/6c8d33c3-1794-4ccf-a7a4-2043ab1930ec)

从图中可以看出，归一化后不同聚类在各个特征上的均值分布更加均匀，有助于更好地理解不同聚类的特征模式。

## 总结

通过对尼日利亚歌曲数据的聚类分析，我们识别了不同类型歌曲的特征模式，并分析了不同特征对聚类结果的影响。K-Means聚类算法在本项目中表现出了良好的聚类效果。我们还发现K-Means算法对初始值有一定的敏感性，归一化可以提升聚类效果。通过分析不同聚类的特征均值，我们可以更好地理解不同类型歌曲的特征模式。
