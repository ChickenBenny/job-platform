from datetime import datetime, timedelta
import pandas as pd
from airflow.providers.postgres.hooks.postgres import PostgresHook

POSTGRES_CONN_ID = 'job_database'

def insert_into_db(processed_data, table):
    processed_data = pd.read_json(processed_data['content'])
    hook = PostgresHook.get_hook(POSTGRES_CONN_ID)
    connection = hook.get_conn()
    cursor = connection.cursor()
    dt = datetime.now().strftime("%Y%m%d")
    for i in range(processed_data.shape[0]):
        try:
            query = f'''INSERT INTO {table}(url_link, title, company, skill, job_type, loc, salary, dt) \
                        VALUES(%s, %s, %s, %s, %s, %s, %s, %s);'''
            data = (processed_data.iloc[i, 0], processed_data.iloc[i, 1], processed_data.iloc[i, 2], processed_data.iloc[i, 3],
                    processed_data.iloc[i, 4], processed_data.iloc[i, 5], processed_data.iloc[i, 6], dt)
            cursor.execute(query, data)
            connection.commit()
            print('success')
        except:
            cursor.close()
            connection.close()
            connection = hook.get_conn()
            cursor = connection.cursor()
            print('fail')
    cursor = connection.cursor()
    print('daily work success')