import os
import shutil

def avenueGetDate(content: list):
    for index, text in enumerate(content):
        text: str
        if ("SUMMARY FOR CURRENT TRADE DATE:" in text):
            dateStr = text.split(' ')[-1].replace(" ", "")
            print(f"date:{dateStr}")
            return dateStr
    return False

def copyAndRenameAvenue(oldFile: str, dateStr: str):
    dateList = dateStr.split("/")
    newFilesDir = ".\\new-files"
    if not os.path.exists(newFilesDir):
        os.makedirs(newFilesDir)
    shutil.copyfile(oldFile, f"{newFilesDir}\\avenue_20{dateList[2]}_{dateList[0]}_{dateList[1]}.pdf")
    return True