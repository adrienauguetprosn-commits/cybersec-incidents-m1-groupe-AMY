from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from pathlib import Path

app = Flask(__name__)
DB = Path(__file__).with_name("incidents.db")

def connect():
    db = sqlite3.connect(DB)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    with connect() as db:
        db.execute("CREATE TABLE IF NOT EXISTS incidents (id INTEGER PRIMARY KEY AUTOINCREMENT, titre TEXT NOT NULL, categorie TEXT NOT NULL, gravite TEXT NOT NULL, statut TEXT NOT NULL DEFAULT 'Nouveau')")
        if db.execute("SELECT COUNT(*) FROM incidents").fetchone()[0] == 0:
            db.executemany("INSERT INTO incidents(titre,categorie,gravite,statut) VALUES(?,?,?,?)", [
                ("Email suspect", "Phishing", "Moyenne", "Nouveau"),
                ("Connexion inhabituelle", "Compte", "Élevée", "En cours"),
                ("Poste à examiner", "Poste", "Faible", "Résolu")])
        db.commit()

@app.get("/")
def index():
    with connect() as db:
        incidents = db.execute("SELECT * FROM incidents ORDER BY id DESC").fetchall()
    return render_template("index.html", incidents=incidents)

@app.post("/incidents")
def add_incident():
    # Version pédagogique volontairement incomplète : contrôles métier à ajouter.
    titre = request.form.get("titre", "")
    categorie = request.form.get("categorie", "")
    gravite = request.form.get("gravite", "")
    with connect() as db:
        db.execute("INSERT INTO incidents(titre,categorie,gravite,statut) VALUES(?,?,?,?)", (titre,categorie,gravite,"Nouveau"))
        db.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="127.0.0.1", port=5000)
