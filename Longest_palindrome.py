s = "forgeeksskeegfor"

f_dic = {}
for i in range(0,len(s)):
  for j in range(1,len(s)):
    sub_string = s[i:j]
    rev_sub_string = s[i:j][::-1]
    if (sub_string == rev_sub_string):
      f_dic[len(sub_string)] = sub_string
x = max(f_dic.keys())
print(f_dic[x])
print(f_dic[x])