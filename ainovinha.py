import os #permite añadir archivos desde la pc
import shutil


carpeta_descargas = r"C:\Users\Krado\Downloads\jaja" #la ruta de descargas

def organizar_archivos(): #la funcion para que pueda organizar los archivos 
    contador = 0
    for archivo in os.listdir(carpeta_descargas):
        ruta_archivo = os.path.join(carpeta_descargas, archivo)
        

        if os.path.isdir(ruta_archivo): 
            continue

        if archivo.endswith('.pdf'):
            nombre_carpeta = 'documentos'
        elif archivo.endswith(('.png', '.jpg', '.jpeg')):
            nombre_carpeta = 'imagenes'
        else:
            nombre_carpeta = 'otros'

        destino = os.path.join(carpeta_descargas, nombre_carpeta)

        if not os.path.exists(destino):
            os.makedirs(destino)

        shutil.move(ruta_archivo, os.path.join(destino, archivo))
        contador += 1
        print(f"Movido: {archivo} a {destino}")

    print(f"¡Listo! Se han organizado {contador} archivos.")
organizar_archivos()