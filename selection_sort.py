arr = [4,2,5,8,1,6,9,-9,2]

for i in range(0,len(arr)-2):
  i_min = i
  for j in range(i+1,len(arr)):
   if arr[i_min] > arr[j]:
    i_min = j
  arr[i],arr[i_min] = arr[i_min],arr[i]

print(arr)
