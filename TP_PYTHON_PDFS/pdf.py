# importez le package
from PyPDF2 import PdfWriter, PdfReader
# ici nous allons manipuler des pdf AVC PYTHON

# pdf writer qui va nous permettre d'écrire dans le ficher pdf
pdf_writer = PdfWriter()
for pdf in ['pdf1.pdf','pdf2.pdf','pdf3.pdf']:
    pdf_reader = PdfReader(pdf)
    for page in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page])

with open('../files_used/merge.pdf', 'wb') as out:
    pdf_writer.write(out)


