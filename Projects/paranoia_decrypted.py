import os
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

def decrypt_pdf(chemin_entree, chemin_sortie, mot_de_passe):
    """
    Fonction pour décrypter un fichier PDF avec un mot de passe donné.

    Args:
        chemin_entree (str): Chemin vers le fichier PDF crypté d'entrée.
        chemin_sortie (str): Chemin vers le fichier PDF de sortie décrypté.
        mot_de_passe (str): Mot de passe pour le décryptage.
    """
    try:
        with open(chemin_entree, 'rb') as fichier_entree:
            lecteur = PdfFileReader(fichier_entree)
            if lecteur.isEncrypted:
                lecteur.decrypt(mot_de_passe)

            redacteur = PdfFileWriter()
            for num_page in range(lecteur.numPages):
                redacteur.addPage(lecteur.getPage(num_page))

            with open(chemin_sortie, 'wb') as fichier_sortie:
                redacteur.write(fichier_sortie)

        print(f"PDF décrypté : {chemin_sortie}")
    except Exception as e:
        print(f"Échec de décryptage pour {chemin_entree} : {e}")

def decrypter_pdfs_dans_dossier(dossier, mot_de_passe):
    """
    Fonction pour décrypter tous les fichiers PDF cryptés dans un dossier et ses sous-dossiers.

    Args:
        dossier (str): Chemin vers le dossier contenant les fichiers PDF cryptés.
        mot_de_passe (str): Mot de passe pour le décryptage.
    """
    for root, dirs, files in os.walk(dossier):
        for fichier in files:
            if fichier.endswith("_crypte.pdf"):
                chemin_entree = os.path.join(root, fichier)
                chemin_sortie = os.path.join(root, f"{os.path.splitext(fichier)[0]}_decrypte.pdf")
                decrypt_pdf(chemin_entree, chemin_sortie, mot_de_passe)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Utilisation : python script.py <chemin_vers_le_dossier> <mot_de_passe>")
        sys.exit(1)

    chemin_dossier = sys.argv[1]
    mot_de_passe = sys.argv[2]

    decrypter_pdfs_dans_dossier(chemin_dossier, mot_de_passe)
