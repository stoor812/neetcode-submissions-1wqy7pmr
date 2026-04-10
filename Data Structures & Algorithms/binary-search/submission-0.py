class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                # Search Right of Middle
                left = middle + 1
            elif nums[middle] > target:
                # Search Left of Middle
                right = middle - 1
            else:
                if nums[middle] == target:
                    return middle
                else:
                    return -1
        return -1