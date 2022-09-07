import pandas as pd
import psycopg2
from datetime import datetime

class preprocessing_cakeresume():
    def __init__(self):
        self.date = datetime.now().strftime("%Y%m%d")

    def process_with_pandas(self, crawling_data):
        df = pd.DataFrame(crawling_data, columns=['job_link', 'job_title', 'job_company', 'skill', 'job_type', 'location', 'salary'])
        df['dt'] = self.date
        try:
            df['job_type'] = df['job_type'].apply(lambda x: x.split('・')[1])
            df['location'] = df['location'].apply(lambda x: x.split('・')[0])
        except:
            pass
        df = df.dropna()
        return df

    def insert_into_db(self, df, table):
        connection = psycopg2.connect(
                            database = "postgres",
                            user = "postgres",
                            password = "postgres",
                            host = "job_database",
                            port = '5432'
                        )
        cursor = connection.cursor()
        for i in range(df.shape[0]):
            try:
                query = f'''INSERT INTO {table}(url_link, title, company, skill, job_type, loc, salary, dt) \
                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s);'''
                data = (df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2], df.iloc[i, 3], df.iloc[i, 4], df.iloc[i, 5], df.iloc[i, 6], df.iloc[i, 7])
                cursor.execute(query, data)
                connection.commit()
            except:
                cursor.close()
                connection.close()
                connection = psycopg2.connect(
                            database = "postgres",
                            user = "postgres",
                            password = "postgres",
                            host = "job_database",
                            port = '5432'
                        )
                cursor = connection.cursor()
        cursor.close()
