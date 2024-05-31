import webbrowser 
import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp

class AppMusica:
    def __init__(self, root):
        self.root = root
        self.root.title("Discipulozz")

        self.label = tk.Label(root, text="Link do Video:")
        self.label.pack()

        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack()

        self.download_button = tk.Button(root, text="Baixar Musica", command=self.download_music)
        self.download_button.pack()

        self.status_label = tk.Label(root, text="")
        self.status_label.pack()

    def download_music(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showwarning("Aviso", "Por favor, insira uma URL.")
            return

        save_path = filedialog.askdirectory()
        if not save_path:
            messagebox.showwarning("Aviso", "Por favor, escolha um diretório para salvar.")
            return

        self.status_label.config(text="Baixando...")

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([url])
                self.status_label.config(text="Download concluído!")
            except Exception as e:
                messagebox.showerror("Erro", str(e))
                self.status_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppMusica(root)
    url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z"
    webbrowser.open(url)
    root.mainloop()

