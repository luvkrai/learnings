import heapq
class item:
  def __init__(self,array,index,value):
    self.array = array
    self.index = index
    self.value = value
  def __lt__(self,other):
    return self.value < other.value

def merge_k_array(a):
  heap = []
  result = []
  for i in range(0,len(a)):
    heapq.heappush(heap,item(i,0,a[i][0]))
  while heap:
    element = heapq.heappop(heap)
    result.append(element.value)
    index = element.index + 1
    if index < len(a[element.array]):
      heapq.heappush(heap,item(element.array,index,a[element.array][index]))
  return result

a = [[1,2],[4],[3,5,6],[30,40,50]]

print(merge_k_array(a))