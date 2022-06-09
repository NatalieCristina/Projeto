import sqlite3
from flask import Flask, jsonify
from flask_cors import CORS

def pega_conexao():
    nome_site = "Next_Game"
    con = sqlite3.connect(nome_site)
    return con

# Aplicação web com Flask
app = Flask(__name__)
CORS(app)
@app.route("/")
def raiz():
    return "Resposta do meu backend em Python!"

@app.route("/todos")
def todos():
    con = pega_conexao()
    cur = con.cursor()
    cur.execute("SELECT * FROM Game")
    try:
        cur.execute("SELECT * FROM Game WHERE")
    except:
        con.close()
        return jsonify("Jogo não encontrado")
    jogos = cur.fetchall()
    con.close()
    return jsonify(dados)

@app.route("/lista/<int:id>") # http://127.0.0.1:5000/lista/1
def lista_um(id):
    con = pega_conexao()
    cur = con.cursor()
    cur.execute(f"SELECT * FROM Game WHERE id={id}")

    try:
        cur.execute("SELECT * FROM Game WHERE")
    except:
        con.close()
        return jsonify("Jogo não encontrado")
           
    jogos = cur.fetchone()
    con.close()
    return jsonify(jogos)
app.run()

