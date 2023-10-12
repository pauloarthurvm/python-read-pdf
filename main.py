import PyPDF2
import os

nomeOficialXp = "XP INVESTIMENTOS CCTVM S/A"
nomeOficialClear = "CLEAR CORRETORA - GRUPO XP"
nomeOficialAvenue = "AVENUE SECURITIES"

pathClear001 = ".\\old-files\\NotaNegociacao_20190718.pdf"
pathXp001 = ".\\old-files\\c1b2d275-60b2-4d66-9d53-7a069b4295c7.pdf"
pathAvenue001 = ".\\old-files\\Document_1092023_65401_AM_DnYqtYMG.pdf"

reader = PyPDF2.PdfReader(pathXp001)

print(f"pages length = {len(reader.pages)}")

for page in range(len(reader.pages)):
    print(f"content={(reader.pages[page-1].extract_text())}")