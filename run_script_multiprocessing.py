#!/bin/python
from pexpect import pxssh
from multiprocessing.dummy import Pool

def run(server):
 try:
    s = pxssh.pxssh(timeout=1)
    s.login(server, "root", "Coolbeans!")
    s.sendline('uname -a')   # run a command
    s.prompt()             # match the prompt
    output = "Server: "+server+"\n"+ s.before
    s.logout()
    return output, 0
 except pxssh.ExceptionPxssh as e:
    return e, 1
 except Exception as e:
    return e, 1

servers = []
for i in range(1,16):
    servers.append("uls-ep-swtools-%s" % str(i).zfill(2))

pool = Pool(15) # Nummber of concurrent commands at a time

for i, (output, returncode) in enumerate(pool.imap(run, servers)):
    if returncode != 0:
       print("Server:{} command failed: {}".format(i+1, output))
    else:
       print("Server:{} success: {}".format(i+1, output))