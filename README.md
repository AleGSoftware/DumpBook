### **Disclaimer**

**ATTENZIONE: Condividere illegalmente contenuto protetto da copyright non è lo scopo di questo programma. Osserva attentamente la legge prima di commettere un reato!**

### **Info**

DumpBook è uno script da me scritto in Python per salvare i libri digitali delle più svariate app, soprattutto per quelle scolastiche, in formato PDF. Il programma funziona

### **Istruzioni per l'installazione e per la configurazione**

1. Scaricare lo zip [dalle Release di questa pagina sul server di GitLab](https://lnk.alegsoftware.ga/xu2zu).
2. Installare Python sul proprio computer rispetto al proprio sistema operativo. Consultare le guide su Internet. **Attenzione**: se lo installate su Windows, abilitate l'aggiunta a PATH durante l'installazione.
3. Installare le dipendenze da terminale / prompt dei comandi di Windows utilizzando: `pip install pyautogui img2pdf Pillow`
4. Aprire con editor di testo il file dumpbook.py.
5. Inserire una directory di appoggio con percorso completo dopo outputdir.
6. Inserire il numero di pagine **totali** in pages. **Attenzione**: controllare che non ci siano pagine in più di quelle indicate dal numero del libro.
7. Indicare le coordinate delle pagine del libro seguendo [questa guida.](https://lnk.alegsoftware.ga/eswz3) Per acquisire le cordinate su Windows, si può usare un programma come [MouseLoc](https://lnk.alegsoftware.ga/64rqj). Per Mac si può utilizzare la scorciatoria Cmd+Shift+4 e se si ha un display Retina adattato dalle impostazioni si deve riportare il dato alla risoluzione originale (se è impostato default basta raddoppiare il valore ottenuto, lo script include già \*2 per quel motivo, rimouvere \*2 se non serve). Per Linux si può usare xdotool con il comando `watch -t -n 0.0001 xdotool getmouselocation`
8. Aggiustare il numero a time.sleep  del file secondo il tempo che il computer personale impiega per girare le pagine.
9. Avviare il programma da terminale / prompt dei comandi con `python3 dumpbook.py ` sostituisci con il percorso di dumpbook.py.
10. Mettere in primo piano il programma del libro entro 3 secondi.
11. Aspettare il termine del processo.
12. Quando avrà finito di girare le pagine ci vorrà un momento per la conversione in PDF, poi quando si chiuderà lo script si troverà nella directory di lancio del programma il file Dumpbook.pdf, che conterrà il libro in PDF.

### **Note e informazioni utili**

* Le coordinate impostate nel file andranno bene solo con la stessa configurazione delle finestre e dei monitor, perciò si consiglia di mettere a schermo intero il reader dei libri.
* Avendo uno schermo con risoluzione più ampia si otterrà una qualità di immagine più alta, ma il file sarà più pesante.
* Per l'utilizzo su Mac si deve acconsentire alla registrazione schermo, all'accesso disco e al controllo accessibilità, ma il popup si aprirà automaticamente al primo avvio dello script.
{% include analytics.html %}
