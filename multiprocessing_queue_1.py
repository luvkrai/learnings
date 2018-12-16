# you can use pip/queue for interprocess communication.
# multiprocessing list,int,dict can be used as well
# Manager can also be used # Geeks for Geeks
import multiprocessing

def my_func(my_list,q):
  for i in my_list:
    q.put(i*i)

def my_print(q):
  while not q.empty():
    print(q.get())
  print("Queue is now empty")

my_list = [1,2,3,4,5]
q = multiprocessing.Queue()
p1 = multiprocessing.Process(target=my_func,args=(my_list,q))
p2 = multiprocessing.Process(target=my_print,args=(q,))

p1.start()
p2.start()
p1.join()
p2.join()