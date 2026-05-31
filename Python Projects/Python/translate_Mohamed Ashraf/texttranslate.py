from googletrans import Translator
import tkinter as tk
from tkinter import ttk

def translate_text():
    src_text = src_text_box.get("1.0", tk.END)
    src_lang = src_lang_combobox.get()
    dest_lang = dest_lang_combobox.get()

    translator = Translator()
    translated = translator.translate(src_text, src=lang_code[src_lang], dest=lang_code[dest_lang])

    dest_text_box.delete("1.0", tk.END)
    dest_text_box.insert(tk.END, translated.text)

# Creating the main window
root = tk.Tk()
root.title("Language Translation Tool")

# Language codes
lang_code = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese": "zh"

}

# Source Language Label and Combobox
tk.Label(root, text="Source Language:").grid(row=0, column=0, padx=10, pady=10)
src_lang_combobox = ttk.Combobox(root, values=list(lang_code.keys()))
src_lang_combobox.grid(row=0, column=1, padx=10, pady=10)
src_lang_combobox.current(0)

# Destination Language Label and Combobox
tk.Label(root, text="Destination Language:").grid(row=1, column=0, padx=10, pady=10)
dest_lang_combobox = ttk.Combobox(root, values=list(lang_code.keys()))
dest_lang_combobox.grid(row=1, column=1, padx=10, pady=10)
dest_lang_combobox.current(1)

# Source Text Box
tk.Label(root, text="Source Text:").grid(row=2, column=0, padx=10, pady=10)
src_text_box = tk.Text(root, height=10, width=40)
src_text_box.grid(row=2, column=1, padx=10, pady=10)

# Destination Text Box
tk.Label(root, text="Translated Text:").grid(row=3, column=0, padx=10, pady=10)
dest_text_box = tk.Text(root, height=10, width=40)
dest_text_box.grid(row=3, column=1, padx=10, pady=10)

# Translate Button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Running the application
root.mainloop()