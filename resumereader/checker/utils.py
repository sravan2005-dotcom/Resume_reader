import docx
import PyPDF2

def check_eligibility(file):
    # Check if the file is a PDF or DOCX file and extract text
    file_extension = file.name.split('.')[-1].lower()
    
    if file_extension == 'pdf':
        text = extract_pdf_text(file)
    elif file_extension == 'docx':
        text = extract_docx_text(file)
    else:
        return 'Not Eligible'

    # Define the eligibility criteria (e.g., keywords)
    keywords = ['Python', 'Django', '5 years experience']

    # Check if the resume contains any of the keywords
    for keyword in keywords:
        if keyword.lower() in text.lower():
            return 'Eligible'

    return 'Not Eligible'

def extract_pdf_text(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ''
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extractText()
    return text

def extract_docx_text(file):
    doc = docx.Document(file)
    text = ''
    for para in doc.paragraphs:
        text += para.text
    return text
