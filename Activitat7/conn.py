import psycopg2

def getConnection():
    conn = psycopg2.connect(
        database="postgres",
        user='user_postgres',
        password='pass_postgres',
        host='localhost',
        port='5432'
    )
    connection = conn.cursor()
    print(connection)
    return connection