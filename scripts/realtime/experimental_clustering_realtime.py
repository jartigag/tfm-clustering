#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df_data = pd.read_csv( open(sys.argv[1]) )
scaler = StandardScaler()
X = scaler.fit_transform(df_data.loc[:,df_data.columns!="src_ip"])

algo = KMeans(n_clusters=5, init='random', n_init=30)
# KMeans params:
#
# - init. {'k-means++', 'random', ndarray, callable}, default='k-means++'
#       Method for initialization:
#       'k-means++' : selects initial cluster centers for k-mean clustering in a smart way to speed up convergence. See section Notes in k_init for more details.
#       'random': choose n_clusters observations (rows) at random from data for the initial centroids.
#   ** "The k-means++ paper provides monte-carlo simulation results that show that k-means++ is both faster and provides a better performance, so there is no guarantee, but results may be better."
#
# - n_init. int, default=10
#       Number of time the k-means algorithm will be run with different centroid seeds. The final results will be the best output of n_init consecutive runs in terms of inertia.

clusters = algo.fit_predict(X)

centroids = scaler.inverse_transform(algo.cluster_centers_)
df_centroids = pd.DataFrame(centroids, columns=df_data.columns.drop('src_ip'))

df_data['cluster'] = pd.Series(algo.labels_)

# {
# print to csv:
df_data.to_csv(f"{sys.argv[1].strip('csv')}experimental.labeled.csv", index=False)

clustresum = f"{sys.argv[1].strip('csv')}experimental.clustresum.csv"
with open(clustresum, mode='a') as clustresumf:
    print("centroids:", file=clustresumf)
    df_centroids.round(2).to_csv(clustresumf, index_label="cluster")
    print(":", file=clustresumf)
    df_data.groupby('cluster').size().to_frame('size(%)').transform( lambda x: 100*x/sum(x) ).round(2).to_csv(clustresumf, index_label="cluster")
# }
