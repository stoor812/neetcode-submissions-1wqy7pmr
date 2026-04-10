class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for n in tokens:
            if n in ('+', '-', '*', '/'):
                y = int(stack.pop())
                x = int(stack.pop())
                if n == '+':
                    val = x + y
                    stack.append(val)
                elif n == '-':
                    val = x - y
                    stack.append(val)
                elif n == '*':
                    val = x * y
                    stack.append(val)
                elif n == '/':
                    val = x / y
                    stack.append(val)            
            else:
                stack.append(n)
        
        eval = int(stack.pop())
        return eval
