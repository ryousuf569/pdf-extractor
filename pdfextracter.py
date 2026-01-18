import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
import os
import tempfile
import sys
import subprocess

class PDFSplitterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Page Extractor")
        self.root.geometry("400x300")

        self.pdf_path = None
        self.preview_path = None
        
        tk.Button(root, text="Select PDF", command=self.select_pdf).pack(pady=10)

        self.file_label = tk.Label(root, text="No file selected")
        self.file_label.pack()

        tk.Label(root, text="Start Page (0-indexed)").pack()
        self.start_entry = tk.Entry(root)
        self.start_entry.pack()

        tk.Label(root, text="End Page (exclusive)").pack()
        self.end_entry = tk.Entry(root)
        self.end_entry.pack()

        tk.Button(root, text="Preview Pages", command=self.preview_pdf).pack(pady=10)
        tk.Button(root, text="Save Extracted PDF", command=self.save_pdf).pack()

    def select_pdf(self):
        self.pdf_path = filedialog.askopenfilename(
            filetypes=[("PDF Files", "*.pdf")]
        )
        if self.pdf_path:
            self.file_label.config(text=os.path.basename(self.pdf_path))

    def extract_pages(self, output_path):
        if not self.pdf_path:
            raise ValueError("No PDF selected")

        start = int(self.start_entry.get())
        end = int(self.end_entry.get())

        reader = PdfReader(self.pdf_path)
        writer = PdfWriter()

        if start < 0 or end > len(reader.pages) or start >= end:
            raise ValueError("Invalid page range")

        for i in range(start, end):
            writer.add_page(reader.pages[i])

        with open(output_path, "wb") as f:
            writer.write(f)

    def preview_pdf(self):
        try:
            temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
            self.preview_path = temp.name
            temp.close()

            self.extract_pages(self.preview_path)
            self.open_pdf(self.preview_path)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_pdf(self):
        try:
            save_path = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF Files", "*.pdf")]
            )
            if save_path:
                self.extract_pages(save_path)
                messagebox.showinfo("Success", "PDF saved successfully!")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def open_pdf(self, path):
        if sys.platform.startswith("win"):
            os.startfile(path)
        elif sys.platform.startswith("darwin"):
            subprocess.run(["open", path])
        else:
            subprocess.run(["xdg-open", path])

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFSplitterGUI(root)
    root.mainloop()
