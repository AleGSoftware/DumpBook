import pyautogui
import time
import os

outputdir = "/Users/aleg/Documents/OUT/"
print("Dumpbook: book to PDF Utility, only to pdf")

import img2pdf
imgs = []
for r, _, f in sorted(os.walk(outputdir)):
	for fname in sorted(f):
		if not fname.endswith(".png"):
			continue
		imgs.append(os.path.join(r, fname))
with open("Dumpbook.pdf","wb") as f:
	f.write(img2pdf.convert(imgs))