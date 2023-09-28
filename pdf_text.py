import PyPDF2

def texter(source_text):
    text=""
    if source_text is not None:
        pdf_reader = PyPDF2.PdfReader(source_text)
        
        num_pages = len(pdf_reader.pages)
        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            page_text = page.extract_text()
            text=text+page_text
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11",pages_text[0])

    return text

