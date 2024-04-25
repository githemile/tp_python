from docx import Document

def generer_invitations(nom_fichier_entree, nom_fichier_sortie):
    """
    Génère des invitations personnalisées sous forme de documents Word.

    Args:
        nom_fichier_entree (str): Chemin vers le fichier contenant les noms des invités.
        nom_fichier_sortie (str): Chemin vers le fichier de sortie pour enregistrer les invitations.
    """
    try:
        # Créer un document Word
        document = Document()

        # Lire les noms des invités depuis le fichier texte
        with open(nom_fichier_entree, 'r') as f:
            noms_invites = f.readlines()

        # Ajouter une invitation pour chaque invité
        for nom_invite in noms_invites:
            # Ajouter un paragraphe avec le nom de l'invité et un message d'invitation
            document.add_paragraph(f"Cher {nom_invite.strip()},\n\nVous êtes cordialement invité à notre événement spécial.\n\nCordialement,\nEmile_Mable")

            # Ajouter un saut de page après chaque invitation
            document.add_page_break()

        # Enregistrer le document Word
        document.save(nom_fichier_sortie)

        print("Invitations générées avec succès !")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Spécifiez le chemin vers le fichier contenant les noms des invités
fichier_entree = "C:/Users/emile/PycharmProjects/LOVI_KOFFI_EMILE_PYTHON_TP_TEST/TP_PYTHON/files_projects/guests.txt"

# Spécifiez le chemin de sortie pour le fichier contenant les invitations
fichier_sortie = "C:/Users/emile/PycharmProjects/LOVI_KOFFI_EMILE_PYTHON_TP_TEST/TP_PYTHON/files_projects/files/invitations.docx"

# Appeler la fonction pour générer les invitations
generer_invitations(fichier_entree, fichier_sortie)
