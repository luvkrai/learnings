

def permute(a,l,r):
  if l == r:
    print("".join(a))
  else:
    for i in range(l,r):
      a[l],a[i] = a[i],a[l]
      permute(a,l+1,r)
      a[l],a[i] = a[i],a[l]


permute(['a','b','c'],0,3)

from itertools import permutations,combinations

for i in combinations(['a','b','c'],3):
  print(i)