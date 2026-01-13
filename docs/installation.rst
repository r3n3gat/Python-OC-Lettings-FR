Installation (local)
====================

Prérequis
---------

- Python 3.13+
- pip
- (optionnel) Docker Desktop

Installation
------------

1. Créer et activer un venv
2. Installer les dépendances
3. Migrer la base
4. Seeder les données
5. Lancer le serveur

Commandes (PowerShell)
----------------------

- Activer le venv : .\.venv\Scripts\Activate.ps1
- Installer : pip install -r requirements.txt
- Migrer : python manage.py migrate
- Seeder : python manage.py seed_data
- Lancer : python manage.py runserver
