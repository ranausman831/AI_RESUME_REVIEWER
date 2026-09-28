from pypdf import PdfReader
from docx import Document


def extract_text(file_path):

    if file_path.endswith(".pdf"):

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:
            text += page.extract_text() + "\n"

        return text

    elif file_path.endswith(".docx"):

        doc = Document(file_path)

        text = ""

        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"

        return text

    else:
        return "Unsupported file type"