class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append((temperatures[i], i))
            elif stack and temperatures[i] <= stack[-1][0]:
                stack.append((temperatures[i], i))
            else:
                # ith temperature is larger
                while stack and temperatures[i] > stack[-1][0]:
                    temperature, index = stack.pop()
                    result[index] = (i - index)
                stack.append((temperatures[i], i))
        
        return result
        