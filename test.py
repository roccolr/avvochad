import sys
import tkinter as tk
from utilities import *
from tkinter import filedialog

file_path = ""
folder_path = ""
global_text = ""

def salva_testo():
    global global_text
    global_text = text_box.get("1.0", tk.END).strip()  # Prende il testo dalla Text Box
    print("Testo salvato:", global_text)  # Visualizza il testo nella console per conferma

def seleziona_file():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        label_file.config(text=f"File selezionato: {file_path}")
    return file_path

def seleziona_cartella():
    global folder_path
    folder_path = filedialog.askdirectory()
    if folder_path:
        label_cartella.config(text=f"Cartella selezionata: {folder_path}")

def cook(PATH_SOURCE, PATH_DEST, api_key):
    path = PATH_SOURCE
    prompts = clear_prompts(get_prompts(path))
    risposte = []
    for prompt in prompts:
        complete_prompt = "potresti spiegare in parole più semplici il seguente documento?" + '\n' + prompt + "\nsenza usare caratteri speciali, corsivo e grassetto"
        risposta = genera(complete_prompt, api_key)
        risposte.append(risposta)

    i = 1
    with open((folder_path+"/testi_rielaborati.txt"), 'a') as file:
        for risposta in risposte:
            file.write("RISPOSTA " + str(i) + '\n')
            file.write(risposta)
            file.write('\n\n')
            i+=1

if __name__ == '__main__':

    initial_setup()
    root = tk.Tk()
    root.title("AvvoChad")

    btn_sfoglia_file = tk.Button(root, text="Sfoglia File", command=seleziona_file)
    btn_sfoglia_file.pack(pady=5)
    label_file = tk.Label(root, text="File selezionato: Nessuno", wraplength=400)
    label_file.pack(pady=5)

    # Pulsante e label per la cartella
    btn_sfoglia_cartella = tk.Button(root, text="Sfoglia Cartella", command=seleziona_cartella)
    btn_sfoglia_cartella.pack(pady=5)
    label_cartella = tk.Label(root, text="Cartella selezionata: Nessuna", wraplength=400)
    label_cartella.pack(pady=5)

    label_text = tk.Label(root, text="Incolla la tua API-KEY:")
    label_text.pack(padx=10, pady=5)
    text_box = tk.Text(root, height=10, width=40)
    text_box.pack(padx=10, pady=5)
    save_button = tk.Button(root, text="Conferma API-KEY", command=salva_testo)
    save_button.pack(padx=10, pady=5)

    btn_avvia_routine = tk.Button(root, text="Avvia Elaborazione", command= lambda: cook(file_path, folder_path, global_text))
    btn_avvia_routine.pack(pady=10)

    root.mainloop()
    # # area di testo per le stampe:
    # text_area = tk.Text(root, height=10, width=50)
    # text_area.pack(padx=10, pady=10)
    

