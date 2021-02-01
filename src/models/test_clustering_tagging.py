import pytest
from src.models.predict_model import clustering


@pytest.mark.parametrize("dataset, cluster_names", [
    ("data/test/2020-09-27-aggmatrix.csv", ['few_cnxs', 'many_cnxs', 'long_duration', 'udp', 'anom'])
])
def test_clustering_tagging(dataset, cluster_names):
    df_data, df_centroids = clustering(dataset, kmeans_executions=50)
    #        in kmeans, initial centroids positions are random, so ^^^ greater kmeans_executions -> more reliable results

    assert list(df_centroids.sort_values('size', ascending=False).index) == cluster_names
    assert df_centroids['dst_ip']['many_cnxs'] > df_centroids['dst_ip']['few_cnxs']
    assert df_centroids['proto'].drop('anom').idxmax() == 'udp'
    assert df_centroids['size'].sum() == len(df_data)
