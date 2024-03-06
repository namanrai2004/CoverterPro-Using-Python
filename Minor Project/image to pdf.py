import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from fpdf import FPDF

class ImageToPDFConverter:
    def __init__(self, master):
        self.master = master
        master.title("Image to PDF Converter")

        self.image_frame = tk.LabelFrame(master, text="Image Converter", padx=10, pady=10, font=("Helvetica", 30, "bold"), bg="#34353b", fg="white", borderwidth=20)
        self.image_frame.pack(padx=200, pady=20, fill="both", expand=True)

        self.image_path = tk.StringVar()

        tk.Label(self.image_frame, text="Select Image:", font=("Helvetica", 20, "bold"), bg="#e3397a", fg="white", borderwidth=10).grid(row=0, column=0, pady=10, padx=10, sticky="e")

        tk.Entry(self.image_frame, textvariable=self.image_path, state="readonly", width=30, font=("Helvetica", 27)).grid(row=0, column=1, pady=10, padx=10)

        tk.Button(self.image_frame, text="Browse", command=self.browse_image, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", borderwidth=20).grid(row=0, column=2, pady=10, padx=10)

        self.convert_button = tk.Button(self.image_frame, text="Convert to PDF", command=self.convert_to_pdf, state=tk.DISABLED, font=("Helvetica", 12))
        self.convert_button.grid(row=1, column=1, pady=10)

    def browse_image(self):
        self.image_path.set(filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]))
        if self.image_path.get():
            self.convert_button.config(state=tk.NORMAL)

    def convert_to_pdf(self):
        image = Image.open(self.image_path.get())
        pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if pdf_path:
            pdf = FPDF()
            pdf.add_page()
            pdf.image(self.image_path.get(), 0, 0, 210, 297)  # A4 size in mm
            pdf.output(pdf_path, "F")
            messagebox.showinfo("Success", "Image converted to PDF successfully!")

def main():
    root = tk.Tk()
    app = ImageToPDFConverter(root)
    root.geometry("800x600")  # Set initial window size
    root.mainloop()

if __name__ == "__main__":
    main()
