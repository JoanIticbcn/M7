import psycopg2
from conn import getConn
from create import insertUser
from create_table import createTable
from delete import delete
from read import read
from update import updatePasswd

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
    if num == 1:
        createTable(connexio, conn)
    if num == 2:
        insertUser(connexio, conn)
    if num == 3:
        read(connexio)
    if num == 4:
        idToUpdate = int(input("Entra el ID de l'usuari que vols actualitzar la contrasenya "))
        updatePasswd(connexio,conn,idToUpdate)
    if num == 5:
        idToDelete = int(input("Entra el ID de l'usuari que vols esborrar "))
        delete(connexio,conn,idToDelete)
    if num == 6:
        connexio.close()
        conn.close()
    if num == 7:
        print(instruccions)
except(Exception, psycopg2.Error) as error:
    #Imprimim el missatge d'error
    print("An error has ocurred " + error)
finally:
    #Tanquem la connexió
    conn.close()
    connexio.close()
    print("Connexio finalitzada")
