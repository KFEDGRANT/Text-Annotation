#write docx file to txt

import os
from docx import Document

rootdir = "path/to/dir"

def getText(filename):
    doc = Document(os.path.join(rootdir, filename))
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

for filename in os.listdir(rootdir):
    if filename.endswith(".docx"):
        fulltext = getText(filename)
        filename.rsplit('.')
        f = open(filename+".txt","w+", encoding="utf-8")
        f.write(os.path.join("path/to/newdir", fulltext))
