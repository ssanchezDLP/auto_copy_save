import datetime
import os
import shutil

from tkinter import *
from tkinter.ttk import *
import time
import os



dt = datetime.datetime.now()

carpeta_origen = "/Users/Usuario/Documents/Escuela Oficial de Idiomas/"

nombre = "copia de seguridad creada el dia {} del mes {} del año {} ".format(dt.day, dt.month, dt.year)


shutil.make_archive(nombre, "zip", carpeta_origen) # esta ruta es donde tiene que buscar el script

                            # para indicar rutas, y más de carpetas en red, sustituye exactamente los "\" por "/" y pon un "/" al final de todo

comienzo = []

total = os.listdir()

for a in total:
    if a.startswith("copia de seguridad creada el dia") == True:
        comienzo.append(a)

ruta_destino = "/Users/Usuario/Documents/00_prueba" # esta ruta es donde va a dejar la copia de seguridad el script

for i in comienzo:
    shutil.move(i, ruta_destino)

# -----------------------------------------------------------
# Barra progreso ---------------------------------------------
# -----------------------------------------------------------

#       Obtenemos primero el peso de la carpeta ---------------------------------------------



def get_folder_size(carpeta_origen):
    # Check if the folder exists
    if os.path.exists(carpeta_origen):
        # Get the size of the folder in bytes
        folder_size = 0
        for path, dirs, files in os.walk(carpeta_origen):
            for file in files:
                carpeta_origen = os.path.join(path, file)
                folder_size += os.path.getsize(carpeta_origen)
        
        # Convert folder size to gigabytes
        folder_size_gb = folder_size / (1024 ** 3)
        return folder_size_gb
    else:
        print("Folder not found.")
        return None


folder_size_gb = get_folder_size(carpeta_origen)


# Ahora sí, ejecutamos también la barra de progreso ---------------------------



def start():
    GB = folder_size_gb
    download = 0
    speed = 0.05
    while(download<GB):
        time.sleep(0.05)
        bar['value']+= (speed/GB) * 100
        download += speed
        porcentaje.set(str(int(download/GB)*100)+"%")
        texto.set(str(download)+"/"+str(GB)+" GB completado/s")
        window.update_idletasks()


window= Tk()

porcentaje= StringVar()
texto= StringVar()


bar= Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

textoLabel= Label(window, textvariable=porcentaje).pack()

comLabel= Label(window, textvariable=texto).pack()

boton= Button(window, text="Descargar", command=start).pack()

window.mainloop



