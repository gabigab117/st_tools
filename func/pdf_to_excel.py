import aspose.pdf as ap
from io import BytesIO


def pdf_to_excel(input_pdf):
    file = input_pdf
    b = BytesIO()
    document = ap.Document(file)
    save_option = ap.ExcelSaveOptions()
    document.save(b, save_option)
    b.seek(0)
    return b