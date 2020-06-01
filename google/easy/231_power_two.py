class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        

        return (n and (not (n & (n-1))))


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n ==0:
            return False
        if n ==2:
            return True
        while (n!=1):
            n=n/2
            if n%2 !=0 and n!=1:
                return False
        return True
               