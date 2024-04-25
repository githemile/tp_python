import PyPDF2

minutesFile = open('/TP_PYTHON/files_used/meetingminutes.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)
#filigramme
pdfWatermarkReader = PyPDF2.PdfFileReader(open('/TP_PYTHON/files_used/watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)
for pageNum in range(1, pdfReader.numPages):
  pageObj = pdfReader.getPage(pageNum)
  pdfWriter.addPage(pageObj)
resultPdfFile = open('/TP_PYTHON/files_used/watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()
