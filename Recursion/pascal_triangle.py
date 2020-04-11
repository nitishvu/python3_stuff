'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
you can find more info visit https://en.wikipedia.org/wiki/Pascal%27s_triangle

Example:

Input: 3
Output: [1,3,3,1]


we can do this iteratively or recursively. lets implement both.
'''




class Solution:
    # iterative method not optimal lets concentrate on reursive one.
    #feel free to submit better version
    def getRow(self, rowIndex):
        previous_row = [1]
        current_row = [1,1]
        for i in range (2,rowIndex+1):
            previous_row = current_row
            current_row = []
            current_row.append(1)
            for j in range(i-1):
                current_row.append(previous_row[j]+previous_row[j+1])
            current_row.append(1)
            #print(previous_row)
            #print(current_row)
   
    def getRowrec(self, rowIndex):
        previous_row = [1]
        current_row = [1,1]
        print(previous_row)
        print(current_row)
        for i in range (2,rowIndex+1):
            previous_row = current_row
            current_row = []
            current_row.append(1)
            current_row= self.get_row(previous_row,i-1,0,current_row)
            #print(previous_row)
            #print(current_row)
    #using recursion get a row in pascal triangle
    #feel free to submit better version here
    def get_row(self,previous_row,index,current_index,current_row):
        if current_index == index:
            current_row.append(1)
            return current_row
        else:
            current_row.append( previous_row[current_index] +previous_row[current_index+1])
            self.get_row(previous_row,index,current_index+1,current_row)
       
        return current_row
import time



sobj = Solution()
start_time = time.time()
sobj.getRowrec(10)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
sobj.getRow(10)
print("--- %s seconds ---" % (time.time() - start_time))