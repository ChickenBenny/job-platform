import psycopg2


def get_data(type: str):
    connection = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="postgres",
        host="job_database",
        port='5432'
    )
    cursor = connection.cursor()
    query = f'SELECT * FROM {type} ORDER BY dt DESC;'
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows
