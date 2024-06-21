# from datetime import timedelta
# from airflow import DAG
# from airflow.operators.python import PythonOperator
# from datetime import datetime
# from airflow.utils.dates import days_ago
# from twitter_etl import run_twitter_etl
# default_args= {
#     'owner':'twitter_etl',
#     'depends_on_past': False,
#     'start_date': datetime(2024,10,1),
#     'email': ["devmukherjeeindia@gmail.com"],
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 1,
#     'retry_delay': timedelta(minutes = 2)
# }

# twitter_dag= DAG('twitter_dag',default_args= default_args,description="Twitter Data Extraction")

# run_etl= PythonOperator(task_id= 'twitter_etl_task' , python_callable= run_twitter_etl, dag= twitter_dag)

# run_etl

from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from datetime import timezone as tzd
from airflow.utils.dates import days_ago
from twitter_etl import run_twitter_etl
default_args= {
    'owner':'twitter_etl',
    'depends_on_past': False,
    'start_date': datetime(2024,6,18,23,10,31,tzinfo=tzd(timedelta(hours= 5, minutes= 30))),
    'email': ["devmukherjeeindia@gmail.com"],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes = 2)
}

twitter_dag= DAG('twitter_dag',default_args= default_args,description="Twitter Data Extraction", schedule_interval='*/5 * * * *',catchup= False)

run_etl= PythonOperator(task_id= 'twitter_etl_task' , python_callable= run_twitter_etl, dag= twitter_dag)

run_etl