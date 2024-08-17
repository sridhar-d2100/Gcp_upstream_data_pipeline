import json
import asyncio
from app.http_api import HttpAPI
from app.jdbc_sqlserver import JDBC_SQLServer
from app.postgres import JDBC_Postgres
from app.bigquery import BigQuery
from utils.logger import get_logger

logger = get_logger(__name__)

def load_config():
    with open('config/config.json', 'r') as f:
        logger.info("Configuration file loaded successfully")
        return json.load(f)

async def main():
    config = load_config()

    # HTTP API Connection
    http_api = HttpAPI(config['http'])
    http_data = await http_api.fetch_data()
    logger.info(f"HTTP API Data: {http_data}")

    # JDBC SQL Server Connection
    sql_server = JDBC_SQLServer(config['jdbc_sqlserver'])
    sql_server.fetch_data()

    # JDBC PostgreSQL Connection
    postgres = JDBC_Postgres(config['jdbc_postgres'])
    postgres.fetch_data()

    # BigQuery Connection
    bigquery = BigQuery(config['bigquery'])
    bigquery.fetch_data()

if __name__ == "__main__":
    asyncio.run(main())
