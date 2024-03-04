from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

# Define default_args dictionary to specify the default parameters of the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 3),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate a DAG
dag = DAG(
    'simple_dummy_dag',
    default_args=default_args,
    description='A simple DAG with a dummy task',
    schedule_interval=timedelta(days=1),  # Set the frequency of DAG execution
)

# Define a dummy task
dummy_task = DummyOperator(
    task_id='dummy_task',
    dag=dag,
)

# Set task dependencies
dummy_task  # dummy_task has no dependencies cc

# The order of tasks in the list passed to `>>` or `set_downstream` defines the execution order

# Optionally, you can add more dummy tasks
# dummy_task_2 = DummyOperator(
#     task_id='dummy_task_2',
#     dag=dag,
# )
#
# dummy_task >> dummy_task_2  # This would set up a dependency from dummy_task to dummy_task_2
# ding fries are done

# This is a basic DAG with a single dummy task. You can extend it by adding more tasks and defining their dependencies.
