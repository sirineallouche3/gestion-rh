
import json
import os

DOSSIER_DATA = "data"


def charger_donnees(nom_fichier):
    """Charger les données depuis un fichier JSON."""

    chemin = os.path.join(DOSSIER_DATA, nom_fichier)

    try:
        with open(chemin, "r", encoding="utf-8") as fichier:
            return json.load(fichier)

    except FileNotFoundError:
        print(f"Fichier {nom_fichier} introuvable.")
        return []

    except json.JSONDecodeError:
        print(f"Erreur : le fichier {nom_fichier} est invalide.")
        return []

def sauvegarder_donnees(nom_fichier, donnees):
    """Sauvegarder les données dans un fichier JSON."""

    os.makedirs(DOSSIER_DATA, exist_ok=True)

    chemin = os.path.join(DOSSIER_DATA, nom_fichier)

    with open(chemin, "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, indent=4, ensure_ascii=False)
