import yt_dlp
import yt_dlp.YoutubeDL


def downtube(link):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
        'outtmpl': '%(tittle)s.%(ext)s',
        'merge_output_format': 'mp4',

        'postprocessors': [
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }
        ]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            print("successful download")
    except Exception as e:
        print(f"There was a problem downloading: {e}")


link = str(input("pega el link del video a descargar: ")).strip()

downtube(link)
