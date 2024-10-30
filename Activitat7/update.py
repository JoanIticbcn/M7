# Funció que actualitza la contrasenya d'un usuari donat el seu ID
def updatePasswd(connexioUpdt, connUpdt, user_id):
    update_query = "UPDATE users SET password = %s WHERE id = %s;"
    # Executa el UPDATE  amb el user_id i la nova contrasenya com a parametres
    connexioUpdt.execute(update_query, ("4321ABC", user_id))
    # Comprova si s'han actualitzat els registres
    if connexioUpdt.rowcount > 0:
        print(f"Password updated correctament per a l'usuari amb ID {user_id}.")
        print(f"La nova contrasenya es 4321ABC per a l'usuari amb ID {user_id}.")
    else:
        print(f"No hi ha cap usuari amb ID {user_id}.")
    # Commit dels canvis per fer-los permanents
    connUpdt.commit()
