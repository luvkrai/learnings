def partition(arr,start,end):
  pivot=arr[end]
  pIndex = start
  for i in range(start,end):
    if arr[i] <= pivot:
      arr[i],arr[pIndex]=arr[pIndex],arr[i]
      pIndex+=1
  arr[pIndex],arr[end] = arr[end],arr[pIndex]
  return pIndex

def QuickSort(arr,start,end):
  if start < end:
      pIndex = partition(arr,start,end)
      QuickSort(arr,start,pIndex-1)
      QuickSort(arr,pIndex+1,end)

a = [4,5,1,8,2,9,3,6]
QuickSort(a,0,7)
print(a)