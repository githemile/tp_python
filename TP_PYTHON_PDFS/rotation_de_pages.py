import PyPDF2


minutesFile = open('/TP_PYTHON/files_used/meetingminutes.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(minutesFile)

page = pdfReader.getPage(0)
page.rotateClockwise(90)

pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(page)
resulPdfFile = open('/TP_PYTHON/files_used/rotatePge.pdf', 'wb')
pdfWriter.write(resulPdfFile)
resulPdfFile.close()
minutesFile.close()

