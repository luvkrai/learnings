a = [1,2,3,5,6]

d = []

for num in a:
  print(d)
  if not d:
    d.append([num,num])
  else:
    for pair in d:
        #if num-1 in range(pair[0],pair[1]+1) or num+1 in range(pair[0],pair[1]+1):
        # pass
        print("heh")
        if num-1 ==  pair[1]:
          d.append([pair[0],num]) 
          d.remove(pair)
        elif num+1== pair[0]:
          d.append([num,pair[1]])
          d.remove(pair)
        else:
          d.append([num,num])

print(d)
