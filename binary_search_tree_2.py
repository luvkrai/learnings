class node():
    def __init__(self,value):
      self.value = value
      self.left_child = None
      self.right_child = None
      self.parent = None

class binary_search_tree():
    def __init__(self):
        self.root = None
    def insert(self,value):
        if self.root == None:
	          self.root = node(value)
        else:
            self._insert(value,self.root)

    def _insert(self,value,cur_node):
        if value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = node(value)
                cur_node.left_child.parent = cur_node
            else:
                self._insert(value,cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = node(value)
                cur_node.right_child.parent = cur_node
            else:
                self._insert(value,cur_node.right_child)
        else:
            print("value {} already exists".format(value))
    def print_tree(self):
        if self.root == None:
            print("Tree is empty")
        else:
            self._print_tree(self.root)
    def _print_tree(self,cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(cur_node.value)
            self._print_tree(cur_node.right_child)
    def height(self):
        if self.root != None:
            return self._height(self.root,0)
        else:
            return 0
    def _height(self,cur_node,cur_height):
        if cur_node == None: return cur_height
        left_height = self._height(cur_node.left_child,cur_height+1)
        right_height = self._height(cur_node.right_child,cur_height+1)
        return max(left_height,right_height)
    def search(self,value):
        if self.root != None:
            return self._search(value,self.root)
        else:
            return False
    def _search(self,value,cur_node):
        if value==cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child != None:
            return self._search(value,cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._search(value,cur_node.right_child)
        else:
            return False
    def delete(self,value):
        if self.root.value == value:
          self.root = None
        else:
          self._delete_node(self.find_node(value))
    def _delete_node(self,node):
        def min_value_node(n):
            current_node = n
            while current_node.left_child != None:
              current_node = current_node.left_child
            return current_node
        def num_of_child(n):
          if n.left_child == None and n.right_child == None:
            return 0
          if n.left_child != None and n.right_child != None:
            return 2
          else:
            return 1
        nu_child = num_of_child(node)
        if nu_child == 0:
          parent = node.parent
          if parent.left_child==node:
            parent.left_child = None
          else:
            parent.right_child = None
        if nu_child == 1:
          parent = node.parent
          if node.left_child != None:
            if parent.left_child == node:
              parent.left_child = node.left_child
            else:
              parent.right_child = node.left_child
            node.left_child.parent = parent
          else:
            if parent.right_child == node:
              parent.right_child = node.right_child
            else:
              parent.right_child = node.right_child
            node.right_child.parent = parent
        if nu_child == 2:
          min_node = min_value_node(node.right_child)
          node.value = min_node.value
          self._delete_node(min_node)
    def find_node(self,value):
      if self.root == None:
        return None
      else:
        return self._find_node(value,self.root)
    def _find_node(self,value,cur_node):
        if value==cur_node.value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child != None:
            return self._find_node(value,cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child != None:
            return self._find_node(value,cur_node.right_child)
        else:
            return None
tree = binary_search_tree()
from random import randint
for _ in range(20):
    tree.insert(randint(0,200))
tree.insert(24)
tree.insert(201)
	
tree.print_tree()
print("Height of the binary tree is {}".format(tree.height()))
n=201
if tree.search(n): print("Value {} is present".format(n))
else:
    print("Value {} is not present".format(n))
tree.delete(24)
tree.print_tree()