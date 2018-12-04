arr = [1,2,3,4,5,6,7]

min1 = min2 = 1000000

for i in range(0,len(arr)):
    if arr[i] < min1:
	    min2 = min1
	    min1 = arr[i]
    elif arr[i] > min1 and arr[i] < min2 and arr[i] != min2:
	    min2 = arr[i]
	

print(min2)
