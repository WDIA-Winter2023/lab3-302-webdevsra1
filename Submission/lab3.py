import os
import crypt

def createUser(username):
    encrypted_password = crypt.crypt(username, "22")
    command = "sudo useradd -p " + encrypted_password + " -s /bin/bash -d /home/" + username + " -m -c \"" + username + "\" " + username
    os.system(command)

with open("usernames.txt", "r") as file:
    for line in file:
        username = line.strip()
        createUser(username)
        os.system("sudo chown " + username + ":" + username + " /home/" + username)
        os.system("sudo usermod -a -G cst8254 " + username)
