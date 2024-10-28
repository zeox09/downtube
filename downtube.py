from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title('DownTube')

Label(root, text='DownTube', font='arial 20 bold').pack()

link = StringVar()
Label(root, text='Pega el link', font='arial 14 bold').place(x=200, y=60)
Entry(root, width=70, textvariable=link).place(x=32, y=90)


def Downloader():
    try:
        url = YouTube(str(link.get()))
        video = url.streams.filter(
            progressive=True, file_extension='mp4').first()
        video.download()
        Label(root, text='Finished Downloading',
              font='arial 20 bold').place(x=200, y=210)
    except Exception as e:
        Label(root, text='Error: ' + str(e),
              font='arial 10 bold').place(x=200, y=210)


Button(root, text='Descargar Video', font='arial 15 bold',
       bg='pale violet red', padx=2, command=Downloader).place(x=180, y=150)

root.mainloop()
