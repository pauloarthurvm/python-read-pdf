import os

def avenueGetDate(content: list):
    for index, text in enumerate(content):
        text: str
        if ("SUMMARY FOR CURRENT TRADE DATE:" in text):
            dateStr = text.split(' ')[-1].replace(" ", "")
            print(f"date:{dateStr}")
            return dateStr
    return False