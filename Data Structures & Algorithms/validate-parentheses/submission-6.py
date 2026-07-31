class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            # ADD TO STACK
            if char in {"(", "{", "["}:
                stack.append(char)
            # CHECK TOP OF STACK FOR MATCH
            else:
                if stack and char == ")" and stack[-1] == "(":
                    stack.pop()
                elif stack and char == "}" and stack[-1] == "{":
                    stack.pop()
                elif stack and char == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
