
class node:
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

class binarySearchTree:
    def __init__(self):
      self.root = None
    def insert(self,value):
      if self.root == None:
        self.root = node(value)
      else:
        self._insert(value,self.root)
    def _insert(self,cur_value,cur_node):
        if cur_value < cur_node.value:
            if cur_node.left_child == None:
                cur_node.left_child = node(cur_value)
                cur_node.left_child.parent = cur_node
            else:
                self._insert(cur_value,cur_node.left_child)
        elif cur_value > cur_node.value:
            if cur_node.right_child == None:
                cur_node.right_child = node(cur_value)
                cur_node.right_child.parent = cur_node
            else:
                 self._insert(cur_value,cur_node.right_child)
        else:
            print("Value {} already exists".format(cur_value))
    def search(self,value):
         if self.root.value == value:
             return True
         else:
             self._search(value,cur_node)
    def _search(self,cur_value,cur_node):
         if cur_value == cur_node.value:
            return True
         elif cur_value < cur_node.value:
            self._search(cur_value,cur_node.left_child)
         elif cur_value > cur_node.value:
            self._search(cur_value,cur_node.right_child)
         else:
            print("Not present")

    def printTree(self):
        if self.root != None:
            self._printTree(self.root)
        else:
            print("Tree is empty")
    def _printTree(self,cur_node):
        if cur_node == None:
            return
        else:
            self._printTree(cur_node.left_child)
            print(cur_node.value)
            self._printTree(cur_node.right_child)

tree = binarySearchTree()

for i in [5,6,1,9,10,2]:
    tree.insert(i)

tree.printTree()

print(tree.search(5))ree.search(5))
