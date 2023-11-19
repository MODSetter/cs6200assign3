import os
import re
import json

# needed objects
collectionpath = "./AP_DATA/ap89_collection/"
# collectionpath = "./testdata/"
docid = ""
heading = ""
author = ""
publishdate = ""
content = ""

textflag = False
alltext = ""

parseddata = {}
innerdict = {}

def remove_html_tags(text):
    import re
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def tagscrape(tag, data):
    reg_str = "<" + tag + ">(.*?)</" + tag + ">"
    res = re.findall(reg_str, data)
    ans = ' '.join(res)
    return ans.strip()

def populateandclear():
    global parseddata
    global innerdict
    global docid
    global heading
    global author
    global publishdate
    global content
    global textflag
    global alltext

    innerdict["heading"] = heading.strip()
    innerdict["author"] = author.strip()
    innerdict["publishdate"] = publishdate.strip()
    innerdict["content"] = content.strip()

    parseddata[docid.strip()] = innerdict.copy()
    print("Mapped Data", parseddata[docid.strip()])
    
    innerdict.clear()
    docid = ""
    heading = ""
    author = ""
    publishdate = ""
    content = ""
    textflag = False
    alltext = ""



def file_parser():
    global parseddata
    global innerdict
    global docid
    global heading
    global author
    global publishdate
    global content
    global textflag
    global alltext
    # read all file names from the directory
    file_name = os.listdir(collectionpath)
    file_name = [collectionpath + i for i in file_name]

    # read each file
    for f in file_name:
        with open(f, "r") as f:
            data = f.readlines()

            for line in data:
                line = line.strip()

                if re.search("</DOC>", line):
                    populateandclear()
                    
                if re.search("</TEXT>", line):
                    textflag = False
                    line = "<TEXT>" + line
                    out = tagscrape("TEXT", line)
                    content += alltext + out
                    content = remove_html_tags(content)

                if textflag:
                    alltext += " " + line
                    continue

                if re.search("<DOCNO>", line):
                    out = tagscrape("DOCNO", line)
                    docid += " " + out

                if re.search("<FILEID>", line):
                    out = tagscrape("FILEID", line)
                    publishdate += " " + out

                if re.search("<HEAD>", line):
                    out = tagscrape("HEAD", line)
                    heading += " " + out

                if re.search("<BYLINE>", line):
                    out = tagscrape("BYLINE", line)
                    author += " " + out
                
                if re.search("<TEXT>", line):
                    textflag = True
                    print()

    return parseddata
                
def write_file(files):
    with open("./parsed_file.json", "w") as f:
        json.dump(files, f)                   

pdata = file_parser()
write_file(pdata)