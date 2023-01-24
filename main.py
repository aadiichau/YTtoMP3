import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import pytube
from pydub import AudioSegment


def download_video():
    try:
        url = url_entry.get()
        youtube = pytube.YouTube(url)
        video = youtube.streams.first()
        filename = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=(("MP4 files", "*.mp4"),("All Files", "*.*")))
        video.download(filename=filename)
        sound = AudioSegment.from_file(filename)
        sound.export(filename.replace('.mp4','.mp3'), format="mp3")
        messagebox.showinfo("Success", "Video downloaded and converted to mp3!")
    except:
        messagebox.showerror("Error", "Failed to download video!")



root = tk.Tk()
root.geometry("600x600")
root.title("Youtube to MP3")


url_label = tk.Label(root, text="Enter YouTube video Link: ")
url_label.pack()


url_entry = tk.Entry(root)
url_entry.pack()
download_button = tk.Button(root, text="Download",
command=download_video)
download_button.pack()

Image = Image.open("/home/aadii/Documents/GITHUB/YTtoMP3/image/arigato.gif")
photo = ImageTk.PhotoImage(Image)
label = tk.Label(root, image=photo)
label.image = photo
label.pack()

root.mainloop()
