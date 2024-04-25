import PyPDF2

pdfFile = open('/TP_PYTHON/files_used/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()
for pageNum in range(pdfReader.numPages):
  pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt('swordfish')
resultPdf = open('/TP_PYTHON/files_used/mot_de_passe.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()

