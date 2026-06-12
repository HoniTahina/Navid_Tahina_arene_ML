# Arène des Algos Machine Learning
## Prédiction de noshow médical

### Document de conception
Contexte : On remarque des patients qui ne viennent pas à leur(s) rendez-vous. Cela peut poser problème pour les professionnels de santé qui programment les rendez-vous et si besoin, leur envoie des SMS de confirmation/rappel. On souhaite donc prédir si, en fonction d'un type profil et de son historique, un patient X va manquer à son rendez-vous. On affichera une probabilité de no-show.

Cela s'inscrit dans le cadre d'une classification binaire : show/no-show.

Avec ce modèle, cela aidera les professionnels de santé à optimiser la planification des rendez-vous et réduire les créneaux perdus

Dataset : Medical Appointment No Shows(Kaggle), 110K lignes, 14 colonnes, 2 classes de no-show (Yes/No).
Répartition déquilibrée. Il faut utiliser un split stratifié afin de conserver la même proportion de classes dans les ensembles train, validation et test. Avec un déséquilibre ~80/20, l'accuracy seule est trompeuse. Il faut donc privilégier recall, précision, F1-score

Les algos candidats (l'Arène) : RégressionLogistique (baseline interprétable) + RandomForest (robuste, peu de
tuning) + GradientBoosting (bon candidat sur format structuré)

Plan d'évaluation des métriques :
- recall dans l'objectif détecter un maximum de patients absents
- précision pour optimiser l'utilisation des ressources de suivi en ciblant prioritairement les patients réellement à risque d'absence.
- F1-score pour équilibrer précision et rappel.

Répartition des rôles : 
- chargement et nettoyage des données : Navid + Tahina --> justification : gain de temps pour les étapes suivantes
- monter l'Arène : Navid
- code la WebApp : Tahina
- prépare la soutenance : Navid + Tahina

Questions ouvertes : pas pour l'instant.

### Pré-requis

1. Créer un environnement virtuel : `navid_tahina_python venv arene_ml_venv` puis l'activer : `.\navid_tahina_arene_ml_venv\Scripts\Activate.ps1`ou commande similaire selon votre terminal/OS
2. Installer les librairies nécessaires : `pip install -r requirements.txt`

### Résultats

📊 Leaderboard

| Modèle               | Accuracy | Recall  | Precision | F1-score |
|---------------------|----------|---------|-----------|----------|
| Gradient Boosting   | 79.81%   | 0.43%   | 51.35%    | 0.84%    |
| Random Forest       | 76.17%   | 19.87%  | 34.42%    | 25.20%   |
| Logistic Regression | 66.91%   | 57.08%  | 32.07%    | 41.06%   |



🏆 Modèle retenu (Champion)
**Logistic Regression**

✔ Meilleur recall

✔ Meilleure détection des no-shows

✔ Meilleur optimisation coût métier

### Évaluation et utilisation du modèle final
📦 Pipeline final

Le modèle final est encapsulé dans un pipeline sklearn :
- StandardScaler
- LogisticRegression (class_weight="balanced")

📈 Matrice de confusion

La performance du modèle est analysée via une matrice de confusion pour évaluer :
- Faux négatifs (patients absents non détectés)
- Faux positifs (fausses alertes)

💾 Sauvegarde du modèle et déploiement dans la WepApp

Le pipeline complet est sérialisé avec joblib, puis chargé dans la WebApp.


🌐 WebApp de démonstration

Une application web interactive a été développée afin de permettre la prédiction des no-shows à partir des informations saisies par l’utilisateur.


🔗 Accès à l’application

[Prédiction de noshow médical](https://yin-deserving-fifth.ngrok-free.dev)