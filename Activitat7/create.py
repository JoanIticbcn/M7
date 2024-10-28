# Funció per introduir,crear,insert un registre nou a la taula Users creada anteriorment
def insertUser(connexioIU, connIU):
    sql = """
        INSERT INTO users (username, email, password, is_active)
        VALUES ('Jhon', 'jhon@example.com', 1234, true);
        """
    # Executem la query de SQL i fem els canvis permanents amb el commit
    connexioIU.execute(sql)
    connIU.commit()
    print("S'ha introudit el registre correctament a la taula users")
