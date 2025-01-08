import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from OllamaWebSummaryModel import OllamaWebSummaryModel
from ollama_checker import ensure_ollama_running
import sys

class OllamaGUI:
    def __init__(self, root):
        if not ensure_ollama_running():
            messagebox.showerror("Error", 
                "Could not start Ollama. Please ensure it is installed correctly.")
            root.destroy()
            sys.exit(1)

        self.model = OllamaWebSummaryModel()
        self.root = root
        self.root.title("Ollama Web Summarizer")

        self.label = tk.Label(root, text="Enter Website URL:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Summarize", command=self.summarize)
        self.button.pack(pady=10)

        self.result_box = scrolledtext.ScrolledText(root, width=60, height=20)
        self.result_box.pack(pady=10)

        self.exit_button = tk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.pack(pady=10)

    def summarize(self):
        url = self.entry.get()
        summary = self.model.summarize_website(url)
        self.result_box.delete(1.0, tk.END)
        self.result_box.insert(tk.END, summary)

if __name__ == "__main__":
    root = tk.Tk()
    gui = OllamaGUI(root)
    root.mainloop()
