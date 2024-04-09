from odf import text,teletype
from odf.opendocument import load


archivo = load("word/documento.odt")
for bloque in archivo.getElementsByType(text.P):
    print(teletype.extractText(bloque))
