class Solution:
    def isValid(self, s: str) -> bool:
        stack_map = {')':'(','}':'{',']':'['}
        stack = []
        for c in s:
            if c in {'(','[','{'}:
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack and stack[-1] == stack_map[c]:
                    stack.pop()
                else: 
                    return False 
        if not stack:
            return True 
        if stack:
            return False


        