#https://www.hackerrank.com/challenges/30-scope/problem
class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = None

	# Add your code here
    def computeDifference(self):
        '''result = []
        for i in range(0,len(self.__elements)):
            for j in range(1,len(self.__elements)):
                result.append(abs(self.__elements[i]-self.__elements[j]))
        self.maximumDifference = max(result)'''
        import sys
        minv = sys.maxsize
        maxv = -sys.maxsize
        for element in self.__elements:
            if element < minv:
                minv = element
            if element > maxv:
                maxv = element
        self.maximumDifference = abs(minv-maxv)



# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)