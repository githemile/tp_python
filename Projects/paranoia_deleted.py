import os
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

"""
Avant de supprimer le fichier original, le programme devrait tenter de lire et de décrypter le fichier pour s'assurer
  qu'il a été correctement crypté.
"""
def encrypt_pdf(chemin_entree, chemin_sortie, mot_de_passe):
    """
    Fonction pour crypter un fichier PDF avec un mot de passe donné et vérifier si le cryptage est réussi.

    Args:
        chemin_entree (str): Chemin vers le fichier PDF d'entrée.
        chemin_sortie (str): Chemin vers le fichier PDF de sortie crypté.
        mot_de_passe (str): Mot de passe pour le cryptage.
    """
    try:
        with open(chemin_entree, 'rb') as fichier_entree:
            lecteur = PdfFileReader(fichier_entree)
            redacteur = PdfFileWriter()

            for num_page in range(lecteur.numPages):
                redacteur.addPage(lecteur.getPage(num_page))

            redacteur.encrypt(mot_de_passe)

            with open(chemin_sortie, 'wb') as fichier_sortie:
                redacteur.write(fichier_sortie)

        print(f"PDF crypté : {chemin_sortie}")

        # Vérifier si le cryptage est réussi en essayant de lire et de décrypter le fichier
        with open(chemin_sortie, 'rb') as fichier_crypte:
            lecteur_crypte = PdfFileReader(fichier_crypte)
            if lecteur_crypte.isEncrypted:
                lecteur_crypte.decrypt(mot_de_passe)
                if lecteur_crypte.getNumPages() == lecteur.getNumPages():
                    print("Cryptage réussi.")
                    # Supprimer le fichier PDF original
                    os.remove(chemin_entree)
                    print(f"Fichier original supprimé : {chemin_entree}")
                else:
                    print("Échec de vérification du cryptage.")
    except Exception as e:
        print(f"Échec de cryptage pour {chemin_entree} : {e}")

def crypter_pdfs_dans_dossier(dossier, mot_de_passe):
    """
    Fonction pour crypter tous les fichiers PDF dans un dossier et ses sous-dossiers.

    Args:
        dossier (str): Chemin vers le dossier contenant les fichiers PDF.
        mot_de_passe (str): Mot de passe pour le cryptage.
    """
    for root, dirs, files in os.walk(dossier):
        for fichier in files:
            if fichier.endswith(".pdf"):
                chemin_entree = os.path.join(root, fichier)
                chemin_sortie = os.path.join(root, f"{os.path.splitext(fichier)[0]}_crypte.pdf")
                encrypt_pdf(chemin_entree, chemin_sortie, mot_de_passe)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Utilisation : python script.py <chemin_vers_le_dossier> <mot_de_passe>")
        sys.exit(1)

    chemin_dossier = sys.argv[1]
    mot_de_passe = sys.argv[2]

    crypter_pdfs_dans_dossier(chemin_dossier, mot_de_passe)
