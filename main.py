import os
import PyPDF2
import util

idXp = "XP INVESTIMENTOS CCTVM S/A"
idClear = "CLEAR CORRETORA - GRUPO XP"
idAvenue = "AVENUE SECURITIES"

# list to store files
listOfFiles = []

oldFilesDir = ".\\old-files"
for file in os.listdir(oldFilesDir):
    file: str
    if os.path.isfile(os.path.join(oldFilesDir, file)) and file.endswith(".pdf"):
        listOfFiles.append(oldFilesDir + "\\" + file)


newFilesDir = ".\\new-files"
if os.path.exists(newFilesDir):
    for file in os.listdir(newFilesDir):
        file_path = os.path.join(newFilesDir, file)
        os.remove(file_path)
else:
    os.makedirs(newFilesDir)

for file in listOfFiles:
    reader = PyPDF2.PdfReader(file)
    for page in range(len(reader.pages)):
        pageContent = (reader.pages[page-1].extract_text().split("\n"))
        for index, text in enumerate(pageContent):
            if (idClear in text):
                print(f"{index} : {text} : {file} : page {page}")
                dateRetrieved = util.genericGetDate(pageContent)
                if (dateRetrieved):
                    util.copyAndRenameGeneric(file, dateRetrieved, "clear")
                break
            elif (idXp in text):
                print(f"{index} : {text} : {file} : page {page}")
                dateRetrieved = util.genericGetDate(pageContent)
                if (dateRetrieved):
                    util.copyAndRenameGeneric(file, dateRetrieved, "xpinv")
                break
            elif (idAvenue in text):
                print(f"{index} : {text} : {file} : page {page}")
                dateRetrieved = util.avenueGetDate(pageContent)
                if (dateRetrieved):
                    util.copyAndRenameAvenue(file, dateRetrieved)
                break