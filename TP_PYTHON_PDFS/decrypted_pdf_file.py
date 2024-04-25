import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open('/TP_PYTHON/files_used/encrypted.pdf', 'rb'))
pdfReader.isEncrypted

# True

# decrupté le ficher
pdfReader.decrypt('rosebud')

"""
pageObj = pdfReader.getPage(0)
text = pageObj.extractText()
print(text)

"""


