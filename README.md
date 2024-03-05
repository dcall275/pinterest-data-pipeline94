
### **Project Overview: Pinterest Data Pipeline Project**

This Pinterest Data Pipeline Project applies data pipeline and processing concepts for both batch and streaming data on Pinterest. 
The primary goal is to establish a consistent and scalable data processing pipeline on Amazon Web Services (AWS), showcasing an end-to-end process for 
setting up the pipeline, performing data analysis and developing an end-to-end data processing pipeline hosted on AWS based on 
Pinterest’s experimental processing pipeline.

### **Key Components:**

## **Cloud Services Utilised:**
Amazon Web Services (AWS) is utilized, offering various services across global data centers.
AWS Services Employed:
S3 (Simple Storage Service)
EC2 (Elastic Compute Cloud)
MSK (Managed Streaming for Kafka)
API Gateway
Managed Apache Airflow (MWAA)
Kinesis

### **Data Pipelining Processes:**

## **Batch Data Processing:**
Extract data from Amazon RDS using Kafka REST API on an EC2 client.
Store data in an S3 bucket in JSON format.
Mount S3 to Databricks for loading and analysis.
Automate using AWS MWAA.

## **Streaming Data Processing:**
Extract data from Amazon RDS using REST API.
Store data in Kinesis streams.
Real-time loading into Databricks, where it appends to dataframes.
Clean and create Delta tables in Databricks.

## **Data Exploration:**
Explore sample data from Amazon RDS, including tables: pinterest_data, geolocation_data, and user_data.

## **Batch Processing Steps:**
Setting up EC2 Instance & Apache Kafka:
Launch EC2 instance with specific security configurations.
Install Kafka and IAM MSK authentication package.
Create MSK clusters and topics for each table.

## **Connecting MSK Cluster to S3 Bucket:**
Create S3 bucket.
Configure IAM role for writing to the destination bucket.
Set up MSK Connect plugin and create a connector.

## **Configuring API in AWS API Gateway:**
Create REST API in API Gateway.
Set up proxy resources and methods for API integration.

## **Setting up Kafka REST Proxy on EC2 client:**
Install Confluent package for REST proxy on EC2.
Configure properties file for Kafka REST proxy.

## **Batch Processing in Databricks:**
Create AWS Access Key and Secret Access Key.
Mount S3 bucket to Databricks and load data into dataframes.
Clean tables using PySpark operations.

## **Data Analysis:**
Perform various analysis tasks, such as identifying the most popular Pinterest category, posts per category per year, user demographics, etc

## **Stream Processing:**
Utilize AWS Kinesis for real-time or near real-time streaming data collection.
Create data streams for tables and set up API access roles.
Using API Gateway, configure resources and methods for data extraction from Amazon RDS and storage in Kinesis streams.
Load streaming data into Databricks, continuously appending to dataframes.
Clean and analyze data using PySpark.







