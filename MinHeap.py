def getLeftChildIndex(parentIndex):
  return parentIndex*2 + 1

def getRightChildIndex(parentIndex):
  return parentIndex*2 + 2

def getParentIndex(childIndex):
  return int((childIndex-1)/2)

def hasLeftChild(index):
  return getLeftChildIndex(index) < size
  
def hasRightChild(index):
  return getRightChildIndex(index) < size
  
def hasParent(index):
  return getParentIndex(index) >= 0

def rightChild(index):
  return heap[getRightChildIndex(index)]

def leftChild(index):
  return heap[getLeftChildIndex(index)]

def parent(index):
  return heap[getParentIndex(index)]

def peek():
  global size
  if size == 0:
    print("Heap is Empty")
    return
  return heap[0]

def swap(index1,index2):
  heap[index1],heap[index2] = heap[index2],heap[index1]


def insert(item):
  global size
  heap.append(item)
  size += 1
  heapifyUp()
  
def remove():
  global size
  if size == 0:
    print("Heap is empty already")
    return
  item = heap[0]
  heap[0] = heap[size-1]
  heap.pop()
  size -= 1
  heapifyDown()
  return item

def heapifyUp():
  global size
  index = size -1
  while(hasParent(index) and parent(index) > heap[index]):
    swap(getParentIndex(index),index)
    index = getParentIndex(index)

def heapifyDown():
  index = 0
  while(hasLeftChild(index)):
    smallerChildIndex = getLeftChildIndex(index)
    if(hasRightChild(index) and rightChild(index) < leftChild(index)):
      smallerChildIndex = getRightChildIndex(index)
    if heap[index] < heap[smallerChildIndex]:
      break
    else:
      swap(index,smallerChildIndex)
    index = smallerChildIndex
    
heap = []
size = len(heap)
insert(20)
insert(15)
insert(10)
insert(25)
insert(17)
print(heap)
print(remove())
print(heap)
print(remove())
print(heap)
print(remove())
print(heap)
print(remove())
print(heap)
print(remove())
print(heap)
print(remove())


# Heap sort maybe??
'''while True:
  ret = remove()
  if ret != None:
    print(ret)
  else:
    break'''