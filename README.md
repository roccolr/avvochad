# avvochad
avvochad è un'applicazione che permette di tradurre un testo amministrativo/giuridico o una serie di testi, separati dal carattere #, in un altro testo il cui lessico è più comune e alla portata di tutti.


## Quick start

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
