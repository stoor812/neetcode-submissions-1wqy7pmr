class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) <= 1: return False

        for letter in s:
            if letter in ('(', "{", "["):
                stack.append(letter)
            else:
                if len(stack) == 0: return False
                
                if stack[-1] == '(' and letter == ')':
                    stack.pop()
                elif stack[-1] == '{' and letter == '}':
                    stack.pop()
                elif stack[-1] == '[' and letter == ']':
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False

        