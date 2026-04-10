class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maxArea = (right - left) * min(heights[left], heights[right])

        while left < right:
            newArea = (right - left) * min(heights[left], heights[right])
            if newArea > maxArea:
                maxArea = newArea

            if heights[right] <= heights[left]:
                right -= 1
            else:
                left += 1
        
        return maxArea