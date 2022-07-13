import sqlite3

nome_banco = "boardgame.db"
con = sqlite3.connect(nome_banco)
cur = con.cursor()
# id INTEGER, como jogar TEXT, idade INTEGER, preco REAL
boardgame = [
    (None,'zombicide','RPG', 12, 400.00),
    (None,'Dixit','Tabuleiro', 10, 250.00),
    (None,'Banco Imobiliario', 'Tabuleiro', 10, 80.00),
    (None,'Cashn Guns','Tabuleiro',10, 215.00)
    ]
cur.executemany("INSERT INTO boardgame VALUES (?, ?, ?, ?, ?)",boardgame)

con.commit()
con.close()