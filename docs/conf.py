from pathlib import Path

project = "OC Lettings FR"
author = "Stevi"
release = "1.0"

extensions = [
    "sphinx.ext.autosectionlabel",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "fr"

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
