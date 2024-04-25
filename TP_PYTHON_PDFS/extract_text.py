# importez le package
import PyPDF2
# extraction du text d'un pdf

pdfFileObj = open('/TP_PYTHON/files_used/meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
text = pageObj.extractText()
print(text)


pdfFileObj.close()