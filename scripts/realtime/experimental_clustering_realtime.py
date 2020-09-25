#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df_data = pd.read_csv( open(sys.argv[1]) )
scaler = StandardScaler()
X = scaler.fit_transform(df_data.loc[:,df_data.columns!="src_ip"])

algo = KMeans(n_clusters=5, init='k-means++', n_init=10)
clusters = algo.fit_predict(X)

centroids = scaler.inverse_transform(algo.cluster_centers_)
df_centroids = pd.DataFrame(centroids, columns=df_data.columns.drop('src_ip'))

df_data['cluster'] = pd.Series(algo.labels_)

# {
# print to csv:
df_data.to_csv(f"{sys.argv[1].strip('csv')}labeled.csv", index=False)

clustresum = f"{sys.argv[1].strip('csv')}clustresum.csv"
with open(clustresum, mode='a') as clustresumf:
    print("centroids:", file=clustresumf)
    df_centroids.round(2).to_csv(clustresumf, index_label="cluster")
    print(":", file=clustresumf)
    df_data.groupby('cluster').size().to_frame('size(%)').transform( lambda x: 100*x/sum(x) ).round(2).to_csv(clustresumf, index_label="cluster")
# }
