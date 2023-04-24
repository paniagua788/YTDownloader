from pytube import YouTube  #   Libreria para descargar videos de YT
from sys import argv    #   Libreria para leer argumentos de la consola
from tqdm import tqdm   #   Libreria para crear el contador de progreso

# Leemos el tipo de descarga que queremos utilizar
tipo = argv[1]

# Leemos el link que se pasa como argumento al llamar al comando y guardamos en "link"
link = argv[2]

# Creamos un objeto de tipo YouTube y le pasamos el link del video
yt = YouTube(link)


#Creamos una funcion que descargara el video
def descargar(ruta):
    # Creamos un loop de progreso que va desde 0 a 100
    for i in tqdm(range(100)):
        # Descargamos el video que obtuvimos anteriormente
        descarga.download(ruta)


# Obtenemos el video en el tipo especificado:  tipos: mp3 o mp4 HD 720p
if tipo == "mp3":
    descarga = yt.streams.get_audio_only("mp3")
    descargar("/home/lucas/Música")

else:
    descarga = yt.streams.get_by_resolution("720p")
    descargar("/home/lucas/Vídeos")



print("Descarga completada !!")