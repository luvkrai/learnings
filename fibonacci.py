'''n=10
sum=0
a=0
b=1
for i in range(0,n+1):
    if i == 0:
        print(a)
    elif i ==1:
        print(b)
    else:
        sum = a + b
        a = b
        b = sum
        print(b)'''		

print("\nrecursion\n")
import time
start_time = time.time()
memo = {}
def fib(n):
    #try:
    #    return memo[n]
    #except:
    #   pass
    if n in memo:
        return memo[n]
    if n == 0:
        value = 0
    elif n == 1:
        value = 1
    else:
       value = fib(n-1) + fib(n-2)
    memo[n] = value
    return value


for i in range(1,50):
    print(fib(i))

print("--- %s seconds ---" % (time.time() - start_time))



