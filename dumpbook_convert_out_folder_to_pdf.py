import pyautogui
import time
import os


#Configura qui parametri
outputdir = "./Out/"
pdfout = "DumpBook.pdf"


print("Dumpbook: book to PDF Utility, only to pdf")

import img2pdf
imgs = []
for r, _, f in sorted(os.walk(outputdir)):
	for fname in sorted(f):
		if not fname.endswith(".png"):
			continue
		imgs.append(os.path.join(r, fname))
with open(pdfout,"wb") as f:
	f.write(img2pdf.convert(imgs))