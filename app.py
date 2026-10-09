from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.config["SECRET_KEY"] = "local-demo-only-change-me"
DB = Path(__file__).with_name("incidents.db")
TITRE_MAX = 120
DESCRIPTION_MAX = 2000
CATEGORIES = {"Phishing", "Compte", "Poste", "Réseau", "Autre"}
GRAVITES = {"Faible", "Moyenne", "Élevée", "Critique"}
STATUTS = {"Nouveau", "En cours", "En revue", "Résolu"}

def connect():
    db = sqlite3.connect(DB)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    with connect() as db:
        db.execute("""CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            description TEXT NOT NULL DEFAULT '',
            categorie TEXT NOT NULL,
            gravite TEXT NOT NULL,
            statut TEXT NOT NULL DEFAULT 'Nouveau',
            responsable TEXT NOT NULL DEFAULT 'Non affecté',
            created_at TEXT NOT NULL DEFAULT (datetime('now'))
        )""")
        db.commit()

@app.get("/")
def index():
    statut = request.args.get("statut", "")
    gravite = request.args.get("gravite", "")
    if statut and statut not in STATUTS:
        statut = ""
    if gravite and gravite not in GRAVITES:
        gravite = ""
    query = "SELECT * FROM incidents WHERE 1=1"
    params = []
    if statut:
        query += " AND statut = ?"
        params.append(statut)
    if gravite:
        query += " AND gravite = ?"
        params.append(gravite)
    query += " ORDER BY id DESC"
    with connect() as db:
        incidents = db.execute(query, params).fetchall()
        stats = {
            "ouverts": db.execute("SELECT COUNT(*) FROM incidents WHERE statut != 'Résolu'").fetchone()[0],
            "critiques": db.execute("SELECT COUNT(*) FROM incidents WHERE gravite = 'Critique' AND statut != 'Résolu'").fetchone()[0],
            "resolus": db.execute("SELECT COUNT(*) FROM incidents WHERE statut = 'Résolu'").fetchone()[0],
        }
    return render_template("index.html", incidents=incidents, stats=stats,
                           statuts=sorted(STATUTS), gravites=sorted(GRAVITES),
                           categories=sorted(CATEGORIES), selected_statut=statut,
                           selected_gravite=gravite)

@app.post("/incidents")
def add_incident():
    titre = request.form.get("titre", "").strip()
    description = request.form.get("description", "").strip()
    categorie = request.form.get("categorie", "")
    gravite = request.form.get("gravite", "")
    errors = []
    if not titre:
        errors.append("Le titre est obligatoire.")
    elif len(titre) > TITRE_MAX:
        errors.append(f"Le titre ne doit pas dépasser {TITRE_MAX} caractères.")
    if len(description) > DESCRIPTION_MAX:
        errors.append(f"La description ne doit pas dépasser {DESCRIPTION_MAX} caractères.")
    if categorie not in CATEGORIES:
        errors.append("La catégorie sélectionnée est invalide.")
    if gravite not in GRAVITES:
        errors.append("La gravité sélectionnée est invalide.")
    if errors:
        for error in errors:
            flash(error, "error")
        return redirect(url_for("index")), 400
    with connect() as db:
        db.execute("""INSERT INTO incidents(titre, description, categorie, gravite, statut)
                      VALUES (?, ?, ?, ?, 'Nouveau')""",
                   (titre, description, categorie, gravite))
        db.commit()
    flash("Incident ajouté avec succès.", "success")
    return redirect(url_for("index"), code=303)

@app.post("/incidents/<int:incident_id>/statut")
def update_status(incident_id):
    statut = request.form.get("statut", "")
    if statut not in STATUTS:
        flash("Le statut sélectionné est invalide.", "error")
        return redirect(url_for("index")), 400
    with connect() as db:
        cursor = db.execute("UPDATE incidents SET statut = ? WHERE id = ?", (statut, incident_id))
        db.commit()
    if cursor.rowcount == 0:
        flash("Incident introuvable.", "error")
        return redirect(url_for("index")), 404
    flash("Statut mis à jour.", "success")
    return redirect(url_for("index"), code=303)

@app.errorhandler(500)
def internal_error(_error):
    return "Une erreur interne est survenue. Réessayez ou contactez l’administrateur.", 500

if __name__ == "__main__":
    init_db()
    # Application pédagogique locale uniquement : ne pas exposer sur Internet.
    app.run(debug=False, host="127.0.0.1", port=5000)
