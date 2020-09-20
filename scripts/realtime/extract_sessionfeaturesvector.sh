#!/usr/bin/env bash
#
# extract session-features-vectors from session-correlation's output.
# a session-features-vector is formed by:
# begin_tstamp,end_tstamp,src_ip,dst_ip,proto,src_port,dst_port,anom_level,threat_level,max_prio,count_events,duration
#
#usage: put it in crontab:
# 0 8 * * * /home/javi/clustering/extract_sessionfeaturesvector.sh
#
#exec time: 5m40s laptop (intel core i5-8265U @ 1.60GHz), 6m5s probe (intel xeon gold 6126 @ 2.60GHz)
#
#input->output:
#(7,9G) FORTINET_FW1_10.251.0.101.1 -> (2,3G) 2020-09-22-FORTINET_FW1_10.251.0.101.csv
#
#input->output example:
#1599141040···1599136049···FW1···2579158799···10.253.15.238···Red desarrollo···13.107.42.18···Internet···tcp···63973···443···450769···4559091···0.00···0.00···5···35···End forward, close, 1; URL allowed category, passthrough, 1; Statistics, accept, 33
# ->
#1599141040,1599136049,10.253.15.238,13.107.42.18,tcp,63973,443,0.00,0.00,5,35,4991

file="FORTINET_FW1_10.251.0.101.1" # yesterday's log, rotated
yesterday="$( date -d yesterday +%F )"
sfeatvectors_file="/disco_grande/javi/clustering/$yesterday-FORTINET_FW1_10.251.0.101.csv"
dataset_file="/home/javi/clustering/$yesterday-dataset.csv"

awk -F"···" '{OFS=","}{print $1,$2,$5,$7,$9,$10,$11,$14,$15,$16,$17}' $file > $sfeatvectors_file

/home/javi/clustering/preprocessing_realtime.py $sfeatvectors_file > $dataset_file
/home/javi/clustering/clustering_realtime.py $dataset_file
