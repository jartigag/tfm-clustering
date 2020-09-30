#dependencies: pip3 install pytest
#
#usage:
#$ pytest -v
#============================================= test session starts =============================================
#platform linux -- Python 3.7.3, pytest-6.1.0, py-1.9.0, pluggy-0.13.1 -- /usr/bin/python3
#cachedir: .pytest_cache
#rootdir: /home/javi/g/tfm/scripts/realtime
#plugins: remotedata-0.3.1, arraydiff-0.3, doctestplus-0.2.0, openfiles-0.3.2
#collected 9 items
#
#test_clustering_realtime.py::test_clustering[datasets/2020-09-19-dataset.csv-cluster_names0] PASSED     [ 11%]
#test_clustering_realtime.py::test_clustering[datasets/2020-09-20-dataset.csv-cluster_names1] PASSED     [ 22%]
#test_clustering_realtime.py::test_clustering[datasets/2020-09-21-dataset.csv-cluster_names2] PASSED     [ 33%]
#test_clustering_realtime.py::test_clustering[datasets/2020-09-22-dataset.csv-cluster_names3] PASSED     [ 44%]
#test_clustering_realtime.py::test_clustering[datasets/2020-09-23-dataset.csv-cluster_names4] PASSED     [ 55%]
#test_clustering_realtime.py::test_clustering[datasets/2020-09-24-dataset.csv-cluster_names5] PASSED     [ 66%]
#test_clustering_realtime.py::test_clustering[datasets/2020-09-25-dataset.csv-cluster_names6] PASSED     [ 77%]
#test_clustering_realtime.py::test_clustering[datasets/2020-09-26-dataset.csv-cluster_names7] PASSED     [ 88%]
#test_clustering_realtime.py::test_clustering[datasets/2020-09-27-dataset.csv-cluster_names8] PASSED     [100%]
#
#============================================== 9 passed in 6.38s ==============================================

import pytest
from clustering_realtime import clustering

@pytest.mark.parametrize("dataset, cluster_names", [
    ("datasets/2020-09-19-dataset.csv", ['few_cnxs', 'many_cnxs', 'udp', 'long_duration', 'anom']),
    ("datasets/2020-09-20-dataset.csv", ['few_cnxs', 'many_cnxs', 'udp', 'long_duration', 'anom']),
    ("datasets/2020-09-21-dataset.csv", ['many_cnxs', 'udp', 'few_cnxs', 'anom', 'long_duration']),
    ("datasets/2020-09-22-dataset.csv", ['many_cnxs', 'udp', 'few_cnxs', 'long_duration', 'anom']),
    ("datasets/2020-09-23-dataset.csv", ['many_cnxs', 'udp', 'few_cnxs', 'long_duration', 'anom']),
    ("datasets/2020-09-24-dataset.csv", ['many_cnxs', 'udp', 'few_cnxs', 'long_duration', 'anom']),
    ("datasets/2020-09-25-dataset.csv", ['many_cnxs', 'udp', 'long_duration', 'few_cnxs', 'anom']),
    ("datasets/2020-09-26-dataset.csv", ['few_cnxs', 'many_cnxs', 'long_duration', 'udp', 'anom']),
    ("datasets/2020-09-27-dataset.csv", ['few_cnxs', 'many_cnxs', 'long_duration', 'udp', 'anom'])
])
def test_clustering(dataset, cluster_names):
    df_data, df_centroids = clustering(dataset, kmeans_executions=50)
    #        in kmeans, initial centroids positions are random, so ^^^ greater kmeans_executions -> more reliable results

    assert list(df_centroids.sort_values('size',ascending=False).index) == cluster_names
    assert df_centroids['dst_ip']['many_cnxs'] > df_centroids['dst_ip']['few_cnxs']
    assert df_centroids['proto'].drop('anom').idxmax() == 'udp'
    assert df_centroids['size'].sum() == len(df_data)
