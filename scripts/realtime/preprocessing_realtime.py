#!/usr/bin/env python3
#
# for each src_ip, aggregate info and calc metrics from its session-features-vectors.
# when a src_ip has been reviewed, it can be excluded adding it to reviewed_ips.txt in a new line (format: "10.0.0.1: i checked it on 2020-10-22. it's from dev environment")
#
#usage: ./preprocessing_realtime.py /disco_grande/javi/clustering/2020-09-22-FORTINET_FW1_10.251.0.101.csv reviewed_ips.txt > /home/javi/clustering/2020-09-22-dataset.csv
#exec time: 3m25s laptop (intel core i5-8265U @ 1.60GHz), 4m7s probe (intel xeon gold 6126 @ 2.60GHz)
#output example:
# $ head 2020-09-22-dataset.csv
# src_ip,dst_ip,proto,src_port,dst_port,anom_level,threat_level,max_prio,count_events,avg_duration,stdev_duration
# 10.253.15.238,98,0,4624,3,0.03,0.00,4,13111,184.49,2563.48
# 172.24.82.135,293,1,3264,6,0.01,0.00,4,12951,321.74,710.02

import sys
from statistics import mean, stdev

raw_data = open(sys.argv[1])
with open(sys.argv[2]) as f:
    reviewed_list = [l.split(":")[0] for l in f.readlines() if l[0]!="#"]
data = {}

for line in raw_data:
    #example:
    # 1589212544,1589993516,172.28.0.83,52.177.165.30,tcp,57541,443,0.00,0.00,5,479
    r = line.rstrip().split(",")

    src_ip = r[2]

    if src_ip in reviewed_list: continue

    if src_ip not in data:
        # []: list. it's a mutable, or changeable, ordered sequence of elements. it preserves order, it admits duplicates
        # set(): it's an unordered collection of distinct hashable objects. it doesn't preserve order, it doesn't admit duplicates
        data[src_ip] = {
            'dst_ip': set(), 'proto': 0, 'src_port': set(), 'dst_port': set(),
            'anom_level': [], 'threat_level': [], 'max_prio': set(), 'count_events': [], 'duration': []
        }

    ### extract features:

    if r[3] not in data[src_ip]['dst_ip']: data[src_ip]['dst_ip'].add(        r[3] )
    # proto: 2 if src_ip has used tcp and udp, 1 if udp, 0 if tcp:
    if r[4]=="udp": data[src_ip]['proto'] = 2 if ( data[src_ip]['proto']==1 ) else 1
    if r[5] not in data[src_ip]['src_port']: data[src_ip]['src_port'].add(    r[5] )
    if r[6] not in data[src_ip]['dst_port']: data[src_ip]['dst_port'].add(    r[6] )
    data[src_ip]['anom_level'].append(                                  float(r[7]))
    data[src_ip]['threat_level'].append(                                float(r[8]))
    if r[9] not in data[src_ip]['max_prio']: data[src_ip]['max_prio'].add(int(r[9]))
    data[src_ip]['count_events'].append(                                 int(r[10]))
    data[src_ip]['duration'].append(                            int(r[0])-int(r[1]))

print("src_ip,dst_ip,proto,src_port,dst_port,anom_level,threat_level,max_prio,count_events,avg_duration,stdev_duration")
for d in data:
    print( "{},{},{},{},{},{:.2f},{:.2f},{},{},{:.2f},{:.2f}".format( d,
        len(data[d]['dst_ip']),data[d]['proto'],len(data[d]['src_port']),len(data[d]['dst_port']),
        mean(data[d]['anom_level']),mean(data[d]['threat_level']),min(data[d]['max_prio']),sum(data[d]['count_events']),
        mean(data[d]['duration']),stdev(data[d]['duration']) if len(data[d]['duration'])>1 else 0))
