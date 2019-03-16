class my:
  def __init__(self):
    self.l = [1,2,3,4,5]
    self.index = -1
  def __iter__(self):
	# When iter() is called on the object of this class, and iterator is returned
    return self
  def __next__(self):
    self.index+=1
    if self.index < len(self.l):
      return self.l[self.index] 
    else:
      raise StopIteration

o = my()
"""
NOTE: "for" will automatically/implicitly call iter() on the object
so below example is similar to this
t = iter(o)
for i in t:
	print(i)

and also

for i in iter(o):
	print(i)
So basically "for" will make an iterable object(list,tuple,set,dict) an iterator by calling iter() which means the iterable object must support __iter__()
and then it just a matter of calling next() next()....and so on until StopIteration is encountered
for Lists, dict tuples etc __iter__ and __next__ method is overidden by "for" automatically/implicitly
"""
for i in o:
  print(i)