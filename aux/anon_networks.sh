#!/bin/bash

#input example:
#src_ip,dst_ip,proto,src_port,dst_port,anom_level,threat_level,max_prio,count_events,avg_duration,stdev_duration,cluster
#192.168.115.51-Redes privadas edificios,243,0,5625,2,0.2,0.0,4,15467,111.82,1606.54,many_cnxs
#output example:
#src_ip,dst_ip,proto,src_port,dst_port,anom_level,threat_level,max_prio,count_events,avg_duration,stdev_duration,cluster
#192.168.115.51-red1,243,0,5625,2,0.2,0.0,4,15467,111.82,1606.54,many_cnxs

#                  __________         so first field is ip_address-network          __________
awk -F, -v OFS="," '
BEGIN{i=0}
{
    split($1,identif,"-");
    #print identif[1],identif[2];
    if(match(identif[1],/[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/)){
        if(!(identif[2] in anon_net_ids)){anon_net_ids[identif[2]]="red"i;i++}
        $1=identif[1]"-"anon_net_ids[identif[2]]
    }
    print $0 >> FILENAME".anon"
}' $1

# #input example:
# #tstamp,src_ip,dst_ip,proto,src_port,dst_port,anom_level,threat_level,max_prio,count_events,avg_duration,stdev_duration,cluster
# #1603173600,192.168.115.51-Redes privadas edificios,243,0,5625,2,0.2,0.0,4,15467,111.82,1606.54,many_cnxs
# #output example:
# #tstamp,src_ip,dst_ip,proto,src_port,dst_port,anom_level,threat_level,max_prio,count_events,avg_duration,stdev_duration,cluster
# #1603173600,192.168.115.51-red1,243,0,5625,2,0.2,0.0,4,15467,111.82,1606.54,many_cnxs
#
# #                         __________ so first field is a tstamp
# awk -F, 'BEGIN{i=0}{if($1>1600000000){split($2,identif,"-");if(!(identif[2] in anon_net_ids)){anon_net_ids[identif[2]]="red"i;i++};
#     print $1","identif[1]"-"anon_net_ids[identif[2]]","$3","$4","$5","$6","$7","$8","$9","$10","$11","$12","$13 >> FILENAME".anon"}else{print $0 >> FILENAME".anon"}}' $1
