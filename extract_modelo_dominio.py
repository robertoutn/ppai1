import os
from PyPDF2 import PdfReader

pdf_path = os.path.join(os.path.dirname(__file__), 'documentos', 'ModeloDeDominio.pdf')
reader = PdfReader(pdf_path)

full_text = ''
for page in reader.pages:
    full_text += page.extract_text() + '\n'

with open('modelo_dominio_extraido.txt', 'w', encoding='utf-8') as f:
    f.write(full_text)

print('Texto extraído guardado en modelo_dominio_extraido.txt')
