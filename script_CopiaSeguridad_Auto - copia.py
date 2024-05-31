import datetime
import os
import shutil
from tqdm import tqdm
from win10toast import ToastNotifier

# Function to create a backup
def create_backup():
    dt = datetime.datetime.now()
    nombre = "{}-{}-{} copia de seguridad de OOS 2.0".format(dt.year, dt.month, dt.day)

    # Display notification
    toaster = ToastNotifier()
    toaster.show_toast("Creating Archive", "Please wait...", duration=10)

    print("Creating archive. Please wait...")

    # Create backup
    shutil.make_archive(nombre, "zip", "//RIG/Users/Public/SQX - Compartida (NO BORRAR)/0_OOS 2.0/")

    # Get list of all files in the current directory
    total = os.listdir()

    # Filter files created by the backup
    comienzo = [a for a in total if a.startswith("{}-{}-{} copia de seguridad de OOS 2.0".format(dt.year, dt.month, dt.day))]

    ruta_destino = "/Users/Admin/Documents/Copia de Seguridad con Script/"

    # Move files to the destination directory
    for i in tqdm(comienzo, desc="Moving files"):
        shutil.move(i, ruta_destino)

    print("All files have been copied successfully.")

# Call the function to create backup
create_backup()
