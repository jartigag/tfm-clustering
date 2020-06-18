#!/usr/bin/env python3
#
#usage: ./preprocess_clustering_dataset.py rawdata_7days
#exec time: 56s
#output:
#$ wc -l dataset_for_clustering.*
#   2884 dataset_for_clustering.19may
#   4837 dataset_for_clustering.20may
#   4802 dataset_for_clustering.21may
#   4883 dataset_for_clustering.22may
#   4876 dataset_for_clustering.23may
#   4671 dataset_for_clustering.24may
#   2931 dataset_for_clustering.25may
#  29884 total

import sys
from statistics import mean, stdev

raw_data = open(sys.argv[1])
data = {}

week_tstamps = [i for i in range(1589752800,                   1590357601,   60*60*8)]
#                               L18may00:00, so L25may00:00 is included^^, 8h step^^
days = ['18may', '19may', '20may', '21may', '22may', '23may', '24may', '25may']
slots = ['night', 'work', 'afterwork']
#     00:00 - 08:00 - 16:00   -   00:00

def print_data():
    global data
    with open("dataset_for_clustering.{}".format(days[int(t/3)]), 'w' ) as f:
        print("src_ip,dst_ip,proto,src_port,dst_port,anom_level,threat_level,max_prio,count_events,avg_duration,stdev_duration,night_sessions,work_sessions,afterwork_sessions", file=f)
        for d in data:
            print( "{},{},{},{},{},{:.2f},{:.2f},{},{},{:.2f},{:.2f},{},{},{}".format( d,
                len(data[d]['dst_ip']),data[d]['proto'],len(data[d]['src_port']),len(data[d]['dst_port']),
                mean(data[d]['anom_level']),mean(data[d]['threat_level']),min(data[d]['max_prio']),sum(data[d]['count_events']),
                mean(data[d]['duration']),
                stdev(data[d]['duration']) if len(data[d]['duration'])>1 else 0,
                data[d]['slots']['night'],data[d]['slots']['work'],data[d]['slots']['afterwork']
            ), file=f)
            #                                                ^^ int() thows away the decimal part
    data = {}

t=0 # counter of actual element on week_tstamps
for line in raw_data:
    #example:
    # 1589212544 1589993516 172.28.0.83 52.177.165.30 tcp 57541 443 0.00 0.00 5 479 780972
    r = line.split()

    initial_tstamp = int(r[0])
    end_tstamp = int(r[1])
    src_ip = r[2]

    if initial_tstamp > week_tstamps[-1]:
    # so all week_tstamps have been covered:
        break

    if initial_tstamp > week_tstamps[t]:
    # so we move forward to the next week fraction:
        t+=1
        if t%3==0:
        # so 'night','work','afterwork' slots have passed and it's a new day:
            print_data()

    if src_ip not in data:
        # []: list. it's a mutable, or changeable, ordered sequence of elements. it preserves order, it admits duplicates
        # set(): it's an unordered collection of distinct hashable objects. it doesn't preserve order, it doesn't admit duplicates
        data[src_ip] = {
            'dst_ip': set(), 'proto': 0, 'src_port': set(), 'dst_port': set(),
            'anom_level': [], 'threat_level': [], 'max_prio': set(), 'count_events': [],
            'duration': [], 'slots': {s: 0 for s in slots}
        }

    ### count this session on the pertinent time slot:

    data[src_ip]['slots'][slots[ t%len(slots)-1 ]] += 1
    #example:
    # src_ip:10.212.138.53,from 1589807186(15:06:26) to 1589807191(15:06:31) -> {'night': 0, 'work': 1, 'afterwork': 0}
    # src_ip:10.212.138.53,from 1589920495(22:34:55) to 1589920504(22:35:04) -> {'night': 0, 'work': 1, 'afterwork': 1}

    i=t
    while end_tstamp > week_tstamps[i]:
    # long sessions count on every slots they are:
        data[src_ip]['slots'][slots[ i%len(slots)-1 ]] += 1
        i+=1
        if i==len(week_tstamps):
        # so end of the observed week has been reached:
            break

    ### count the rest of the features:

    if r[3] not in data[src_ip]['dst_ip']: data[src_ip]['dst_ip'].add(         r[3] )
    if r[4]=="udp": data[src_ip]['proto'] = 2 if ( data[src_ip]['proto']==1 ) else 1
    if r[5] not in data[src_ip]['src_port']: data[src_ip]['src_port'].add(     r[5] )
    if r[6] not in data[src_ip]['dst_port']: data[src_ip]['dst_port'].add(     r[6] )
    data[src_ip]['anom_level'].append(                                   float(r[7]))
    data[src_ip]['threat_level'].append(                                 float(r[8]))
    if r[10] not in data[src_ip]['max_prio']: data[src_ip]['max_prio'].add(int(r[9]))
    data[src_ip]['count_events'].append(                                  int(r[10]))
    data[src_ip]['duration'].append(                                      int(r[11]))
