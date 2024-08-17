from pyspark.sql import SparkSession
from utils.logger import get_logger

class JDBC_SQLServer:
    def __init__(self, config):
        self.url = config['url']
        self.username = config['username']
        self.password = config['password']
        self.logger = get_logger(__name__)

    def fetch_data(self):
        try:
            spark = SparkSession.builder \
                .appName("JDBC SQL Server Connection") \
                .config("spark.jars.packages", "com.microsoft.sqlserver:mssql-jdbc:8.4.1.jre8") \
                .getOrCreate()

            df = spark.read.format("jdbc") \
                .option("url", self.url) \
                .option("dbtable", "your_table_name") \
                .option("user", self.username) \
                .option("password", self.password) \
                .load()

            self.logger.info("Data fetched successfully from SQL Server")
            df.show()
            spark.stop()
        except Exception as e:
            self.logger.error(f"Failed to fetch data from SQL Server: {e}")
            raise
