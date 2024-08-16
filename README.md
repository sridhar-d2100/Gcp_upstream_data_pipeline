# Gcp_upstream_data_pipeline
Using Gcp as cloud for deployment phase .Where by collecting data from various sources via Rest api , sql server (jdbc),static file ,real time files via pub/sub.Processing code from spark 

Collecting data sources 
1. Backend system  by api .
2. Microsoft sql server by jdbc connection .
3. Static files located  in drives by reading via spark .
4. real time data is consumed by kakfka .

File formats handled 
1.json
2.xml
3.csv
4.xlxs
5.parquet


