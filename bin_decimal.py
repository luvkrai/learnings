a = 1001101
s=0
count=0
while a > 0:
  r = a%10
  n = r*(2**count)
  s+=n
  a=int(a/10)
  count+=1
print(s)	