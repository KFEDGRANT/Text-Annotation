#https://automatetheboringstuff.com/chapter13/
#write docx file to txt

#pull text from .docx
def getText(filename):
    doc = Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

#write text to .txt
directory = #filepath
for filename in os.listdir(directory):
    if filename.endswith(".docx"):
        fulltext = getText(filename)
        filename.rsplit('.')
        f = open(filename+".txt","w+")
        f.write(fulltext)
    else:
        continue
