class Node:
  def __init__(self,data=None):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
  def insert(self,data):
    new_node = Node(data)
    if self.head == None:
      self.head = new_node
    else:
      cur_node = self.head
      while cur_node.next!=None:
        cur_node = cur_node.next
      cur_node.next = new_node
  def print(self):
    cur_node = self.head
    while cur_node!=None:
      print(cur_node.data,"->",end='')
      cur_node = cur_node.next

  def reverse(self):
    prev_node = None
    cur_node = self.head
    while cur_node!=None:
      next = cur_node.next
      cur_node.next = prev_node
      prev_node = cur_node
      cur_node = next
    self.head = prev_node
  def head_p(self):
    print(self.head.data)

l = LinkedList()

l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(5)
l.print()
print()
l.reverse()
l.print()
#l.head_p()