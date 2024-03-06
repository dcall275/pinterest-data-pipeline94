
## **Project Overview: Pinterest Data Pipeline Project**

This Pinterest Data Pipeline Project applies data pipeline and processing concepts for both batch and streaming data on Pinterest. 
The primary goal is to establish a consistent and scalable data processing pipeline on Amazon Web Services (AWS), showcasing an end-to-end process for 
setting up the pipeline, performing data analysis and developing an end-to-end data processing pipeline hosted on AWS based on 
Pinterest’s experimental processing pipeline.

### **Description of Tools Used For The Pinterest Data Pipeline Project**

- Apache Kafka: A relatively new open-source technology for distributed data storage, optimized for ingesting and processing streaming data in real-time.

- Amazon MSK (Managed Streaming for Apache Kafka): A fully managed service used to build and run applications that process data using Apache Kafka.

- MSK Connect: A feature of AWS MSK that enables users to stream data to and from their MSK-hosted Apache Kafka clusters. It facilitates the deployment of fully 
  managed connectors for data movement between popular data stores like Amazon S3 and Amazon OpenSearch Service, as well as connections with external systems.

- AWS API Gateway: A fully managed service simplifying the creation, publication, maintenance, monitoring, and securing of APIs at any scale. APIs serve as the 
  "front door" for applications to access data, business logic, or functionality from backend services.

- Kafka REST Proxy: Integration providing a RESTful interface to a Kafka cluster, making it easy to produce and consume messages, view cluster states, or perform a 
  administrative actions without using native Kafka protocols or clients.

- Amazon S3 (Simple Storage Service): An object storage service offering industry-leading scalability, data availability, security, and performance.

- AWS MWAA (Managed Workflows for Apache Airflow): A managed service designed to seamlessly integrate Apache Airflow in the cloud with minimal setup, enabling 
  efficient scheduling and monitoring of workflows.

- Apache Spark: A unified engine for large-scale distributed data processing on computer clusters.

- PySpark: The Python API for Apache Spark, enabling real-time, large-scale data processing in a distributed environment using Python.

- Databricks: The Databricks Lakehouse Platform, a unified solution providing tools for building, deploying, sharing, and maintaining enterprise-grade data solutions 
  at scale. It integrates with cloud storage, ensuring security, and facilitates the management and deployment of cloud infrastructure.

- AWS Kinesis: Capable of collecting streaming data, such as event logs, social media feeds, application data, and IoT sensor data, in real-time or near real-time. 
  Kinesis allows processing and analysis of incoming data for instant response and timely analytics insights.

### **About The Pinterest Data Used**

There are 2 files used to emulate Pinterest's data, the first to run the batch processing emulation and the second to run the stream processing of the Pinterest data.   This project requires a two scripts to be run to emulate the flow of the Pinterest data: user_posting_emulation.py, which contains login credentials for an RDS database. The database holds three tables, resembling data received by the Pinterest API during a user's POST request, including:


**Pinterest Data Tables:**
- pinterest_data: Information about posts updated to Pinterest.
- geolocation_data: Data about the geolocation of each Pinterest post.
- user_data: Information about users who have uploaded posts. 

**For the streaming tasks, the following data streams are created:**
- streaming_df_pin: Streamed information about posts updated to Pinterest.
- streaming_df_geo: Streamed data about the geolocation of each Pinterest post.
- streaming_df_user: Streamed information about users who have uploaded posts.

The second script is user_posting_emulation_streams.py which emulates real time streaming of the Pinterest Data.  

## **About the Data Pipeline Process used:**

This data pipelining process involves two distinct processes:

## **Batch Data Processing:**

- Extraction of data from Amazon RDS is accomplished through the Kafka REST API, installed on an EC2 Client machine.
- Extracted data is stored in an Amazon S3 Bucket in JSON format.
- The S3 Bucket is mounted to Databricks, facilitating data loading into the platform.
- Data is then stored in dataframes, subsequently undergoing cleaning and analysis processes.
- To streamline and automate this batch processing, AWS MWAA (Managed Workflows for Apache Airflow) can be employed.

## **Streaming Data Processing:**
- Data extraction from Amazon RDS is achieved using the REST API.
- The extracted data is stored in Kinesis streams, organized into shards for efficient processing.
- Real-time loading of streaming data into Databricks takes place, continuously appending to the existing dataframe.
- The data undergoes a cleaning process, and delta tables are generated within Databricks for further analysis.

## **Key Components:**

### **Cloud Services Utilised:**
- Amazon Web Services (AWS) is utilized, offering various services across global data centers.

### **AWS Services Employed:**
- S3 (Simple Storage Service)
- EC2 (Elastic Compute Cloud)
- MSK (Managed Streaming for Kafka)
- API Gateway
- Managed Apache Airflow (MWAA)
- Kinesis

### **Data Pipelining Processes:**

### **Batch Data Processing:**
- Extract data from Amazon RDS using Kafka REST API on an EC2 client.
- Store data in an S3 bucket in JSON format.
- Mount S3 to Databricks for loading and analysis.
- Automate using AWS MWAA.

### **Streaming Data Processing:**
- Extract data from Amazon RDS using REST API.
- Store data in Kinesis streams.
- Real-time loading into Databricks, where it appends to dataframes.
- Clean and create Delta tables in Databricks.

### **Data Exploration:**
- Explore sample data from Amazon RDS, including tables: pinterest_data, geolocation_data, and user_data.

### **Batch Processing Steps:**
- Setting up EC2 Instance & Apache Kafka:
- Launch EC2 instance with specific security configurations.
- Install Kafka and IAM MSK authentication package.
- Create MSK clusters and topics for each table.

### **Connecting MSK Cluster to S3 Bucket:**
- Create S3 bucket.
- Configure IAM role for writing to the destination bucket.
- Set up MSK Connect plugin and create a connector.

### **Configuring API in AWS API Gateway:**
- Create REST API in API Gateway.
- Set up proxy resources and methods for API integration.

### **Setting up Kafka REST Proxy on EC2 client:**
- Install Confluent package for REST proxy on EC2.
- Configure properties file for Kafka REST proxy.

### **Batch Processing in Databricks:**
- Create AWS Access Key and Secret Access Key.
- Mount S3 bucket to Databricks and load data into dataframes.
- Clean tables using PySpark operations.

### **Data Analysis:**
- Perform various analysis tasks, such as identifying the most popular Pinterest category, posts per category per year, user demographics, etc

### **Stream Processing:**
- Utilize AWS Kinesis for real-time or near real-time streaming data collection.
- Create data streams for tables and set up API access roles.
- Using API Gateway, configure resources and methods for data extraction from Amazon RDS and storage in Kinesis streams.
- Load streaming data into Databricks, continuously appending to dataframes.
- Clean and analyze data using PySpark.







