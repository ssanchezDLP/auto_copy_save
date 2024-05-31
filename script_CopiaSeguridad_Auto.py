import datetime
import os
import shutil

dt= datetime.datetime.now()

nombre= "copia de seguridad creada el dia {} del mes {} del año {} ".format(dt.day, dt.month, dt.year)

shutil.make_archive(nombre, "zip","//RIG/Users/Public/SQX - Compartida (NO BORRAR)/0_OOS 2.0/") # esta ruta es donde tiene que buscar el script

                            # para indicar rutas, y más de carpetas en red, sustituye exactamente los "\" por "/" y pon un "/" al final de todo

comienzo= []

total= os.listdir()

for a in total:
    if a.startswith("copia de seguridad creada el dia") == True:
        comienzo.append(a)

ruta_destino= "/Users/Admin/Documents/Copia de Seguridad con Script/" # esta ruta es donde va a dejar la copia de seguridad el script

for i in comienzo:
    shutil.move(i, ruta_destino)


