from google.cloud import bigquery
from utils.logger import get_logger

class BigQuery:
    def __init__(self, config):
        self.project_id = config['project_id']
        self.private_key_path = config['private_key_path']
        self.logger = get_logger(__name__)

    def fetch_data(self):
        try:
            client = bigquery.Client.from_service_account_json(self.private_key_path)
            query = "SELECT * FROM `your_dataset.your_table` LIMIT 10"
            query_job = client.query(query)

            results = query_job.result()
            self.logger.info("Data fetched successfully from BigQuery")
            for row in results:
                print(row)
        except Exception as e:
            self.logger.error(f"Failed to fetch data from BigQuery: {e}")
            raise
