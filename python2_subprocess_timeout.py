#!/usr/bin/env python
from subprocess import Popen
from threading import Timer
import psutil

def kill(p):
    #timeout["value"] = True
    for sub_proc in psutil.Process(p.pid).children(recursive=True):
        sub_proc.kill()

timeout_sec=3
p = Popen("sleep 10 & sleep 20 & sleep 30",shell=True)
#timeout = {"value": False}
timer = Timer(timeout_sec, kill, [p])
try:
     timer.start()
     stdout, stderr = p.communicate()
finally:
     timer.cancel()