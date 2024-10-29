import customtkinter
import yt_dlp
from yt_dlp import YoutubeDL

# *** Downloader ***


def downtube(link):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
        'outtmpl': 'D:/descargas/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }
        ]
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            print("successful download")
    except Exception as e:
        print(f"There was a problem downloading: {e}")


# **** Window *****
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')
window = customtkinter.CTk()
window.geometry('500x300')
window.title('DownTube')  # Añadir título a la ventana

text = customtkinter.CTkLabel(window, text='DownTube')
url = customtkinter.CTkEntry(window, placeholder_text='Enlace')


def on_download():
    link = url.get()
    downtube(link)


window.iconbitmap('./dt.ico')

button = customtkinter.CTkButton(window, text="Download", command=on_download)

text.pack(padx=10, pady=10)
url.pack(padx=10, pady=10)
button.pack(padx=10, pady=10)

window.mainloop()
