import psycopg2
from conn import getConn
from create import insertUser
from create_table import createTable

# Fem el try except per capturar errors i tanquem les connexió amb el finally
try:
    # Creem una conexió per a treballar en la base de dades, la pasarem com a parametre en les funcions i es tanca al finalitzar el programa
    conn = getConn()
    # Creem el cursor per a treballar a partir de la connexio
    connexio = conn.cursor()

    # Instruccions per a l'usuari final pugi operar el programa de forma senzilla
    instruccions = ("1:Create table\n"
                    "2:Create un registre a la taula\n"
                    "3:Read llegeix els registres de la taula\n"
                    "4:Update actualitza un registre de la taula\n"
                    "5:Delete un registre de la taula donant el seu id\n"
                    "6:Tanca la connexio (es tanca automaticament al final)\n"
                    "7:Imprimeix les intruccions\n")
    print(instruccions)

    # Alternativa al switch de java per a executar la operacio en funcio de l'entrada de l'usuari
    num = int(input("Entra el numero de l'operacio desitjada "))
    if (num == 1):
        createTable(connexio, conn)
    if (num == 2):
        insertUser(connexio, conn)
    if (num == 3):
        pass
    if (num == 4):
        pass
    if (num == 5):
        pass
    if (num == 6):
        connexio.close()
        conn.close()
    if (num == 7):
        print(instruccions)
except(Exception, psycopg2.Error) as error:
    print("An error has ocurred " + error)
finally:
    conn.close()
    connexio.close()
