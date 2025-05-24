import os
from docx import Document

# Ruta a la carpeta de documentos
documentos_dir = os.path.join(os.path.dirname(__file__), 'documentos')

roles = set()

for filename in os.listdir(documentos_dir):
    if filename.lower().endswith('.docx'):
        doc_path = os.path.join(documentos_dir, filename)
        doc = Document(doc_path)
        for para in doc.paragraphs:
            text = para.text.strip()
            if 'rol' in text.lower() or 'usuario' in text.lower():
                roles.add(text)

print('Posibles roles encontrados:')
for r in roles:
    print('-', r)
