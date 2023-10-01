# PDF-Translator

<h2> PDF to TXT translator</h2>

- Packages needed for this are:
    - "googletrans" --> pip googletrans==4.0.0rc1
    - "PyPDF2"      --> pip install PyPDF2
- The function receives 3 arguments which of them, 2 are optional.
- The first "path" should be filled with the name of the PDF, which should be positioned in the same folder with the .py files.
- The origin language can be specified for a more acurate traduction. Default is auto.
    if the file has mixed languages it could potentially impact on the accuracy of the translation. (origin='language')
- The destination language can be specified, with English as the default. (destin='language')
- Some of the most common abreviations of languages are:
            - en --> english
            - es --> spanish
            - fr --> french
            - de --> german
            - ru --> russian
- More languages can be found in the google translate doc https://cloud.google.com/translate/docs/languages
- The function will create and open a text file, which should be saved in the storage if needed. 
    
