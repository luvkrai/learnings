#https://www.hackerrank.com/challenges/30-2d-arrays/problem
A = [[1, 1, 1, 0, 0, 0], 
    [0, 1, 0, 0, 0, 0], 
    [1, 1, 1, 0, 0, 0], 
    [0, 0, 2, 4, 4, 0], 
    [0, 0, 0, 2, 0, 0], 
    [0, 0, 1, 2, 4, 0]]

def calculate_hour_glass(A,row_start,row_end,col_start,col_end):
  t_sum = 0
  row=1
  for l in range(row_start,row_end):
    col=1
    for m in range(col_start,col_end):
      if not (row == 2 and col==1) and not (row==2 and col==3):
        print(A[l][m],end=" ")
        t_sum+=A[l][m]
      col+=1
    row+=1
    print("")
  return t_sum
 

result = []
for i in range(4):
  for j in range(4):
    result.append(calculate_hour_glass(A,i,i+3,j,j+3))
print(max(result))