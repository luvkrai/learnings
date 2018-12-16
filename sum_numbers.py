a = 12345
s=0
for i in str(a):
  s+=int(i)
print(s)
s=0
while a > 0:
  r = a%10
  s+=r
  a=int(a/10)
print(s)
