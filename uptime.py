#~/bin/python

from pexpect import pxssh
for i in range(1,16):
 try:
    s = pxssh.pxssh(timeout=1)
    server_name = "uls-ep-swtools-%s" % str(i).zfill(2)
    s.login(server_name, "root", "Coolbeans!")
    s.sendline('uptime')   # run a command
    s.prompt()             # match the prompt
    print("Server: "+server_name+"\n")
    print(s.before)        # print everything before the prompt.
    s.logout()
 except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)
 except Exception as e:
    print(e)
    print("Powered off")