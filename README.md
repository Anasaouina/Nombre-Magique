# 🎮 Jeu "Nombre Magique" - Client/Serveur en Python

Ce projet est un jeu en réseau où le client doit deviner un **nombre magique** généré aléatoirement par le serveur.

## 💠 Technologies utilisées

* Python 3.13.1
* Sockets TCP (`socket`)
* Communication entre deux machines sur le même réseau (LAN)

## 📦 Fichiers inclus

* `server_game.py` : Code du serveur qui génère le nombre magique et traite les réponses.
* `client.py` : Code du client qui envoie les propositions et reçoit les indices.

## 🚀 Comment exécuter le projet

### 1. Lancer le serveur

Sur la machine serveur (qui héberge `server_game.py`) :

```bash
python server_game.py
```

Le serveur démarre, génère un nombre magique entre 1 et 100, et attend la connexion d’un client.

### 2. Lancer le client

Sur une autre machine du réseau (ou la même pour un test local) :

```bash
python client.py
```

Assurez-vous de modifier l'adresse IP dans `client.py` si le serveur est sur une autre machine :

```python
serverAddress = ('172.16.20.201', 9090)  # Remplacer par l'IP réelle du serveur
```

## 🎯 Règles du jeu

* Le serveur génère un nombre entre 1 et 100.
* Le client envoie des propositions numériques.
* Le serveur répond avec :

  * "0" → Le nombre proposé est trop petit.
  * "1" → Le nombre proposé est trop grand.
  * "2" → Bingo ! Le nombre est trouvé.

Le client continue jusqu'à ce qu’il trouve le bon nombre.

## 💬 Exemple d’interaction

**Serveur :**

```
Nombre magique choisi : 42
Connexion de ('172.16.20.5', 50432)
```

**Client :**

```
Entrer un nombre : 25
Trop petit ! Essayez encore.
Entrer un nombre : 80
Trop grand ! Essayez encore.
Entrer un nombre : 42
Bravo ! Vous avez trouvé le nombre magique 🎉
Fin du jeu.
```

## ✅ Conditions de réussite

* Le client reçoit un retour correct à chaque tentative.
* Le jeu se termine lorsque le nombre est deviné.
* Aucune erreur n’interrompt l’échange.

## 📈 Améliorations futures possibles

* Prise en charge de plusieurs clients (multi-threading)
* Limitation du nombre de tentatives
* Affichage du score ou du nombre d’essais
* Interface graphique (Tkinter ou PyQt)
* Version web (avec Flask ou Django)

---

## 🔒 Remarque réseau

* Le pare-feu Windows ou de votre système peut bloquer le port 9090. Autorisez-le si nécessaire.
* Pour des tests locaux, vous pouvez utiliser `localhost` ou `127.0.0.1`.
* Pour des tests sur 2 machines, assurez-vous qu'elles sont bien sur le même réseau local.

---

© 2025 - Projet pédagogique Python Socket – Jeu du Nombre Magique
