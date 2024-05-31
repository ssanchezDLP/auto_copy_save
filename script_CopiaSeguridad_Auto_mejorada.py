import datetime
import os
import shutil

from win10toast import ToastNotifier


dt= datetime.datetime.now()

nombre= "{}-{}-{} copia de seguridad de OOS 2.0".format(dt.year, dt.month, dt.day)

# Display notification
toaster = ToastNotifier()
toaster.show_toast("Creating Archive", "Please wait until notified", duration=10)

print("Creating archive. Please wait until notified")



shutil.make_archive(nombre, "zip","//RIG/Users/Public/SQX - Compartida (NO BORRAR)/0_OOS 2.0/") # esta ruta es donde tiene que buscar el script

                            # para indicar rutas, y más de carpetas en red, sustituye exactamente los "\" por "/" y pon un "/" al final de todo


comienzo= []

total= os.listdir()


for a in total:
    if a.startswith("{}-{}-{} copia de seguridad de OOS 2.0".format(dt.year, dt.month, dt.day)) == True:
        comienzo.append(a)


ruta_destino= "/Users/Admin/Documents/Copia de Seguridad con Script/" # esta ruta es donde va a dejar la copia de seguridad el script


for i in comienzo:
    shutil.move(i, ruta_destino)


# Display notification
toaster = ToastNotifier()
toaster.show_toast("Archive Created", "Please check it.", duration=10)

print("All files have been copied successfully.")