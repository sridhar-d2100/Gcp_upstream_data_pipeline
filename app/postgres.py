from pyspark.sql import SparkSession
from utils.logger import get_logger

class JDBC_Postgres:
    def __init__(self, config):
        self.url = config['url']
        self.username = config['username']
        self.password = config['password']
        self.logger = get_logger(__name__)

    def fetch_data(self):
        try:
            spark = SparkSession.builder \
                .appName("JDBC PostgreSQL Connection") \
                .config("spark.jars.packages", "org.postgresql:postgresql:42.2.16") \
                .getOrCreate()

            df = spark.read.format("jdbc") \
                .option("url", self.url) \
                .option("dbtable", "your_table_name") \
                .option("user", self.username) \
                .option("password", self.password) \
                .load()

            self.logger.info("Data fetched successfully from PostgreSQL")
            df.show()
            spark.stop()
        except Exception as e:
            self.logger.error(f"Failed to fetch data from PostgreSQL: {e}")
            raise
