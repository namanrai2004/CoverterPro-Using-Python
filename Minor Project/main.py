import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import cv2

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Converter_Pro--Easily Done Anything")
        self.root.geometry("1600x700")
        self.font_family = "Helvetica"

        # Variables to store file paths
        self.image_path = tk.StringVar()
        self.video_path = tk.StringVar()

        # Frontend Code:

        # Image converter frame
        image_frame = tk.LabelFrame(root, text="Image Converter", padx=10, pady=10, font=("Helvetica", 30, "bold"),bg="#34353b", fg="white",borderwidth=20)
        image_frame.pack(padx=200, pady=20, fill="both", expand=True)

        tk.Label(image_frame, text="Select Image:", font=("Helvetica", 20, "bold"),bg="#e3397a",fg="white",borderwidth=10).grid(row=0, column=0, pady=10, padx=10, sticky="e")

        tk.Entry(image_frame, textvariable=self.image_path, state="readonly",width=30, font=("Helvetica", 27)).grid(row=0, column=1, pady=10, padx=10)

        tk.Button(image_frame, text="Browse", command=self.browse_image, font=(self.font_family, 12, "bold"), bg="#4CAF50", fg="white",borderwidth=20).grid(row=0, column=2, pady=10, padx=10)

        # Dropdown menu for selecting image format
        self.image_format = tk.StringVar()
        self.image_format.set("Select")   #Default

        option_menu = tk.OptionMenu(image_frame, self.image_format, "png", "jpg", "gif", "jpeg", "bmp", "tif", "psd", "svg", "raw", "ico", "heif")

        option_menu.config(font=(self.font_family, 12, "bold"), bg="#4CAF50", fg="white",borderwidth=10)
        option_menu.grid(row=1, column=1, pady=10, padx=10)

        tk.Button(image_frame, text="Convert", command=self.convert_image,font=("Helvetica", 15, "bold"),bg="#577ceb", fg="white",borderwidth=20).grid(row=2, column=1, pady=20)

        
        # Video converter frame
        video_frame = tk.LabelFrame(root, text="Video Converter", padx=10, pady=10, font=("Helvetica", 30, "bold"),bg="#34353b", fg="white",borderwidth=20)
        video_frame.pack(padx=200, pady=20, fill="both", expand=True)

        tk.Label(video_frame, text="Select video:", font=("Helvetica", 20, "bold"),bg="#e3397a",fg="white",borderwidth=10).grid(row=0, column=0, pady=10, padx=10, sticky="e")

        tk.Entry(video_frame, textvariable=self.video_path, state="readonly", width=30, font=("Helvetica", 27)).grid(row=0, column=1, pady=10, padx=10)

        tk.Button(video_frame, text="Browse", command=self.browse_video, font=(self.font_family, 12, "bold"), bg="#4CAF50", fg="white",borderwidth=20).grid(row=0, column=2, pady=10, padx=10)

        # Dropdown menu for selecting video format
        self.video_format = tk.StringVar()
        self.video_format.set("Select")  #Default

        tk.Button(video_frame, text="Convert", command=self.convert_video,font=("Helvetica", 15, "bold"),bg="#577ceb", fg="white",borderwidth=20).grid(row=2, column=1, pady=20)

        option_menu = tk.OptionMenu(video_frame, self.video_format, "mp4","mms","avi", "mov", "mkv", "wmv", "flv", "webm", "mpeg", "3gp", "h264")
        option_menu.config(font=(self.font_family, 12, "bold"), bg="#4CAF50", fg="white",borderwidth=10)
        option_menu.grid(row=1, column=1, pady=10, padx=10)


    #   Backend Code:
    def browse_image(self):  #For browsing image files
        file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.tiff;*.psd;*.svg;*.raw;*.ico;*.heif")])
        self.image_path.set(file_path)

    def browse_video(self):   #For browsing videos files
        file_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video Files", "*.mms;*.mp4;*.avi;*.mkv;*.mov;*.wmv;*.flv;*.webm;*.mpeg;*.3gp;*.h264")])
        self.video_path.set(file_path)



#Image Converter Logic
    def convert_image(self):
        try:
            image_path = self.image_path.get()
            if image_path:
                img = Image.open(image_path)
                img = img.convert("RGB")

                save_path = filedialog.asksaveasfilename(defaultextension=self.image_format.get(), filetypes=[("Image Files", f"*{self.image_format.get()}"), ("All files", "*.*")])
                img.save(save_path)
                messagebox.showinfo("Success", " kaam Ho Gaya Apna....😃😃😃.")
        except Exception as e:
            messagebox.showerror("Error", f"Ye Toh Gadbad Hai Re Baba....😓😓😓: {str(e)}")


#Image Converter Logic
    def convert_video(self):
        try:
            video_path = self.video_path.get()
            if video_path:
                cap = cv2.VideoCapture(video_path)

                save_path = filedialog.asksaveasfilename(defaultextension=self.video_format.get(), filetypes=[("Video Files", f"*{self.video_format.get()}"), ("All files", "*.*")])
                fourcc = cv2.VideoWriter_fourcc(*"mp4v")
                out = cv2.VideoWriter(save_path, fourcc, cap.get(cv2.CAP_PROP_FPS), (int(cap.get(3)), int(cap.get(4))))

                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    out.write(frame)

                cap.release()
                out.release()
                messagebox.showinfo("Success", "Tera kaam Ho Gaya Tu Jaa😃😃😃.")
        except Exception as e:
            messagebox.showerror("Error", f"Ye Toh Gadbad Hai Re Baba😓😓😓: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()
