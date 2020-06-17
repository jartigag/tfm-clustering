# Pruebas en BigML

(Solo en las que he visto algo aprovechable)

* **K-Means con k=5**, sin características temporales ("active\_hours\_vector" mal usado)
    * [link al clustering en bigml.com](https://bigml.com/shared/cluster/hLPZxrkgYdtfRnqsUSyKM23vM1m)
    * [summary report](kmeans5-data3.out)

* **G-Means con el valor crítico mínimo -> k=3**, usando las características "{night,work,afterwork}\_sessions" con agrupación semanal
    * [link al clustering en bigml.com](https://bigml.com/shared/cluster/kE5CUUpCF3q6IIeSHSIRxOqCzOt)
    * [summary report](gmeans3-data5.out)

* **K-Means con k=5**, usando las características "{night,work,afterwork}\_sessions" con agrupación diaria
    * [link al clustering X20may en bigml.com](https://bigml.com/shared/cluster/zWYlcZWrFJ9Lmizf2CrdvI6IUg7)
    * [link al clustering J21may en bigml.com](https://bigml.com/shared/cluster/zuy4qvE8SUPLCoMw93jnTTYZ55U)
    * [link al clustering V22may en bigml.com](https://bigml.com/shared/cluster/6VbvqR4DZChzdKT0WragDjxj0Nn)

De momento, estoy trabajando con estas 5 categorías que he inferido:
* Normal, pocas conexiones
* Normal, muchas conexiones
* Protocolo UDP
* Conexiones largas
* Muchísimos eventos y conexiones
