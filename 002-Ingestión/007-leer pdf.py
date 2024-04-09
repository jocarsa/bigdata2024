import PyPDF2

archivo = PyPDF2.PdfFileReader("pdf/prueba.pdf")
paginas = archivo.numPages
print(paginas)

for pagina in range(0,paginas):
    actual = archivo.getPage(0)
    print(actual.extractText())
