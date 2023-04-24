from pytube import YouTube  #   Libreria para descargar videos de YT
from sys import argv    #   Libreria para leer argumentos de la consola
from tqdm import tqdm   #   Libreria para crear el contador de progreso

# Leemos el link que se pasa como argumento al llamar al comando y guardamos en "link"
link = argv[1]
# Creamos un objeto de tipo YouTube y le pasamos el link del video
yt = YouTube(link)

# Obtenemos el video en la resolucion HD 720p
descarga = yt.streams.get_by_resolution("720p")

# Creamos un loop de progreso que va desde 0 a 100
for i in tqdm(range(100)):
    # Descargamos el video que obtuvimos anteriormente
    descarga.download("/home/lucas/Vídeos")

print("Descarga completada !!")