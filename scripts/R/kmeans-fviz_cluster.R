# https://uc-r.github.io/kmeans_clustering

library(tidyverse)  # data manipulation
library(cluster)    # clustering algorithms
library(factoextra) # clustering algorithms & visualization

df <- read.csv("~/g/tfm/scripts/datasets/2020-09-20-dataset.csv")

df$src_ip <- NULL
df <- scale(df)
df = subset(df, select = -(threat_level))
k5 <- kmeans(df, centers = 5, nstart = 30)
df$src_ip <- NULL
df <- scale(df)
df = subset(df, select = -(threat_level))

k5 <- kmeans(df, centers = 5, nstart = 30)

fviz_cluster(k5, data = df, show.clust.cent=TRUE, main="Clusters obtenidos con K-Means sobre los datos del 20-09-2020\n(se usa PCA para la visualización)", labelsize=0)
# Possible values of object `k5` are also any list object with data and cluster components (e.g.: object = list(data = mydata, cluster = myclust))
