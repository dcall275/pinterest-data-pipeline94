import requests
from time import sleep
import datetime
import random
from multiprocessing import Process
import boto3
import json
import sqlalchemy
from sqlalchemy import text


random.seed(100)


class AWSDBConnector:

    def __init__(self):

        self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
        self.USER = 'project_user'
        self.PASSWORD = ':t%;yCY3Yjg'
        self.DATABASE = 'pinterest_data'
        self.PORT = 3306
        
    def create_db_connector(self):
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
        return engine


new_connector = AWSDBConnector()


def run_infinite_post_data_loop():
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:

            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            pin_selected_row = connection.execute(pin_string)
            
            for row in pin_selected_row:
                pin_result = dict(row._mapping)

            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            geo_selected_row = connection.execute(geo_string)
            
            for row in geo_selected_row:
                geo_result = dict(row._mapping)

            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)


            invoke_url1 = "https://01cw9fs2p4.execute-api.us-east-1.amazonaws.com/Production/streams/streaming-0a07b87658a3-pin/record"

            #To send JSON messages
            payload1 = json.dumps({
                "stream-name": "streaming-0a07b87658a3-pin",
                "Data": {
                        #Data should be send as pairs of column_name:value, with different columns separated by commas      
                        "index": pin_result["index"], "unique_id": pin_result["unique_id"], "title": pin_result["title"], "description": pin_result["description"], "poster_name": pin_result["poster_name"], 
       "follower_count": pin_result["follower_count"], "tag_list": pin_result["tag_list"], "is_image_or_video": pin_result["is_image_or_video"], "image_src": pin_result["image_src"], "downloaded": pin_result["downloaded"], 
       "save_location": pin_result["save_location"], "category": pin_result["category"]
                        },
                        "PartitionKey": "desired-name"
                        })


            invoke_url2 = "https://01cw9fs2p4.execute-api.us-east-1.amazonaws.com/Production/streams/streaming-0a07b87658a3-geo/record"

            #To send JSON messages
            payload2 = json.dumps({
                "stream-name": "streaming-0a07b87658a3-geo",
                "Data": {
                        #Data should be send as pairs of column_name:value, with different columns separated by commas      
                        "ind": geo_result["ind"], "timestamp": geo_result["timestamp"].strftime("%Y-%m-%d %H:%M:%S"), "latitude": geo_result["latitude"], "longitude": geo_result["longitude"], "country": geo_result["country"]
                        },
                        "PartitionKey": "desired-name"
                        })


            invoke_url3 = "https://01cw9fs2p4.execute-api.us-east-1.amazonaws.com/Production/streams/streaming-0a07b87658a3-user/record"
            
            #To send JSON messages
            payload3 = json.dumps({
                "stream-name": "streaming-0a07b87658a3-user",
                "Data": {
                        #Data should be send as pairs of column_name:value, with different columns separated by commas      
                        "ind": user_result["ind"], "first_name": user_result["first_name"], "last_name": user_result["last_name"], "age": user_result["age"], "date_joined": user_result["date_joined"].strftime("%Y-%m-%d %H:%M:%S")
                        },
                        "PartitionKey": "desired-name"
                        })


            headers = {'Content-Type': 'application/json'}

            response1 = requests.request("PUT", invoke_url1, headers=headers, data=payload1)
            response2 = requests.request("PUT", invoke_url2, headers=headers, data=payload2)
            response3 = requests.request("PUT", invoke_url3, headers=headers, data=payload3)

            print(f"Payload 1: {payload1}") #print the payload and response content for each one
            print(f"Response 1 content: {response1.content}")

            print(f"Payload 2: {payload2}") #print the payload and response content for each one
            print(f"Response 2 content: {response2.content}")

            print(f"Payload 3: {payload3}") #print the payload and response content for each one
            print(f"Response 3 content: {response3.content}")

            print(f"Response 1 status code: {response1.status_code}")
            print(f"Response 2 status code: {response2.status_code}")
            print(f"Response 3 status code: {response3.status_code}")

        
             


if __name__ == "__main__":
    run_infinite_post_data_loop()
    # print('Working')