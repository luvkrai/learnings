def merge(LA,RA,A):
  Ln = len(LA)
  Rn = len(RA)
  An = len(A)
  i=j=k=0
  while(i<Ln and j<Rn):
    if LA[i] < RA[j]:
      A[k] = LA[i]
      i+=1
    else:
      A[k] = RA[j]
      j+=1
    k+=1
  while(i<Ln):
    A[k] = LA[i]
    i+=1
    k+=1
  while(j<Rn):
    A[k] = RA[j]
    j+=1
    k+=1

def mergeSort(A):
  if len(A) < 2:
    return
  mid = int(len(A)/2)
  LA = A[:mid]
  RA = A[mid:]
  mergeSort(LA)
  mergeSort(RA)
  merge(LA,RA,A)

A = [4,6,1,3,9,12,5]
mergeSort(A)
print(A)
