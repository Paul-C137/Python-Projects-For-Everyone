#!/usr/bin/python3
"""Alta3 Research | PLack@alta3.com
   Learning about Python SSH
   Modify your credz file to reflect
   credentials for machines in your 
   network.  Create a private key if
   you do not have one."""

import json
import paramiko

def open_file():
    with open('credz.txt') as of:
        content = of.read()
        credz = json.loads(content)
    return credz

def main():
    """Our runtime code that calls other functions"""
    # describe the connection data
    credz = open_file()

    # harvest private key for all 3 servers
    mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

     # loop across the collection credz
    for cred in credz:
        ## create a session object
        sshsession = paramiko.SSHClient()

        ## add host key policy
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ## display our connections
        print("Connecting to... " + cred.get("un") + "@" + cred.get("ip"))

        ## make a connection
        sshsession.connect(hostname=cred.get("ip"), username=cred.get("un"), pkey=mykey)

        ## touch the file goodnews.everyone in each user's home directory
        sshsession.exec_command("touch /home/" + cred.get("un") + "/goodnews.everyone")

        ## list the contents of each home directory
        sessin, sessout, sesserr = sshsession.exec_command("ls /home/" + cred.get("un"))

        ## display output
        print(sessout.read().decode('utf-8'))
        with open('logfile.txt', 'a') as log_file:
            log_file.write(sessout.read().decode('utf-8'))


        ## close/cleanup SSH connection
        sshsession.close()

    print("Thanks for looping with Alta3!")

main()