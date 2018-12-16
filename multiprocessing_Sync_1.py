import multiprocessing

def add(balance,lock):
  for i in range(10000):
    lock.acquire()
    balance.value += 1
    lock.release()

def withdraw(balance,lock):
  for i in range(10000):
    lock.acquire()
    balance.value -= 1
    lock.release()


# This variable is shared between the processes p1 p2
balance = multiprocessing.Value('i',500)
# creating a lock object 
lock = multiprocessing.Lock()
print("Starting balance is: {}".format(balance.value))
p1 = multiprocessing.Process(target=add,args=(balance,lock))
p2 = multiprocessing.Process(target=withdraw,args=(balance,lock))
p1.start()
p2.start()
p1.join()
p2.join()
print("Final balance is: {}".format(balance.value))