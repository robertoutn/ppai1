import os
from docx import Document

doc_path = os.path.join(os.path.dirname(__file__), 'documentos', 'ModeloDeDominio.docx')
doc = Document(doc_path)

with open('modelo_dominio_docx_extraido.txt', 'w', encoding='utf-8') as f:
    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            f.write(text + '\n')

print('Texto extraído guardado en modelo_dominio_docx_extraido.txt')
