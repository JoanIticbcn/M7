import psycopg2

#Funció que retorna una connexió sense cursor necessari per a fer el commit
def getConn():
    try:
        #Parametres de la connexio
        conn = psycopg2.connect(
            database="postgres",
            user='user_postgres',
            password='pass_postgres',
            host='localhost',
            port='5432'
        )
        return conn
    except(Exception,psycopg2.Error) as error:
        print("Error ",error)