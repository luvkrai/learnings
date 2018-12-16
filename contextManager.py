from contextlib import contextmanager

class open_class():
    def __init__(self,filename,mode):
	    self.filename = filename
	    self.mode = mode
		
    def __enter__(self):
	    self.file = open(self.filename,self.mode)
	    return self.file
		
    def __exit__(self,exec_type,exec_eval,traceback):
	    self.file.close()
			
with open_class('test.txt','w') as f:
    f.write("testing")
	
print(f.closed)

@contextmanager
def open_func(filename,mode):
    try:
        f = open(filename,mode)
        yield f
    finally:
        f.close()

with open_func('test.txt','w') as f:
    f.write("testing")
	
print(f.closed)
