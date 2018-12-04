#!/usr/bin/env python
from __future__ import print_function
from subprocess import Popen, PIPE
from threading import Timer
import psutil


class ExecutionTimeout(Exception):
    pass

# it is always better to use subprocess (subprocess32 in case of python 2.7) built in timeout features which will take care of all of this ugly ways
def kill(p):
    timeout["value"] = True
    for sub_proc in psutil.Process(p.pid).children(recursive=True):
        sub_proc.kill()

timeout_sec=8
#p = Popen("sleep 10 & sleep 20 & sleep 30",stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
p = Popen("sh sleep.sh",stdout=PIPE, stderr=PIPE, universal_newlines=True,shell=True)
timeout = {"value": False}
timer = Timer(timeout_sec, kill, [p])
timer.start()
for stdout_line in iter(p.stdout.readline, ""):
        print (stdout_line)
stdout, stderr = p.communicate()
timer.cancel()
try:
    if timeout['value'] == True:
        raise ExecutionTimeout
except ExecutionTimeout:
    print("caught")
rc = p.returncode
if rc:
        print("failed",stderr)