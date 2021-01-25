# Requires BigML Python bindings
#
# Install via: pip install bigml
#
# or clone it:
#   git clone https://github.com/bigmlcom/python.git
from bigml.cluster import Cluster
from bigml.api import BigML
# Downloads and generates a local version of the cluster, if it
# hasn't been downloaded previously.
cluster = Cluster('cluster/5ef23a10cb4f962b4a007ced',
                  api=BigML("jartigag",
                            "67c4ce22d5b1c3ec57d74d4bca5dcf217be34b61",
                            domain="bigml.io"))
# To predict centroids fill the desired input_data
# in next line. Numeric fields are compulsory.
input_data = {
    "max_prio": 1,
    "dst_port": 1,
    "anom_level": 1,
    "proto": 1,
    "src_port": 1,
    "src_ip": 1,
    "dst_ip": 1,
    "count_events": 1,
    "avg_duration": 1,
    "afterwork_sessions": 1,
    "night_sessions": 1,
    "work_sessions": 1,
    "stdev_duration": 1}
cluster.centroid(input_data)
# The result is a dict with three keys: distance, centroid_name and
# centroid_id
