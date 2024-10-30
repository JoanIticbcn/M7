# Funció que borra un usuari de la taula users donat el seu ID

def delete(connexioD,connD,user_id):
    delete_query = "DELETE FROM users WHERE id = %s;"
    # Executa la query de delete amb el user_id passat com a parametre de la funcio
    connexioD.execute(delete_query, (user_id,))
    # Comprovar si ha borrat algo o no
    if connexioD.rowcount > 0:
        print(f"Usuari amb  ID {user_id} borrat correctament.")
    else:
        print(f"No s'ha trobat cap usuari amb l'ID {user_id}.")
    # Commit de la trasnició
    connD.commit()
