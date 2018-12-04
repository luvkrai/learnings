import os
import time
import gc
from psutil import virtual_memory

mem = virtual_memory()
print(mem.used/(1024.**2))


def gen():
    for i in list(os.walk('C:\\')):
        yield i
		
		
t1 = time.time()
for _ in list((os.walk('C:\\'))):
    pass

#for _ in gen():
#   pass
#gc.collect()
#for _ in os.walk('C:\\'):
#    pass
t2 = time.time()

print("total time : {}".format(t2-t1))
mem = virtual_memory()
print(mem.used/(1024.**2))

