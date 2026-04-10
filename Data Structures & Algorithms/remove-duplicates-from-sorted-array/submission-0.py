class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 0
        k = 0

        for right in range(len(nums)):
            if right == 0:
                k += 1
            elif nums[right] != nums[right - 1]:
                left += 1
                k += 1
                nums[left] = nums[right]

        return k


        
        
        