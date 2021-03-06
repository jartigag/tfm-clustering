#!/usr/bin/env python3
#
#usage: ./src/models/predict_model.py data/processed/FORTINET_FIREWALL.aggmatrix.csv
#exec time: 1s
#output example:
# $ head FORTINET_FIREWALL.aggmatrix.csv
# src_ip,dst_ip,proto,src_port,dst_port,anom_level,threat_level,max_prio,events,uniq_events,avg_duration,stdev_duration
# 10.132.44.51-red0,178,0,4102,2,0.12,0.00,4,10656,7,137.86,472.89
# 192.168.117.63-red1,150,0,2802,2,0.20,0.00,4,6536,7,148.42,308.92
# $ column -ts, FORTINET_FIREWALL.centroids.csv
#cluster        dst_ip  proto  src_port  dst_port  anom_level  threat_level  max_prio  count_events  avg_duration  stdev_duration  size  size(%)
#few_cnxs       55.9    0.01   1779.96   2.11      0.2         0.0           4.0       4152.83       64.34         998.82          2083  51.88
#many_cnxs      193.43  0.01   6356.54   2.87      0.1         0.0           3.98      26315.38      102.68        1348.81         1029  25.63
#long_duration  38.03   0.16   599.7     1.73      0.0         0.0           5.0       1204.69       330.53        1260.9          471   11.73
#udp            136.95  1.48   4170.53   4.27      0.11        0.0           3.99      12111.91      125.02        1789.91         430   10.71
#anom           3.0     0.0    3.0       1.5       0.0         0.0           5.0       1256.5        69041.3       57776.48        2     0.05

import sys
import pandas as pd
#from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
#from datetime import datetime


def clustering(dataset_file, kmeans_executions=30):
    """ Given processed data in a csv file (from data/processed),
        returns one dataframe with labeled data
        and another dataframe with centroids.
    """
    df_data = pd.read_csv(dataset_file)
    scaler = StandardScaler()
    X = scaler.fit_transform(df_data.loc[:, df_data.columns!="src_ip"])

    algo = KMeans(n_clusters=5, n_init=kmeans_executions)
    # KMeans params:
    #
    # - init. {'k-means++', 'random', ndarray, callable}, default='k-means++'
    #       Method for initialization:
    #       'k-means++' : selects initial cluster centers for k-mean clustering in a smart way to speed up convergence. See section Notes in k_init for more details.
    #       'random': choose n_clusters observations (rows) at random from data for the initial centroids.
    #   ** "The k-means++ paper provides monte-carlo simulation results that show that k-means++ is both faster and provides a better performance,
    #       so there is no guarantee, but results may be better."
    #
    # - n_init. int, default=10
    #       Number of time the k-means algorithm will be run with different centroid seeds. The final results will be
    #       the best output of n_init consecutive runs in terms of inertia.
    algo.fit_predict(X) # this returns the clusters

    #print("Silhouette Coefficient: %0.2f" % metrics.silhouette_score(X, algo.labels_))

    centroids = scaler.inverse_transform(algo.cluster_centers_)
    df_centroids = pd.DataFrame(centroids, columns=df_data.columns.drop('src_ip'))

    df_data['cluster'] = pd.Series(algo.labels_)
    # sort clusters by size (from biggest to smallest):
    df_centroids['size'] = df_data.groupby('cluster').size().to_frame('size').sort_values('size', ascending=False)

    # assign meaningful names to clusters (mapping based just on empirical observations):
    mapping_dict = {}

    # 1- the smallest cluster will always be named 'anom', so it isn't a candidate:
    anom_index = df_centroids['size'].idxmin()
    mapping_dict[anom_index] = "anom"
    df_candidate_centroids = df_centroids.drop(anom_index)

    # 2- assign udp cluster and remove it from candidates:
    udp_index = df_candidate_centroids['proto'].idxmax()
    mapping_dict[udp_index] = "udp"
    df_candidate_centroids.drop(udp_index, inplace=True)

    # 3- assign long_duration cluster and remove it from candidates:
    long_duration_index = df_candidate_centroids['avg_duration'].idxmax()
    mapping_dict[long_duration_index] = "long_duration"
    df_candidate_centroids.drop(long_duration_index, inplace=True)

    # 4- assign many_cnxs cluster and remove it from candidates:
    many_cnxs_index = df_candidate_centroids['dst_ip'].idxmax()
    mapping_dict[many_cnxs_index] = "many_cnxs"
    df_candidate_centroids.drop(many_cnxs_index, inplace=True)

    # 5- few_cnxs cluster is the one remaining:
    few_cnxs_index = df_candidate_centroids.iloc[0].name
    mapping_dict[few_cnxs_index] = "few_cnxs"

    # use the mapping_dict to replace cluster indices by meaningful names in every dataframe:
    df_centroids.rename(mapping_dict, inplace=True, axis='index')
    df_data['cluster'].replace(mapping_dict, inplace=True)

    return df_data, df_centroids


def print_dataframes(df_labeled_data, df_centroids, df_labeled_data_filename, df_centroids_filename):
    # express size in percents:
    df_centroids['size(%)'] = df_centroids['size'].transform(lambda x: 100*x/sum(x))

    # print all to csv files:
    df_labeled_data.to_csv(df_labeled_data_filename, index=False)
    df_centroids.sort_values('size(%)', ascending=False).round(2).to_csv(df_centroids_filename, index_label="cluster")


if __name__ == '__main__':

    dataset_filename = sys.argv[1]
    df_labeled_data, df_centroids = clustering(dataset_filename)

    # add tstamp
    #tstamp=int(datetime.timestamp(datetime.strptime(sys.argv[1][-22:-12], "%Y-%m-%d"))) # add tstamp as first column
    #df_data.insert(loc=0, column='tstamp', value=tstamp)
    #df_centroids.insert(loc=0, column='tstamp', value=tstamp)

    print_dataframes(df_labeled_data, df_centroids, dataset_filename)
