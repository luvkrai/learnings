string = "abc"

def permute(a,l,r):
  if (l == r):
    print(''.join(a))
  else:
    for i in range(l,r+1):
      a[l],a[i] = a[i],a[l]
      permute(a,l+1,r)
      a[l],a[i] = a[i],a[l]

arr = list(string)
permute(arr,0,len(string)-1)