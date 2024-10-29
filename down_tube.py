import customtkinter
import yt_dlp
from yt_dlp import YoutubeDL
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

# *** Downloader ***


def downtube(link, formato_video):
    ydl_opts = {
        'format': f"{formato_video}+bestaudio[ext=m4a]",
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
            messagebox.showinfo("Descarga completada",
                                "El video se ha descargado exitosamente.")
    except Exception as e:
        messagebox.showerror("Error de descarga",
                             f"Hubo un problema descargando: {e}")

# *** Obtener resoluciones ***


def obtener_resoluciones(link):
    resoluciones = []
    titulo = ''
    miniatura = None
    try:
        with YoutubeDL() as ydl:
            info = ydl.extract_info(link, download=False)
            formats = info.get('formats', [])
            titulo = info.get('title', 'Sin título')
            miniatura_url = info.get('thumbnail')
            response = requests.get(miniatura_url)
            img_data = response.content
            image = Image.open(BytesIO(img_data))
            # Redimensionar la imagen
            image = image.resize((640, 360), Image.LANCZOS)
            miniatura = ImageTk.PhotoImage(image)
            for f in formats:
                if f.get('vcodec') != 'none':  # solo videos, no audios
                    resoluciones.append(
                        f"{f['format_id']} - {f['height']}p - {f['vcodec']}")
    except Exception as e:
        messagebox.showerror("Error al obtener resoluciones",
                             f"Hubo un problema obteniendo resoluciones: {e}")
    return resoluciones, titulo, miniatura


# **** Window *****
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')
window = customtkinter.CTk()
window.geometry('500x500')
window.title('DownTube')
text = customtkinter.CTkLabel(window, text='DownTube')
url = customtkinter.CTkEntry(window, placeholder_text='Enlace')
formato = customtkinter.CTkComboBox(
    window, values=["Selecciona primero el enlace"])
formato.set("Selecciona primero el enlace")

thumbnail_label = customtkinter.CTkLabel(
    window, text="")  # Etiqueta de miniatura sin texto
title_label = customtkinter.CTkLabel(window, text='Título del video')


def on_download():
    link = url.get()
    formato_seleccionado = formato.get().split(
        ' - ')[0]  # Obtener el formato_id del ComboBox
    downtube(link, formato_seleccionado)


def on_url_change(event):
    link = url.get()
    resoluciones, titulo, miniatura = obtener_resoluciones(link)
    formato.configure(values=resoluciones)
    formato.set("Selecciona la resolución")
    title_label.configure(text=titulo)
    thumbnail_label.configure(image=miniatura)
    thumbnail_label.image = miniatura  # Referencia para evitar garbage collection


url.bind("<FocusOut>", on_url_change)
window.iconbitmap('./dt.ico')
button = customtkinter.CTkButton(window, text="Download", command=on_download)
text.pack(padx=10, pady=10)
url.pack(padx=10, pady=10)
formato.pack(padx=10, pady=10)
title_label.pack(padx=10, pady=10)
thumbnail_label.pack(padx=10, pady=10)
button.pack(padx=10, pady=10)
window.mainloop()
