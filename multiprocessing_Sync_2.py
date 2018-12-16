#https://www.geeksforgeeks.org/synchronization-pooling-processes-python/
import multiprocessing

def add(balance):
  for i in range(10000):
    balance.value += 1

def withdraw(balance):
  for i in range(10000):
    balance.value -= 1


# This variable is shared between the processes p1 p2
balance = multiprocessing.Value('i',500)
print("Starting balance is: {}".format(balance.value))
p1 = multiprocessing.Process(target=add,args=(balance,))
p2 = multiprocessing.Process(target=withdraw,args=(balance,))
p1.start()
p2.start()
p1.join()
p2.join()
print("Final balance is: {}".format(balance.value))
