#https://www.geeksforgeeks.org/multiprocessing-python-set-2/
#https://www.geeksforgeeks.org/synchronization-pooling-processes-python/

import multiprocessing

result = []

def my_func(my_list):
  global result
  for i in my_list:
    result.append(i*i)
  print(result)

my_list = [1,2,3,4,5]

p1 = multiprocessing.Process(target=my_func,args=(my_list,))
p1.start() 
  
# wait until process is finished 
p1.join() 

print(result) # this will pring empty list, as the p1 will change the result list in its own memory space.