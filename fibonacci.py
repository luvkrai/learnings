n=10
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
        print(b)		

print("\nrecursion\n")
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
       return fib(n-1) + fib(n-2)


print(fib(8))





