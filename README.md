# Caracterización de equipos informáticos mediante clustering en una red empresarial

> Aquí tengo que poner el abstract. Y antes, hacer un abstract

Para enterarte bien de todos los detalles, mejor leer la [memoria en pdf](TFM.pdf), pero este README ya te da una idea.

# Índice general

## 1. Introducción

## 2. Objetivos y metodología

![](graphs/esquema.png)

## 3. Estado del arte

Referencias interesantes:

### 3.1. Aprendizaje automático en la clasificación de tráfico

["A survey of techniques for internet traffic classification using machine learning" (H.T. Nguyen y G. Armitage, 2008)](https://doi.org/10.1109/SURV.2008.080406)

["Why Should Machines Learn?" (S. Herbert, 1983)](https://doi.org/10.1007/978-3-662-12405-5_2)

["Issues and future directions in traffic classification" (A. Dainotti, A. Pescape y K.C. Claffy, 2012)](https://doi.org/10.1109/MNET.2012.6135854)

["Experiences of Internet traffic monitoring with tstat" (A. Finamore et al., 2011)](https://doi.org/10.1109/MNET.2011.5772055)

["BLINC: Multilevel Traffic Classification in the Dark" (T. Karagiannis, K. Papagiannaki y M. Faloutsos, 2006)](https://doi.org/10.1145/1090191.1080119)

### 3.2. Detección de anomalías sobre actividad de red


["A Survey on Big Data for Network Traffic Monitoring and Analysis", (A. D'Alconzo et al., 2019)](https://doi.org/10.1109/TNSM.2019.2933358)

["A Comprehensive Survey on Machine Learning for Networking: Evolution, Applications and Research Opportunities", (R. Boutaba et al., 2018)](https://doi.org/10.1186/s13174-018-0087-2)

["Anomaly-based network intrusion detection: Techniques, systems and challenges", (P. García-Teodoro, 2009)](https://doi.org/10.1016/j.cose.2008.08.003)

["Intrusion Detection: A Survey", (A. Lazarevic, 2005)](https://doi.org/10.1007/0-387-24230-9_2)

### 3.3. Clustering


["Intrusion Detection with Unlabeled Data Using Clustering" (L. Portnoy, 200)](https://doi.org/10.7916/D8MP5904)

["A clustering-based method for unsupervised intrusion detections" (S. Jian et al., 2006)](https://doi.org/10.1016/j.patrec.2005.11.007)

["Flow Clustering Using Machine Learning Techniques" (A. McGregor et al., 2004)](https://doi.org/10.1007/978-3-540-24668-8_21)

["Automated traffic classification and application identification using machine learning" (S. Zander, T. Nguyen y G. Armitage, 2005)](https://doi.org/10.1109/LCN.2005.35)

["Traffic Classification on the Fly" (L. Bernaille et al., 2006)](https://doi.org/10.1145/1129582.1129589) y [conti](https://doi.org/10.1145/1368436.1368445)-[nuaciones](10.1007/978-3-540-71617-4_17)

"Unsupervised Anomaly Detection in Network Intrusion Detection Using Clusters" (K. Leung y C. Leckie, 2005)

["Next Generation Intrusion Detection Expert System (NIDES) Statistical Algorithms Rationale and Rationale for Proposed Resolver" (H. Javitz et al., 1993)](https://doi.org/10.13140/RG.2.1.1847.9521)

["Network Anomaly Detection: Methods, Systems and Tools" (M.H. Bhuyan, 2014)](https://doi.org/10.1109/SURV.2013.052213.00046)

["Unsupervised clustering approach for network anomaly detection" (I. Syarif et al., 2012)](https://doi.org/10.1007/978-3-642-30507-8_7)

["Computational Complexity between K-Means and K-Medoids Clustering Algorithms for Normal and Uniform Distributions of Data Points" (T. Velmurugan y T. Santhanam, 2010)](https://doi.org/10.3844/jcssp.2010.363.368)

["Distance-Based Outlier Detection: Consolidation and Renewed Bearing" (G. H. Orair et al., 2010)](https://doi.org/10.14778/1920841.1921021)

## 4. Desarrollo

Preprocesado con este [script](scripts/preprocess_clustering_dataset.py), ensayos en [bigml/](bigml/).

## 5. Resultados

[Centroides](https://github.com/jartigag/tfm-clustering/tree/master/bigml#centroides) con K-Means (k=5) sobre los datos finales, [análisis de silueta](https://github.com/jartigag/tfm-clustering/blob/master/scripts/clustering3.ipynb).

## 6. Conclusiones y líneas futuras
