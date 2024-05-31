import datetime
import os
import shutil
import time
from tkinter import *
from tkinter.ttk import *

# Function to create a backup
def create_backup():
    dt = datetime.datetime.now()
    carpeta_origen = "/Users/Usuario/Documents/Escuela Oficial de Idiomas/"
    nombre = "copia_de_seguridad_{:04d}{:02d}{:02d}".format(dt.year, dt.month, dt.day)
    shutil.make_archive(nombre, "zip", carpeta_origen)
    return nombre + ".zip"

# Function to move the backup to the destination folder
def move_backup(backup_name, ruta_destino):
    shutil.move(backup_name, ruta_destino)

# Function to get the size of a folder
def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size / (1024 * 1024 * 1024)  # Convert bytes to gigabytes

# Function to start the progress bar
def start_progress_bar():
    global folder_size_gb
    total_size_gb = folder_size_gb
    download_size = 0
    speed = 0.05  # Speed of progress simulation
    while download_size < total_size_gb:
        time.sleep(0.05)
        progress_bar['value'] += (speed / total_size_gb) * 100
        download_size += speed
        if total_size_gb != 0:
            progress_percentage.set("{:.1f}%".format((download_size / total_size_gb) * 100))
        else:
            progress_percentage.set("0%")
        progress_text.set("{:.2f}/{:.2f} GB completed".format(download_size, total_size_gb))
        window.update_idletasks()



# Initialize Tkinter window
window = Tk()
window.title("Backup Progress")
window.geometry("400x200")

# Perform backup
backup_name = create_backup()

# Move backup to destination folder
ruta_destino = "/Users/Usuario/Documents/00_prueba"
move_backup(backup_name, ruta_destino)

# Get folder size for progress calculation
folder_path = "/Users/Usuario/Documents/Escuela Oficial de Idiomas/"
folder_size_gb = get_folder_size(folder_path)

# Initialize progress bar
progress_bar = Progressbar(window, orient=HORIZONTAL, length=300)
progress_bar.pack(pady=10)

# Label for progress percentage
progress_percentage = StringVar()
Label(window, textvariable=progress_percentage).pack()

# Label for progress text
progress_text = StringVar()
Label(window, textvariable=progress_text).pack()

# Button to start progress
Button(window, text="Start", command=start_progress_bar).pack()

window.mainloop()
