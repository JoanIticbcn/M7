# Funció que crea una taula a la base de dades de la connexio pasada com a parametre en POSTGRESQL
def createTable(connexioCT, connCT):
    sql = """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,         -- Unique ID for each user, auto-incremented
            username VARCHAR(50) NOT NULL, -- Username field, required
            email VARCHAR(100) NOT NULL,   -- Email field, required
            password VARCHAR(100) NOT NULL,-- Password field, required
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when user was created
            is_active BOOLEAN DEFAULT TRUE -- Indicates if the user is active
        );
        """
    # Executem la query de SQL i fem els canvis permanents amb el commit
    connexioCT.execute(sql)
    connCT.commit()
    print("Taula users creada exitosament amb els seguents camps: id,username,email,password,created_at,is_active")
