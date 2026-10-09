# Fiche de sensibilisation — repérer et signaler un phishing

## Les signaux d'alerte
- **Email :** expéditeur ou domaine légèrement différent, urgence inhabituelle, lien inattendu, pièce jointe non sollicitée, fautes ou demande de secret.
- **SMS :** numéro inconnu, URL raccourcie, menace de blocage, demande de paiement ou de code.
- **QR code :** destination masquée avant le scan, autocollant suspect posé sur un code officiel, page demandant de se reconnecter sans raison.
- **Faux message type :** « Votre compte sera suspendu dans 30 minutes. Confirmez immédiatement votre identité via ce lien. » L'urgence artificielle et la demande de connexion par un lien reçu sont des signaux d'alerte.

## Les bons réflexes
1. Ne pas cliquer, scanner ou ouvrir la pièce jointe.
2. Ne jamais communiquer mot de passe, code MFA ou code de récupération.
3. Vérifier l'adresse du site en passant par un favori ou le portail officiel, pas par le lien du message.
4. Signaler rapidement le message au canal informatique/SOC officiel ; conserver le message selon la procédure interne.
5. Si un lien a été ouvert ou des identifiants saisis, prévenir immédiatement l'équipe sécurité depuis un canal connu. Ne pas effacer les preuves.
6. Activer le MFA et utiliser un gestionnaire de mots de passe approuvé.
7. Ne pas transférer le message suspect à des collègues pour « demander leur avis ».

## Procédure de réponse à incident
**Détecter → Signaler → Qualifier → Contenir → Remédier → Clôturer**
- Détecter : noter l'heure, le canal et les indices sans interagir davantage.
- Signaler : utiliser le canal officiel prévu par l'organisation.
- Qualifier : l'analyste évalue le risque et la gravité à partir des éléments disponibles.
- Contenir : si nécessaire, bloquer l'URL ou isoler un poste selon la procédure autorisée ; révoquer les sessions et réinitialiser les secrets compromis via le canal officiel.
- Remédier : supprimer le message selon la procédure, analyser les traces autorisées et appliquer les correctifs.
- Clôturer : documenter les actions, notifier les personnes concernées et tirer les enseignements.

## Exemple d'enregistrement dans CyberSec Incident Manager
- Titre : `Suspicion de phishing — faux avis de suspension`
- Catégorie : `Phishing`
- Gravité : `Élevée` (à ajuster après qualification)
- Description : `Message fictif menaçant de suspendre le compte sous 30 minutes et demandant une confirmation via un lien. Aucun lien ouvert dans le scénario de démonstration.`
- Statut initial : `Nouveau`

Cette fiche est destinée à la sensibilisation. Elle ne remplace pas la procédure interne de sécurité.
