class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s: 
            if char in "({[" :
                stack.append(char)
            elif len(stack)>0: 
                tmp = stack.pop()
                if (char==')' and tmp!='(' or 
                    char=='}' and tmp!='{' or
                    char==']' and tmp!='['):
                    return False
            else: 
                return False
        return len(stack) ==0
                



            
        
