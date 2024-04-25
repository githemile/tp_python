import os
import PyPDF2

dossier_pdf = "C:/Users/emile/PycharmProjects/LOVI_KOFFI_EMILE_PYTHON_TP_TEST/TP_PYTHON/pdfs/"
pdfFiles = []
for filename in os.listdir(dossier_pdf):
    if filename.endswith('.pdf'):
        pdfFiles.append(os.path.join(dossier_pdf, filename))

pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

pdfOutPut = open('/TP_PYTHON/pdfs/allminutes.pdf', 'wb')
pdfWriter.write(pdfOutPut)
pdfOutPut.close()
