# CyberSec Incident Manager — V1 améliorée

Projet pédagogique Master 1 : application locale de suivi d'incidents fictifs avec Flask et SQLite.

## Fonctionnalités
- Déclaration d'incidents avec validation côté serveur.
- Catégories, gravités et statuts contrôlés par listes autorisées.
- Mise à jour du statut.
- Filtres par statut et gravité.
- Indicateurs : ouverts, critiques non résolus, résolus.
- Requêtes SQL paramétrées et tests automatisés.

## Installation (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```
Puis ouvrir http://127.0.0.1:5000.

## Lancer les tests
À la racine du dépôt :
```powershell
python -m unittest discover -s tests -v
```
Les tests utilisent une base temporaire et ne doivent pas modifier la base de démonstration.

## Vérification des dépendances
```powershell
python -m pip install pip-audit
python -m pip_audit
```
Conserver la sortie réelle dans le compte rendu. Un audit n'est pas une preuve d'absence absolue de vulnérabilités.

## Parcours de démonstration
1. Ouvrir la page d'accueil et photographier les indicateurs.
2. Créer un incident fictif valide.
3. Tester un titre vide et une description trop longue.
4. Filtrer par gravité.
5. Changer le statut d'un incident.
6. Lancer les tests automatisés et capturer la sortie.

## Limites et sécurité
- Application prévue pour un usage local uniquement (`127.0.0.1`).
- Pas d'authentification ni d'autorisation robuste : ne pas exposer sur Internet.
- `SECRET_KEY` de démonstration à remplacer si l'application évolue.
- Utiliser uniquement des données fictives ; aucun secret ou donnée personnelle réelle.
- Une mise en production nécessiterait notamment authentification, contrôle d'accès par rôle, protection CSRF, journalisation sécurisée, gestion des secrets et configuration de déploiement adaptée.

## Organisation Scrum et preuves
Voir `docs/PLAN_TP_ET_CAPTURES.md`, `docs/MATRICE_RISQUES.md` et `docs/PHISHING.md`.
Les captures du dépôt/Project/Issues/PR doivent être prises sur GitHub après réalisation effective de ces actions ; elles ne sont pas simulées dans ce dépôt.
