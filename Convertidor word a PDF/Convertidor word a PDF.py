import os
from docx2pdf import convert

def convert_docx_to_pdf():
    # Obtiene la ruta del directorio actual
    current_dir = os.getcwd()

    # Lista todos los archivos en el directorio actual
    files = os.listdir(current_dir)

    # Filtra los archivos .docx
    docx_files = [f for f in files if f.endswith('.docx')]

    # Convierte cada archivo .docx a PDF
    for docx_file in docx_files:
        pdf_file = os.path.splitext(docx_file)[0] + '.pdf'
        convert(docx_file, pdf_file)
        print(f'Converted {docx_file} to {pdf_file}')

if __name__ == "__main__":
    convert_docx_to_pdf()

