from pytube import YouTube, Playlist  #   Libreria para descargar videos de YT
from sys import argv    #   Libreria para leer argumentos de la consola
from tqdm import tqdm   #   Libreria para crear el contador de progreso

# Leemos el tipo de descarga que queremos utilizar
tipo = argv[1]

# Leemos el link que se pasa como argumento al llamar al comando y guardamos en "link"
link = argv[2]

# Creamos un variables donde se guarda la ruta de destino de los archivos
video_path = "/home/lucas/Vídeos"
audio_path = "/home/lucas/Música"
# Creamos un objeto de tipo YouTube y le pasamos el link del video
yt = YouTube(link)
lista = Playlist(link)

#Creamos una funcion que descargara el video

# Creamos un loop de progreso que va desde 0 a 100
for i in tqdm(range(100)):
    # Obtenemos el video en el tipo especificado:  tipos: mp3, playlist o mp4
    if tipo == "mp3":
        yt.streams.filter(only_audio=True).get_audio_only().download(audio_path)

    elif tipo == 'mp4':
        yt.streams.get_by_resolution("720p").download(video_path)
    elif tipo == "lista-mp4":
        for video in lista.video_urls:
            yt = YouTube(video)
            yt.streams.get_by_resolution("720p").download(video_path)
            print(f"Se descargó el video: {yt.title}")
    elif tipo == "lista-mp3":
        for video in lista.video_urls:
            yt = YouTube(video)
            yt.streams.filter(only_audio=True).get_audio_only().download(audio_path)
            print(f"Se descargó el audio del video: {yt.title}")
    else:
            print("Especifique un tipo de descarga: \n Sintaxis: python3 ytDownloader.py <tipo> <link>\n Los tipos pueden ser: mp3, mp4, lista-mp3 o lista-mp4")
print("Descarga completada !!")