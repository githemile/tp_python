import os
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter


"""
Utilisant la fonction os.walk() du chapitre 10, écrivez un script qui parcourra chaque fichier PDF dans un dossier
 (et ses sous-dossiers) et cryptera les PDF en utilisant un mot de passe fourni en ligne de commande. 
 Enregistrez chaque PDF crypté en ajoutant un suffixe _encrypted.pdf au nom de fichier original. 
 
Ensuite, écrivez un programme qui trouve tous les PDFs cryptés dans un dossier (et ses sous-dossiers) et crée une copie
 décryptée du PDF en utilisant un mot de passe fourni. Si le mot de passe est incorrect, le programme devrait imprimer
  un message à l'utilisateur et passer au PDF suivant.


"""

def encrypt_pdf(chemin_entree, chemin_sortie, mot_de_passe):
    """
    Fonction pour crypter un fichier PDF avec un mot de passe donné.

    Args:
        chemin_entree (str): Chemin vers le fichier PDF d'entrée.
        chemin_sortie (str): Chemin vers le fichier PDF de sortie crypté.
        mot_de_passe (str): Mot de passe pour le cryptage.
    """
    try:
        # Ouvrir le fichier PDF en mode lecture binaire
        with open(chemin_entree, 'rb') as fichier_entree:
            # Créer un objet PdfFileReader pour lire le fichier PDF
            lecteur = PdfFileReader(fichier_entree)
            # Créer un objet PdfFileWriter pour écrire le fichier PDF de sortie
            redacteur = PdfFileWriter()

            # Parcourir chaque page du PDF d'entrée et l'ajouter au rédacteur
            for num_page in range(lecteur.numPages):
                redacteur.addPage(lecteur.getPage(num_page))

            # Crypter le fichier PDF avec le mot de passe fourni
            redacteur.encrypt(mot_de_passe)

            # Enregistrer le fichier PDF crypté
            with open(chemin_sortie, 'wb') as fichier_sortie:
                redacteur.write(fichier_sortie)

        # Afficher un message de confirmation
        print(f"PDF crypté : {chemin_sortie}")
    except Exception as e:
        # En cas d'erreur, afficher un message d'erreur
        print(f"Échec de cryptage pour {chemin_entree} : {e}")


def crypter_pdfs_dans_dossier(dossier, mot_de_passe):
    """
    Fonction pour crypter tous les fichiers PDF dans un dossier et ses sous-dossiers.

    Args:
        dossier (str): Chemin vers le dossier contenant les fichiers PDF.
        mot_de_passe (str): Mot de passe pour le cryptage.
    """
    # Parcourir tous les fichiers et sous-dossiers dans le dossier spécifié
    for root, dirs, files in os.walk(dossier):
        for fichier in files:
            # Vérifier si le fichier est un fichier PDF
            if fichier.endswith(".pdf"):
                # Construire les chemins d'entrée et de sortie
                chemin_entree = os.path.join(root, fichier)
                chemin_sortie = os.path.join(root, f"{os.path.splitext(fichier)[0]}_crypte.pdf")
                # Appeler la fonction pour crypter le fichier PDF
                encrypt_pdf(chemin_entree, chemin_sortie, mot_de_passe)


if __name__ == "__main__":
    # Vérifier si le nombre d'arguments est correct
    if len(sys.argv) != 3:
        print("Utilisation : python script.py <chemin_vers_le_dossier> <mot_de_passe>")
        sys.exit(1)

    # Récupérer les arguments en ligne de commande
    chemin_dossier = sys.argv[1]
    mot_de_passe = sys.argv[2]

    # Appeler la fonction pour crypter les PDFs dans le dossier spécifié
    crypter_pdfs_dans_dossier(chemin_dossier, mot_de_passe)

# pour executer
# python script.py chemin_vers_le_dossier mot_de_passe
