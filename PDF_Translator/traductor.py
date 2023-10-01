import time
from googletrans import Translator
import PyPDF2
import os               #to open the new archive


def translation(pdf_name, origin='auto', destin='en'):
    """
    - Packages needed for this are:
                - "googletrans" --> pip googletrans==4.0.0rc1
                - "PyPDF2"      --> pip install PyPDF2

    - As path it should include the relative or absolute path of the pdf file
    - The origin language can be specified for a more acurate traduction. Default is auto.
        if the file has mixed languages it could potentially impact on the accuracy of the translation. (origin='language')
    - The destination language can be specified, with English as the default. (destin='language')
    - Some of the most common abreviations of languages are:
                - en --> english
                - es --> spanish
                - fr --> french
                - de --> german
                - ru --> russian
    - more languages can be found in the google translate doc https://cloud.google.com/translate/docs/languages
    - The function will create and open a text file, which should be saved in the storage if needed. 
    
    
    """
    
    
    translator = Translator()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))

    location = os.path.join(script_dir, pdf_name)

    
    with open(location, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        text = ''

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    
    chunk_size = 4500    #limit the len of the traduction chunks so it doesnt fail
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    translated_text = ''

    for chunk in chunks:
        translated_chunk = translator.translate(chunk,dest=destin, src=origin)
        time.sleep(2)
        translated_text += translated_chunk.text


    with open('translated_text.txt','w', encoding='utf-8') as text_file:
        text_file.write(translated_text)

    return os.startfile('translated_text.txt')
