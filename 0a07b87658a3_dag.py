from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from datetime import datetime, timedelta

#Define params for Submit Run Operator
notebook_task = {
    'notebook_path': 'Users/**************@********.co.uk/mounting_s3_to_db',
}

#Define params for Run Now Operator
notebook_params = {
    "Variable":5
}

# Define default_args for your DAG
default_args = {
    'owner': '0a07b87658a3',
    'depends_on_past': False,
    'start_date': datetime(2024, 2, 21),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=2),
}

with DAG('0a07b87658a3_dag',
    # should be a datetime format
    start_date=datetime(2024, 2, 20),
    schedule_interval='0 0 * * *', # Set to run daily at midnight
    catchup=False,
    default_args=default_args
    ) as dag:


 opr_submit_run = DatabricksSubmitRunOperator(
        task_id='submit_run',
        # the connection we set-up previously
        databricks_conn_id='databricks_default',   
        existing_cluster_id='1108-162752-8okw8dgg',
        notebook_task=notebook_task
    )
opr_submit_run    




