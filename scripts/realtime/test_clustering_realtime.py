import pytest
from clustering_realtime import clustering

@pytest.mark.parametrize("dataset, cluster_names", [
    ("datasets/2020-09-19-dataset.csv", ['few_cnxs', 'many_cnxs', 'udp', 'long_duration', 'anom']),
    ("datasets/2020-09-20-dataset.csv", ['few_cnxs', 'many_cnxs', 'udp', 'long_duration', 'anom']),
    ("datasets/2020-09-21-dataset.csv", ['few_cnxs', 'many_cnxs', 'long_duration', 'udp', 'anom']),
    ("datasets/2020-09-22-dataset.csv", ['many_cnxs', 'udp', 'few_cnxs', 'long_duration', 'anom']),
    ("datasets/2020-09-23-dataset.csv", ['many_cnxs', 'udp', 'few_cnxs', 'long_duration', 'anom']),
    ("datasets/2020-09-24-dataset.csv", ['many_cnxs', 'udp', 'few_cnxs', 'long_duration', 'anom']),
    ("datasets/2020-09-25-dataset.csv", ['many_cnxs', 'udp', 'long_duration', 'few_cnxs', 'anom']),
    ("datasets/2020-09-26-dataset.csv", ['few_cnxs', 'many_cnxs', 'long_duration', 'udp', 'anom']),
    ("datasets/2020-09-27-dataset.csv", ['few_cnxs', 'many_cnxs', 'long_duration', 'udp', 'anom'])
])
def test_clustering(dataset, cluster_names):
    df_data, df_centroids, df_clusters_sizes = clustering(dataset, kmeans_executions=50)
    #        in kmeans, initial centroids positions are random, so ^^^ greater kmeans_executions -> more reliable results
    assert list(df_clusters_sizes.index) == cluster_names
    assert df_centroids['dst_ip']['many_cnxs'] > df_centroids['dst_ip']['few_cnxs']
    assert df_centroids['proto'].drop('anom').idxmax() == 'udp'
