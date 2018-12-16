class pair:
    def __init__(self,first=0,second=0):
        self.first = first
        self.second = second

# Check if the number is just +1 greater than the second pair, so we can replace the second pair with the number
# 3-->(1,2)  3 is +1 of 2, so final pair would be (1,3)
def findFirstRange(curNum):
  for num in d:
      if curNum-1 == num.second:
          return num
  return False

# Check if the number is -1 of the first pair, so we can replace the first pair with the number
# 1-->(2,5) 1 is -1 of the first pair, so final pair would be (1,5)
def findSecondRange(curNum):
  for num in d:
      if curNum+1 == num.first:
          return num
  return False
   
def print_d():
  for pairs in d:
    print("({},{})".format(pairs.first,pairs.second),end='') 

def f(input):
    for curNum in input:
      first_range = findFirstRange(curNum)
      second_range = findSecondRange(curNum)
      # This means, number can be put into two different range pairs, so we update one pair and delete the other (union n shit)
      # 3 --> (1,2) (4,5), here 2 can be second range of the first pair or first range of the second pair
      # so we'll can simply take the min and max value in the ranges (as 3 will fall in between) and delete the second pair
      # (1,2*)<-->(*4,5) == (1,5) (min and max of the original pair which is first number of the first pair and second member of the second pair
      if first_range != False and second_range != False:
          first_range.second = second_range.second
          d.remove(second_range)
      # This means that there is one range who's second range can be increased by one or be equal to the curNum
      # 5---> (3,4)== (3,4+1) == (3,5)
      elif first_range != False:
          #first_range.second += 1
          first_range.second = curNum
      # This means that there's one range who's first range can be decreased by one or be equal to the curNum
      # 1---> (2,5) == (2-1,5) == (1,5)
      elif second_range != False:
          #d.append(pair(curNum,second_range.second))
          #second_range.first -=1
          second_range.first = curNum
          #d.remove(second_range)
      # This has to be a number which doesn't fall in any of the existing ranges, make a new entry
      # 8 --> (3,6) == (3,6)(8,8)
      # or 1--> (3,7) == (1,1)(3,7)
      else:
          d.append(pair(curNum,curNum))
		     
#a=[7,1,6,4,9,8,5,2,10,3]
a=[1,2,4,6,7,5,3]
d=[]
f(a)
print_d()
