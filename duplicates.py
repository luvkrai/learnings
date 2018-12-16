dic = {}
list = [1,2,3,3,5,6,7,8,3,7,9]

for item in list:
        try:
            dic[item]+=1
        except:
            dic[item]=1 

print(dic)
for key,value in dic.items():
    if value > 1:
        print(key)

