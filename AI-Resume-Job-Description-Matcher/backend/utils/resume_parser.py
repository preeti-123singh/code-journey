import docx2txt
import PyPDF2

def parse_resume(file):
    """Extract text from PDF or DOCX resumes"""
    text = ""
    filename = file.filename.lower()

    if filename.endswith('.pdf'):
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + " "
    elif filename.endswith('.docx'):
        text = docx2txt.process(file)
    elif filename.endswith('.txt'):
        text = file.read().decode('utf-8')
    else:
        text = ""

    return text.lower()
