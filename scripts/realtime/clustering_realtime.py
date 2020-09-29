#!/usr/bin/env python3
#
#usage: ./clustering_realtime.py /home/javi/clustering/2020-09-22-dataset.csv
#exec time: 7s
#output example:
# $ head 2020-09-22-dataset.labeled.csv
# src_ip,dst_ip,proto,src_port,dst_port,anom_level,threat_level,max_prio,count_events,avg_duration,stdev_duration,cluster
# 10.253.15.238,98,0,4624,3,0.03,0.0,4,13111,184.49,2563.48,1
# 172.24.82.135,293,1,3264,6,0.01,0.0,4,12951,321.74,710.02,0
#$ column -ts, 2020-09-19-dataset.clustresum.csv
#centroids:
#cluster            dst_ip  proto  src_port  dst_port  anom_level  threat_level  max_prio  count_events  avg_duration  stdev_duration
#0                  290.83  0.81   7035.31   4.86      0.08        0.0           3.99      24410.53      99.11         741.55
#1                  92.25   0.1    2051.89   2.25      0.18        0.0           4.0       4840.12       57.37         675.72
#2                  8.18    0.4    387.35    3.0       0.0         0.0           5.0       1045.94       357.9         872.4
#3                  21.0    2.0    980.0     1051.0    0.0         0.0           5.0       2319.0        48.32         102.88
#4                  37.71   0.26   613.76    2.15      0.1         0.0           4.5       3148.45       2587.11       10194.99
#size of clusters:
#cluster            size(%)
#0                  33.15
#1                  52.19
#2                  12.56
#3                  0.02
#4                  2.08

import sys
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def clustering(dataset_file, kmeans_executions=10):
    df_data = pd.read_csv(dataset_file)
    scaler = StandardScaler()
    X = scaler.fit_transform(df_data.loc[:,df_data.columns!="src_ip"])

    algo = KMeans(n_clusters=5, n_init=kmeans_executions)
    clusters = algo.fit_predict(X)

    centroids = scaler.inverse_transform(algo.cluster_centers_)
    df_centroids = pd.DataFrame(centroids, columns=df_data.columns.drop('src_ip'))

    df_data['cluster'] = pd.Series(algo.labels_)
    # sort clusters by size (from biggest to smallest):
    df_clusters_sizes = df_data.groupby('cluster').size().to_frame('size(%)').sort_values('size(%)',ascending=False)

    # assign meaningful names to clusters (mapping based just on empirical observations):
    mapping_dict = {}

    # 1- the smallest cluster will always be named 'anom', so it isn't a candidate:
    anom_index = df_clusters_sizes.iloc[-1].name
    mapping_dict[anom_index] = "anom"
    df_candidate_centroids = df_centroids.drop(anom_index)
    df_candidate_clusters = df_clusters_sizes.drop(anom_index)

    # 2- assign udp cluster and remove it from candidates:
    udp_index = df_candidate_centroids['proto'].idxmax()
    mapping_dict[udp_index] = "udp"
    df_candidate_centroids.drop(udp_index, inplace=True)
    df_candidate_clusters.drop(udp_index, inplace=True)

    # 3- assign long_duration cluster and remove it from candidates:
    long_duration_index = df_candidate_centroids['avg_duration'].idxmax()
    mapping_dict[long_duration_index] = "long_duration"
    df_candidate_centroids.drop(long_duration_index, inplace=True)
    df_candidate_clusters.drop(long_duration_index, inplace=True)

    # 4- assign many_cnxs cluster and remove it from candidates:
    many_cnxs_index = df_candidate_centroids['dst_ip'].idxmax()
    mapping_dict[many_cnxs_index] = "many_cnxs"
    df_candidate_centroids.drop(many_cnxs_index, inplace=True)
    df_candidate_clusters.drop(many_cnxs_index, inplace=True)

    # 5- few_cnxs cluster is the one remaining:
    few_cnxs_index = df_candidate_clusters.iloc[0].name
    mapping_dict[few_cnxs_index] = "few_cnxs"

    # use the mapping_dict to replace cluster indices by meaningful names in every dataframe:
    df_centroids.rename(mapping_dict, inplace=True, axis='index')
    df_clusters_sizes.rename(mapping_dict, inplace=True, axis='index')
    df_data['cluster'].replace(mapping_dict, inplace=True)

    return df_data, df_centroids, df_clusters_sizes

#TODO: print all in 12-column format:
#cluster            dst_ip   proto          src_port  dst_port  anom_level  threat_level  max_prio  count_events  avg_duration  stdev_duration   percent_size
#udp                136.95   1.48           4170.53   4.27      0.11        0.0           3.99      12111.91      125.02        1789.91          51.86
#few_cnxs           193.17   0.01           6341.14   2.87      0.1         0.0           3.98      26233.76      102.76        1350.78          25.65
#many_cnxs          55.76    0.01           1778.82   2.11      0.2         0.0           4.0       4150.86       64.22         997.16           11.73
#cat4               38.03    0.16           599.7     1.73      0.0         0.0           5.0       1204.69       330.53        1260.9           10.71
#anom               3.0      0.0            3.0       1.5       0.0         0.0           5.0       1256.5        69041.3       57776.48         0.05

if __name__ == '__main__':

    dataset_filename = sys.argv[1]
    df_data, df_centroids, df_clusters_sizes = clustering(dataset_filename)

    # express size in percents:
    df_clusters_sizes['size(%)'] = df_clusters_sizes['size(%)'].transform( lambda x: 100*x/sum(x) ).round(2)

    # {
    # print to csv:
    df_data.to_csv(f"{dataset_filename.strip('csv')}labeled.csv", index=False)

    clustresum = f"{dataset_filename.strip('csv')}clustresum.csv"
    with open(clustresum, mode='a') as clustresumf:
        print("centroids:", file=clustresumf)
        df_centroids.round(2).to_csv(clustresumf, index_label="cluster")
        print("size of clusters:", file=clustresumf)
        df_clusters_sizes.to_csv(clustresumf, index_label="cluster")
    # }
