class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        middle = 0

        # No Rotation or Len(1)
        if nums[left] <= nums[right]: return nums[left]

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                # Search Right Part of the Array
                left = middle + 1
            elif nums[middle] < nums[right]:
                right = middle
            else:
                return nums[middle]

    