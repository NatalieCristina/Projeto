import sqlite3

nome_banco = "Boardgame"
con = sqlite3.connect(nome_banco)
cur = con.cursor()
# id INTEGER, como jogar TEXT, idade INTEGER, preco REAL
Jogos = [
    (None, 'zombicide', 'RPG', 400.00,),
    (None, 'Dixit', 'Tabuleiro',250.00, 1),
    (None, 'Banco Imobiliario', 'Tabuleiro', 80.00, 1)
]

cur.executemany("INSERT INTO Boardgame VALUES (?, ?, ?, ?, ?, ?)", 'boardgame')

con.commit()
con.close() 