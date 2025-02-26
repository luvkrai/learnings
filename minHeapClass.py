
class minHeapClass:
    def __init__(self):
        self.minHeap = []
        self.size = 0
    def getLeftChildIndex(self, parentIndex):
        return parentIndex*2 + 1
    def getRightChildIndex(self, parentIndex):
        return parentIndex*2 + 2
    def getParentIndex(self,childIndex):
        return int((childIndex - 1)/2)
    def hasLeftChild(self,index):
        return (self.getLeftChildIndex(index) < self.size)
    def hasRightChild(self,index):
        return (self.getRightChildIndex(index) < self.size)
    def hasParent(self,index):
        return (self.getParentIndex(index) >= 0)
    def getLeftChild(self,parentIndex):
        return self.minHeap[self.getLeftChildIndex(parentIndex)]
    def getRightChild(self,parentIndex):
        return self.minHeap[self.getRightChildIndex(parentIndex)]
    def getParent(self,index):
        return self.minHeap[self.getParentIndex(index)]
    def swapItems(self,i,j):
        self.minHeap[i], self.minHeap[j] = self.minHeap[j], self.minHeap[i]
    def peek(self):
        if self.size == 0:
            return None  
        return self.minHeap[0]

    def add(self, item):
        self.minHeap.append(item)
        self.size += 1
        self.heapifyUp()

    def remove(self):
        if self.size == 0:
            print("heap is empty")
            return
        topItem = self.minHeap[0]
        self.minHeap[0] = self.minHeap[self.size - 1]
        self.minHeap.pop()
        self.size -= 1
        self.heapifyDown()
        return topItem

    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and self.minHeap[index] < self.getParent(index):
                self.swapItems(self.getParentIndex(index), index)
                index = self.getParentIndex(index)

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallestValueIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.minHeap[smallestValueIndex] > self.getRightChild(index):
                smallestValueIndex = self.getRightChildIndex(index)
            if self.minHeap[index] < self.minHeap[smallestValueIndex]:
                break
            else:
                self.swapItems(index, smallestValueIndex)
            index = smallestValueIndex


    
        

myHeap = minHeapClass()


# Peek into the heap
myHeap.peek()

# Add items
myHeap.add(9)
myHeap.add(4)
myHeap.add(1)
myHeap.add(6)
myHeap.add(2)
myHeap.add(8)
myHeap.add(5)
myHeap.add(3)

print(myHeap.minHeap)
# Peek again
print("Top element--->", myHeap.peek())

# remove items
print("Removed item:", myHeap.remove())
# Peek again
print("Top element--->", myHeap.peek())
print(myHeap.minHeap)


# remove items
print("Removed item:", myHeap.remove())
print("Top element--->", myHeap.peek())
print(myHeap.minHeap)


print("Removed item:", myHeap.remove())
# Peek again
print("Top element--->", myHeap.peek())
print(myHeap.minHeap)




