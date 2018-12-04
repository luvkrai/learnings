str1 = "abcabc"
mid = int((len(str1)+1)/2)
print(mid)
flag=True
for i in range(0,mid):
    if str1[i] == str1[mid]:
        pass
    else:
        flag=False
        break
    mid+=1
if flag:
    print("Yes")
else:
    print("No")

