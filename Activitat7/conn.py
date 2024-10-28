import psycopg

conn = psycopg.connect(
    database="",
    user='',
    password='',
    host='localhost',
    port='5432'
)
connection = conn.cursor()
