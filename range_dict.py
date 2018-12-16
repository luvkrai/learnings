a = [7,1,6,5,9,2,10,3,11,4,8]
d = {}
for i in a:
  if not d:
      d[(i,i)] = i
  elif (i) in d.keys():
    pass
  elif (i+1) in d.keys() or (i-1) in d.keys():
    if (i+1) in d.keys():
      d[i] = (i,d[i+1][1])
      del d[i+1]
    else:
      d[i] = (d[i-1][0],i)
      del d[i-1]
  else:
    d[i] = (i,i)
print(d)
