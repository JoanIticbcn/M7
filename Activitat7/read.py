# Funció que llegeix tots els registres de la taula users i els mostra per pantalla
def read(connexioR):
    # Defineix la query del select
    select_query = "SELECT * FROM users;"
    # Executa la query
    connexioR.execute(select_query)
    # Fetch de totes les columnes del resultat
    rows = connexioR.fetchall()
    print("Registres de la taula users:")
    # Imprimeix cada columa linia a linia
    for row in rows:
        print(row)
