import requests
import datetime
from time import sleep
import random
from multiprocessing import Process
import boto3  # Still imported for potential future use
import json
import sqlalchemy
from sqlalchemy import text

# Set random seed for consistency
random.seed(100)

# Define user ID and API invoke URL
user_id = "0a07b87658a3"
invoke_url = "https://01cw9fs2p4.execute-api.us-east-1.amazonaws.com/Production"

# Kafka bootstrap servers (S3 information removed)
bootstrap_servers = ",".join([
    "b-2.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098",
    "b-1.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098",
    "b-3.pinterestmskcluster.w8g8jt.c12.kafka.us-east-1.amazonaws.com:9098"
])

# Database connector class with connection pooling
class AWSDBConnector:
    def __init__(self):
        self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
        self.USER = 'project_user'
        self.PASSWORD = ':t%;yCY3Yjg'
        self.DATABASE = 'pinterest_data'
        self.PORT = 3306

    def create_db_connector(self):
        engine = sqlalchemy.create_engine(
            f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4",
            pool_size=5,  # Adjust based on your application's needs
            max_overflow=10,  # Adjust based on your application's needs
            pool_recycle=3600  # Adjust based on your application's needs
        )
        return engine

new_connector = AWSDBConnector()


def fetch_random_row(table_name):
    random_row = random.randint(0, 11000)
    query = text(f"SELECT * FROM {table_name} LIMIT {random_row}, 1")
    return query


def fetch_data_from_table(connection, query):
    selected_row = connection.execute(query)
    # **Convert datetime objects to JSON-compatible strings before returning**
    result = [
        {key: value.strftime("%Y-%m-%d %H:%M:%S") if isinstance(value, datetime.datetime) else value for key, value in dict(row._mapping).items()}
        for row in selected_row
    ]
    return result[0] if result else None


def send_data_to_api(data, topic):
    try:
        response = requests.post(invoke_url, json=data)
        response.raise_for_status()  # Check for API errors
        print(f"Successfully sent data to API for topic: {topic}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to API for topic {topic}: {e}")


def run_infinite_post_data_loop():
    while True:
        sleep(random.uniform(0, 2))
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:
            try:
                pin_query = fetch_random_row("pinterest_data")
                pin_result = fetch_data_from_table(connection, pin_query)
                send_data_to_api(pin_result, f"topics/{user_id}.pin")

                geo_query = fetch_random_row("geolocation_data")
                geo_result = fetch_data_from_table(connection, geo_query)
                send_data_to_api(geo_result, f"topics/{user_id}.geo")

                user_query = fetch_random_row("user_data")
                user_result = fetch_data_from_table(connection, user_query)
                send_data_to_api(user_result, f"topics/{user_id}.user")

            except Exception as e:
                print(f"Error occurred: {e}")
        # Optionally implement additional error handling


if __name__ == "__main__":
  run_infinite_post_data_loop()

