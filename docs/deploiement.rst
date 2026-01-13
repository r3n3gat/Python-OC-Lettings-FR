Déploiement
===========

CI (GitHub Actions)
-------------------

- Lint (flake8)
- Tests + coverage
- Build Docker + push (si configuré)

Render (build depuis le repo)
-----------------------------

- Push sur la branche suivie
- Render reçoit le webhook
- Render clone le repo, build, puis redémarre le service

Read the Docs
-------------

- Read the Docs build la doc à partir du fichier ``.readthedocs.yaml``.
