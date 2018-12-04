
class node():
  def __init__(self,data=None):
    self.data = data
    self.next = None

class linkedList():
  def __init__(self):
     self.head = node()
  def append(self,data):
    new_node = node(data)
    cur_node = self.head
    while cur_node.next!=None:
      cur_node = cur_node.next
    cur_node.next = new_node

  def print_linked_list(self):
    cur_node = self.head
    while cur_node.next!=None:
      cur_node = cur_node.next
      print(cur_node.data)
  def erase(self,data):
    cur_node = self.head
    while cur_node.next!=None:
      last_node = cur_node
      cur_node = cur_node.next
      if cur_node.data == data:
          last_node.next = cur_node.next
          return True 



l_list = linkedList()
l_list.append(1)
l_list.append(3)
l_list.append(5)
l_list.append(6)
l_list.append(7)
l_list.print_linked_list()
l_list.erase(3)
l_list.print_linked_list()
