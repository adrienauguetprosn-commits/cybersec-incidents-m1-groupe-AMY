# Matrice de risques (scénarios pédagogiques)

Échelle indicative : vraisemblance et impact de 1 (faible) à 3 (fort). Niveau = produit ; 1–2 faible, 3–4 moyen, 6–9 élevé.

| Menace/scénario | Vraisemblance | Impact | Niveau | Mesures de réduction |
|---|---:|---:|---|---|
| Saisie de champs invalides ou excessifs | 3 | 2 | 6 — Élevé | Validation côté serveur, limites de longueur, listes autorisées, tests |
| Injection SQL par une entrée utilisateur | 2 | 3 | 6 — Élevé | Requêtes paramétrées, tests de régression |
| Accès non autorisé aux incidents | 2 | 3 | 6 — Élevé | Limiter à localhost ; pour une évolution, authentification et rôles |
| Divulgation de détails techniques dans une erreur | 2 | 2 | 4 — Moyen | Messages génériques côté utilisateur, logs maîtrisés |
| Collaborateur clique sur un lien de phishing | 3 | 3 | 9 — Élevé | Sensibilisation, MFA, vérification du domaine, signalement rapide |
| Dépendance Python vulnérable | 2 | 2 | 4 — Moyen | `pip-audit`, mises à jour contrôlées et suivi des avis |

Cette matrice est une évaluation pédagogique initiale, à réviser selon le contexte et les constats réels.
