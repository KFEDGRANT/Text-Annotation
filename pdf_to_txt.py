import textract

for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        text = textract.process(filename)
        filename.rsplit('.')
        f= open(filename+".txt","w+")
        f.write(fulltext)
    else:
        continue
