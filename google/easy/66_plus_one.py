class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strnum = []
        for num in  digits:
            strnum.append(str(num))
            
        strnum = int("".join(strnum))
        num = int(strnum)
        num = num +1
        return [int(char) for char in str(num)]
        