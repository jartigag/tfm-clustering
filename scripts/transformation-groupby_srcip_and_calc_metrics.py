#!/usr/bin/env python3
#
#usage: ./transformation-groupby_srcip_and_calc_metrics.py dataset_raw/*18may > data.18may
#
#performance example:
# dataset_raw/*18may:                      65MB
# time ./transform*.py dataset_raw/*18may:  12s
#                        1M lines input -> 4837 lines output

import csv
import sys
from statistics import mean, stdev
import numpy as np

f = open(sys.argv[1])
raw_data = list( csv.reader(f, delimiter=" ") )

data = {}

def active_hours_vector(tstamps, breaks=24):
    vector, bin_edges = np.histogram( np.array(tstamps), bins=breaks )
    return ";".join([str(i) for i in vector])

###
# 1. aggregate:
###

for r in raw_data[1:]: # no header
    src_ip = r[0]

    if src_ip not in data:
        # []: list. it's a mutable, or changeable, ordered sequence of elements. it preserves order, it admits duplicates
        # set(): it's an unordered collection of distinct hashable objects. it doesn't preserve order, it doesn't admit duplicates
        data[src_ip] = {
            'dst_ip': set(), 'proto': set(), 'src_port': set(), 'dst_port': set(),
            'anom_level': [], 'threat_level': [], 'max_prio': set(), 'count_events': [],
            'duration': [], 'end_tstamps': []
        }

    if r[1] not in data[src_ip]['dst_ip']: data[src_ip]['dst_ip'].add(         r[1] )
    if r[2] not in data[src_ip]['proto']: data[src_ip]['proto'].add(           r[2] )
    if r[3] not in data[src_ip]['src_port']: data[src_ip]['src_port'].add(     r[3] )
    if r[4] not in data[src_ip]['dst_port']: data[src_ip]['dst_port'].add(     r[4] )
    data[src_ip]['anom_level'].append(                                   float(r[5]))
    data[src_ip]['threat_level'].append(                                 float(r[6]))
    if r[7] not in data[src_ip]['max_prio']: data[src_ip]['max_prio'].add( int(r[7]))
    data[src_ip]['count_events'].append(                                   int(r[8]))
    data[src_ip]['duration'].append(                                      int(r[10]))
    data[src_ip]['end_tstamps'].append(                                    int(r[9]))

###
# 2. calculate:
###

print("src_ip,dst_ip,proto,src_port,dst_port,anom_level,threat_level,max_prio,count_events,avg_duration,stdev_duration,active_hours_vector")
for d in data:

    print( "{},{},{},{},{},{:.2f},{:.2f},{},{},{:.2f},{:.2f},{}".format( d,
        len(data[d]['dst_ip']),len(data[d]['proto']),len(data[d]['src_port']),len(data[d]['dst_port']),
        mean(data[d]['anom_level']),mean(data[d]['threat_level']),min(data[d]['max_prio']),sum(data[d]['count_events']),
        mean(data[d]['duration']),
        stdev(data[d]['duration']) if len(data[d]['duration'])>1 else 0,
        active_hours_vector(data[d]['end_tstamps'])
    ) )
