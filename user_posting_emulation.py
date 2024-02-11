import requests
from time import sleep
import random
import json
import sqlalchemy
from sqlalchemy import text

random.seed(100)

class AWSDBConnector:
    def __init__(self):
        # Store connection details securely (use environment variables or other best practices)
        self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
        self.USER = 'project_user'
        self.PASSWORD = ':t%;yCY3Yjg'
        self.DATABASE = 'pinterest_data'
        self.PORT = 3306

    def create_db_connector(self):
        # Create engine once outside the loop for efficiency
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
        return engine

new_connector = AWSDBConnector()
engine = new_connector.create_db_connector()

def run_infinite_post_data_loop():
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)

        # Connect to database for each iteration
        with engine.connect() as connection:
            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string).fetchone()

            if pin_selected_row:
                pin_result = dict(pin_selected_row._mapping)

                # ... Proceed with geo and user data using appropriate methods and handling potential None values
                # Include detailed logging (data retrieved, API calls made, response codes)

                # ... (your code for geo and user data retrieval and API calls)

                # After sending each API request, print the response status code for debugging


                # After sending each API request, print the response status code for debugging
                response1 = requests.request("POST", invoke_url1, headers=headers)
                print(f"Response 1 status code: {response1.status_code}")

                response2 = requests.request("POST", invoke_url2, headers=headers)
                print(f"Response 2 status code: {response2.status_code}")

                response3 = requests.request("POST", invoke_url3, headers=headers)
                print(f"Response 3 status code: {response3.status_code}")

            else:
                print("No row found at specified random index.")

# Create invoke URLs and headers outside the loop for efficiency
invoke_url1 = "https://01cw9fs2p4.execute-api.us-east-1.amazonaws.com/production/topics/0a07b87658a3.pin"
invoke_url2 = "https://01cw9fs2p4.execute-api.us-east-1.amazonaws.com/production/topics/0a07b87658a3.geo"
invoke_url3 = "https://01cw9fs2p4.execute-api.us-east-1.amazonaws.com/production/topics/0a07b87658a3.user"

headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}

if __name__ == "__main__":
    run_infinite_post_data_loop()
