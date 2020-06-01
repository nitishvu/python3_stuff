class Solution:
    def isValid(self, s: str) -> bool:
        brackets_stack = []
        
        for i in s:
            if i =="(" or i =="[" or i=="{":
               brackets_stack.append(i)
            else:
                if not brackets_stack:
                    return False
                current_char = brackets_stack.pop()
                if  i == ")":
                    if current_char != "(":
                        return False
                if  i == "]":
                    if current_char != "[":
                        return False
                if  i == "}":
                    if current_char != "{":
                        return False
                
        if len(brackets_stack)>0:
            return False
        else:
            return True
            
 
            
        