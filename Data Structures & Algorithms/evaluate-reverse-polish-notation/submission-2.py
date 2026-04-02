class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ('+','-','*','/')
        res = 0 
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                if(i == '+'):
                    res = stack.pop() + stack.pop()
                    stack.append(res)
                elif(i == '-'):
                    b, a = stack.pop(), stack.pop()
                    res = a - b
                    stack.append(res)

                elif(i == '*'):
                    res = stack.pop() * stack.pop()
                    stack.append(res)
                elif(i == '/'):
                    b, a = stack.pop(), stack.pop()
                    res = int(a / b)  # Ensures truncation toward zero
                    stack.append(res)

        return stack.pop()


        