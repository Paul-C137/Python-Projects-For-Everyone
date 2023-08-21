#!/usr/bin/env python3
"""Alta3 Research | PLack@alta3.com
   Moving files with SFTP"""

## import paramiko so we can talk SSH
import paramiko
import os

def movethemfiles(sftp):
    for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
        if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
            sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

def main():
    ## where to connect to
    t = paramiko.Transport("10.10.2.3", 22) ## IP and port

    ## how to connect (see other labs on using id_rsa private/public keypairs)
    t.connect(username="bender", password="alta3")

    ## Make an sftp connection object
    sftp = paramiko.SFTPClient.from_transport(t)

    movethemfiles(sftp)

    ## close the connections
    sftp.close() # close the connection
    t.close()