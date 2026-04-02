class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack_map = {')':'(', '}':'{',']':'['}
        for c in s:
            if c in stack_map:
                if not stack:
                    return False 
                if stack[-1] == stack_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False 


        