l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
myDict = [None]*26

def hash_func(value):
  hash_value = ord(value) - 97
  return hash_value

for item in l:
  myDict[hash_func(item)] = item

print(myDict)