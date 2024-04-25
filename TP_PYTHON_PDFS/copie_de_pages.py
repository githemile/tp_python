import PyPDF2

pdf1File = open('/TP_PYTHON/files_used/meetingminutes.pdf', 'rb')
pdf2File = open('/TP_PYTHON/files_used/meetingminutes2.pdf', 'rb')

pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

for pageNum in range(pdf2Reader.numPages):
    pageObj = pdf2Reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

pdfOutPutFile = open('/TP_PYTHON/files_used/combinedminutes.pdf', 'wb')
pdfWriter.write(pdfOutPutFile)

pdfOutPutFile.close()
pdf1File.close()
pdf2File.close()
