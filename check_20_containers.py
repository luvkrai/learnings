#!/bin/python
from pexpect import pxssh
from multiprocessing.dummy import Pool

def run(server_port):
 server = server_port[0]
 port = server_port[1]
 try:
    s = pxssh.pxssh(timeout=1)
    s.login(server, "root", "Build",port=port)
    s.sendline("uname -a")
    s.prompt()             # match the prompt
    output = "Server: "+server+" Port: "+str(port)+"\n"+ s.before
    s.logout()
    return output, 0
 except pxssh.ExceptionPxssh as e:
    return e, 1
 except Exception as e:
    return e, 1

servers_port = []
for i in range(2100,2120):
    servers_port.append(["10.206.119.46",i])

pool = Pool(15) # Nummber of concurrent commands at a time

for i, (output, returncode) in enumerate(pool.imap(run, servers_port)):
    if returncode != 0:
       print("Server:{} command failed: {}".format(i+1, output))
    else:
       print("Server:{} success: {}".format(i+1, output))