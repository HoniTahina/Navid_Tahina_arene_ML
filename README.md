# Arène des Algos Machine Learning
## Prédiction de noshow médical

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