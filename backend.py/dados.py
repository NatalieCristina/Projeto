import sqlite3

nome_banco = "boardgame"
con = sqlite3.connect("boardgame")
cur = con.cursor()
# id INTEGER, como jogar TEXT, idade INTEGER, preco REAL
Jogos = [
    ('zombicide', 'RPG', 12,  400.00,),
    ('Dixit', 'Tabuleiro', 10 ,250.00,),
    ('Banco Imobiliario', 'Tabuleiro', 10,  80.00,)
    ('Cashn Guns','Tabuleiro',10, 215,00)
    ]

cur.executemany("INSERT INTO Boardgame VALUES (?, ?, ?, ?,?)", "boardgame")

con.commit()
con.close()