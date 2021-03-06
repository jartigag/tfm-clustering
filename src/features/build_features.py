#!/usr/bin/env python3
#
# for each src_ip, aggregate info and calc metrics from its session-features-vectors.
#
#usage: ./src/features/build_features.py data/interim/FORTINET_FIREWALL.sessionfeaturesvectors.csv > data/processed/FORTINET_FIREWALL.aggmatrix.csv
#exec time: 3m25s laptop (intel core i5-8265U @ 1.60GHz), 4m7s probe (intel xeon gold 6126 @ 2.60GHz)
#output example:
# $ head FORTINET_FIREWALL.aggmatrix.csv
# src_ip,dst_ip,proto,src_port,dst_port,anom_level,threat_level,max_prio,count_events,uniq_count_events,avg_duration,stdev_duration
# 10.253.15.238,98,0,4624,3,0.03,0.00,4,13111,151,184.49,2563.48
# 172.24.82.135,293,1,3264,6,0.01,0.00,4,12951,210,321.74,710.02

#TODO: when a src_ip has been reviewed, it can be excluded adding it to reviewed_ips.txt in a new line (format: "10.0.0.1: i checked it on 2020-10-22. it's from dev environment")

import sys
from statistics import mean, stdev
import string


def process(input_file, output_file=sys.stdout, time_slots=False):
    """ Turns preprocessed data (from data/interim) into
        processed data (saved in data/processed), ready to be the model input.
    """

    def print_data():
        with open(output_file, "w") if output_file!=sys.stdout else output_file as outf:
            print("src_ip,dst_ip,proto,src_port,dst_port,anom_level,threat_level,max_prio,events,uniq_events,avg_duration,stdev_duration{}".format(
                ",night_hours,work_hours,afterwork_hours" if time_slots else ''),
                file = outf
            )
            for d in data:
                d_slots = ''
                if time_slots:
                    d_slots = ",".join('', data[d]['slots']['night'], data[d]['slots']['work'], data[d]['slots']['afterwork'])
                print( "{},{},{:d},{:d},{:d},{:.2f},{:.2f},{:d},{:d},{:d},{:.2f},{:.2f}{}".format( d,
                        len(data[d]['dst_ip']), data[d]['proto'], len(data[d]['src_port']), len(data[d]['dst_port']),
                        mean(data[d]['anom_level']), mean(data[d]['threat_level']),
                        min(data[d]['max_prio']), sum(data[d]['count_events']), len(set(data[d]['events'])),
                        mean(data[d]['duration']), stdev(data[d]['duration']) if len(data[d]['duration'])>1 else 0,
                        d_slots
                    ), file = outf)

    data = {}
    strip_nums = str.maketrans('', '', string.digits) # translation table to remove numbers from events string

    if time_slots:
        #TODO: generalize
        week_tstamps = [i for i in range(1589752800, 1590357601, 60*60*8)]
        #            L18may00:00, so L25may00:00 is included^^, 8h step^^
        slots = ['night', 'work', 'afterwork']
        #     00:00 - 08:00 - 16:00   -   00:00

        t=0 # counter of actual element on week_tstamps

    with open(input_file) as f:
        for line in f:
            #example:
            # 1589212544,1589993516,172.28.0.83,52.177.165.30,tcp,57541,443,0.00,0.00,5,479
            r = line.rstrip().split(",")

            src_ip = r[2]

            if time_slots:
                initial_tstamp = int(r[0])
                end_tstamp = int(r[1])

                if initial_tstamp > week_tstamps[-1]:
                # so all week_tstamps have been covered:
                    break

                if initial_tstamp > week_tstamps[t]:
                # so we move forward to the next week fraction:
                    t+=1
                    if t%3==0:
                    # so 'night','work','afterwork' slots have passed and it's a new day:
                        print_data()
                        data = {}

            if src_ip not in data:
                # []: list. it's a mutable, or changeable, ordered sequence of elements. it preserves order, it admits duplicates
                # set(): it's an unordered collection of distinct hashable objects. it doesn't preserve order, it doesn't admit duplicates
                data[src_ip] = {
                    'dst_ip': set(), 'proto': 0, 'src_port': set(), 'dst_port': set(),
                    'anom_level': [], 'threat_level': [],
                    'max_prio': set(), 'count_events': [],
                    'events': set(), 'duration': []
                }
                if time_slots:
                    data[src_ip]['slots'] = {s: 0 for s in slots}

            if time_slots:
                # count this session on the pertinent time slot:

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

            # count the rest of the features:

            if r[3] not in data[src_ip]['dst_ip']: data[src_ip]['dst_ip'].add(                   r[3] )
            # proto = 2 if src_ip has used tcp and udp, 1 if udp, 0 if tcp:
            if r[4]=="udp": data[src_ip]['proto'] = 2 if ( data[src_ip]['proto']==1 ) else 1
            if r[5] not in data[src_ip]['src_port']: data[src_ip]['src_port'].add(               r[5] )
            if r[6] not in data[src_ip]['dst_port']: data[src_ip]['dst_port'].add(               r[6] )
            data[src_ip]['anom_level'].append(                                             float(r[7]))
            data[src_ip]['threat_level'].append(                                           float(r[8]))
            if r[9] not in data[src_ip]['max_prio']: data[src_ip]['max_prio'].add(           int(r[9]))
            data[src_ip]['count_events'].append(                                            int(r[10]))
            for x in "".join(r[11:]).translate(strip_nums).split(';'):
                data[src_ip]['events'].add(x.strip())
                #example:
                # src_ip.sessionfeatvector1.events: "End forward, close, 1; URL allowed category, passthrough, 1"
                # src_ip.sessionfeatvector2.events: "End forward, close, 1; Statistics, accept, 3"
                # src_ip.events: {'URL allowed category passthrough', 'End forward close', 'Statistics accept'}
            data[src_ip]['duration'].append(                                       int(r[0])-int(r[1]))

    print_data()


if __name__ == '__main__':
    preprocessed_data = sys.argv[1]
    process(preprocessed_data)
