a = [5,1,6,7,2,4,9,3]

for i in range(1,len(a)):
  value = a[i]
  hole = i
  while(hole > 0 and a[hole-1] > value):
    a[hole]= a[hole-1]
    hole=hole-1
  a[hole]=value
print(a)