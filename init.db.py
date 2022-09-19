import sqlite3 as sql

con = sql.connect("problemas.db")

with open('schema.sql') as f:
    con.executescript(f.read())

cur = con.cursor()

cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
            ('Aluno', 'PI-II')
            )
cur.execute("INSERT INTO poste(codigo, rua, bairro, cidade)"
            "VALUES(?, ?, ?, ?)",
            ('PI-II Poste 0001', 'Luis Pereira de Campos', 'Vila Itapanhaú', 'Bertioga - SP')
            )

con.commit()
con.close()
