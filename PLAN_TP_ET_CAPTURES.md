# Plan de TP et guide des captures

**Règle de preuve :** faire des captures datées à partir de l'environnement réel. Nommer les fichiers `C01_...png`, etc. Ne pas retoucher les résultats. Pour chaque capture, ajouter dans le rapport : objectif, manipulation, résultat observé, interprétation.

## Phase 1 — Analyse et installation
- **C01** — dépôt GitHub et arborescence des fichiers.
- **C02** — terminal : création/activation de l'environnement virtuel et installation (`pip install -r requirements.txt`).
- **C03** — terminal montrant `python app.py`, puis navigateur sur `http://127.0.0.1:5000`.
- **C04** — page d'accueil avec les trois indicateurs et le formulaire.
- **C05** — diagnostic V1 : citer les éléments observés dans la version initiale (validation incomplète, statuts non modifiables, filtres absents, absence d'authentification).

## Phase 2 — Scrum/GitHub
- **C06** — Product Backlog avec US01–US08 et priorités.
- **C07** — GitHub Project Board avec Todo, In Progress, In Review, Done.
- **C08** — Issue d'une User Story avec critères d'acceptation, priorité, estimation et responsable.
- **C09** — branche de fonctionnalité et commits descriptifs.
- **C10** — Pull Request liée à l'Issue, revue réelle et fusion après approbation.
- **C11** — Board Sprint 1 après review.
- **C12** — backlog repriorisé après la demande du Product Owner pour le Sprint 2.

## Phase 3 — Tests fonctionnels et sécurité
- **C13** — création d'un incident valide affiché dans le tableau.
- **C14** — test de titre vide : message de validation et absence d'enregistrement.
- **C15** — test gravité inconnue : requête rejetée (preuve automatisée dans la sortie unittest).
- **C16** — description de plus de 2 000 caractères rejetée.
- **C17** — statut invalide rejeté.
- **C18** — filtre gravité/statut appliqué.
- **C19** — mise à jour d'un statut et indicateurs cohérents.
- **C20** — terminal : sortie complète de `python -m unittest discover -s tests -v`.
- **C21** — terminal : sortie de `python -m pip_audit` si installé ; documenter honnêtement toute erreur d'installation ou de réseau.
- **C22** — test de régression avec chaîne ressemblant à une injection SQL : elle reste une valeur littérale, grâce aux requêtes paramétrées.

## Phase 4 — Phishing et livraison
- **C23** — fiche de sensibilisation `docs/PHISHING.md`.
- **C24** — Board final avec les statuts réels mis à jour.
- **C25** — README et arborescence finale du dépôt.

## Grille de tests
| ID | Test | Résultat attendu |
|---|---|---|
| T01 | Page d'accueil | HTTP 200, indicateurs visibles |
| T02 | Création valide | redirection 303, incident visible |
| T03 | Titre vide | HTTP 400, aucune insertion |
| T04 | Gravité inconnue | HTTP 400 |
| T05 | Description trop longue | HTTP 400 |
| T06 | Statut invalide | HTTP 400 |
| T07 | Filtre gravité | seuls les incidents correspondants sont affichés |
| T08 | Régression SQL | la chaîne est traitée comme une donnée, pas comme une requête |

## Scrum — proposition à adapter à la réalité de l'équipe
- **Sprint 1 — objectif :** fiabiliser la saisie des incidents et permettre une qualification basique.
- **Sprint 2 — objectif :** améliorer le suivi, les indicateurs, les filtres et la sensibilisation.
- Pour chaque sprint, noter la date réelle, les participants, le feedback du PO, les décisions et les actions de rétrospective. Ne pas inventer des réunions ou contributions qui n'ont pas eu lieu.
