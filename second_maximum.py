arr = [1,2,3,4,5,6,7]
max1=max2=-1

for i in range(0,len(arr)):
    if arr[i] > max1:
	    max2 = max1
	    max1 = arr[i]
    elif arr[i] < max1 and arr[i] > max2 and arr[i] != max2:
	    max2 = arr[i]
		
		
print(max2)
