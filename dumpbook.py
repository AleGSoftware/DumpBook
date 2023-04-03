import pyautogui
import time
import os
import glob


#Configura qui parametri
pages = 493
bookleft = 597
booktop = 87
bookwid = 662
bookhei = 892
outputdir = "./Out/"
pdfout = "DumpBook.pdf"
sleeptime = 1.5


i = 1
files = glob.glob(outputdir + "*")
for f in files:
    os.remove(f)
print("Dumpbook: book to PDF Utility")
print("")
print("Loaded configuration:")
print("Screen Size: " + str(pyautogui.size()))
print(bookleft,booktop, bookwid, bookhei)
time.sleep(3)
while i <= pages:
    print ("Taking page ", str(i))
    time.sleep(sleeptime)    
    fn = outputdir + str(i).zfill(3) + ".png"
    print ("Saving to " + fn)
    im = pyautogui.screenshot(fn,region=(bookleft,booktop, bookwid, bookhei))
    i = i+1
    pyautogui.hotkey("right")
import img2pdf
imgs = []
for r, _, f in sorted(os.walk(outputdir)):
	for fname in sorted(f):
		if not fname.endswith(".png"):
			continue
		imgs.append(os.path.join(r, fname))
with open(pdfout,"wb") as f:
	f.write(img2pdf.convert(imgs))