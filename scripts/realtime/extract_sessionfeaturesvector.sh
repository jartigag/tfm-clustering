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
sfeatvectors_file="/disco_grande/javi/clustering/$yesterday-FORTINET_FW1_10.251.0.101"
reviewed="/home/javi/clustering/reviewed_ips.txt"
dataset_file="/home/javi/clustering/$yesterday-dataset"
tmp_dir="/home/javi/clustering/tmp"

awk -F"···" '{OFS=","}{print $1,$2,$5,$7,$9,$10,$11,$14,$15,$16,$17}' $file > $sfeatvectors_file.csv

mv /home/javi/clustering/*.csv /home/javi/clustering/old/

/home/javi/clustering/preprocessing_realtime.py $sfeatvectors_file.csv $reviewed > $dataset_file.csv
/home/javi/clustering/clustering_realtime.py $dataset_file.csv
/home/javi/clustering/experimental_clustering_realtime.py $dataset_file.csv

# print daily tops by dst_ips, src_ports, dst_ports, count_events and avg_duration
tops=( 0 0 0 dst_ips 0 src_ports dst_ports 0 0 0 count_events avg_duration )
for i in 3 5 6 10 11; do
    printf "%0.s," $(seq 1 $((i-1))) >> $dataset_file.tops.csv
    echo ${tops[i]} >> $dataset_file.tops.csv
    sort -t, -nrk$i,$i $dataset_file.labeled.csv | head >> $dataset_file.tops.csv
    echo >> $dataset_file.tops.csv
done
echo -e "\n\n\n" >> $dataset_file.tops.csv
column -tnes, $dataset_file.tops.csv > $tmp_dir/$yesterday-dataset.tops.csv

# idea in progress: exploring which are the most repeated hosts among all daily tops by dst_ips, src_ports, dst_ports, count_events and avg_duration
grep -hve",," /home/javi/clustering/old/*.tops.csv /home/clustering/*.tops.csv | \
    awk -F, '{count[$2]++; arr[$2]=arr[$2]"\n"$0}END{for(i in arr)if(count[i]>1)print arr[i]}' | grep -v -e '^$' \
    > /home/javi/clustering/$yesterday-repeated_in_tops.csv
