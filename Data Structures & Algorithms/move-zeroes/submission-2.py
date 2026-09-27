class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 1


        while right < len(nums):

            print(nums[left])
            print(nums[right])

            if nums[left] == 0:
                # SHIFT RIGHT
                if nums[right] == 0:
                    right += 1
                # UPDATE LEFT
                else:
                    nums[left] = nums[right]
                    nums[right] = 0
                    left += 1
            else:
                left += 1
                right = left + 1
