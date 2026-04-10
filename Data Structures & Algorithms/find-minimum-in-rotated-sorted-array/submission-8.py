class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                # Search Right Part of the Array
                left = middle + 1
            elif nums[middle] < nums[right]:
                # Search Left Part of the Array
                right = middle
            else:
                return nums[middle]

        return nums[left]

    