class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        heights.append(0)
        for i in range(len(heights)):
            if i == 0:
                stack.append((i, heights[i]))
            else:
                # Next Bar is Smaller
                if stack and heights[i] < stack[-1][1]:
                    newStart = i
                    while stack and heights[i] < stack[-1][1]:
                        start, height = stack.pop()
                        newStart = start
                        # Calculate Area
                        newArea = (i - start) * height
                        if newArea > maxArea: maxArea = newArea
                    stack.append((newStart, heights[i]))

                # Next Bar is Equal or Bigger
                elif heights[i] >= stack[-1][1]:
                    stack.append((i, heights[i]))



        return maxArea
        