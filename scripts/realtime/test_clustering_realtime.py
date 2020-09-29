import pytest
from clustering_realtime import clustering

#TODO: deducir qué lista de nombres de clusters debería tener cada dataset
@pytest.mark.parametrize("dataset, cluster_names", [
    ("datasets/2020-09-19-dataset.csv", ['many_cnxs', 'few_cnxs', 'udp', 'cat4', 'anom']),
    #("datasets/2020-09-20-dataset.csv", ['many_cnxs', 'few_cnxs', 'udp', 'cat4', 'anom']),
    #("datasets/2020-09-21-dataset.csv", ['many_cnxs', 'few_cnxs', 'cat4', 'udp', 'anom']),
    #("datasets/2020-09-22-dataset.csv", ['many_cnxs', 'udp', 'few_cnxs', 'cat4', 'anom']),
    ("datasets/2020-09-23-dataset.csv", ['many_cnxs', 'udp', 'few_cnxs', 'cat4', 'anom']),
    ("datasets/2020-09-24-dataset.csv", ['many_cnxs', 'udp', 'few_cnxs', 'cat4', 'anom']),
    ("datasets/2020-09-25-dataset.csv", ['many_cnxs', 'udp', 'few_cnxs', 'cat4', 'anom']),
    ("datasets/2020-09-26-dataset.csv", ['many_cnxs', 'few_cnxs', 'cat4', 'udp', 'anom'])
    #("datasets/2020-09-27-dataset.csv", ['few_cnxs', 'many_cnxs', 'cat4', 'udp', 'anom']),
])
def test_clustering(dataset, cluster_names):
    df_data, df_centroids, df_clusters_sizes = clustering(dataset)
    assert list(df_clusters_sizes.cluster_names) == cluster_names
    #assert df_centroids['dst_ip']['many_cnxs'] > df_centroids['dst_ip']['few_cnxs']
    #assert df_centroids['proto'].idxmax() == 'udp' #TODO: re-think this assertion
