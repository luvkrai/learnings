from threading import Thread
import time
flag = True
i=1
class OddThread(Thread):
    def run(self):
        global flag
        global i
        while True:
            if flag:   
                time.sleep(1)
                print("ODD_THREAD:",i)
                i = i+1
                flag= False
			    
class EvenThread(Thread):
    def run(self):
        global flag
        global i
        while True:
            if not flag:
                time.sleep(1)
                print("EVEN_THREAD:",i)
                i = i+1
                flag = True			
				
# Run following code when the program starts
if __name__ == '__main__':
   # Declare objects of MyThread class
   myThreadOb1 = OddThread()
 
   myThreadOb2 = EvenThread()
 
   # Start running the threads!
   myThreadOb1.start()
   myThreadOb2.start()
 
   # Wait for the threads to finish...
   myThreadOb1.join()
   myThreadOb2.join()
 
   print('Main Terminating...')

