# Scraper RSS Intelligent

## Objectif
Ce projet a pour but de scanner des centaines de flux RSS pour y repérer automatiquement les articles contenant certains mots-clés définis par l'utilisateur.

## Fichiers du projet
- "rss_list.txt" → contient la liste de plus de 1900 flux RSS à analyser.
- "mots_cles.txt" → fichier texte avec un mot-clé par ligne.
- "notebook_scraper_ilies_final.py" → script principal à exécuter.
- "resultat.txt" → fichier généré contenant les articles pertinents trouvés.

## Installation
Assurez-vous d'avoir Python 3 installé sur votre machine.

Puis installez la bibliothèque nécessaire :

```bash
pip install feedparser
```

## Utilisation
1. Placez vos mots-clés dans un fichier nommé "mots_cles.txt" (ex : "cyber", "piratage", "hacking").
2. Assurez-vous que les fichiers "rss_list.txt", "mots_cles.txt" et le script ".py" sont dans le même dossier.
3. Exécutez le script :
```bash
python notebook_scraper_Ilies_BOUDHAN.py
```

## Fonctionnement
Le script :
- Charge les flux RSS à partir de "rss_list.txt"
- Utilise "feedparser" pour récupérer les titres, descriptions, dates et liens des articles
- Filtre les articles qui contiennent au moins un des mots-clés
- Affiche les articles trouvés dans la console
- Enregistre les résultats dans un fichier "resultat.txt" sous la forme :

```
[Titre de l'article]
[Date de publication]
[URL]
Mot-clé : [mot]
```


## Exemple de mots_cles.txt
```
Nutella
```

## Résultat
Le fichier "resultat.txt" contiendra tous les articles pertinents trouvés selon les mots-clés.

## Auteur
Projet réalisé par Ilies BOUDHAN