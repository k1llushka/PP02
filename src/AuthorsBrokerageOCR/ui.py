import os
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox

from app.ocr_wrapper import recognize_document
from app.parser import extract_client_data
from app.database import save_document


class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Авторы Брокеридж — Распознавание документов")
        self.root.geometry("750x550")

        tk.Button(root, text="Открыть документ", command=self.open_file).pack(pady=10)

        self.textbox = scrolledtext.ScrolledText(root, wrap=tk.WORD)
        self.textbox.pack(fill="both", expand=True, padx=10, pady=10)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Images", "*.png *.jpg *.jpeg *.pdf")]
        )

        if not file_path:
            return

        try:
            self.textbox.delete(1.0, tk.END)
            self.textbox.insert(tk.END, "Распознавание...\n")

            text = recognize_document(file_path)
            data = extract_client_data(text)

            self.textbox.insert(tk.END, text)

            save_document(
                os.path.basename(file_path),
                data["fio"],
                data["passport"],
                text
            )

        except Exception as e:
            messagebox.showerror("Ошибка", str(e))


def run_ui():
    root = tk.Tk()
    OCRApp(root)
    root.mainloop()
