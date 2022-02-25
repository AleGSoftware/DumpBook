import pyautogui
import time
import os
import glob


i = 1
pages = 504
bookleft = 397 *2
booktop = 64*2
bookwid = 581*2
bookhei = 789*2
outputdir = "/Users/aleg/Documents/OUT/"
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
    time.sleep(2.5)    
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
with open("Dumpbook.pdf","wb") as f:
	f.write(img2pdf.convert(imgs))