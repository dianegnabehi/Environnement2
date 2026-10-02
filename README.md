# Environnement2

Simulation en Python d'un système intelligent de régulation thermique : un
environnement qui produit les températures extérieures d'une journée complète
et un système expert qui pilote chauffage et climatisation pour maintenir la
maison entre deux seuils de confort définis par l'utilisateur.

## Aperçu

Le projet se compose de deux scripts :

- **environment.py** : simule l'évolution de la température extérieure sur
  24 heures (48 relevés, un toutes les 30 minutes). La température de départ
  est tirée au hasard dans la plage de la saison, puis chaque tranche applique :
  - une variation sinusoïdale (amplitude de 5 °C) pour reproduire le cycle
    jour/nuit ;
  - un bruit aléatoire de ±1 °C pour l'irrégularité naturelle.

  Les relevés sont arrondis à deux décimales et affichés un par un.

- **expert_system.py** : exécute environment.py (saison `spring`), capture ses
  relevés via un sous-processus, puis ajuste la température intérieure pour la
  maintenir dans la plage de confort. À chaque relevé, une action est décidée :

  | Situation | Action | Effet sur la maison |
  |---|---|---|
  | Intérieur < seuil min | `heating` | +0.5 °C |
  | Intérieur > seuil max | `cooling` | −0.5 °C |
  | Dans la plage de confort | `nothing` | dérive de 0.25 °C vers l'extérieur |

  Chaque ligne affiche la température extérieure, l'action décidée et la
  température intérieure. La simulation s'arrête automatiquement après
  48 secondes.

## Prérequis

- Python 3.8 ou supérieur
- Aucune dépendance externe (uniquement `sys`, `time`, `random`, `math`,
  `subprocess` et `re`)

## Installation

```bash
git clone git@github.com:dianegnabehi/Environnement2.git
cd Environnement2
```

## Utilisation

Lancer le système expert avec deux seuils en degrés Celsius :

```bash
python3 expert_system.py 19 22
```

Exemple de sortie :

```
External temperature: 12.34 | Action: heating | In-house temperature: 12.34
External temperature: 12.87 | Action: heating | In-house temperature: 12.84
External temperature: 13.20 | Action: heating | In-house temperature: 13.34
...
External temperature: 15.02 | Action: nothing | In-house temperature: 19.12
```

Il est aussi possible de lancer la simulation seule :

```bash
python3 environment.py spring
```

Saisons acceptées :

| Saison | Mot-clé | Numéro | Plage de base |
|---|---|---|---|
| Hiver | `winter` | 1 | −5 – 10 °C |
| Printemps | `spring` | 2 | 10 – 20 °C |
| Été | `summer` | 3 | 20 – 35 °C |
| Automne | `autumn` / `fall` | 4 | 10 – 20 °C |

Toute autre valeur lève une `ValueError` affichée proprement dans la console.

## Structure du projet

```
.
├── environment.py    # Simulation de la température extérieure
├── expert_system.py  # Système expert de régulation
├── README.md         # Documentation du projet
├── .gitignore        # Fichiers exclus du dépôt
└── LICENSE           # Licence MIT
```

## Fonctions principales

| Fichier | Fonction | Rôle |
|---|---|---|
| environment.py | `get_season_temperature_range(season)` | Renvoie la plage (min, max) associée à une saison. |
| environment.py | `simulate_temperature(season)` | Génère et affiche les 48 relevés d'une journée. |
| environment.py | `main()` | Point d'entrée : lit la saison en argument. |
| expert_system.py | `regulate_temperature(min, max, temps)` | Ajuste la température intérieure à chaque relevé. |
| expert_system.py | bloc `__main__` | Lance le sous-processus et extrait les températures par regex. |

## Auteur

Diane Gnabehi — projet 42 Paris.

## Licence

Ce projet est distribué sous licence MIT — voir le fichier LICENSE.
