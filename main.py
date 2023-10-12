import PyPDF2
import os

nomeOficialXp = "XP INVESTIMENTOS CCTVM S/A"
nomeOficialClear = "CLEAR CORRETORA - GRUPO XP"
nomeOficialAvenue = "AVENUE SECURITIES"

pathClear001 = ".\\old-files\\NotaNegociacao_20190718.pdf"
pathXp001 = ".\\old-files\\c1b2d275-60b2-4d66-9d53-7a069b4295c7.pdf"
pathAvenue001 = ".\\old-files\\Document_1092023_65401_AM_DnYqtYMG.pdf"

reader = PyPDF2.PdfReader(pathAvenue001)

print(f"pages length = {len(reader.pages)}")

# list to store files
listOfFiles = []
oldFilesDir = ".\\old-files"
for file in os.listdir(oldFilesDir):
    if os.path.isfile(os.path.join(oldFilesDir, file)):
        listOfFiles.append(oldFilesDir + "\\" + file)
        
for page in range(len(reader.pages)):
    pageContent = (reader.pages[page-1].extract_text().split("\n"))
    for index, text in enumerate(pageContent):
        print(f"{index} : {text}")