import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube

class YouTubeDownloader:
    def __init__(self, master):
        self.master = master
        master.title("YouTube Video Downloader")

        self.image_frame = tk.LabelFrame(master, text="YouTube Video Downloader", padx=10, pady=10, font=("Helvetica", 30, "bold"), bg="#34353b", fg="white", borderwidth=20)
        self.image_frame.pack(padx=200, pady=20, fill="both", expand=True)

        self.label = tk.Label(self.image_frame, text="Enter YouTube Video URL:", font=("Helvetica", 14), fg="white", bg="#34353b")
        self.label.pack()

        self.entry = tk.Entry(self.image_frame, width=50)
        self.entry.pack(pady=5)  # Add padding on top

        self.download_button = tk.Button(self.image_frame, text="Download", command=self.download_video, font=("Helvetica", 12))
        self.download_button.pack(pady=5)  # Add padding below

    def download_video(self):
        url = self.entry.get()
        try:
            yt = YouTube(url)
            stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
            file_path = filedialog.asksaveasfilename(defaultextension='.mp4', filetypes=[("MP4 files", "*.mp4")])
            if file_path:
                stream.download(output_path=file_path)
                messagebox.showinfo("Success", "Video downloaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error downloading video: {str(e)}")

def main():
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.geometry("800x600")  # Set initial window size
    root.mainloop()

if __name__ == "__main__":
    main()
