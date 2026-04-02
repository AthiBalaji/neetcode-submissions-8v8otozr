class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                a = stack.pop()
                b = stack.pop()
                a = int(a)
                b = int(b)
                stack.append(str(a+b))
            elif c == '-':
                a = stack.pop()
                b = stack.pop()
                a = int(a)
                b = int(b)
                stack.append(str(b-a))
            elif c == '*':
                a = stack.pop()
                b = stack.pop()
                a = int(a)
                b = int(b)
                stack.append(str(a*b))
            elif c == '/':
                a = stack.pop()
                b = stack.pop()
                a = int(a)
                b = int(b)
                stack.append(str(int(b/a)))
            else:
                stack.append(c)
        return int(stack[0])
        