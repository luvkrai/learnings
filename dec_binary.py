a = 77

bin_str = ""

while a > 0:
  tmp = a%2
  bin_str+=str(tmp)
  a=int(a/2)

print(bin_str[::-1])