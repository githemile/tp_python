import PyPDF2


def brute_force_decrypt(pdf_file, dictionary_file):
    # Charger le fichier dictionnaire
    with open(dictionary_file, 'r') as f:
        words = f.readlines()

    # Supprimer les sauts de ligne
    words = [word.strip() for word in words]

    # Essayer chaque mot du dictionnaire
    for word in words:
        # Convertir le mot en minuscules et majuscules
        attempts = [word.lower(), word.upper()]

        for attempt in attempts:
            try:
                # Tenter de déchiffrer le PDF avec le mot de passe actuel
                if PyPDF2.PdfFileReader(open(pdf_file, 'rb')).decrypt(attempt) == 1:
                    print(f"Mot de passe trouvé : {attempt}")
                    return
            except:
                continue

    print("Aucun mot de passe trouvé dans le dictionnaire.")


if __name__ == '__main__':
    pdf_file_crypted = 'C:/Users/emile/PycharmProjects/LOVI_KOFFI_EMILE_PYTHON_TP_TEST/TP_PYTHON/files_projects/pdf1_crypte.pdf'
    dictonnary_file = 'C:/Users/emile/PycharmProjects/LOVI_KOFFI_EMILE_PYTHON_TP_TEST/TP_PYTHON/files_projects/dictionary.txt'

    brute_force_decrypt(pdf_file_crypted, dictonnary_file)