# Gcp_upstream_data_pipeline
Using Gcp as cloud for deployment phase .Where by collecting data from various sources via Rest api , sql server (jdbc),static file ,real time files via pub/sub.Processing code from spark 

Collecting data sources 
1. Backend system  by spark api .
2. Microsoft sql server by spark jdbc connection .
3. Static files located  in drives by reading via spark .
4. real time data is consumed by kakfka .

File formats handled - json,xml,csv,xlxs,parquet.

Deployment - once code is pused into github .And Airflow Dag is changed ,the pipeline is triggered .Both the case 
1.Change in pyspark code 
2.Change in the airflow dag task code as well
Primarily utlised Tek-ton pipeline is used .But setting the configuration in the yaml file 
