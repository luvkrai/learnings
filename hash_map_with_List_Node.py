class Node:
  def __init__(self,key,value):
    self.key = key
    self.value = value

class myhash():
  def __init__(self):
    self.store = [None for _ in range(16)]
    self.size = 16
  def get(self,key):
    index = self._hash(key)
    if self.store[index] is None:
      return None
    else:
      found = False
      for item in self.store[index]:
        if item.key == key:
          found = True
          return item.value
      if not found:
        return None
  def put(self,key,value):
    n = Node(key,value)
    index = self._hash(key)
    if self.store[index] is None:
      self.store[index] = [n]
    else:
      added = False
      for item in self.store[index]:
        if item.key == key:
          item.value = value
          added = True
          break
      if not added:
        self.store[index].append(n)
  def _hash(self, key):
    hash = 0
    for char in str(key):
      hash += ord(char)
    print(hash)
    return hash % self.size

hm = myhash()
hm.put("1", "sachin")
hm.put("2", "sehwag")
hm.put("a","luv")
print(hm.get("1"))
print(hm.get("2"))
print(hm.get("a"))
print(hm.get("1"))
print(hm.store)