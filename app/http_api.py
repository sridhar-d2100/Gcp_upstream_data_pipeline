import requests
import asyncio
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from utils.logger import get_logger

class HttpAPI:
    def __init__(self, config):
        self.client_id = config['client_id']
        self.client_secret = config['client_secret']
        self.token_url = config['token_url']
        self.data_url = config['data_url']
        self.logger = get_logger(__name__)
        self.spark = SparkSession.builder.appName("Fetch Data via HTTP").getOrCreate()

    async def get_access_token(self) -> str:
        try:
            response = requests.post(
                self.token_url,
                data={
                    'grant_type': 'client_credentials',
                    'client_id': self.client_id,
                    'client_secret': self.client_secret
                }
            )
            response.raise_for_status()
            self.logger.info("Access token retrieved successfully")
            return response.json().get('access_token')
        except Exception as e:
            self.logger.error(f"Failed to retrieve access token: {e}")
            raise

    async def fetch_data(self) -> DataFrame:
        token = await self.get_access_token()
        headers = {'Authorization': f'Bearer {token}'}
        try:
            response = requests.get(self.data_url, headers=headers)
            response.raise_for_status()
            self.logger.info("Data fetched successfully from HTTP API")


            data = response.json()
            
            # If the data is a single dictionary, wrap it in a list
            if isinstance(data, dict):
                data = [data]
            
            # Convert the list of dictionaries to a Spark DataFrame
            df = self.spark.createDataFrame(data)
            self.logger.info("Data converted to Spark DataFrame")
            return df
        except Exception as e:
            self.logger.error(f"Failed to fetch data: {e}")
            raise


