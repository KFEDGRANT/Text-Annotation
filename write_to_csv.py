import re
from re import finditer
import csv
import os

ENT = #enter custom ENT name here

def line_and_index(keyterm):
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            #return start and end index positions for keyword
            spans = []
            for match in finditer(keyterm, open(filename, encoding="utf8", errors='ignore').read()):
                spans.append(match.span())

            #return line numbers for keyword
            lines = []
            rexp = re.compile(keyterm)
            with open(filename, encoding="utf8", errors='ignore') as f:
                for i, line in enumerate(f, 1):
                    if keyterm in line:
                        match = rexp.findall(line)
                        line = i
                        for i in range(len(match)):
                            lines.append(line)

            #combine doc title with line number, index span, and entity name 
            info = []
            for i in range(len(spans)):
                info.append((doc,)+(lines[i],)+spans[i]+(ENT,))
        else:
            continue

        #write to csv
        with open("annotations.csv", "a+", encoding="utf-8") as csv_file:    
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["File", "Line", "Begin Offset", "End Offset", "Type"])
            for i in range(len(info)):
                csv_writer.writerow([info[i][0],info[i][1],info[i][2],info[i][3],info[i][4],])
