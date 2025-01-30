# avvochad
avvochad è un'applicazione che permette di tradurre un testo amministrativo/giuridico o una serie di testi, separati dal carattere #, in un altro testo il cui lessico è più comune e alla portata di tutti.


## Installazione

Assicurati di avere python 3.9 o versione successive. Puoi scaricare python da qui (https://www.python.org/downloads/). È necessario anche git (https://git-scm.com/downloads/win).

Dopo aver installato python, assicurati che l'installazione sia andata a buon fine lanciando il comando da terminale:

```bash
  python --version 
```
A questo punto, crea una cartella e da terminale lancia il comando


```bash
  git clone https://github.com/roccolr/avvochad.git
```

poi il comando 

```bash
  cd avvochad 
```

poi ancora, un comando alla volta: 


```bash
  pip install -r requirements.txt
  pip install google.generativeai
```

infine esegui il comando 


```bash
  python ./test.py
```


## Quick start
Ottieni la tua API-KEY qui (https://aistudio.google.com/app/apikey)
Nell'interfaccia del programma, clicca su seleziona file per selezionare il file di testo.txt dove ci sono i segmenti testuali da semplificare, separati se più di uno da #. Consulta il file prompts.txt per un esempio. Invece con seleziona cartella si sceglia una cartella dove memorizzare il file testuale di output. Incolla la tua API-KEY, conferma e avvia l'elaborazione, che dovrebbe durare qualche secondo. 
