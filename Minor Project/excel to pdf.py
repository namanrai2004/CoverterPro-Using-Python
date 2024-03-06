import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table

class ExcelToPDFConverter:
    def __init__(self, master):
        self.master = master
        master.title("Excel to PDF Converter")

        self.image_frame = tk.LabelFrame(master, text="Excel to PDF Converter", padx=10, pady=10, font=("Helvetica", 30, "bold"), bg="#34353b", fg="white", borderwidth=20)
        self.image_frame.pack(padx=200, pady=20, fill="both", expand=True)

        self.label = tk.Label(self.image_frame, text="Select an Excel file to convert:", font=("Helvetica", 14), fg="white", bg="#34353b")
        self.label.pack()

        self.select_button = tk.Button(self.image_frame, text="Select Excel File", command=self.select_excel_file, font=("Helvetica", 12))
        self.select_button.pack()

        self.convert_button = tk.Button(self.image_frame, text="Convert to PDF", command=self.convert_to_pdf, font=("Helvetica", 12))
        self.convert_button.pack()

    def select_excel_file(self):
        self.excel_file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if self.excel_file_path:
            self.convert_button.config(state=tk.NORMAL)

    def convert_to_pdf(self):
        try:
            df = pd.read_excel(self.excel_file_path)
            pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if pdf_path:
                doc = SimpleDocTemplate(pdf_path, pagesize=letter)
                data = [df.columns.tolist()] + df.values.tolist()
                table = Table(data)
                doc.build([table])
                messagebox.showinfo("Success", "Excel file converted to PDF successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error converting Excel file to PDF: {str(e)}")

def main():
    root = tk.Tk()
    app = ExcelToPDFConverter(root)
    root.geometry("800x600")  # Set initial window size
    root.mainloop()

if __name__ == "__main__":
    main()
