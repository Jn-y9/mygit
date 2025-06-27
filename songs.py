import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体字体
plt.rcParams['axes.unicode_minus'] = False    # 显示负号

# 加载数据
data = pd.read_csv('nigerian-songs.csv')

# 数据预处理
# 检查缺失值
print("缺失值情况：")
print(data.isnull().sum())

# 填补缺失值
# 对于数值型特征，使用中位数填补
numeric_features = ['length', 'popularity', 'danceability', 'acousticness', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'time_signature']
data[numeric_features] = data[numeric_features].fillna(data[numeric_features].median())

# 对于分类特征，使用众数填补
categorical_features = ['artist_top_genre']
data[categorical_features] = data[categorical_features].fillna(data[categorical_features].mode().iloc[0])

# 检查是否还有缺失值
print("\n处理后的缺失值情况：")
print(data.isnull().sum())

# 数据分析
# 统计描述
print("\n数据统计描述：")
print(data.describe())

# 特征分布
plt.figure(figsize=(15, 10))
for i, feature in enumerate(numeric_features):
    plt.subplot(4, 3, i + 1)
    sns.histplot(data[feature], kde=True)
    plt.title(feature)
plt.show()

# 相关性分析
plt.figure(figsize=(12, 8))
sns.heatmap(data[numeric_features].corr(), annot=True, cmap='coolwarm')
plt.title("特征相关性矩阵")
plt.show()

# 数据归一化
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data[numeric_features])

# K-Means 聚类
# 选择最佳的 K 值
inertia = []
silhouette_scores = []
K_range = range(2, 11)
for K in K_range:
    kmeans = KMeans(n_clusters=K, random_state=42)
    kmeans.fit(data_scaled)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(data_scaled, kmeans.labels_))


# 绘制轮廓系数图
plt.figure(figsize=(10, 5))
plt.plot(K_range, silhouette_scores, marker='o')
plt.xlabel('K')
plt.ylabel('Silhouette Score')
plt.title('轮廓系数图')
plt.show()

# 选择最佳 K 值
best_K = K_range[np.argmax(silhouette_scores)]
print(f"最佳 K 值：{best_K}")

# 使用最佳 K 值进行 K-Means 聚类
kmeans = KMeans(n_clusters=best_K, random_state=42)
data['cluster'] = kmeans.fit_predict(data_scaled)

# 聚类效果分析
print("\n聚类中心：")
print(kmeans.cluster_centers_)

# 聚类结果分布
plt.figure(figsize=(10, 6))
sns.countplot(x='cluster', data=data)
plt.title('聚类结果分布')
plt.show()

# 聚类结果与特征的关系
plt.figure(figsize=(15, 10))
for i, feature in enumerate(numeric_features):
    plt.subplot(4, 3, i + 1)
    sns.boxplot(x='cluster', y=feature, data=data)
    plt.title(feature)
plt.show()

# K-Means 初始值敏感性分析
# 使用不同的初始值进行聚类
inertia_random = []
for _ in range(10):
    kmeans_random = KMeans(n_clusters=best_K, random_state=None)
    kmeans_random.fit(data_scaled)
    inertia_random.append(kmeans_random.inertia_)

# 绘制不同初始值的惯性
plt.figure(figsize=(10, 5))
plt.plot(range(1, 11), inertia_random, marker='o')
plt.xlabel('随机初始值')
plt.ylabel('Inertia')
plt.title('K-Means 初始值敏感性分析')
plt.show()

# 数据归一化对 K-Means 的影响
# 使用 MinMaxScaler 进行归一化
minmax_scaler = MinMaxScaler()
data_minmax_scaled = minmax_scaler.fit_transform(data[numeric_features])

# 使用归一化后的数据进行 K-Means 聚类
kmeans_minmax = KMeans(n_clusters=best_K, random_state=42)
kmeans_minmax.fit(data_minmax_scaled)

# 比较归一化前后的轮廓系数
silhouette_score_original = silhouette_score(data_scaled, kmeans.labels_)
silhouette_score_minmax = silhouette_score(data_minmax_scaled, kmeans_minmax.labels_)

print(f"归一化前的轮廓系数：{silhouette_score_original}")
print(f"归一化后的轮廓系数：{silhouette_score_minmax}")

# 特征分析
# 计算每个特征在每个聚类中的均值
cluster_centers = pd.DataFrame(kmeans.cluster_centers_, columns=numeric_features)
print("\n每个聚类的特征均值：")
print(cluster_centers)

# 特征重要性分析（基于聚类中心的距离）
cluster_centers_minmax = pd.DataFrame(kmeans_minmax.cluster_centers_, columns=numeric_features)
print("\n归一化后的每个聚类的特征均值：")
print(cluster_centers_minmax)

