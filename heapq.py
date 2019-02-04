# Putting an object in heap and modifying the comparison value
# if you normally put an int or float in a min heap it'll work normally, but if you need to put any object then you need to specify using __lt__ method to heapq which element it is suppose to pick to make a min heap
import heapq
class MyObject:
     def __init__(self, array,index,value):
         self.array = array
         self.index = index
         self.value = value
     def __lt__(self, other):
         return self.value < other.value

'''q = []
heapq.heappush(q, MyObject(50,1,4))
heapq.heappush(q, MyObject(40,3,5))
heapq.heappush(q, MyObject(30,4,8))
heapq.heappush(q, MyObject(20,77,45))
heapq.heappush(q, MyObject(200,68,89))
obj = heapq.heappop(q)
print(obj.array)'''

def merge(arr):
  q = []
  result = []
  size = 0
  # Put the first elements of each k array into the heap
  for i in range(0,len(arr)):
    size += len(arr[i])
    if len(arr[i]) > 0:
      heapq.heappush(q,MyObject(i,0,arr[i][0]))
  # While there are items in the heap or in this case the list q (heapq is operated on a list)
  # keep poping out the first element(min) from the heap to put it into the result list, then find the next element in the same list where the last minimum came from to put into the min heap
  while q:
    # Get the minimum of the k elements in the heap
    n = heapq.heappop(q)
	# Minimum Element added into the result list
    result.append(n.value)
	# Find the next element to put into the heap
    newIndex = n.index + 1
	# Make sure the list has some elements to put into the heap, because all k list can be of different sizes, If this is the case then the next minimum element will come from a different list, then the operation will continue on the next list and so on, till there are no elements in the heap or q and the program stops
    if (newIndex < len(arr[n.array])):
      heapq.heappush(q,MyObject(n.array,newIndex,arr[n.array][newIndex]))
  return result
arr = [[1,3,5],[4,6,8],[2]]

print(merge(arr))