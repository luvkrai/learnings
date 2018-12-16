l = "geeksskeeg"
mid = int(len(l)/2+1)
for i in range(0,mid):
  if l[i] == l[len(l)-i-1]:
     pass
  else:
    print("Not a palindrome")
    break
else:
  print("palindrome")