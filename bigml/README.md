# Pruebas en BigML

(Solo en las que he visto algo aprovechable)

* **K-Means con k=5**, sin características temporales ("active\_hours\_vector" mal usado)
    * [link al clustering en bigml.com](https://bigml.com/shared/cluster/hLPZxrkgYdtfRnqsUSyKM23vM1m)
    * [summary report](kmeans5-data3.out)

* **G-Means con el valor crítico mínimo -> k=3**, usando las características "{night,work,afterwork}\_sessions" con agrupación semanal
    * [link al clustering en bigml.com](https://bigml.com/shared/cluster/kE5CUUpCF3q6IIeSHSIRxOqCzOt)
    * [summary report](gmeans3-data5.out)

* **K-Means con k=5**, usando las características "{night,work,afterwork}\_sessions" con agrupación diaria
    * [link al clustering 19may en bigml.com](https://bigml.com/shared/cluster/79lPjUiIP9HsS96W0Y4QipTlnXK)
    * [link al clustering X20may en bigml.com](https://bigml.com/shared/cluster/zWYlcZWrFJ9Lmizf2CrdvI6IUg7)
    * [summary report X20](kmeans5-data5.20may.out)
    * [link al clustering J21may en bigml.com](https://bigml.com/shared/cluster/zuy4qvE8SUPLCoMw93jnTTYZ55U)
    * [summary report J21](kmeans5-data5.21may.out)
    * [link al clustering V22may en bigml.com](https://bigml.com/shared/cluster/6VbvqR4DZChzdKT0WragDjxj0Nn)
    * [summary report V22](kmeans5-data5.22may.out)
    * [link al clustering 23may en bigml.com](https://bigml.com/shared/cluster/iesmrMCEl5G6sTOTbRTHVz0ZGg4)
    * [link al clustering 24may en bigml.com](https://bigml.com/shared/cluster/fxUCFNKEM7WYEl4cWYhBhWmGrcd)
    * [link al clustering 25may en bigml.com](https://bigml.com/shared/cluster/7Iy3Ztt7iJQ1IL7eQeJ8okIcXji)

De momento, estoy trabajando con estas 5 categorías que he inferido:
* Normal, pocas conexiones
* Normal, muchas conexiones
* Protocolo UDP
* Conexiones largas o muchas IPs destino
* Anomalías: muchísimos eventos y conexiones

### Centroides

#### 19may

|       Cluster       |   dst_ip |   proto |   src_port | dst_port | max_prio | count_events | avg_duration | stdev_duration |
|:-------------------:|---------:|--------:|-----------:|---------:|---------:|-------------:|-------------:|---------------:|
| normal, muchas cnxs | 6.01804  | 0.00095 | 11.60096   | 1.65770  | 4.00017  | 37.34305     | 2.814073e+04 | 6.248710e+04   |
|  normal, pocas cnxs | 2.80882  | 0.02243 | 3.69528    | 1.32046  | 5.00000  | 16.00688     | 6.686527e+04 | 3.459539e+04   |
|         udp         | 14.36877 | 0.91403 | 30.71805   | 2.08824  | 4.19200  | 93.89411     | 8.591931e+04 | 2.661488e+05   |
|     cnxs largas     | 7.69652  | 0.06257 | 12.92530   | 2.24677  | 4.19007  | 1595.11654   | 7.224113e+06 | 1.398783e+07   |
|       anom(2)       | 24.64706 | 0.49020 | 2191.00000 | 2.00000  | 4.50980  | 86121.09804  | 8.512289e+05 | 3.709370e+06   |

#### 20may

|       Cluster       |   dst_ip |   proto |   src_port | dst_port | max_prio | count_events | avg_duration | stdev_duration |
|:-------------------:|---------:|--------:|-----------:|---------:|---------:|-------------:|-------------:|---------------:|
| normal, muchas cnxs | 43.84316 | 0.04837 | 112.67718  | 2.04181  | 4.00000  | 296.99434    | 14157.92980  | 54004.72215    |
|  normal, pocas cnxs | 5.11645  | 0.03475 | 9.84700    | 1.44820  | 5.00000  | 20.30733     | 19812.79107  | 20215.99608    |
|         udp         | 43.60057 | 1.72259 | 137.24005  | 4.11450  | 4.16152  | 359.39521    | 65984.58362  | 187667.52753   |
|    muchas dst_ip    | 97.34976 | 0.16824 | 492.50022  | 2.23692  | 4.00119  | 1239.55768   | 10575.59195  | 66178.72904    |
|       anom(16)      | 68.50611 | 0.31239 | 7324.59511 | 2.18674  | 4.05759  | 38265.85515  | 4469.58464   | 99635.59162    |

#### 21may

|       Clusters      |   dst_ip |   proto |    src_port | dst_port | max_prio | count_events | avg_duration | stdev_duration |
|:-------------------:|---------:|--------:|------------:|---------:|---------:|-------------:|-------------:|---------------:|
| normal, muchas cnxs | 58.61328 | 0.07595 | 257.97569   | 2.06424  | 4.00087  | 697.09332    | 34366.40104  | 74.43229       |
|  normal, pocas cnxs | 4.80514  | 0.04395 | 9.98093     | 1.41045  | 5.00000  | 18.16667     | 7914.26119   | 1.78275        |
|         udp         | 52.93117 | 1.64372 | 171.56478   | 3.87045  | 4.11538  | 400.45142    | 65689.04251  | 44.95344       |
|     cnxs largas     | 33.25556 | 0.21111 | 86.52222    | 2.13333  | 4.38889  | 2015.05556   | 722651.46667 | 23.28889       |
|       anom(2)       | 46.50000 | 0.50000 | 15709.50000 | 3.00000  | 4.50000  | 68211.50000  | 1.00000      | 21119.50000    |

#### 22may

|       Cluster       |   dst_ip |   proto |    src_port | dst_port | max_prio | count_events | avg_duration | stdev_duration |
|:-------------------:|---------:|--------:|------------:|---------:|---------:|-------------:|-------------:|---------------:|
| normal, muchas cnxs | 57.97209 | 0.28652 | 253.07345   | 2.13778  | 4.00061  | 679.49076    | 10235.43411  | 36196.79903    |
|  normal, pocas cnxs | 6.02046  | 0.10247 | 13.55686    | 1.44002  | 4.99797  | 23.83739     | 7345.21212   | 9476.48047     |
|         udp         | 7.14881  | 1.39583 | 130.93452   | 10.94048 | 4.19345  | 264.87798    | 20494.34226  | 75272.26190    |
|     cnxs largas     | 40.46416 | 0.36007 | 114.77645   | 2.30034  | 4.26451  | 489.55973    | 249823.38737 | 617650.08703   |
|       anom(1)       | 45.00000 | 2.00000 | 16152.00000 | 4.00000  | 4.00000  | 94864.00000  | 10.00000     | 1164.00000     |

#### 23may

|       Cluster       |   dst_ip |   proto |   src_port | dst_port | max_prio | count_events | avg_duration | stdev_duration |
|:-------------------:|---------:|--------:|-----------:|---------:|---------:|-------------:|-------------:|---------------:|
| normal, muchas cnxs | 56.84590 | 0.33985 | 202.58551  | 2.17969  | 4.00043  | 523.68805    | 1.027965e+04 | 32559.60156    |
|  normal, pocas cnxs | 6.21987  | 0.08465 | 12.88631   | 1.50636  | 5.00000  | 21.53616     | 8.968844e+03 | 7923.57668     |
|         udp         | 26.92878 | 0.81070 | 107.49697  | 5.37070  | 4.23481  | 408.55701    | 1.018409e+05 | 365880.91254   |
|   muchos src_ports  | 64.25430 | 0.00043 | 7209.30164 | 2.00000  | 4.13167  | 26836.11403  | 6.439548e+02 | 7962.58219     |
|       anom(5)       | 1.20349  | 0.00000 | 1.20543    | 1.00194  | 5.00000  | 141.85465    | 1.925538e+06 | 338833.03876   |

#### 24may

|       Cluster       |   dst_ip |   proto |   src_port | dst_port | max_prio | count_events | avg_duration | stdev_duration |
|:-------------------:|---------:|--------:|-----------:|---------:|---------:|-------------:|-------------:|---------------:|
| normal, muchas cnxs | 55.42397 | 0.00793 | 227.65998  | 2.10401  | 3.99720  | 610.90485    | 22825.61567  | 97734.84981    |
|  normal, pocas cnxs | 6.30008  | 0.02190 | 13.40876   | 1.48256  | 5.00000  | 22.57015     | 17373.38281  | 15749.55474    |
|         udp         | 53.53086 | 1.36111 | 169.91358  | 2.48457  | 4.02623  | 497.80864    | 18522.75154  | 70955.22377    |
|     cnxs largas     | 5.78182  | 1.38182 | 115.85455  | 11.09091 | 4.20000  | 256.49091    | 24985.20000  | 92374.05455    |
|       anom(19)      | 75.75000 | 0.06250 | 7933.31250 | 2.18750  | 4.06250  | 30504.37500  | 856.00000    | 25463.00000    |

#### 25may

|             Cluster |   dst_ip |   proto |   src_port | dst_port | max_prio | count_events | avg_duration | stdev_duration |
|--------------------:|---------:|--------:|-----------:|---------:|---------:|-------------:|-------------:|---------------:|
| normal, muchas cnxs | 54.51417 | 0.04203 | 257.24389  | 2.02590  | 4.00098  | 660.99560    | 9426.71261   | 33187.10117    |
|  normal, pocas cnxs | 5.54273  | 0.00900 | 17.40630   | 1.38681  | 4.99400  | 34.45727     | 8385.74213   | 9746.59820     |
|         udp         | 50.07285 | 1.60927 | 234.74834  | 2.48344  | 4.11258  | 602.45033    | 16391.64901  | 57167.76159    |
|     cnxs largas     | 6.15385  | 0.66667 | 65.48718   | 5.41026  | 4.48718  | 367.28205    | 503875.35897 | 735594.61538   |
|       anom(28)      | 68.48148 | 0.07407 | 8785.88889 | 2.07407  | 4.03704  | 35278.18519  | 771.92593    | 6427.07407     |

